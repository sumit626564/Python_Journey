'''Each item/element in a list has its own unique index. This index can be used to access any particular item from the list.
    The first item has index [0], the second item has index [1], the third item has index [2], and so on.
'''


"""=========> Accessing list items <==============="""

# Positive Indexing
'''As we have seen that list have index, we can access items using these indexes.'''
colors = ["Sumi", "Singh", 12, 133.2]
print(colors[2])
print(colors[0])
print(colors[3])

# Negative Indexing
''' Similar to positive indexing, negative indexing is also used to access items, but from the end of the list.
    The last item has index [-1], the second[-2], the third last index item has index [-3], and so on.
'''
print(colors[-1])

# Check for item:
''' We can check if a given item is present in the list. This is done using in keyowrd.
'''

if "Sumit" in colors:
    print("Sumit is present.")
else:
    print("Sumit is not present.")

# Range of Index
'''You can print a range fo list items by specifying where you want to start, where you want to end,
    and if you want to skip elements in between the range.

    Syntax=> List[start : end : jumpIndex(optional)]
'''
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7]) # using the positive indexes
print(animals[-7:-2]) # using the negative indexes

'''Note: The element of the end index provided will not be included.

Example: printing all elements from a given index till the end

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes'''