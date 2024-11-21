''' Este archivo se utiliza para realizar la importacion de las configuraciones globales
    tales como la importacion de la app, las rutas generales del proyecto, definir si el
    servidor corre en modo debug, Registro de la BD, etc.'''

from flask import Flask, render_template, request #render la utilizamos para  devolver el html y el template son las plantillas(cosas que se jalan de la base de datos)
from flask_sqlalchemy import SQLAlchemy #orm que va a mapear nuestro codigo a codigo sql 
from myapp.config import DevConfig 


app = Flask(__name__) #template_folder="/pages" utilizar el framework flask para hacer un objeto global "app"
#app.register_blueprint(taskRoute) # configurar, tomar rutas que se encuentren en el archivo
#app.debug = True
app.config.from_object(DevConfig) #config. para decirle al servidor si se ejecuta en modo produccion(publico sin errores) o modo desarrollo(aun en desarrollo)

#Para la configuracion de la BD
db = SQLAlchemy(app) #app objeto principal 
from myapp.task.controllers import taskRoute
app.register_blueprint(taskRoute)
#Para la creacion de las tablas en la base de datos
with app.app_context(): #arrancar la base de datos
    db.create_all()


@app.route('/') #esta es una ruta global
def hello_world() -> str: #esto es una tupla y la va a guardar abajo
    name = request.args.get('name', 'Valor por defecto')
    return render_template('index.html', task="Josue",name=name) #aqui nos va a regresar un html con los datos que metimos y los de la base de datos 
