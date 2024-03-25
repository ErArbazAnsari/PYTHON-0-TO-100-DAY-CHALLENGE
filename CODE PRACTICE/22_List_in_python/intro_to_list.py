# list are ordered pair of data items
# They store multiple values in a single veriable
# List items are separated by commas and enclosed within square brackets []
# Lists are changeable meaning we can alter them after creation.
# item available in the list has its own index address. start with 0

list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

list1.append(1)
print("Printing data")
print(list1[-3])
print(list1[len(list1) - 3])
print(list1[6 - 3])
print(list1[3])
print(list1)
print("Printing of list1 data is over")
list2 = [1, "Arbaz Ansari", 24018, "Section-A", True]
print(list2)

print("\n\nIf 24018 is present is list2 print 'Yes'")
if "Arbaz" in list2:
    print("Yes")
else:
    print("Searching element is not present int list2")

# Same things is applied for strings as well
if "Ara" in "Arbaz Ansari":
    print("Yes")
else:
    print("No")
