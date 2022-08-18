import os

file_path = os.path.abspath(os.getcwd())+"\database_school.db"
#FICHERO CONFIGURACION DE NUESTRO ENTORNO
class Config(object):
    SECRET_KEY = os.environ.get("MY_SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True              #tipoDB://usuario:pasword@servidor/nombreDB
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/flasksql'
    SQLALCHEMY_DATABASE_URI = 'postgresql://nsjjmjjbuliuzo:adbac41d4c795c5715ea958a63234982856309bfeb7e7d313bfdf518c9182311@ec2-52-210-97-223.eu-west-1.compute.amazonaws.com/den809vt5139qn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False