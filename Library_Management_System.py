import datetime

class Library:    
    list_books         = []
    list_user          = []
    list_of_loans_made = []

    @classmethod
    def get_list_books(cls):
        return cls.list_books

    @classmethod
    def add_book(cls,item):           
        cls.get_list_books().append(item)  
        return print(f"New book added: {item}")


    @classmethod
    def get_list_of_loans_made(cls):
        return cls.list_of_loans_made   

    @classmethod
    def add_loan_made_it(cls,item):
        cls.get_list_of_loans_made().append(item) 




    @classmethod
    def find_book(cls,book_id):
        list_books = cls.get_list_books()        
        book_found = list(filter(lambda i: i["id"] == book_id, list_books))      

        if len(book_found) != 0:
            return book_found[0]           
        return False          


    @classmethod
    def lend_book(cls,book_id):

        book = cls.find_book(book_id) 

        if book is False : raise ValueError("Book not found.")  
        if book['Availability'] == "False":
            raise ValueError("This book is not currently available.")  

        # Update the availability to "False"
        book['Availability'] = "False"

        return_date       = datetime.date.today() + datetime.timedelta(days=14)
        
        # create dic 
        context = {}
        context["Date"]   =  datetime.date.today().strftime("%Y-%m-%d")    
        context["User"]   = None    
        context["Book"]   = book['Title']
        context["Author"] = book['Author'] 
        context["Isbn"]   = book['Isbn']        
        context["Return_date"] = return_date.strftime("%Y-%m-%d")  
        context["Returned"] = False

        return print(f"Borrowed Book: {context}")     


class Book(Library):
    def __init__(self,title,author,genre,isbn,availability): 

        if not title:  raise ValueError("Title must be provided for a book.")    
        if not author: raise ValueError("Author must be provided for a book.")  
        if not genre:  raise ValueError("Genre must be provided for a book.")   
        if not isbn:   raise ValueError("ISBN must be provided for a book.")  
        if not availability: raise ValueError("Availability must be provided for a book.")  
        
        self.__title  = title
        self.__author = author
        self.__genre  = genre 
        self.isbn   = isbn  
        self.__availability = availability 


    def get_title(self):
        return self.__title 

    def get_author(self):
        return self.__author      

    def get_genre(self):
        return self.__genre 
    
    @property
    def isbn(self):
        return self.__isbn 

    @isbn.setter
    def isbn(self, value):
        value = value.replace('-', '').replace(' ', '')  # Normalize the ISBN

        if len(value) not in (10, 13):
            raise ValueError("ISBN must be either 10 or 13 digits long.")

        if not value.isdigit():
            raise ValueError("ISBN must contain only digits.") 

        booksID_list = list(map(lambda i: i["Isbn"], super().get_list_books()))             
        if value in booksID_list:
            raise ValueError(f"ISBN '{value}' already exists. ISBN must be unique for each book.")    

        self.__isbn = value  # Set the validated ISBN 
        
    def get_availability(self):
        return self.__availability

    
    def __str__(self):
        title  = self.get_title()
        author = self.get_author()
        genre  = self.get_genre()
        isbn   = self.isbn
        status = self.get_availability()

        return f"Title: {title}, Author: {author}, Genre: {genre}, ISBN: {isbn}, Availability: {status}"  


    def add_book(self):
        id     = len(super().get_list_books()) + 1     
        title  = self.get_title()
        author = self.get_author()
        genre  = self.get_genre()
        isbn   = self.isbn
        status = self.get_availability()        
        item = {"id":id,"Title":title,"Author":author,"Genre":genre,"Isbn":isbn,"Availability":status}
        return super().add_book(item)            
             



try:
    book  = Book("The Catcher in the Rye I", "J.D. Salinger", "Fiction", "978-0316769488","True").add_book()
    book2 = Book("The Catcher in the Rye II", "J.D. Salinger", "Fiction", "978-0316769487","True").add_book()
    book  = Book("The Catcher in the Rye III", "J.D. Salinger", "Fiction", "978-0316749488","True").add_book()
    book2 = Book("The Catcher in the Rye IV", "J.D. Salinger", "Fiction", "978-0386769487","True").add_book()
    Library.lend_book(3)    
except ValueError as e:
    print("ValueError:", e)    



