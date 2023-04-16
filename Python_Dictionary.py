# Dictionary In Python
dict1 = {}
print(type(dict1))

# How to insert values in Dictionary
dict2 = {}
dict2["Name"] = "Talha Ahmad"
dict2["Age"] = 21
dict2["Skills"] = ["Python","Java","SQL"]
dict2["Jobs"] = ("Data Analyst","Data Engineer")
dict2[1710111290553] = "ID Number"
#print(dict2)

#Nested Dictionary : Dictionary within Dictionary
#By Creating Another Dictionary
dict3 = {"Color" : "Blue", "Nationality" : "Pakistan"}
dict2["Other_Details"] = dict3

#By Direct Assigning Values In The Form Of Dictionary
dict2["Other"] = {"Sport" : "Cricket", "Language" : "Urdu"}

#print(dict2)

#Check Lenght Of Dictionary
print(len(dict2))

#How To Access The Value Of A Particular Key
print(dict2["Name"])
print(dict2["Skills"])

#how to print secondary skill of Talha
print(dict2["Skills"][1]) # dict2["Skills"] is used as List Variable here For Displaying Secondary Skill

# Explanation
# temp = dict2["Skills"] -- dict2["Skills"] Returns A List And Store In Variable temp
# print(temp)
# print(temp[1]) -- Simple List Indexing For Accessing A Particular Value

#How To Know The Nationality Of Talha
print(dict2["Other_Details"]["Nationality"]) # Same Concept As Used For List in a Dictionary

# Overview
# dict2["Skills"] --> List Is Returned As Output
# dict2["Other_Details"] --> Dictionary Is Returned As Output


#How To Update Value On A Particular Key
dict2["Age"] = 22
print(dict2["Age"])

#How To Get The Keys From A Dictionary
total_keys = list(dict2.keys())
print("Toatal Keys In Dictionary : ",total_keys)

#How To Get Values From A Dictionary
total_values = list(dict2.values())
print("Toatal Values In Dictionary : ",total_values)

#How To Itrate Over A Dictionary
for k,v in dict2.items(): # -- dict2.items() returns a list key, values pair
    print(k," : ",v) 

# Compare Dictionary ??
dict4 = {'a' : 1, 'b' : 2, 'c' : 3}
dict5 = {'b' : 2, 'c' : 3, 'a' : 1}
print(dict4 == dict5) # --> True Because Dictionary is a Non-Sequential Data Structure

# How to delete specific key value pair from dictionary
print(dict2)
del dict2["Other"]
del dict2[1710111290553]
print(dict2)

# How to check if key exist in dictionary
# print(dict2.has_key("Skills")) --> Suported In Python 2 not in Python 3
keys_in_dict = list(dict2.keys())
if "Skills" in keys_in_dict:
    print(True)
else:
    print(False)