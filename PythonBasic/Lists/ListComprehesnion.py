# List Comprehension
"""List Comprehension are used for creating new lists form other iterable like lists, tuples, dictionaries, sets, and even in arrays and strings.
    Syntax:-
            List = [expression(item) for item in iterable if condition]
        
            (*) Expression it is the item which is being ierated..
            (*) iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
            (*) condition: condition checks if the item should be added to th new list or not.
"""

# Example 1: accepts items with the small letter "o" in the ne list
names = ["Milo", "Bruno", "Anastasia", "Rosa"]
namesWith_o = [summ for summ in names if "o" in summ]   # item or summ is jsut like behave variable
print(namesWith_o)