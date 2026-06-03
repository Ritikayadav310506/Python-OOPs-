class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} ({status})"


class Member:
    def __init__(self, name):
        self.name = name
        self.books_issued = []

    def __str__(self):
        return f"Member: {self.name}, Books issued: {[book.title for book in self.books_issued]}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def display_available_books(self):
        print("\nAvailable Books:")
        available = [book for book in self.books if not book.is_issued]
        if available:
            for book in available:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books available.")

    def issue_book(self, book_title, member):
        for book in self.books:
            if book.title == book_title and not book.is_issued:
                book.is_issued = True
                member.books_issued.append(book)
                print(f"Book '{book.title}' issued to {member.name}.")
                return
        print(f"Book '{book_title}' is not available.")

    def return_book(self, book_title, member):
        for book in member.books_issued:
            if book.title == book_title:
                book.is_issued = False
                member.books_issued.remove(book)
                print(f"Book '{book.title}' returned by {member.name}.")
                return
        print(f"{member.name} does not have the book '{book_title}'.")


# Demonstration
library = Library()

# Add books
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Create members
alice = Member("Alice")
bob = Member("Bob")

# Display available books
library.display_available_books()

# Issue books
library.issue_book("1984", alice)
library.issue_book("The Great Gatsby", bob)

# Display available books after issuing
library.display_available_books()

# Return a book
library.return_book("1984", alice)

# Display available books after return
library.display_available_books()
