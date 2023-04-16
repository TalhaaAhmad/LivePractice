# How to create a class
class Employee:

    # Constructor of a class
    # It is mainly used for assignment of instance variables
    def __init__(self,name,salary):
        # Instance Variables or Instance Attributes
        self.emp_name = name
        self.emp_salary = salary

    # Method of a class
    def displayEmployeeInfo(self): # Self keyword is a reference to current object of class
        print("Employee Name : ",self.emp_name)
        print("Employee Salary : ",self.emp_salary)

# Object Creation
emp1 = Employee('Talha Ahmad', 1000)
emp2 = Employee('Haris Khan', 2000)
emp3 = Employee('Junaid Khan', 3000)


# Calling the displayEmployeeInfo() method
emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()
emp3.displayEmployeeInfo()


# What is the difference between Class Variable and Instance Variable