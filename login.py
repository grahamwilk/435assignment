from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret_key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    if request.json.get('username') != 'username' or request.json.get('password') != 'password':
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify(create_access_token(identity='username')), 200

if __name__ == '__main__':
    app.run(debug=True)