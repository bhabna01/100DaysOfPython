class Library:
    def __init__(self):
        self.books = []
        self.no_books = 0

    def addBooks(self, book):
        self.books.append(book)
        self.no_books = len(self.books)

    def showBooks(self):
        return self.books

    def getNumberOfBooks(self):
        return self.no_books


l1 = Library()
l1.addBooks("Harry Potter1")
l1.addBooks("Harry Potter2")
l1.addBooks("Harry Potter3")
print(l1.showBooks())
print("The number of books are ", l1.getNumberOfBooks())

# book2 = Library()
# book2.addBooks("SecretOfDevineLove")
# print(book2.showBooks())
# print(book2.getNumberOfBooks())
