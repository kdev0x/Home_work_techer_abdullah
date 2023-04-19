
# Create a class Book with attributes like title, author, and status (available or borrowed). Use encapsulation (private attributes) and provide getter and setter methods for the attributes.
# Create a class Borrower with attributes like name, borrowed_books (a list to store books the borrower has borrowed). Again, use encapsulation and provide getter and setter methods.
# Create an abstract class Library that has methods like add_book, add_borrower, borrow_book, and return_book. The methods should be declared but not implemented.
# Create a class LibrarySystem that inherits from the Library abstract class. Implement the methods defined in the Library class. Use composition to manage the relationship between books and borrowers.
# Make sure to use proper access modifiers (public, private, and protected) for attributes and methods.
# Tips:

# Break down the project into smaller tasks and focus on one task at a time.
# Use comments to describe what each class and method does.
# Test your code frequently to ensure everything works as expected.
# This project will help cover the following topics:

# Polymorphism
# Abstract classes
# Public, private, and protected access modifiers
# Encapsulation
# Composition and aggregation
# By working on this project, the student will have a better understanding of the OOP concepts that need more study or haven't been covered yet in the PCAP exam preparation.
class Library:
    def __init__(self, user_option,title,author,name,borrowed_book =  {}):
        self.__user_option = user_option
        self.__title = title
        self.__author = author
        self.__name = name
 
      
class Borrower(Library):
         def __init__(self, user_option,title,author,name,borrowed_book = []):
            super().__init__(user_option,title,author,name,borrowed_book = [])
      

         def Show_bowwerd_book(self):
            if self.borrowed_book == 0:
                print("You did not borrow any books")
            else:
                print("--Youre name is", self.name , "and you have borrowed",len(self.borrowed_book) , "and they are \n", self.borrowed_book )

class Add_Book(Library):
    def __init__(self, user_option,title,author,name,borrowed_book = []):
            super().__init__(user_option,title,author,name,borrowed_book = [])

    def book_adder(self):
          self.borrowed_book[self.__title,self.__author] 

class Ret_Book(Library):
    def __init__(self, user_option,title,author,name,borrowed_book = []):
        super().__init__(user_option,title,author,name,borrowed_book = [])
 
    def delete_book(self):
          self.borrowed_book.pop(self.__author)
    

option = input ("what do you want")
if option == " add a book":
     user_1 = Add_Book
     user_1.book_adder()
elif option == "view books":
     user_1 = Borrower
     user_1.Show_bowwerd_book
     Ret_Book()
elif option == "return a book":
     user_1 = Ret_Book
     user_1.delete_book

else:
     raise ValueError("This option is not curntly avalible")
