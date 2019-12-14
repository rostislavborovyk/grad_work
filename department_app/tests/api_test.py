import unittest
import requests

API_URL = 'http://localhost:5000/employees/api'


class TestApi(unittest.TestCase):

    def test_get(self):
        response = requests.get(API_URL + '/4')
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
