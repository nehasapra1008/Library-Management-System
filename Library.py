from Books import Book
class Libraray:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id=input("Enter the book_id->") # String 
        title=input("Enter the title ->")
        author=input("Enter the author ->")
        
        book=Book(book_id,title,author)
        self.books.append(book)
        print("Book added successfully.")

       
        
    def issue_book(self):
         book_id =input("Enter Book Id")
         for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
            print("Book not found.")

    def  return_book(self):   
        print("return book")

    def display_books(self):
        if not self.books:
            print("No books in the library.")

        print("\nBook List:")

        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.available}")



