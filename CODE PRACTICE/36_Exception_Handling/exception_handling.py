# Exception Handling in python
# table = input("Enter Table Number: ")

# try:
#     for i in range(1, 11):
#         print(f"{table} X {i} = {int(table)*i}")
# except Exception as e:
#     print("Your Response is Invalid!!!\n", e)

# print("\n\nImportant Code of Program")
# print("Program is Ended...")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")
