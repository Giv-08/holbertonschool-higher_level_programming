#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = '12345abcde'
jwt = JWTManager(app)

users = {
    "admin": {
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    },
    "user_1": {
        "password": generate_password_hash("user_password"),
        "role": "user"
    }

}

def varify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return True
    return False

@app.route('/login')
@auth.login_required
def index():
    return "Hello, {}! You've logged in!".format(auth.username())

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/admin')
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if users[current_user]["role"] == "admin":
        return "Welcome Admin!"
    else:
        return jsonify({"msg": "You do not have access to this route."}), 403

@app.route('/user')
@jwt_required()
def user():
    current_user = get_jwt_identity()
    if users[current_user]["role"] == "user":
        return f"Welcome, {current_user}!"
    else:
        return jsonify({"msg": "You do not have access to this route."}), 403

if __name__ == '__main__':
    app.run(debug=True)
