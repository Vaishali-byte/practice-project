from flask import Flask,render_template,request,redirect, url_for
import application
from application.models import db,EmployeeModel
from application import app, db, forms 
from application.forms import EmployeeForm
#from flask import abort

 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    form = EmployeeForm()
    if form.validate_on_submit(): 
        employees = EmployeeModel(name = form.name.data, age = form.age.data, position = form.position.data)
        
        db.session.add(employees)
        db.session.commit()
        return redirect(url_for('RetrieveList'))    

        
    return render_template('createpage.html', form = form)
 
 
@app.route('/', methods=['GET'])
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template('data.html', employees = employees)
 
 
@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"
 
 
@app.route('/data/update/<int:id>', methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.get(id)
    form = EmployeeForm()
    if form.validate_on_submit(): 
        employee.name = form.name.data  
        employee.age = form.age.data          
        employee.position = form.position.data            
        db.session.commit()
        return redirect(url_for('RetrieveList'))
                   
    elif request.method == 'GET':
        form.name.data = employee.name
        form.age.data = employee.age
        form.position.data = employee.position
    return render_template('update.html', form = form)
 
    
@app.route('/data/delete/<int:id>')
def delete(id):
    employee = EmployeeModel.query.get(id)    
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('RetrieveList'))      
 
    
