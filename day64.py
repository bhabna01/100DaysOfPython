class Library:
    books = []
    no_of_books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = self.no_of_books+1

    def getBook(self):
        return self.books

    def getNumOfBooks(self):
        return len(self.books)


book1 = Library()
book1.addBook("ReclaimYourHeart")
print(book1.getBook())
book2 = Library()
book2.addBook("Don't be sad")
print(book2.getBook())
print(book2.getNumOfBooks())
