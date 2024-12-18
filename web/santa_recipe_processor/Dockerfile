FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "FLAG-{W3R3-1N-4-P1CKL3-W17H-7H15-UN7RU573D-D474}" > /flag.txt

# Move flag to root-owned directory and set proper permissions
RUN chmod 444 /flag.txt && \
    # Make app directory read-only for nobody user
    chmod -R 555 /app && \
    # Create directory for gunicorn to write its pid file
    mkdir -p /var/run/gunicorn && \
    chown -R nobody:nogroup /var/run/gunicorn

USER nobody

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--pid", "/var/run/gunicorn/pid", "app:app"]