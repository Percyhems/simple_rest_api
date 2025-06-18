from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user_id = str(uuid.uuid4())
    user = {'id': user_id, 'name': data['name'], 'email': data['email']}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
