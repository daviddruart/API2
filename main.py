from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# configuración SQLite dentro del codespace
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE _URI"] = "sqlite///" + os.path.join(BASE_DIR, "users.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    def to_dict(self):
        return {"id": self.id, "name": self.name, "telefono": self.telefono}

# Crear base de datos
with app.app_context():
    db.create_all()

# RUTAS CRUD

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
    return jsonify([u.to_dict() for u in users]), 200

# GET: obtener un usuario por id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
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
    data = request.get_json()  
    if not data.get("name") or not data.get("telefono"):
        return jsonify({"error": "Faltan datos"}), 400
    
    new_user = User(name=data["name"], telefono=data["telefono"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# PUT: actualizar un usuario existente
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    data = request.get_json()
    user.name = data.get("name", user.name)
    user.telefono = data.get("telefono", user.telefono)
    db.session.commit()
    return jsonify(user.to_dict()), 200

# DELETE
# DELETE: eliminar un usuario
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = User.query.get(user_id)
    if not user:
        return jsonify({"error":"Usuario no encontrado"}), 404
        
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"Usuario {user_id} eliminado"}), 200


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0")