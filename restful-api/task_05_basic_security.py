
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"password": generate_password_hash("password1"), "role": "admin"},
    "user2": {"password": generate_password_hash("password2"), "role": "user"}
}



@app.route('/login', methods=['POST'])
def login():
    
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': users[username]['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return jsonify({"msg": "This is a protected route with basic auth"}), 200

@app.route('/jwt-protected', methods=['GET'])
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

def role_required(role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != role:
                return jsonify({"msg": "Access forbidden: insufficient role"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

@app.route('/admin', methods=['GET'])
@role_required('admin')
def admin():
    return jsonify({"msg": "This is a protected route for admin"}), 200

if __name__ == '__main__':
    app.run(debug=True)