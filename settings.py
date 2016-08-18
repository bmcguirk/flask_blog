import os

SECRET_KEY = b"\xb9[\x9a\x16\xce\xa7/}\xa1\x85\x94\xcaJyl4h\x18\xcd\x9d\x8b\x85O\x9eW\xf7V\x9a\xd0B\xc2'"
DEBUG = True
DB_USERNAME = 'brianmcguirk'
DB_PASSWORD = ''
BLOG_DB_NAME = 'blog'
DB_HOST = os.getenv('IP','0.0.0.0')
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True