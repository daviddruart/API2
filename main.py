from flask import Flask, jsonify, request


app = Flask(__name__)

# GET: obtener información

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id":user_id, "name": "test", "telefono": "999-666-333"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

# POST: crear información
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get.json()
    return jsonify(data), 201

if __name__ =="__main__":
    app.run(debug=True)