from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
            "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
            }
@app.route("/data", methods=["GET"])
def get_data():
    # usernames = list(users.keys())
    # return jsonify(usernames)
    return jsonify(users), 200

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# alice = {
#     "username": "alice",
#     "name": "Alice",
#     "age": 25,
#     "city": "San Francisco"
# }

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username:
        return jsonify({"error":"Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({
        "message": "User added succesfully!",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
