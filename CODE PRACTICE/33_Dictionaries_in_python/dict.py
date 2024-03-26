#  Dictionaries in python
#  Dictionaries stored the data in ordered way

dict = {"Name": "Arbaz Ansari", "Roll_No": 24018, "Section": "CSE-1"}
print(dict["Name"])
print(dict["Roll_No"])
print(dict["Section"])

print("\nDictionary Data\n", dict)


# to access perticular data
# print(dict["Name"])
# print(dict.get["Roll_No"])

print(dict.keys())
print(dict.values())

list1 = []
for key in dict.keys():
    list1.append(dict[key])

print(list1)

print("\n\n", dict.items())
