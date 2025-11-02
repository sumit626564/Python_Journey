str4 = "Captain"
str5 = "Americe"
print(str4 + "  " + str5)

# So what's the solution..?
# We make use of the "format()" method. The  format() method places the arguments  within the  string  wherever the placeholder specified
name = "Guzman"
age = 18
statment = "My name is {} and age is {}."
print(statment.format(name, age))

'''We can also make use of indexes to place the arguments in a specified order.'''
Quantity = 2
fruit = "Apples"
cost = 120.0
stm = "I want to buy {2} dozen {0} for {1}$"
print(stm.format(fruit, cost, Quantity))