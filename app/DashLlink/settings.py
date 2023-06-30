import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3' if not os.environ.get('DATABASE_URL') else os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '4128c5e3a66aba8278a0f4523f123d9c'
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')