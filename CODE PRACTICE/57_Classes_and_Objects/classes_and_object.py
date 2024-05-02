class Person:
    name = "Arbaz Ansari"
    profession = "Software Devloper"

    def displayDetails(self):
        print(f"Name: {self.name}\nProfession is: {self.profession}\n")


p1 = Person()
p1.name = "Vikas"
p1.profession = "Content Writer"
# print(p1.name)
# print(p1.profession)
p1.displayDetails()

p2 = Person()
p2.displayDetails()

p3 = Person()
p3.name = "Happy Bro"
p3.profession = "Engineer"
p3.displayDetails()
