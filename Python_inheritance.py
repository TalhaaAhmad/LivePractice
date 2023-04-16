# Inheritab=nce in Python

# Base Class aka Parent Class
class Person():

    # Contructor
    def __init__(self, name):
        self.name = name

    # Method Of The Class
    def displayName(self):
        print("Name : ",self.name)

    # By Default We Can Say That Particular Person Is Unemployed
    def isEmployed(self):
        print("{} is Un-Employed !!".format(self.name))


# Derived Class aka Child Class    
class Employee(Person):

    # Derived Class Constructor
    def __init__(self, emp_name, id_num, salary, designation):
        self.idNUmber = id_num
        self.empSalary = salary
        self.empDesignation = designation

        # Calling Constructor of Base Class By Using Class Name
        "Person.__init__(self,emp_name)"
        # Calling Constructor of Base Class By Using super()
        super().__init__(emp_name)

    # Derived Class Method
    def isEmployed(self):
        print("{} is Employed !!".format(self.name)) 

    # Display Employee Details
    def empDetails(self):
        print("Employee Id Number : {}".format(self.idNUmber))
        print("Employee Salary : {}".format(self.empSalary))
        print("Employee Designation : {}".format(self.empDesignation))

    

# Parent Class Object
"""
Parent Class Have Only Constructor

emp1 = Person("Talha")
emp1.displayName()
emp1.isEmployed()

"""

# Child Class Object
"""
Child Class Have No Constructor

emp2 = Employee("Ahmad")
emp2.displayName()
emp2.isEmployed()

"""

# Creating Object Of Child Class With Constructor
emp3 = Employee("Talha Ahmad", 101, 1500, "Data Engineer")

# Calling Different Methods
emp3.displayName()
emp3.isEmployed()
emp3.empDetails()