#from flask import Blueprint, render_template, request, redirect, url_for
import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from myapp.task import operationsCRUD #mandar a llmar el archivo 
from myapp.task import forms
from myapp import config
from werkzeug.utils import secure_filename


#taskRoute = Blueprint('task', __name__, url_prefix='/task') #conjunto de rutas definidas que van a estar dentro del modulo
#task_list = ['tasks 1', 'tasks 2', 'tasks 3']
taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')

#Creacion de rutas en el modulo rutas, todas estas son rutas que definimos 
@taskRoute.route('/') #aqui muestra todo el contenido de la tabla "task" index
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items) #consulta a la base 
    #return render_template('dashboard/task/index.html', tasks=task_list)# manda a llamar la lista de arriba 
    return render_template('dashboard/task/index.html', tasks=operationsCRUD.getAll())

@taskRoute.route('/<int:id>') # solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    #aqui podemos meter la funcion de borrar y posterior la pagina
     if id != None and id != "":
        #del task_list[id]
        operationsCRUD.delete(id)
        return redirect(url_for('task.index'))

@taskRoute.route('/create', methods=('GET','POST'))#crear pagina que tenga un formulario, usar get y post sirven para enviar info, get para info x y post para info sensible
def create():
    #task = request.form.get('task') #de una peticion estamos obteniendo un formulario de ese vamos a obtener task y sus valores y se guarda en taks
    #if task != None and task != "": #si task no es es none o no es cadena vacia 
        #task_list.append(task) # mete la tarea a ese arreglo
        #return redirect(url_for('task.index')) #lo estamos mandando a llamar arriba lo estamos retornando a la funcion index de task 
    #return render_template('dashboard/task/create.html')

    form = forms.Task()
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data)
       return redirect(url_for('tasks.index'))
    return render_template('dashboard/task/create.html', form=form)
    

@taskRoute.route('/update/<int:id>', methods=['GET','POST']) 
def update(id:int):
    #task = request.form.get('task')
    #if task != None and task != "":
        #task_list[id] = task

        task = operationsCRUD.getById(id, True)
        form = forms.Task()
    
        if request.method == 'GET':
            form.name.data = task.name
    
        if form.validate_on_submit():
            operationsCRUD.update(id, form.name.data)
        
            print(form.file.data)
            print(form.file.data.filename)
            f = form.file.data
            if f and config.allowed_extensions_file(form.file.data.filename):
            
                filename = secure_filename(f.filename)
                f.save(os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'], filename))

        #return redirect(url_for('task.index'))
        
    #return render_template('dashboard/task/update.html') #Al usuario le estamos diciendo con que datos vamos a darle
        return render_template('dashboard/task/update.html', form=form, id=id)