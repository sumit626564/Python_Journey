import ListIndex as li

# Add List Items
'''There are three  methods to add  items  to a list append(), insert(), and extend()'''

# append():
# This method appends item to the end  of existing list
li.colors.append("Sumit")
print(li.colors)

# insert()
# This method inserts an item at the given index. The user has to specify  the index and the item to be insetred within the insert() method
li.colors.insert(1, "green") 
print(li.colors)

#============================================================================================================================================

'''What if you want to append an entier list or any other collection (set, tuple, dictionary) to the existing list?'''
# extend():  --> This method adds an entier list or any other collection datatype(set, tuplle, dictionary) to the existing list.

# Example 1: add to list in a existing list
print(li.colors)  # print the existing list
rainbow = ["green", "yellow", "orange", "red"]
li.colors.extend(rainbow)
print(li.colors)

# add tuples in list
cars = ["Hyundai", "Tata", "mahindra"]
cars2 = ("Mercedes", "Volkswagen", "BMW")   # tuples with in brackets ()
print(type(cars2))
cars.extend(cars2)
print(cars)

# add a set to a list
car3 = ["Tata","Safari","Scorpio"]
cars4 = {"Nexon", "Volvo", "Tvs"}
print(type(cars4))
car3.extend(cars4)
print(car3)

# add a dictionary to a list
students = ["Sumit", "Aaditya", "Ritika"]
students2 = {"Yash": 18, "Devika":19, "Sumit":23, "Niharika":24}   #only adds key, does not  add values
print(type(students2))
students.extend(students2)
print(students)

#=======================================================================================================
# Concatenate two lists:
# You can simply concatenate two lists to join them

colors2 = ["Yellow", "Blue"]
print(students + colors2)