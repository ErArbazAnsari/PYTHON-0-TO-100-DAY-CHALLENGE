# def doubleValu(x):
#     return x * 2
doubleValu = lambda x: x * 2
newFun = lambda: print("You are my besty")
average = lambda x, y, z: (x + y + z) / 3
print(doubleValu(5))
print(newFun())
print(average(10, 20, 30))


def newFunction(fx, value):
    return 6 + fx(value)


x = 2
print(newFunction((lambda x: x * x), 2))
