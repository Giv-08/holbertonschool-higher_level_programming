from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask API!</h1>"

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
            "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
            }
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

users = {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
}

users = {}

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username:
        return jsonify({"error":"Username is required"})
    if not username in users:
        return jsonify({"error": "User not found"})

    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({
        "message": "User added succesfully!",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
