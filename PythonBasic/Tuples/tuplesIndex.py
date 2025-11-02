# Tuples 
""" Tuples are ordered collections of data items. They store multiple items in a single variable. Tuple items are seperated by commans and enclosed within round bracked().
    Tuples are unchangeable, meaning we cannot alter them  after creation
"""
tuple1 =   (1, 2, 3, 4, 5, 6)
tuple2 = ("Sumit", "Singh", "Rajput")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)


# we can access the both type of index "positive or negative"  we had seen earlier in list
# check for item
#           We can check if a given item is present in the tuple. This is done using the "in" keyword.
country = ("Spain", "Italy", "India", "England", "Germany")
if "India" in country:
    print("India is present.")
else:
    print("Check another country")

# Range of Index:
"""You can print a range of tuple items by specifying where you want to start, where you want to end. and if you want to skip elements in between the range."""
# Syntax:-  Tuple[start : end : jumpIndex]
# Note:- "jumpIndex" is  optional. We will see this in given examples.
# Example :- Printing elements within a particular range:
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:6])  # Positive index
print(animals[-7:-2]) # negative Index