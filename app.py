from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from minio import Minio
import os

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret_key'
jwt = JWTManager(app)

os.makedirs('tmp', exist_ok=True)

#Login
@app.route('/login', methods=['POST'])
def login():
    if request.json.get('username') != 'username' or request.json.get('password') != 'password':
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify(create_access_token(identity='username')), 200

#minio_client
minio_client = Minio(
    'localhost:9000',
    access_key='aaaaaaaa',
    secret_key='aaaaaaaa',
    secure=False
    )

@app.route('/post', methods=['POST'])
@jwt_required()
def upload_post():
    username = get_jwt_identity()
    object_id = username + "-" + str(request.json.get('object_id'))
    content = request.json.get('content')
    with open(f"tmp/{object_id}.txt", "w") as f:
        f.write(content)
    
    minio_client.fput_object('posts', object_id, f"tmp/{object_id}.txt")
    os.remove(f"tmp/{object_id}.txt")

    return jsonify({"message": "File uploaded successfully", "object_id": object_id}), 200

@app.route('/get', methods=['GET'])
@jwt_required()
def get_all_posts():
    objects = minio_client.list_objects('posts')
    post_list = []
    for obj in objects:
        post = minio_client.get_object('posts', obj.object_name)
        post_list.append({"object_id": obj.object_name, "content": post.data.decode()})
    return jsonify(post_list), 200

@app.route('/delete', methods=['POST'])
@jwt_required()
def delete_post():
    username = get_jwt_identity()
    object_id = request.json.get('object_id')
    if username not in object_id:
        return jsonify({"message": "Unauthorized to delete this post"}), 401
    print(object_id)
    minio_client.remove_object('posts', object_id)
    return jsonify({"message": "File deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)