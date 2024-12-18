from ftp import FtpClient
from pathlib import Path
from flask import Flask, render_template, session
from flask_pydantic import validate
import uuid
import os
import time
from timeout import Timeout

from pydantic import BaseModel, Field

CASES_DIR = Path("cases").resolve()

app = Flask(__name__)
app.secret_key = open("secret.key").read()


class SubmitModel(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    temperature: int = Field(ge=-30, le=30)
    symptoms: str = Field(min_length=1, max_length=512)


def create_session():
    session["sid"] = uuid.uuid4()


@app.before_request
def ensure_session():
    if session.get("sid") is not None:
        return
    create_session()


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/submit")
@validate()
def submit(form: SubmitModel):
    app.logger.info(f"Received case: {form}")

    safe_path = (
        CASES_DIR.joinpath(f"{session['sid']}.json").resolve().relative_to(CASES_DIR)
    )
    safe_path = CASES_DIR.joinpath(safe_path)

    case_json = form.model_dump_json()
    open(safe_path, "w").write(case_json)

    upload_cases_to_triage()
    create_session()

    return render_template("triaging.html")


def upload_cases_to_triage():
    client = FtpClient("triage-server", 21)
    client.connect()
    client.login(os.getenv("TRIAGEUSER"), os.getenv("TRIAGEPASS"))

    for file in os.listdir(CASES_DIR):
        case_file = CASES_DIR.joinpath(file)

        try:
            with Timeout(3):
                client.upload_file(case_file, Path(file))
                time.sleep(1)  # don't overload ftp server
        except:
            pass

        os.remove(case_file)
