from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import InputRequired
#Creacion del formulario
class Task(FlaskForm):
    name = StringField('Name', validators=[InputRequired()]) 
    file = FileField('Document', ) 