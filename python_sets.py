# Sets in Python
set1 = set() # Empty Set
print(type(set1))

#Add Values In Set
set2 = {1,2,3,1,3,1,6,5,7,4,3,5}
print(set2)
print(type(set2))

# list1 = [1,2,3,1,3,1,6,5,7,4,3,5]
# set3 = set(list1)
# print(set3)
# print(type(set3))

# Dictionary Not Empty Set
# set1 = {}
# print(type(set1)) --> <class 'dict'>

# How to itrate elements in a set
for num in set2:
    print(num)

# How to convert a set into a list
list1 = [1,2,3,1,3,1,6,5,7,4,3,5]
set5 =list(set(list1))
print(type(set5))
print(set5[-1])

# How to insert elements in set
set6 = set()
set6.add(1)
set6.add(1)
set6.add(2)
set6.add(3)
set6.add(4)
set6.add(2)
set6.add(5)
set6.add(4)
print(set6)

# use of update method
tmp = [1,2,3,4,1,4,5,2,6,7,3,7,8,9,10,8,9]
set6.update(tmp)
print(set6)

# calculate the lenght of a set
print(len(set6))


# Set Operations
set_a = {1,2,3,4,5,6,}
set_b = {1,4,7,9,8,6}

# Union Operation
print(set_a | set_b)

# Intersection
print(set_a & set_b)

# Differences In Sets
# A - B --> Keep All Elements Of Set A Except Which Are In Set B
print(set_a - set_b)
# B - A --> Keep All Elements Of Set B Except Which Are In Set A
print(set_b - set_a)

# Comparison In Sets
set_x = {1,2,3,4,5,6} # (1,2,3,4,5,6)
set_y = {1,4,2,5,3,6} # (1,2,3,4,5,6)
print(set_x == set_y)

set_x = {1,2,3,4,5,6,7} # (1,2,3,4,5,6,7)
set_y = {1,4,2,5,3,6} # (1,2,3,4,5,6)
print(set_x == set_y)