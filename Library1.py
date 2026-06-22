from Books import Book


class Library1:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nBook List:")
        print("-" * 40)

        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(f"Book id : {book.book_id}")
            print(f"Title   : {book.title}")
            print(f"Author  : {book.author}")
            print(f"Status  : {status}")
            print("-" * 40)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


library = Library1()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book_id = input("Enter book ID to issue: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Enter book ID to return: ")
        library.return_book(book_id)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
