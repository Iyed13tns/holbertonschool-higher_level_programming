import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestFlaskAPI(unittest.TestCase):
    def test_home_route(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data_route_no_users(self):
        # Clear users dictionary for this test
        response = requests.get(f"{BASE_URL}/data")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "No users found"})

    def test_data_route_with_users(self):
        response = requests.get(f"{BASE_URL}/data")
        self.assertEqual(response.status_code, 200)
        self.assertIn("jane", response.json())
        self.assertIn("john", response.json())

    def test_status_route(self):
        response = requests.get(f"{BASE_URL}/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_get_user_existing(self):
        response = requests.get(f"{BASE_URL}/users/john")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        })

    def test_get_user_non_existing(self):
        response = requests.get(f"{BASE_URL}/users/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "User not found"})

    def test_add_user_valid(self):
        new_user = {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "Seattle"
        }
        response = requests.post(f"{BASE_URL}/add_user", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "User added")
        self.assertEqual(response.json()["user"], new_user)

    def test_add_user_missing_username(self):
        new_user = {
            "name": "Bob",
            "age": 40,
            "city": "Chicago"
        }
        response = requests.post(f"{BASE_URL}/add_user", json=new_user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Username is required"})

    def test_add_user_duplicate_username(self):
        duplicate_user = {
            "username": "jane",
            "name": "Jane Doe",
            "age": 35,
            "city": "San Francisco"
        }
        response = requests.post(f"{BASE_URL}/add_user", json=duplicate_user)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.json()["user"]["name"], "Jane Doe")  # Ensure original user remains

if __name__ == "__main__":
    unittest.main()