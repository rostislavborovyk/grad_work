"""
Configuration module, contains configs for different ways of running the app
"""


class BaseConfig:
    DEBUG = False
    SECRET_KEY = '8ed308dc-4028-410b-a104-09bde4f507b9'
    SQLALCHEMY_DATABASE_URI = 'mysql://wxtuYnuHC0:FfjxV5hUB4@remotemysql.com:3306/wxtuYnuHC0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://wxtuYnuHC0:FfjxV5hUB4@remotemysql.com:3306/wxtuYnuHC0'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
