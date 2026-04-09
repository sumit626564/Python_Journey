# Change List Items
"""Changing item from a list is easier; you just have to specify the index where you want to replace the item with an existing item"""
names = ["Haary", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)

# You can also change more than a single item at once. To do this. just specify the index range over which you want to change the items.
names[2:4] = ["Juan","Anastasia"]
print(names)

#==================================
# What if the range of the index is more than the list of items provided...?
# In this case, all  the items within the index range of the original list are replaced by the items that are provided.
names[1:4] = ["Juan", "Anastasia"]
print(names)