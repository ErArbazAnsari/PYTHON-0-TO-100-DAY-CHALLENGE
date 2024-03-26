#  Methods of dictionaries

ep1 = {1: 50, 2: 70, 3: 10, 4: 40}
ep2 = {5: 50, 100: 100, 200: 1}

ep1.update(ep2)
print(ep1)


# To clear the dictionary
ep2.clear()
print(ep1, "\n", ep2)


#  How to create an empty dictionary
emptyDic = {}
print(emptyDic, "\nType is :", type(emptyDic))

# To remove any key: value pair from dict.
ep1.pop(1)
print(ep1)


# To remove last value pair from dict
ep1.popitem()
print(ep1)

# to delete any dict completely
del ep2
# print(ep2) # Error occurs: ep2 is not defined

del ep1[2]  # To delete any perticular pair.
print(ep1)
