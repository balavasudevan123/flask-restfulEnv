from os import environ 

SECRET_KEY = environ.get('JWT_SECRET_KEY')