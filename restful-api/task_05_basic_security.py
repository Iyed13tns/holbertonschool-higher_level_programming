#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = verify_password(username, password)
    if not user:
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")

if __name__ == '__main__':
    app.run(debug=True)