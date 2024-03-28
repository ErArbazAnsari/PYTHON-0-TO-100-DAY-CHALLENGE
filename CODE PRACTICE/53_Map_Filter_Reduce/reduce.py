from functools import reduce

numbers = [5, 10, 15, 20, 25, 30]
ans = reduce((lambda x, y: x + y), numbers)
print(ans)
