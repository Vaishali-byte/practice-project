from asyncio import Task
from wsgiref import validate
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Departments, EmployeeModel
from application.forms import EmployeeForm, DepartmentForm
from application.models import Departments, EmployeeModel

 # READ BOTH DATABASES
@app.route('/', methods=['POST','GET'])
def RetrieveList():
    employees = EmployeeModel.query.all()
    departments = Departments.query.all()
    return render_template('data.html',title="current employees", employees = employees, departments = departments)


# CREATE DEPARTMENT INFORMATION
@app.route('/data/createdepartment', methods = ['GET','POST'])
def createdepartment():
    form = DepartmentForm()
    if form.validate_on_submit():
        departments = Departments(name = form.name.data)
        db.session.add(departments)
        db.session.commit()
        return redirect(url_for('RetrieveList'))
    return render_template('createdepart.html', title= "Add anew department", form=form)

 # CREARE EMPLOYEE INFORMATION
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    form = EmployeeForm()
    if form.validate_on_submit(): 
        employees = EmployeeModel(name = form.name.data, age = form.age.data, position = form.position.data, fk_did = form.fk_did.data)
        
        
        db.session.add(employees)
        db.session.commit()
        return redirect(url_for('RetrieveList')) 

    return render_template('createpage.html', title="Employee information is created", form=form)

# UPDATE DEPARTMENT INFORMATION
@app.route('/data/updatedepartment/<int:did>', methods = ['GET','POST'])
def updatedepartment(did):
    form = DepartmentForm()

    departments = Departments.query.get(did)

    if form.validate_on_submit():
        departments.name = form.name.data
        db.session.commit()
        return redirect(url_for('RetrieveList'))
    elif request.method ==  'GET':
        form.name.data = departments.name
    return render_template('updatedepartment.html', title="update your department", form=form) 
    
# UPDATE EMPLOYEE INFORMATION
@app.route('/data/update/<int:id>', methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.get(id)
    form = EmployeeForm()
    if form.validate_on_submit(): 
        employee.name = form.name.data  
        employee.age = form.age.data          
        employee.position = form.position.data   
        employee.fk_did = form.fk_did.data         
        db.session.commit()
        return redirect(url_for('RetrieveList'))
                   
    elif request.method == 'GET':
        form.name.data = employee.name
        form.age.data = employee.age
        form.position.data = employee.position
        form.fk_did.data = employee.fk_did
    return render_template('update.html', form = form)  


# DELETE EMPLOYEE INFORMATIN
@app.route('/data/delete/<int:id>')  
def delete(id):
    employee = EmployeeModel.query.get(id)    
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('RetrieveList'))  

# DELETE DEPARTMENT INFORMATION
@app.route('/deletedepartment/<int:did>') 
def deleted(did):
    departments = Departments.query.get(did)
    db.session.delete(departments)
    db.session.commit()
    return redirect(url_for('RetrieveList'))
 
    
