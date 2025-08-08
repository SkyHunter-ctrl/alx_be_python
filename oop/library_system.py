# understanding of inheritance and composition in Python by creating a system that models a library with different types of books.
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def get_info(self):
        return f"{self.title}, by {self.author}"
    def get_details(self):
        return f"{self.title}, by {self.author}"
    def __str__(self):
        return self.get_details()
# Derived classes EBook and PrintBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.file_size = file_size
    def get_details(self):
        return f"{self.title}, by {self.author} {self.file_size}MB"
    def __str__(self):
        return self.get_details()
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.page_count = page_count
    def get_details(self):
        return f"{self.title}, by {self.author} Page count: {self.page_count}"
    def __str__(self):
        return self.get_details()
# Composition - Library:
class Library:
    def __init__(self):
        self.books: list[Book] = []
    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        print("📚 Library Collection:")
        for book in self.books:
            print(" -", book.get_details())
    def get_details(self):
        return f"{self.title}, by {self.author}"
        if isinstance(self, EBook):
            return f"{self.title}, by {self.author} (File size: {self.file_size}MB)"
        elif isinstance(self, PrintBook):
            return f"{self.title}, by {self.author} (Page count: {self.page_count})"
        else:
            return super().get_info()
        


