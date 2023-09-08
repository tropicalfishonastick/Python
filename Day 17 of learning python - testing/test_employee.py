'''Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.'''

import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    return Employee("John", "Doe", 50000)

def test_give_default_raise(employee_instance):

    employee_instance.give_raise()
    assert employee_instance.annual_salary == 55000

def test_give_custom_raise(employee_instance):
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 60000

'''Here's an explanation of the code:
In employee.py, we define the Employee class with an __init__ method to initialize the employee's attributes: first name, 
last name, and annual salary. It also includes a give_raise method that adds a default raise of $5,000 to the annual salary unless a 
custom raise amount is specified.
In test_employee.py, we import the necessary modules and create a fixture called employee_instance that returns an instance of the Employee 
class with some initial values.
We write two test functions:
test_give_default_raise: This function tests whether the give_raise method correctly adds the default raise of $5,000 to the annual salary. 
We use the employee_instance fixture to create an employee and perform the test.
test_give_custom_raise: This function tests whether the give_raise method correctly adds a custom raise amount of $10,000 to the annual salary. 
Again, we use the employee_instance fixture.'''