```py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def send_email(email, token):
    cmd = 'curl --request POST  --header "Authorization: Bearer ..."  --header "Content-Type: application/json"  --data \'{ "message": { "template": "WGESMQYMWM4VPDG0QBK25MJT2AD4", "to": { "email": "EMAIL" }, "data": { "url": "https://flask-hello-world-fawn-kappa.vercel.app/account?token=TOKEN" } } }\'  https://api.courier.com/send'.replace("EMAIL", email).replace("TOKEN", token)
#    print(cmd)
    os.system(cmd)

# who needs a database ayways
accounts = []

def find_account(token):
    global accounts
    for account in accounts:
        if account["token"] == token:
            return account
    return None

def is_admin(email):
    print(email)
    domain = email.split("@")[1]
    print(domain)
    if domain == "niclov.in":
        return True
    return False
@app.route('/')
def home():
    return "Hello world!"

@app.route('/signin', methods=['POST']) 
def signin():
    data = request.json
    email = data["email"]
    if "'" in email or '"' in email or "$" in email or "`" in email:
        return '\' " $ and ` are not allowed in email addresses'

    token = os.urandom(32).hex()
    send_email(email, token)
    global accounts
    accounts += [{"email":email, "token": token}]

    return "A confirmation email was sent"

@app.route('/account')
def account():
    token = request.args.get("token")
    email = find_account(token)["email"]
    if email is None:
        return "wrong token"
    admin = is_admin(email)

    return "Your email is {}. Admin: {}".format(email, admin)

# access to /admin has been blocked using vercel firewall rules (https://vercel.com/docs/security/vercel-waf/custom-rules#get-started):
# if Request Path == "/admin" then deny
# if Raw Path == "/admin" then deny
# if Target Path == "/admin" then deny
@app.route('/admin')
def send():
    token = request.args.get("token")
    account = find_account(token)
    if account is None:
        return "wrong token"

    if is_admin(account["email"]):
        return "FLAG-..."
    else:
        return "user is not admin"
```