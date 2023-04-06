# create a book class that represemts single books in the library
class Book:
    def __init__(self, title, author, isbn, available: bool) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
        else:
            print('Book is not available')

    def checkin(self):
        if self.available == False:
            self.available = True
        else:
            print('Book was not given out')

    def __str__(self):
        return f'Title: {self.title}; Author: {self.author}; ISBN: {self.isbn}; Available: {self.available}'                    


class Library:
    def __init__(self) -> None:
        self.library = []

    def addbook(self, book: Book):
        self.library.append(book)   

    def addbooks(self, books: list):
        for book in books:
            self.library.append(book) 

    def remove(self, book: Book):
        self.library.remove(book)

    def displayavailablebook(self):
        for book in self.library:
          if book.available == True:
              print(book)

    def searchbook(self, title, author):
        for book in self.library:
         if (book.title == title) & (book.author == author):
            print(book)
         else: 
            print('Could not find book in the library')        

book1 = Book('Harry Potter', 'John Brown', 'ISBN019939400', True)
book2 = Book('Things fall apart', 'Chinwe Achebe', 'ISBN01253670', True)
book3 = Book('Americana', 'Chimamanda', 'ISBN495937445', True)

nationalLibrary = Library()
nationalLibrary.addbook(book3)

nationalLibrary.searchbook('Americana', 'Chimamanda')
