from flask_sqlalchemy import SQLAlchemy
from application import db
 

class EmployeeModel(db.Model):   
    employee_id = db.Column(db.Integer, primary_key=True)
    #employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    


    
 
    