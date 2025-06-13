from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs (en mémoire)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    # Retourne la liste des noms d'utilisateurs
    if not users:
        return jsonify({"message": "No users found"}), 404
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # Vérifie si le username est présent
    if not request.json or 'username' not in request.json:
        return jsonify({"error": "Username is required"}), 400
    
    user_data = request.json
    username = user_data['username']
    
    # Ajoute le nouvel utilisateur
    users[username] = {
        "username": username,
        "name": user_data.get('name', ""),
        "age": user_data.get('age', 0),
        "city": user_data.get('city', "")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
