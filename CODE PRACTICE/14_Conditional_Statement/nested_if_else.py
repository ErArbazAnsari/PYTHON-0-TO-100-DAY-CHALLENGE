number = int(input("Enter a number:"))

if number < 0:
    print("Number is negative")
elif number > 0:
    if number > 10 and number < 20:
        print("Number is in between 10-20")
    elif number > 20 and number < 50:
        print("Number is in between 20-50")
    else:
        print("Number is greater than 50")
else:
    print("Number is zero")