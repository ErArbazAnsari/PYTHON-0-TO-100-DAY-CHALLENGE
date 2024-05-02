class Emp:
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age

    def showdetails(self):
        print(self.name, self.salary, self.age)


class programmer(Emp):
    def language(self):
        print("the default language is hindi.")


p1 = Emp("Arbaz Ansari", 10000, 20)
p1.showdetails()

p2 = programmer("Arman",20000,15)
p2.showdetails()
