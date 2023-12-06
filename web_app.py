from flask import Flask, render_template
from db_connector import DBConnector

app = Flask(__name__)

# Initialize database connector
new_db = DBConnector()

@app.route('/users/get_user_data/<int:user_id>')
def get_user_data(user_id):
    user_name = db.get_user(user_id)

    if user_name is not None:
        return render_template('user_data.html', user_name=user_name)
    else:
        return render_template('error.html', error_message="No such ID")

if __name__ == '__main__':
    app.run(port=5001, debug=True)
