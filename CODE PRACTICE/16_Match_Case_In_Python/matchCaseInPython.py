print("Match Case in Python")
x = int(input("enter the value: "))

match (x):
    case 0:
        print("Case 0 matches")
    case 1:
        print("Case 1 matches")
    case 2:
        print("Case 2 matches")
    case _ if x == 90:
        print("Value is 90")
    case _ if x == 80:
        print("Value is 80")
    case _:
        print("Default Case Occurs...")
