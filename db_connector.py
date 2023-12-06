import mysql.connector
from datetime import datetime

class DBConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user='admin',
            password='admin_password',
            database='default',
            #charset='utf8mb4',
            #cursorclass=mysql.connector.cursor.DictCursor
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return result

    def check_user_exists(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        result = self.execute_query(query, (user_id,))
        return bool(result)

    def create_user(self, user_id, user_name):
        query = "INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)"
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.execute_query(query, (user_id, user_name, creation_date))

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        result = self.execute_query(query, (user_id,))
        return result[0] if result else None

    def update_user(self, user_id, user_name):
        query = "UPDATE users SET user_name = %s WHERE user_id = %s"
        self.execute_query(query, (user_name, user_id))

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        self.execute_query(query, (user_id,))

    def close(self):
        self.connection.close()