import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'2\x92\xd4\xb4\xa4}\x91\xe4\x18\xd8\xe9\x0c\xf4J\xfd\xcf'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    