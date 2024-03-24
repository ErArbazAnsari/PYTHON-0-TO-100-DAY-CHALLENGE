# Methods of Strings in Python
# Strings are immutable in python. This means that elements of a string cannot be changed once they have been assigned. We can simply reassign different strings to the same name.

myString = "!!!Hello World123xyz!!!"
print(myString)

# upper() method
upperCase = myString.upper()
print(upperCase)

# lower() method
lowerCase = myString.lower()
print(lowerCase)

# rstrip() method
rightStrip = myString.rstrip("!")
print(rightStrip)

# lstrip() method
leftStrip = rightStrip.lstrip("!")
print(leftStrip)

# replace() method
replacedString = myString.replace("Hello", "Arbaz Ansari's Programming World")
print(replacedString)


# split() method
string1 = "introduction to PYTHON programming language"
completedString = string1.split(" ")
print(string1)
print(completedString)


print(
    string1.capitalize()
)  # Capitalize the first letter of the string and make all other letters lower case.

# casefold() method
print(string1.casefold())  # Make the string lower case.

# center() method
centerString = "Welcome to Python Programming"
print(centerString.center(100))  # Center the string within the specified width.

# count() method
coutString = "Welcome to Python Programming, Arbaz Ansari"
print(
    coutString.count("o")
)  # Count the number of times a specified value occurs in a string.


# endswith() method
endString = "<b>Welcome to Python Programming, Arbaz Ansari</b>"
print(
    endString.endswith("</b>")
)  # Returns true if the string ends with the specified value.
print(endString.endswith("Python", 0, 20))  # Return True

# find() method
findString = "Welcome is Python Programming, Arbaz Ansari is a computer science student"
print(
    findString.find("11is")
)  # Search the string for a specified value and return the position of where it was found. If the value is not found, the find() method returns -1.

# index() method
indexString = (
    "Welcome is Python Programming, Arbaz Ansari is a computer science student"
)
print(
    indexString.index("Arbaz")
)  # Search the string for a specified value and return the position of where it was found. If the value is not found, the index() method raises an exception.

# isalnum() method
alnumString = "Welcometest3423"
print(
    alnumString.isalnum()
)  # Returns True if all characters in the string are alphanumeric. If not, it returns False. A character is alphanumeric if it is either a letter or a number. Example of characters that are not alphanumeric: (space)!#%&? etc.

# isalpha() method
alphaString = "WelcomeXYZ00"
print(
    alphaString.isalpha()
)  # Returns True if all characters in the string are in the alphabet. If not, it returns False. Example of characters that are not in the alphabet: (space)!#%&? etc. Example of characters that are in the alphabet: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ etc.


# islower() method
lowerString = "welcome to PYTHON programming"
print(
    lowerString.islower()
)  # Returns True if all characters in the string are lower case. If not, it returns False.

# isupper() method
upperString = "WELCOME TO PYTHON PROGRAMMING"
print(
    upperString.isupper()
)  # Returns True if all characters in the string are upper case. If not, it returns False.


# printable() method
printableString = "Welcome to Python \tProgramming"
print(
    printableString.isprintable()
)  # Returns True if all characters in the string are printable. If not, it returns False. Example of characters that are not printable: (space)!#%&? etc.

# isspace() method
spaceString = "  "  # This will return True
spaceString = " arbaz "  # This will return False
print(
    spaceString.isspace()
)  # Returns True if all characters in the string are must contains whitespaces. If not, it returns False.


# istitle() method
titleString = "Welcome to Python Programming"  # This will return false because the first letter of the word is not in uppercase.
print(
    titleString.istitle()
)  # Returns True if the string follows the rules of a title. If not, it returns False. A string is considered a title if all words in the string start with an upper case letter followed by lower case letters.


# swapcase() method
swapcaseString = "Welcome to Python Programming"
print(
    swapcaseString.swapcase()
)  # Swaps cases, lower case becomes upper case and vice versa.


# tile() method
titleString = "Welcome to python programming"
print(titleString.title())  # Make the first letter in each word upper case.
