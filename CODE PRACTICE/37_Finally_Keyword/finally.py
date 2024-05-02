def abc():
    try:
        list1 = [1, 2, 3]
        data = int(input("Enter Value: "))
        print(list1[data])
        return 1
    except:
        print("Some error is occured.")
        return 0
    # print("I am always executes.")
    finally:
        print("I am always executes.")


print(abc())
