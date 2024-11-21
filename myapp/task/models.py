
#archivos mas importantes que necesitamos para la base de datos, aqui creamos todas las tablas para la bd
from myapp import db 
#Creacion de los modelos
class Task(db.Model):
    __tablename__='tasks' # nombre
    id=db.Column(db.Integer, primary_key=True) #campo 
    name=db.Column(db.String(255)) #campo 

    