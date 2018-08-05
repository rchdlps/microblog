import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # os.environ.get('MAIL_SERVER') 'smtp.gmail.com'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # int(os.environ.get('MAIL_PORT') or 25) '587'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # os.environ.get('MAIL_USE_TLS') is not None '1'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    # os.environ.get('MAIL_USERNAME') 'lopes.dexatec@gmail.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['rchdlps@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['pt', 'en', 'es']
    # key from Microsoft =
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
