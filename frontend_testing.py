import unittest
from selenium import webdriver

class FrontendTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_get_user_data(self):
        self.driver.get("http://127.0.0.1:5000/users/1") #
        element = self.driver.find_element_by_id('user_name')
        #self.assertIsNotNone(element)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()