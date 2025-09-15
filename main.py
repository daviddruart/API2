from flask import Flask, jsonify, request


app = Flask(__name__)


# GET
# GET: obtener información
@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id":user_id, "name": "test", "telefono": "999-666-333"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

# GET: obtener todos los usuarios
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET: obtener un usuario por id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuario no encontrado"}), 404



# POST
# POST: crear información
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get.json()
    return jsonify(data), 201

# POST: crear un nuevo usuario
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()  # corregido get.json → get_json
    if not data.get("name") or not data.get("telefono"):
        return jsonify({"error": "Faltan datos"}), 400
    
    new_id = users[-1]["id"] + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "telefono": data["telefono"]}
    users.append(new_user)
    return jsonify(new_user), 201

# PUT: actualizar un usuario existente
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["telefono"] = data.get("telefono", user["telefono"])
    return jsonify(user), 200

# DELETE
# DELETE: eliminar un usuario
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"Usuario {user_id} eliminado"}), 200







if __name__ =="__main__":
    app.run(debug=True)