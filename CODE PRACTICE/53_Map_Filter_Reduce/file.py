def cuber(x):
    return x * x * x


print(cuber(10))

oldList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
# for data in oldList:
#     newList.append(cuber(data))

newList = list(map(cuber, oldList))
print(newList)


# Filter in python
def mymenthod(a):
    return a > 4


# list1 = list(filter(mymenthod, oldList))
list1 = list(filter((lambda a: a>4),oldList))
print(list1)
