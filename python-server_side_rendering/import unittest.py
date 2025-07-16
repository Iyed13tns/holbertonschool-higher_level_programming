import unittest
from task_01_jinja import app

# FILE: test_task_01_jinja.py

class TestTask01Jinja(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "Home page did not return status code 200")

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200, "About page did not return status code 200")

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200, "Contact page did not return status code 200")

if __name__ == '__main__':
    unittest.main()