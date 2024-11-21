from sqlalchemy.orm import Session
from myapp.task import models
from myapp import db
def getById(id: int): #select por id 
    #task = db.session.query(models.Task).filter(models.Task.id == id).first()
    task = db.session.query(models.Task).get(id) #query para busqueda 
    #task = models.Task.query.get_or_404(id) 
    return task
    
def getAll(): # trae tdo lo de la tabla
    tasks = db.session.query(models.Task).all() #devuelve todo 
    return tasks

def create(name: str): #hacer un insert pasandole los datos id, nombre 
    taskdb = models.Task(name=name) #name hace referenciael primero al pg admon y el segundo a la variable
    db.session.add(taskdb) #se agrega
    db.session.commit()#se guarda
    db.session.refresh(taskdb) #se refresca 
    return taskdb

def update(id:int, name: str): #actualizar por id y por nombre 
    taskdb = getById(id=id) #buscar el registro 
    taskdb.name = name #lo actualiza 
    db.session.add(taskdb) #lo añade 
    db.session.commit() #lo guarda
    db.session.refresh(taskdb)
    return taskdb
    
    
def delete(id:int): #necesitamos el id
    taskdb = getById(id=id) #obtenemos el registro
    db.session.delete(taskdb) #lo borramos
    db.session.commit() #guardamos
    
def pagination(page:int=1, size:int=10): # solo nos muestra 10 de la pagina 1 
    taskdb = models.Task.query.paginate(page=page, per_page=size)
    return taskdb


