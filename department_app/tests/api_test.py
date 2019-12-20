import unittest
import requests

API_URL = 'http://localhost:5000/employees/api'


class TestApi(unittest.TestCase):
    def test_post(self):
        data = {"name": "TestUser", "department": 1, "salary": 2000, "birth_date": "1990-02-10"}
        response = requests.post(API_URL, json=data)
        self.assertEqual(response.status_code, 201)

    def test_get(self):
        response = requests.get(API_URL + '/4')
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
