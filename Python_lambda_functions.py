# How to create lambda funtion


# First normal funtion to add integer 5 to given numbers
def add_five(num):
    result = num + 5
    return result

x = 7
print(add_five(x))

# Same program using lambda function
lambda_add_five = lambda x : x + 5

y = 10
print(lambda_add_five(y))

# Write a lambbda funtion add two input numbers
lambda_add_two_nums = lambda x , y : x + y

a = 30
b = 20
print(lambda_add_two_nums(a,b))

# Write a lambda funtion to concatenate two input strings
lambda_con_two_strings = lambda st1 , st2 : st1 + " " + st2

fname = "Talha"
lname = "Ahmad"
print(lambda_con_two_strings(fname,lname))

# Write a lambda function to calculate the maximum of two numbers
def max_of_two_nums(num1,num2):
    if num1 > num2 :
        return num1
    else :
        return num2
n1 = 12
n2 = 16
print(max_of_two_nums(n1,n2))

lambda_max_q = lambda num1 , num2 :num1 if num1 > num2 else num2

n1 = 12
n2 = 13
print(lambda_max_q(n1,n2))

# How to work with map(), filter(), reduce()

# Implement map() funtion
# Write a lambda function to calculate the square of the numbers in a given list using map()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_num = lambda x : x*x
square_list = list(map(square_num, list1))
print(square_list)

# How above map() works
"""
for i in list1:
    square_list.append(i**2)
"""


# Add sequential respective elements in two given lists
list_a = [1, 2, 3, 4, 5]
list_b = [5, 4, 3, 2, 1]

# The Required Resulant Output : [6, 6, 6, 6, 6]

# Lambda Funtion 
sum_two_elements = lambda x,y : x+y

# Mapping The Lambda Function
result = list(map(sum_two_elements,list_a,list_b))

# Showing Output
print(result)

# How to use reduce() ??
# Import Reduce Function Available in Functools Library
import functools

# Calculate the sum of all the elements in the given list
list_x = [1, 3, 5, 7, 9]

# Required Result : 25

#Lambda Function
sum_of_list = lambda x,y : x+y

# Using The Reduce() Function
result = functools.reduce(sum_of_list,list_x)

# Showing Output
print(result)


# How to use filter()
# Create a list of odd numbers
list_x = [1, 2, 3, 5, 7, 8, 9, 10]

# Lambda function
filter_odd = lambda x : x % 2 != 0

# Using Filter Funtion
result = list(filter(filter_odd,list_x))

# Showing Output
print(result)