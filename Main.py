from Library import Libraray


print("library management system")
print("1.add book")
print("2.display books")
print("3. issue book")
print("4.return book")
print("5.exit")

library=Libraray()

while True:
    
    choice = input("enter your choice: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.display_books()   
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        print("exit")
        break
    else:
        print("invalid choice.plase try again")