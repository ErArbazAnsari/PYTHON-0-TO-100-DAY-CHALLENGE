tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print("Count of 3 in tuple1 is:", res)


tuple2 = (1, 2, 3, 4, 5)
print("\nTupe Value:", tuple2)
print("\nTupe Length:", len(tuple2))

newList = list(tuple2)
newList.append(1000)
tuple2 = newList
print("\nTupe Value:", tuple2)
print("\nTupe Length:", len(tuple2))
