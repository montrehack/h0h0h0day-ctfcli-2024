from flask import Blueprint, request, jsonify, redirect, send_file, render_template, make_response
from db.database import *
from handler import generate_token, verify_cookie, sanitize

web_routes = Blueprint('web', __name__)
api_routes = Blueprint('api', __name__)


@web_routes.route('/')
def index():
    return render_template('login.html')
    
@web_routes.route('/register')
def register():
    return render_template('register.html')

@web_routes.route('/dashboard')
def welcome():
    cookie = request.cookies.get('access_token')
    user = verify_cookie(cookie, 'username')
    if (user):
        return render_template('welcome.html')
    else:
        return redirect('/')
        
@web_routes.route('/profile')
def profile():
    cookie = request.cookies.get('access_token')
    user = verify_cookie(cookie, 'username')
    if (user):
        return render_template('update.html')
    else:
        return redirect('/')


@api_routes.route('/register', methods=['POST'])
def register_post():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    register = insert_user(username, password, email)
    if (register):
        return make_response(jsonify({"message": "Registration successful"}))
    else:
        return make_response(jsonify({"message": "Username already taken"}),401)


@api_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    login = login_user(username, password)
    if (login):
        token = generate_token(username)
        response = make_response(jsonify({"message": "Login successful"}))
        response.set_cookie('access_token', token)
        return response
    else:
        return make_response(jsonify({"message": "Wrong username or password"}),401)


@api_routes.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    cookie = request.cookies.get('access_token')
    user = verify_cookie(cookie, 'username')
    if (user):
        for key in data:
            if not (check_column(key)):
                return make_response(jsonify({"message":"Column does not exist"}),401)
            
        for key in data:       
            if not (data[key] == ""):
                update_user(key, data[key], user)
        return make_response(jsonify({"message":"Profile updated successful"}))
    else:
        return make_response(jsonify({"message":"Cookie is invalid"}),401)
   
   
@api_routes.route('/list/<int:user_id>')
def get_data(user_id):
    user = list_user(user_id)
    if (user):
        data = {
            'id': user[0],
            'username': user[1],
            'email': user[3],
            'is_naughty': user[6],
            'created_at': user[7]
        }
        return make_response(jsonify(data))
    else:
        return make_response(jsonify({"message":"Cannot find a user with that ID"}),404)


@api_routes.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    cookie = request.cookies.get('access_token')
    naughty = verify_cookie(cookie, 'is_naughty')
    if (naughty == False):
        requested = data.get('file')
        safe = sanitize(requested)
        if not (safe):
            return make_response(jsonify({"message": "Filename not allowed"}),403)
        try:
            return make_response(send_file(safe))
        except FileNotFoundError:
            return make_response(jsonify({"message": f"File '{safe}' not found"}),404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}),500)
    else:
        return make_response(jsonify({"message": "Unauthorized"}),403)


@api_routes.route('/gifts')
def gifts():
    gifts = list_gifts()
    results = []
    for gift in gifts:
        results.append({
            'name': gift[1],
            'description': gift[2],
            'recipient': gift[3],
            'occasion': gift[4],
            'price': gift[5],
            'is_wrapped': gift[6]
        })
       
    return make_response(jsonify({"message":results}))
        
        
@api_routes.route('/')
def get_status():
    status = {"status": "API is working fine. Merry Christmas!"}
    return jsonify(status)
