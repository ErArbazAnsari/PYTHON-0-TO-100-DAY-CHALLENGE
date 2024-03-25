oriList = [11, 2, 30, 4, 3]
print("Ori List:", oriList)

# append()
oriList.append(60)
print("New List:", oriList)

# sort()
oriList.sort()
print("New List:", oriList)

# sort() in reverse order
oriList.sort(reverse=True)
print("New List:", oriList)

# reverse()
oriList.reverse()
print("New List:", oriList)

# extend()
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print("Printing List1 which is extend with list2:", list1)

# concatenation of two list
list3 = list2 + list1
print("Value of List 3:", list3)

# index() // Returns first occurence of the value.
print("Index of 3:", oriList.index(3))

# count() // To count number of times element present in the list.
print("Count of 60 in list is:", oriList.count(60))


# Referencing
newList = oriList
newList[0] = "Arbaz Ansari"
print(oriList)
print(newList)

# Copy()
newList = oriList.copy()
newList[0] = "Arbaz"
print(newList)


# insert()
newList.insert(0, 10000)
print(newList)
