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
        "username": "admin",
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    },
    "user1": {
        "username": "user1",
        "password": generate_password_hash("user_password"),
        "role": "user"
    }
}

@auth.verify_password
def varify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

# @app.route("/")
# def home():
#     return "Welcome to the Flask API"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    # username = request.json.get("username", None)
    # password = request.json.get("password", None)
    # current_user = get_jwt_identity()
    # user = users.get(username)
    # if username not in users or not check_password_hash(users[username]["password"], password):
    # if not user or not check_password_hash(user["password"], password):
    #     return jsonify({"msg": "Wrong username or password"}), 401

    # access_token = create_access_token(identity=username)
    # return jsonify(access_token=access_token), 200
    data = request.get_json()

    if data["username"] not in users or not check_password_hash(users[data["username"]]["password"], data["password"]):
        return jsonify({"msg": "Wrong username or password"}), 401
    access_token = create_access_token(identity=data["username"])
    return jsonify({"access_token": access_token})

@app.route('/jwt-protected')
@jwt_required()
def protected():
    # current_user = get_jwt_identity()
    # return jsonify(logged_in_as=current_user), 200
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user in users or users[current_user]["role"] == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"msg": "You do not have access to this route."}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    # app.run(host='localhost', port=5000, debug=True)
    app.run()
