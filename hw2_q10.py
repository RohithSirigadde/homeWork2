class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def adding_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"New book '{book}' added to the library.")
        else:
            print(f"Book '{book}' already exists in the library.")

    def removing_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' does not exist in the library.")

    def finding_book(self, book):
        if book in self.books:
            print(f"Book '{book}' is available in the library.")
        else:
            print(f"Book '{book}' is not available in the library.")

    def adding_patron(self, patron):
        if patron not in self.patrons:
            self.patrons.append(patron)
            print(f"New patron '{patron}' added to the library.")
        else:
            print(f"Patron '{patron}' already exists in the library.")

    def removing_patron(self, patron):
        if patron in self.patrons:
            self.patrons.remove(patron)
            print(f"Patron '{patron}' removed from the library.")
        else:
            print(f"Patron '{patron}' does not exist in the library.")

    def borrowing_book(self, book, patron):
        if book in self.books:
            self.books.remove(book)
            patron.borrowed_books.append(book)
            print(f"Patron '{patron}' borrowed the book '{book}'.")
        else:
            print(f"Book '{book}' is not available in the library.")

    def return_book(self, book, patron):
        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            self.books.append(book)
            print(f"Patron '{patron}' returned the book '{book}'.")
        else:
            print(f"Book '{book}' was not borrowed by patron '{patron}'.")

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __repr__(self):
        return self.name


# Creating library instance
library = Library()

# Adding books
library.adding_book("Nightmare Abbey")
library.adding_book("The Piligrim's Progress")
library.adding_book("Moby-Dick")

# Adding patrons
library.adding_patron("Rohtih")
library.adding_patron("Nithin")
library.adding_patron("Srinath")

# Borrowing books
patron1 = Patron("Rohith")
library.borrowing_book("Nightmare Abbey", patron1)
library.borrowing_book("The Piligrim's Progress", patron1)

# Returning books
library.return_book("Nightmare Abbey", patron1)

# Finding books
library.finding_book("The Piligrim's Progress")
library.finding_book("Moby-Dick")

# Removing books
library.removing_book("Moby-Dick")

# Removing patrons
library.removing_patron("Nithin")
