import requests

response = requests.get('http://127.0.0.1:5000/users/1')
data = response.json()

if response.status_code == 200 and data['status'] == 'ok':
    user_name = data['user_name']
    print(f"User name: {user_name}")
else:
    print("Error retrieving user information")

response = requests.get('http://127.0.0.1:5000/users/2')
data = response.json()

if response.status_code == 200 and data['status'] == 'ok':
    user_name = data['user_name']
    print(f"User name: {user_name}")
else:
    print("Error retrieving user information")