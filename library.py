class Library:
    def __init__(self, booklist):
        self.book = booklist

    def allBooks(self):
        print("The books present in the Library are as follows: \n")
        for book in self.book:
            print("\t*" + book)

    def borrow(self,bookname):
        takebook =  None
        if bookname in self.book:
            print(f"Thanks for using our library. Please take care of the book you borrowed - '{bookname}'. Please retuen it within 30 days.\n")
            self.book.remove(bookname)
        else:
            print("The book you are trying to borrow is not available \n")


class Student:

    def __init__(self):
        pass

    def requestedbooks(self, bookname):
        pass

    def returnedbooks(self, bookname):
        pass



while(True):
    myLib = Library(["python", "java", "flutter", "C",
                    "javascript", "c++", "react", "django"])

    myLib.allBooks()
    myLib.borrow("python")
    # myLib.allBooks()