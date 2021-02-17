class Library():
    def __init__(self, booklist):
        self.book = booklist

    def allBooks(self):
        print("The books present in the Library are as follows: \n")
        for book in self.book:
            print("\t*" + book)

    def borrow(self,bookname):
        if bookname in self.book:
            print(f"Thanks for visiting our library. Please take care of the book you borrowed - '{bookname}'. Please return it within 30 days.\n")
            self.book.remove(bookname)
            return True
        else:
            print("The book you are trying to borrow is not available \n")
            return False

    def returnBk(self,bookname):
        if bookname != self.book:
            self.book.append(bookname)
            print("Thanks for visiting our Library. Visit again!")
        else:
            print("This book is not beign issued. Thanks for visiting Worlds Library")
        

class Student:

    def requestedbooks(self):
        reqbook = input("Enter the name of the book you want to borrow : ")
        return reqbook

    def returnedbooks(self):
        retnbook = input("Enter the name of the book you want to return : ")
        return retnbook



if __name__ == '__main__':
    myLib = Library(["python", "java", "flutter", "C",
                    "javascript", "c++", "react", "django"])
    student = Student()

    while(True):
        welcomeMsg = ''' \n * * * * * WORLD LIBRARY * * * * * \n
        Please choose an option:
        1. List all available books
        2. Request books
        3. Return books 
        4. Exit the Library \n
        '''
        print(welcomeMsg)

        opt = int(input("Please enter the option number : "))

        if opt == 1:
            myLib.allBooks()
        elif opt == 2:
            myLib.borrow(student.requestedbooks())
        elif opt == 3:
            myLib.returnBk(student.returnedbooks())
        elif opt == 4:
            exit()
        else:
            print("Not a valid option. Please choose from 1-4. ")