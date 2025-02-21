#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/data')
def data():
    return jsonify({'key': 'value'})

@app.route('/status')
def status():
    return jsonify({'status': 'OK'})

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    users[username] = user_data
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)