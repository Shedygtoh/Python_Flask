import requests
from selenium import webdriver
from db_connector import DBConnector

# Set up the API endpoint
api_url = 'http://127.0.0.1:5000/users'
web_url = 'http://127.0.0.1:5001/users/get_user_data'
user_id = 1
user_name = 'John'

# Initialize DBConnector
db = DBConnector()

# Initialize driver as None
driver = None

try:
    # ... (Your existing code for POST and GET requests)

    # Start a Selenium Webdriver session
    driver = webdriver.Chrome()

    # Navigate to web interface URL using the new user id
    driver.get(f'{web_url}/{user_id}')

    # Check that the user name is correct
    user_name_element = driver.find_element_by_id('user_name')

    # Print the text of the element for debugging
    print(f"User Name Element Text: {user_name_element.text}")

    if user_name_element.text != user_name:
        raise Exception("Checking the user name in the web interface failed.")

except Exception as e:
    print(f"Test failed: {e}")
finally:
    # Close the database connection and the browser window
    db.close()
    if driver is not None:
        driver.quit()
