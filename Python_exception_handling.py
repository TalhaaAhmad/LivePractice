# How to handle Exception in Python

# Some Few Basic Errors
"""
DIVISION BY ZERO ERROR
a = 10
print( a/0)

INDEX ERROR -> INDEX OUT RANGE
list_a = [1, 2, 3, 4, 5]
print(list_a[7]) 
"""

# Demonstration of try and except block         
a = 5
try: 
    """
    
    IDENTIFY THE MOST ERROR CRON AREAS IN THE CODE AND 
    PUT IT IN THE TRY BLOCK.

    """
    result = a/0
    print(result)

except:
    """

    IF SOME ERROR OCCURED IN THE TRY BLOCK
    IT WILL BE CATCH BY THE EXCEPT BLOCK AND THE FLOW 
    EXECUTION IS CHANGED.

    """
    print("Some Error Has Occured !!!")


# TRY BLOCK WITH MULTIPLE ERROR OCCURING PROBABILTY
num = 5
list_a = [1, 2, 3, 4, 5, 6, 7, 10]
dict_a = {"Talha" : 22, "Haris" : 24, "Junaid" : 21}

try:
    print("Divide By Zero")
    result = num/0
    print(result)
    print("Step 1 Done")

    print("Access 11th element from List")
    print(list_a[11])
    print("Step 2 Done")

    print("Access Value of Khalfan from Dictionary ")
    print(dict_a["Khalfan"])
    print("Step 3 Done")

except ZeroDivisionError:
    print("This Error Was Occured Because Division By 0 Happened")

except IndexError:
    print("This Error Was Occured Because Index Out Of Range")

except KeyError:
    print("This Error Was Occured Because Key Not Found")

except Exception as err:
    print("Error Occured and Message : ", err)



# TRY BLOCK WITH ELSE
a = 5
try:
    result = a/0

except ZeroDivisionError:
    print("This Error Was Occured Because Division By 0 Happened")

else:
    print("Calculation Completed !!")
    print(result)


# FINALLY BLOCK
a = 5
try:
    result = a/0

except ZeroDivisionError:
    print("This Error Was Occured Because Division By 0 Happened")

else:
    print("Calculation Completed !!")
    print(result)

finally:
    print("Doesn't Matter try-except But I Will Print Myself !!")
