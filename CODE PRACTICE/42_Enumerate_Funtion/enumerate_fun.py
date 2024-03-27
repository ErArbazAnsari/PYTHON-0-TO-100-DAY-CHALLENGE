marks = [10, 20, 30, 40, 50]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Very Good Arbaz")
#     index+=1


for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Very Good Arbaz")


# Loop over a list and print the index (starting at 1) and value of each element
fruits = ["Cappie", "mango", "banana"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
