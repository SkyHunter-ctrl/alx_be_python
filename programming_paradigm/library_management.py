# a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
from library_management import Library, Book
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"You have checked out: {book}")
                return
        print("Book not available for checkout.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                print(f"You have returned: {book}")
                return
        print("Book not found or not checked out.")
def __init__(self, name):
        self.name = name
        self.books = []
def main():
    # Create a library instance
    library = Library("Home Library")
    # Create some add book instances
    library.add_book(Book("1984", "George Orwell", "Dystopian"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Classic"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"))
    # List all books in the library
    print("Available books after setup:")
    library.list_available_books()
    # check out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books() 
    # return a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
    if __name__ == "__main__":
        main()
