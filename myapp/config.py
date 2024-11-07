class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config): #nuestro servidor arranca en modo desarrollo porque esta en true, si fuera false estaria en modo produccion 
    DEBUG = True #debug significa "desarrollo"
    