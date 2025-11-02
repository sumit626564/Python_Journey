# Length of a string:
# We can find the length of a string using the "len()" function

fruit =  "Mango"
len1 =  len(fruit)
print("Mango is a", len1, "letter word", len(fruit))

# String as an Array:
'''A string is essentially a sequence of characters, also called an array. Thus we can access the elements of this array.'''
pie = "ApplePie"
print("starting index of pie:",pie[:3])
print(pie[6])   # returns character at specified index

# Note: This method of specifying the start and end index to specify a part of a string is called slicing.

print("Slicing from start: ", pie[:5])
print("Slicing till end: ", pie[5:])
print("Slicing in between: ", pie[2:6])
print("Slicing using negative index: ", pie[-8:])

# Loop thorugh a string;
# Strings are arrays, and arrays are iterable. Thus we can loop through strings.
alphabets = "ABCDE"
for i in alphabets:
    print(i)