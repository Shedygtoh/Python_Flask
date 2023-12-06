from flask import Flask, request, jsonify
from db_connector import DBConnector

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def users(user_id):
    db = DBConnector()

    if request.method == 'POST':
        user_name = request.json['user_name']
        try:
            db.create_user(user_id, user_name)
            return jsonify(status="ok", user_added=user_name), 200
        except pymysql.err.IntegrityError:
            return jsonify(status="error", reason="id already exists"), 500

    elif request.method == 'GET':
        result = db.get_user(user_id)
        if result is None:
            return jsonify(status="error", reason="no such id"), 500
        else:
            return jsonify(status="ok", user_name=result['user_name']), 200

    elif request.method == 'PUT':
        new_name = request.json['user_name']
        db.update_user(user_id, new_name)
        return jsonify(status="ok", user_updated=new_name), 200

    elif request.method == 'DELETE':
        db.delete_user(user_id)
        return jsonify(status="ok", user_deleted=user_id), 200

    db.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)