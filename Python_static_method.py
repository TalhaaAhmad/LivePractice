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

# Print instance variables of an object
print(emp1.emp_name)
print(emp1.emp_salary)

# Lets access Class variable from instance itself
print(emp2.empCount)
print(emp3.empCount)

# Explicitly Changing Class Variables
emp3.empCount = 10
emp1.empCount = 15
emp2.empCount = 20

# Checking The Impact of Explicitly Changing the Class Variable
print(emp3.empCount)
print(emp2.empCount)
print(emp3.empCount)

# Accessing The Class Variable With Class Name
print(Employee.empCount) # We Will Get The Shared Value Which is EmpCount = 3


# What Is Static Method In Python?
class Car:
    # Constructor of a class
    # It is mainly used for assignment of instance variables
    def __init__(self, name, color):
        # Instance Variables or Instance Attributes
        self.car_name = name
        self.car_color = color

     # Method of a class
    def displayCarDetails(self): # Self keyword is a reference to current object of class
        # Display Car Details
        print("Car Name : ", self.car_name)
        print("Car Color : ", self.car_color)

    # Static Method Creation
    @staticmethod
    def initialMessage():
        print("Nice Car !!!")

# Calling Methods Without creating Objects
Car.initialMessage()
"Car.displayCarDetails()" # Error Not a Static Method

# Creating Object and Calling Method By Its Object
car1 = Car("XUV 700", "RED")
car1.displayCarDetails()

# Now Again Calling Method With Class Name
"Car.displayCarDetails()" # Still Getting Error Required One Positional Argument Self

# iNeuron Student
class Student:
    
    # Static Method
    @staticmethod
    def isStudent():
        print('I am a Student of iNeuron !!')

# Calling Static Method
Student.isStudent()

# Another Example with Parameters
class Calculation:

    # Static Method
    @staticmethod
    def addTwoNumbers(num1, num2):
        print("Sum Of Two Numbers : ", num1 + num2)

Calculation.addTwoNumbers(10, 15)



