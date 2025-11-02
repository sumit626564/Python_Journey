import ListIndex as ls

# Remove List Items
"""There are various methods to remove items from the list:
    pop()  --> This method removes the last of the list if no index is provided. if an index is provided, then it removes the item at that specified index.
    remove()   --> user for rmove
    del()      --> use for delete
    clear()     --> clear and print the list
"""

# pop()
animal  = ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey', 'goat', 'cow']
print(animal)
animal.pop()        # removes the last item fo the last
print(animal)     
print(animal[1])    # removes the using index(1) 

# What if you want to remove a specific item from the list...?
# remove():
# This method removes a specific item from the list.
animal.remove('dog')
print(animal)

# del()
# del() is not a method, rather it is keyword which deleted an item at a specific index from the list, or deleted the list entirely.
del animal[3]
print(animal)

# What if we don't want to delete the  entire list, we just want to delete all items within that list..?
# clear()   --> This method clears all items in the  list and prints an empty list.
animal.clear()
print(animal)