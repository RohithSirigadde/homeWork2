class Book:
    def __init__(self, title, author):
        self.title_OfBook = title
        self.author_OfBook = author
        self.checked_out_to_OfBook = None
        self.waiting_list_OfBook = []

    def add_to_waiting_list(self, patron):
        self.waiting_list_OfBook.append(patron)

    def remove_from_waiting_list(self, patron):
        self.waiting_list_OfBook.remove(patron)

    def is_checked_out(self):
        return self.checked_out_to_OfBook is not None

    def check_out(self, patron):
        if not self.is_checked_out():
            self.checked_out_to_OfBook = patron
            patron.check_out_book(self)
            print(f"{self.title_OfBook} has been checked out to {patron.name}.")
        else:
            print(f"{self.title_OfBook} is already checked out.")

    def return_book(self):
        if self.is_checked_out():
            patron = self.checked_out_to_OfBook
            self.checked_out_to_OfBook = None
            patron.return_book(self)
            if self.waiting_list_OfBook:
                next_patron = self.waiting_list_OfBook[0]
                self.remove_from_waiting_list_OfBook(next_patron)
                self.check_out_OfBook(next_patron)
            else:
                print(f"{self.title_OfBook} has been returned.")
        else:
            print(f"{self.title_OfBook} is not checked out.")
            
            
class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if len(self.checked_out_books) < 3:
            self.checked_out_books.append(book)
            print(f"{book.title_OfBook} has been checked out to {self.name}.")
        else:
            print(f"{self.name} has reached the maximum limit of checked out books.")

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            print(f"{book.title_OfBook} has been returned by {self.name}.")
        else:
            print(f"{self.name} did not have {book.title_OfBook} checked out.")






book1 = Book("The Piligrim's Progress", "John Bunyan")
book2 = Book("Tom Jones" , "Henry Fielding ")
book3 = Book("Emma" , "Jane Austin")
book4 = Book("Nightmare Abbey" ,"Thomas Love Peacock")
book5 = Book("Moby-Dick" ,"Herman Melville")
book6 = Book("MiddleMarch", "George Eliot")

patron1 = Patron("Rohith")
patron2 = Patron("Nithin")
patron3 = Patron("Srinath")

book1.check_out(patron1)
book5.check_out(patron2)
book3.check_out(patron3)  

book2.check_out(patron1)
book3.check_out(patron2)

book1.return_book()  

book3.return_book()
book2.check_out(patron3)  

book1.check_out(patron3)  


book1.return_book()



