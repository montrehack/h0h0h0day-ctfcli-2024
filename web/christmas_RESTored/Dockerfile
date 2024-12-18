FROM python:3.8-slim

RUN apt-get update && apt-get install -y sqlite3
RUN pip install Flask && pip install pyjwt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /christmas/files/
COPY files/ /christmas/files/
COPY flag.txt /flag.txt

WORKDIR /app
COPY challenge/ .
COPY setup.sql .
RUN sqlite3 christmas.db < setup.sql && rm setup.sql
 
EXPOSE 5000

CMD ["/bin/bash", "-c", "python3 app.py"]
