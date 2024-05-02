# Write a Library class with no_of_books and books as two instance variables. Write a Program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!


class Library:
    no_of_books = 0
    books = []

    def __init__(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def display(self):
        print(self.books)
        print("Total No. Of Books Available in Library is:", self.no_of_books)


b1 = Library("Rich Dad Poor Dad")
b1 = Library("Rich")
b1 = Library("Dad")
b1 = Library("Rich Dad Poor Dad")
b1 = Library("Rich")
b1 = Library("Dad")
b1.display()

b2 = Library("Arbaz")
print("\nLibrary 2")
b2.display()

b3 = Library("Ansari")
print("\nLibrary 3")
b3.display()
