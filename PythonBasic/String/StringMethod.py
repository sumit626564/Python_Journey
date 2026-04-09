'''String Methods
    Python provides a set of built-in methods that we can use to alter and modify the strings.

    1. upper() 
            """The upper()  method converts a string to upper case. """
    2. lower()
            The lower()  method converts a string to lower case.
    3. strip()
            The strip() method removes any white spaces before and after the string
    4. rstrip()
            The rstrip() removes any trailing characters.
    5. replace()
            The replace() method replaces a string with another string.
    6. split()
                The split() method splits the given string at the specified instance and returns the separated strings as list items.
    7. capitalize()
                The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase
    8. center()
    9. count()
    10. endswith()
    11. find()
    12. index()

'''

str1 = "AbcDEfghIj"
print(str1.upper())
print(str1.lower())

str2 = " Silver Spoon "
print(str2.strip())

str3 = "Hello !!!"
print(str3.rstrip("!"))

str4 = "Silver Spoon Sp"
print(str4.replace("Sp", "M"))

print(str4.split(" "))