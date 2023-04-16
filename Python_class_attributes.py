# How to create a class
class Employee:

    # Class Attribute Or Class Variable
    empCount = 0

    # Constructor of a class
    # It is mainly used for assignment of instance variables
    def __init__(self,name,salary):
        # Instance Variables or Instance Attributes
        self.emp_name = name
        self.emp_salary = salary

        # Incrementing The Class Variable Value
        Employee.empCount += 1

    # Method of a class
    def displayEmployeeInfo(self): # Self keyword is a reference to current object of class
        print("Employee Name : ",self.emp_name)
        print("Employee Salary : ",self.emp_salary)

    # Method of a class to show value of Class Variable
    def displayEmployeeCount(self): # Self keyword is a reference to current object of class
        print("Employee Count : ",Employee.empCount)

# 1st Object Creation & Calling the displayEmployeeInfo() & displayEmployeeCount() method
emp1 = Employee('Talha Ahmad', 1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

# 2nd Object Creation & Calling the displayEmployeeInfo() & displayEmployeeCount() method
emp2 = Employee('Haris Khan', 2000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

# 3rd Object Creation & Calling the displayEmployeeInfo() & displayEmployeeCount() method
emp3 = Employee('Junaid Khan', 3000)
emp3.displayEmployeeInfo()
emp2.displayEmployeeCount()

# Checking The Value Of Class Variable
emp1.displayEmployeeCount()
emp2.displayEmployeeCount()
emp3.displayEmployeeCount()


