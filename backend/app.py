from flask import Flask, jsonify, request
from flask_cors import CORS

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


@app.route("/users", methods=["GET"])
def get_users():
    return user_api.get_all_users()

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return user_api.get_user_by_id(user_id)

@app.route("/users", methods=["POST"])
def create_user():
    return user_api.create_user()

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return user_api.delete_user(user_id)

if __name__ == "__main__":
    app.run(debug=True)
