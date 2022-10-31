from flask import url_for 
from flask_testing import TestCase
from application import app, db 
from application.models import Departments, EmployeeModel

class TestBase(TestCase):
    def create_app(self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="Test_Example_key",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app 

    def setup(self): 
        # Create tables
        db.create_all()
#This will be called before every test. It is creating a database with a test game and a test customer.
    def setUp(self):
        db.create_all()
        department1 = Departments(name="department1")
        db.session.add(department1)
        db.session.commit()
        employee1 = EmployeeModel(name="TestName1",age="TestAge1", position="TestPosition1", fk_did=department1.did)
        db.session.add(employee1)
        db.session.commit()
# This will be called after every test to close the database session and remove its contents.
    def tearDown(self):
        db.session.remove()
        db.drop_all()
# This is a test class for READ functionality.
class TestViews(TestBase):
    def test_RetrieveList_get(self):
        response = self.client.get(url_for('RetrieveList'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestDepartment1", response.data)
        self.assertIn(b"Testemployee1", response.data) 

# These are tests for the CREATE functionality.
class TestViews(TestBase):
    def createdepartment():
        def test_createdepartment_get(self):
            response = self.client.get(url_for('createdepartment'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Testdepartment1", response.data) 
class TestViews(TestBase):
    def createdepartment():
        def test_createdepartment_get(self):
            response = self.client.post(url_for('createdepartment'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Testdepartment1", response.data) 
class TestViews(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", response.data)
class TestViews(TestBase):
    def test_create_get(self):
        response = self.client.post(url_for('create'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", response.data)

# These are tests for the UPDATE functionality.
class TestViews(TestBase):
    def test_updatedepartment_get(self):
        response = self.client.get(url_for('updatedepartment'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", 1, response.data)
class TestViews(TestBase):
    def test_updatedepartment_post(self):
        response = self.client.post(url_for('updatedepartment'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", 1, response.data)
    def test_update_get(self):
        response = self.client.get(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", 1, response.data)
    def test_update_post(self):
        response = self.client.post(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", 1, response.data)

# These are tests for the DELETE functionality.
class TestViews(TestBase):
    def test_deleted_post(self):
        response = self.client.get(url_for('RetrieveList'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestDepartment1", 1, response.data)
# class TestViews(TestBase):
    def test_delete_post(self):
        response = self.client.post(url_for('RetrieveList'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Testemployee1", 1, response.data)


