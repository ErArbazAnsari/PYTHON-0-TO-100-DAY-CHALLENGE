newTuple = 1  # This is not a tuple. To crete a tuple with single element add comma(,) also after the value
print(newTuple)
print(type(newTuple))

# Example of Tuple in Python
myTuple = (1,)
print(myTuple)
print(type(myTuple))

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)
