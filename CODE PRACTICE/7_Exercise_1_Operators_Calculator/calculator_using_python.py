def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def myCalculator():
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Addition: ", sum(num1, num2))
    elif choice == 2:
        print("Subtraction: ", sub(num1, num2))
    elif choice == 3:
        print("Multiplication: ", mul(num1, num2))
    elif choice == 4:
        print("Division: ", div(num1, num2))
    else:
        print("Invalid Choice")


myCalculator()
