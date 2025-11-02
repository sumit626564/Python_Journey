# Join Sets
""" Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the set jsut like mathematics"""

#   I. union() and update():
#   The union() and update() methods print all items that are present in the two sets. The union() method returns a new set whereas the update() method adds items into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# insertsection() and intersection_update():
#The intersection() and intersection_update() methods print only items that are similar to both sets. The intersection() method returns a new set whereas the intersection_update() method updates the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# symmetric_difference() and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods print only items that are not similar to both sets. The symmetric_difference() method returns a new set whereas the symmetric_difference_update() method updates the existing set from another set.

cities5 = cities.symmetric_difference(cities2)
print(cities5)

# difference() and difference_update():
# The difference() and difference_update() methods print only items that are only present in the original set and not in both sets. The difference() method returns a new set whereas the difference_update() method updates the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)