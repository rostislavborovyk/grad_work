"""
Unittests for app
"""

import unittest

from department_app import app


class AppTest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')


if __name__ == '__main__':
    unittest.main()
