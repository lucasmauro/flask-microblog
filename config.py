import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ultra-mega-master-blaster-secret-key'
