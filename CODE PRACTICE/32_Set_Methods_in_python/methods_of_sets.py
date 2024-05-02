# Methods of Set in python

s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 1, 2}

print("Union of Both Sets:", s1.union(s2))
print("Intersection of Both sets:", s1.intersection(s2))

# Value of set1 and set2 after above operation was untouched
print(s1, s2)

# update()
s1.update(s2)
print(s1, s2)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))

print(s1.issubset(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s1.add(3)
print(s2)
s1.remove(9)  # if element is not present error show
print(s1)

s1.discard(8)  # if element is not preset in set then error not showing.
print(s1)

deleteItem = (
    s1.pop()
)  # pop() pop any element random as we know in set data will stored in unorder way
print(s1)
print("poped item:", deleteItem)
# del s1
# print(s1)  # Error-> s1 is not defined


#  if we don't want to delete the complete set, we just want to clear the data or elements for the set, then we used clear()
s1.clear()
print(s1)

#  Item present or not
set1 = {"Arbaz Ansari", "Gurgaon"}
if "Arbaz Ansari" in set1:
    print("element is present.")
else:
    print("element is not present.")
