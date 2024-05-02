import time
import random

Time1 = time.time()
list1 = [i**999 for i in range(10000) if i % 2 == 0]
Time2 = time.time()
print(list1)
print("\n\nTime Taken:", (Time2 - Time1) * 10, "Seconds")
