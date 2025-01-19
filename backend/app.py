from flask import Flask, jsonify, request
from flask_cors import CORS

import time

from src.models.Url import URL

app = Flask(__name__)
CORS(app)

url = URL()

# Base de datos simulada
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

class UserAPI:
    def get_all_users(self):
        """Devuelve todos los usuarios."""
        return jsonify(users), 200

    def get_user_by_id(self, user_id):
        """Devuelve un usuario por ID."""
        user = next((user for user in users if user["id"] == user_id), None)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "User not found"}), 404

    def create_user(self):
        """Crea un nuevo usuario."""
        data = request.json
        if "name" not in data or "email" not in data:
            return jsonify({"error": "Name and email are required"}), 400
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "email": data["email"],
        }
        users.append(new_user)
        return jsonify(new_user), 201

    def delete_user(self, user_id):
        """Elimina un usuario por ID."""
        global users
        users = [user for user in users if user["id"] != user_id]
        return jsonify({"message": "User deleted"}), 200

# Instancia de la clase UserAPI
user_api = UserAPI()

# Rutas de la API
@app.route("/shorten", methods=["POST"])
def get_shorten():
    return url.get_shorten()

@app.route("/shorten/<shortCode>", methods=["GET"])
def get_long_url(shortCode):
    return url.get_long_url(shortCode)

@app.route("/shorten/<shortCode>/stats", methods=["GET"])
def get_stats(shortCode):
    return url.get_stats(shortCode)

@app.route("/shorten/<shortCode>", methods=["PUT"])
def get_shorten_update(shortCode):
    return url.get_shorten_update(shortCode)

@app.route("/shorten/<shortCode>", methods=["DELETE"])
def get_shorten_delete(shortCode):
    return url.get_shorten_delete(shortCode)

if __name__ == "__main__":
    app.run(debug=True)
