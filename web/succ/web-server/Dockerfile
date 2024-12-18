FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir cases

COPY app.py ftp.py timeout.py secret.key ./
COPY templates templates/
COPY static static/ 

CMD ["python3", "-m", "gunicorn", "-w=4", "-b=0.0.0.0:5000", "app:app"]