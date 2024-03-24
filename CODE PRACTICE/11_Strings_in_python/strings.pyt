# Strings in python programming language.
# Strings are used in python programming language to record text information, such as name. Strings in python are actually a sequence, which basically means python keeps track of every element in the string as a sequence. For example, python understands the string "hello" to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

# This idea of a sequence is an important one in python and we will touch upon it later on in the future.

name = "Saurabh"
print(name)

# Indexing in python
print(name[1])

# Slicing in python
print(name[0:7])

# Concatenation in python
print(name + name[0:2])

# string 2
string2 = "Arbaz Ansari"
print(string2)

# string 3
string3 = """this is arbaz"""
print(string3)

# string 4
string4 = """This is arbaz ansari from 4th year"""
print(string4)
for character in string4:
    print(character)

string5 = "Arbaz Ansari"
lenght_of_string = len(string5)
print(lenght_of_string)

print(string5[0:11])
