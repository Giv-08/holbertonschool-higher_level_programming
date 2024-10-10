#!/usr/bin/python3
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.get_json() is None:
        abort(400, "It is not a JSON")
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # if username in data:
    #     return jsonify({"error": "User with this username already exists"}), 400

    # username = data.get("username")
    # name = data.get("name")
    # age = data.get("age")
    # city = data.get("city")


    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({
        "message": "User added successfully!",
        "user": users[username]
    }), 201

# @app.route("/users", methods=["GET"])
# def get_users():
#     return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
