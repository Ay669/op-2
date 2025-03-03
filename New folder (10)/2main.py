class Library:

    def __init__(self, list_of_books, name):
        self.bookslist = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.bookslist:
            print("sorry, we do not have that book.")
        elif book in self.lendDict:
                print(f"the book is already being used by {self.lendDict[book]}")
        else:
             self.lendDict[book] = user
             print("Lender-Book database has been updated. You can take the book now.")

    def addBook(self, book):
        self.bookslist.append(book)
        print(f"{book} has been added to the book list")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print("The book has been returned.")
        else:
            print("that book wasn't borrowed from us.")

if __name__ == '__main__':
    books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "let's Upskill")
    user_name = input(" Welcome to our library! Please enter your name: ")

    while(True):
        print(f"\nHello {user_name},welcome to the {books.name} library. please choose an option:")
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Exit")
        
        user_choice = input("enter your choice to continue: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option")
            continue

        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        elif user_choice == '5':
            print("Thanks for using our library. Have a great day ahead!")
            break


    
        
            
