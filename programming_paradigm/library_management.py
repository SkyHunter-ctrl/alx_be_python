# a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
from library_management import Library, Book
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
