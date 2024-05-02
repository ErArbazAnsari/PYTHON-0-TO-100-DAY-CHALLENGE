import time

timeStamp = time.strftime("%H:%M:%S")
print(timeStamp)
timeStamp = int(time.strftime("%H"))
# print(timeStamp)
# timeStamp = time.strftime('%M')
# print(timeStamp)
# timeStamp = time.strftime('%S')
# print(timeStamp)

if timeStamp > 0 and timeStamp < 12:
    print("Good, Morning...")
if timeStamp > 12 and (timeStamp < 16):
    print("Good, Afternoon...")
if timeStamp > 16 and timeStamp < 24:
    print("Good, Night...")
