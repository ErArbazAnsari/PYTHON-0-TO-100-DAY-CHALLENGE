class Person:
    def __init__(self, name, occupasion):
        self.name = name
        self.occu = occupasion

    def display(self):
        print(f"Hello, I'm {self.name} and I am a {self.occu}")


p1 = Person("Arbaz Ansari", "Engineer")
p1.display()
