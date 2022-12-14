# Links the database with your routes, by creating input forms. 

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, IntegerField

# from application.models import EmployeeModel

class EmployeeForm(FlaskForm):
    employee_id = IntegerField("employee_id")
    name = StringField("Name")
    fk_did = IntegerField("Department_id")
    age =IntegerField("age")
    position = StringField("position")
    submit = SubmitField("Submit")
    
class DepartmentForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")



    
