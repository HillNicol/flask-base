from flask import Blueprint

taskRoute = Blueprint('task', __name__, url_prefix='/task') #conjunto de rutas definidas que van a estar dentro del modulo

#Creacion de rutas en el modulo rutas, todas estas son rutas que definimos 
@taskRoute.route('/') #aqui muestra todo el contenido de la tabla "task"
def index():
    return 'Index'

@taskRoute.route('/<int:id>') # solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    #aqui podemos meter la funcion de borrar y posterior la pagina
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))#crear pagina que tenga un formulario, usar get y post sirven para enviar info, get para info x y post para info sensible
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST']) 
def update(id:int):
    return 'update '+str(id)