"""
Allows to run migrations from the terminal
"""

from department_app.models import manager

if __name__ == '__main__':
    manager.run()
