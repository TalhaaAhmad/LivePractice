# Write a program to generate the list of 10 numbers
result = []
for i in range(1,11):
    result.append(i)
print(result)

# How to do it with the help of list comprehension ?
result = [ x for x in range(1,11) ]
print(result)

# Get a list of the even numbers between 1 to 50
result = [ x for x in range(1,51) if x % 2 == 0]
print(result)

# Get a list of the even numbers from a given list
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [ x for x in list_a if x % 2 == 0]
print(result)

# Convert all string in the given list to Upper Case
list_a = ["hi" , "hello" , "bye" , "nice"]
result = [ x.upper() for x in list_a ]
print(result)

# Put all the negative numbers after positve numbers in the given list
list_a = [9,-1,2,1,-5,10,-7]
result1 = [ x for x in list_a if x > 0 ]
result2 = [ x for x in list_a if x < 0 ]
print(result1 + result2)

# OR More Comprehensed Way
result = [ x for x in list_a if x > 0 ] + [ x for x in list_a if x < 0 ]
print(result)