import jwt
import datetime
from config import secret_key
from db.database import check_naughty


def generate_token(username):
    is_naughty = check_naughty(username)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    token = jwt.encode({
        'username': username,
        'exp': expiration_time,
        'is_naughty': is_naughty
    }, secret_key, algorithm='HS256')
    return token


def verify_cookie(token, key):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        if (key == "is_naughty" and decoded[key] == False):
            return False
        elif decoded[f'{key}']:
            return decoded[f'{key}']
        else:
            return None
    except Exception as e:
        print(e)
        return None


def sanitize(filename):
    if "flag" in filename:
        print("Flag attempt detected")
        return None
    if not (filename.startswith("/christmas/files/")):
        print("Invalid path detected")
        return None
    if ".." in filename:
        filename = filename.replace("../","")
    return filename
