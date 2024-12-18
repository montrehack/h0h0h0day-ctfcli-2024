from flask import Flask, request, render_template
import pickle
import base64
import subprocess


# Looooooooool :)
def block(*args, **kwargs):
    return """
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'subprocess'
"""


subprocess_functions = (x for x in dir(subprocess) if callable(getattr(subprocess, x)))
for i in subprocess_functions:
    setattr(subprocess, i, block)

app = Flask(__name__)


@app.route("/source_code_81c1a009af50005171a33f3c17", methods=["GET"])
def source_code():
    with open(__file__, "r") as f:
        source_code = f.read()
    return source_code


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    # Get data from either POST or GET
    recipe_data_form = request.form.get("recipe_data")
    recipe_data = recipe_data_form or request.args.get("recipe_data", "")

    if recipe_data:
        try:
            decoded_data = base64.b64decode(recipe_data)
            # dangerous!
            unpickled_data = pickle.loads(decoded_data)
            result = f"Output data: {unpickled_data}"
        except Exception as e:
            error = f"Error: {e}"

    return render_template(
        "index.html", result=result, error=error, recipe_data=recipe_data
    )
