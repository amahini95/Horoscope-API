from decouple import config
'''
Basic workflow:

1. Horoscope data will be scraped from Horoscope.com.
2. Data will then be used by Flask server to send JSON response to user.
'''


#configurations (attributes) for project stored HERE
class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True