"""
Unittests for app
"""
import unittest

from department_app import app
from department_app.views import *


class AppTest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(200, response.status_code)

    def test_departments(self):
        tester = app.test_client(self)
        response = tester.get('/departments')
        self.assertEqual(200, response.status_code)

    def test_employees(self):
        tester = app.test_client(self)
        response = tester.get('/employees')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
