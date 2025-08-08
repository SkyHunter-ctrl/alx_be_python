# a Book class that uses specific magic methods to enhance its functionality.
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        print(f"{self.title} by {self.author}, published in {self.year}")    
    def __del__(self):
        print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author} {self.year}"
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year})"
from book_class import Book
# Example usage
def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)  # Calls __str__
    print(repr(my_book))  # Calls __repr__
    del my_book  # Calls __del__
if __name__ == "__main__":
    main()