"""
Main module for running the app in production
"""

from department_app.main import app

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
