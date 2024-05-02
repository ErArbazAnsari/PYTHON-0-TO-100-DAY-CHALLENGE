# Python For Loop
"""
- A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
- It allows you to perform a set of statements repeatedly for each item in the sequence.
- The loop continues until all items in the sequence have been processed.
- The basic syntax of a for loop in Python is:
    for item in sequence:
        # code to be executed for each item

- The "item" variable represents the current item in the sequence during each iteration.
- You can choose any name for this variable.
- The "sequence" can be any iterable object, like a list, tuple, string, or range.
- The code inside the loop is indented and will be executed for each item in the sequence.
- After the code block is executed for each item, the loop moves to the next item in the sequence.
- You can use the "break" statement to exit the loop prematurely.
- The "continue" statement can be used to skip the current iteration and move to the next item.
- The "else" block can be added after the loop to specify code that should be executed once the loop is finished, but only if the loop completed normally (i.e., not terminated by a "break" statement).
"""
# Example:
name = "Arbaz Ansari"
for character in name:
    print(character, end=", ")

print("\n")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num, end=", ")

print("\n")
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for char in color:
        print(char, end=", ")
    print("\n")
