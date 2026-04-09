"""
What are String...?
In Python, Anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data.
"""
''' String are used whenworking with Unicide characters.'''
name = "Sumit"
print("Hello, " +  name)  # This method is used in Java
print("hello: ", name)      # is the method of Python

# It does not matter whether you enclose your string in single or double quotes, teh output remains the same.
'''Sometimes, the user migth need to put quotation marks in between the string.
    Consider the sentence: He said, "I want to eat an apple".'''

# Wrong way ------------>  print("He said, "I want to eat an apple".") 

# Right way
print('He said, "I want to eat"') 
#OR
print("He said, \"I want to eat an apple\".")


# If you want to write multiline strings..?
'''Sometimes the programmer might want to include a note, or  a set of instructions, or just might want to explain a place of code.
    Although this might be done using multiline comments, the programmer may want to display this in execution of Programmer.
        This is done using multiline strings.'''

receipe = """
1. Heat the pan and add oil
2. Crack the  egg
3. Add  salt in egg and mix well
4. Pour the mixture in pan
5. Fry on medium heat
"""
print(receipe)

note = '''
This is a multiline string
It is used  to display multiline message in the program
'''
print(note)