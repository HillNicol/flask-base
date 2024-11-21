import psycopg2 #controlador de la base de datos 
import os

class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config): #nuestro servidor arranca en modo desarrollo porque esta en true, si fuera false estaria en modo produccion 
    DEBUG = True #debug significa "desarrollo"

    #SQLite3:
    '''BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
    DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")'''
    #MySQL:
    '''DB_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="", password="", hostname="", databasename="")'''
    #PostgreSQL:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{hostname}/{databasename}".format(username="curso", password="12345", hostname="localhost", databasename="proyecto")
