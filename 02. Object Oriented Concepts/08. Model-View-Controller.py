# Model: Represents the data and the business logic
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookModel:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

# View: Represents the user interface
class BookView:
    @staticmethod
    def display_books(books):
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}")

# Controller: Acts as an intermediary between the Model and View
class BookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self, title, author):
        book = Book(title, author)
        self.model.add_book(book)

    def display_books(self):
        books = self.model.get_books()
        self.view.display_books(books)

if __name__ == "__main__":
    # Create the Model, View, and Controller
    model = BookModel()
    view = BookView()
    controller = BookController(model, view)

    # Add books through the controller
    controller.add_book("1984", "George Orwell")
    controller.add_book("To Kill a Mockingbird", "Harper Lee")

    # Display books through the controller
    controller.display_books()
