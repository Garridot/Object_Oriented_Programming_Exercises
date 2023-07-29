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

        if len(book_found) != 0: return book_found[0]           
        return False          


    @classmethod
    def lend_book(cls,book_id,user_id):

        book = cls.find_book(book_id) 

        user = User.get_user(user_id)

        if user == False : raise ValueError("User not found.") 

        if book is False : raise ValueError("Book not found.")  
        if book['availability'] == "False":
            raise ValueError("This book is not currently available.")  

        return_date  = datetime.date.today() + datetime.timedelta(days=14)
        
        # create dic 
        context = {}
        context["date"]                 =  datetime.date.today().strftime("%Y-%m-%d")          
        context["user_name"]            = user["name"]  
        context["user_identification"]  = user["identification"]   
        context["book"]                 = book['title']        
        context["isbn"]                 = book['isbn']        
        context["return_date"]          = return_date.strftime("%Y-%m-%d")  
        context["returned"]             = False

        
        # Update the availability to "False"
        book['availability'] = "False"

        cls.add_loan_made_it(context)

        return print(f"Borrowed Book: {context}")  

           
    @classmethod
    def return_book(cls,book_id,user_id):    
        book = cls.find_book(book_id) 
        user = User.get_user(user_id)

        if user == False : raise ValueError("User not found.") 
        if book is False : raise ValueError("Book not found.")  
        
        if book['availability'] == "True":
            raise ValueError("This book has not been loaned out.") 

        list_books_borrowed = cls.get_list_of_loans_made() 

        book_retorned = list(filter(lambda i: i["user_identification"] == user["identification"] and i["isbn"] == book["isbn"], list_books_borrowed)) 

        book_retorned = book_retorned[-1]

        book_retorned["returned"] = True

        # Update the availability to "False"
        book['availability'] = "True"   

        return print(f"Returned book: {book_retorned}")

        



    @classmethod
    def get_list_users(cls):
        return cls.list_user  

    @classmethod
    def add_list_user(cls,user):
        cls.get_list_users().append(user)



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

        book_id_list = list(map(lambda i: i["isbn"], super().get_list_books()))             
        if value in book_id_list:
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

        return f"title: {title}, author: {author}, genre: {genre}, isbn: {isbn}, availability: {status}"  


    def add_book(self):
        id     = len(super().get_list_books()) + 1     
        title  = self.get_title()
        author = self.get_author()
        genre  = self.get_genre()
        isbn   = self.isbn
        status = self.get_availability()        
        item = {"id":id,"title":title,"author":author,"genre":genre,"isbn":isbn,"availability":status}
        return super().add_book(item)            



class User(Library):
    def __init__(self,name,identification,address):

        if not name:  raise ValueError("Name must be provided for a user.")    
        if not identification: raise ValueError("Identification must be provided for a user.")  
        if not address:  raise ValueError("Address must be provided for a user.")   
        
        self.__name = name   
        self.identification = identification     
        self.__address = address        
        self.__books_borrowed = []

    def get_name(self):
        return self.__name 

    @property
    def identification(self):
        return self.__identification  

    def get_address(self):
        return self.__address 

    def get_books_borrowed(self):
        return self.__books_borrowed 


    @identification.setter
    def identification(self,value): 
        if not value.isdigit():
            raise ValueError("Identification must contain only digits.") 

        user_id_list = list(map(lambda i: i["identification"], super().get_list_users()))             
        if value in user_id_list:
            raise ValueError(f"Identification '{value}' already exists. Identification must be unique for each user.")    

        self.__identification = value  # Set the validated identification   

    
    def add_user(self):
        user = {}

        user["id"]             = len(self.get_list_users()) + 1
        user["name"]           = self.get_name()
        user["identification"] = self.identification
        user["address"]        = self.get_address()    

        self.add_list_user(user)
        return print(f"New user added: {user}")


    @classmethod
    def get_user(cls,user_id):
        list_user = cls.get_list_users()   
        find_user = list(filter(lambda i: i["identification"] == user_id, list_user))
        if len(find_user) != 0: return find_user[0]
        return False    
          

    @classmethod
    def get_user_books_borrowed(cls,user_id):
        user = cls.get_user(user_id)  
        if user == False : raise ValueError("User not found.")  

        list_books_borrowed = cls.get_list_of_loans_made()
        find_loans = list(filter(lambda i: i["user_identification"] == user["identification"], list_books_borrowed))
        
        if len(find_loans) == 0 : return print("It appears that the user has not borrowed any books.")

        return find_loans


     





       



try:
    book1  = Book("The Catcher in the Rye I", "J.D. Salinger", "Fiction", "978-0316769488","True").add_book()
    book2  = Book("The Catcher in the Rye II", "J.D. Salinger", "Fiction", "978-0316769487","True").add_book()
    book3  = Book("The Catcher in the Rye III", "J.D. Salinger", "Fiction", "978-0316749488","True").add_book()
    book4  = Book("The Catcher in the Rye IV", "J.D. Salinger", "Fiction", "978-0386769487","True").add_book()

    user1  = User("Albert Ferdinand I", "001", "742 Evergreen Terrace",).add_user()
    user2  = User("Albert Ferdinand II", "002", "741 Evergreen Terrace",).add_user()
    user1  = User("Albert Ferdinand III", "003", "740 Evergreen Terrace",).add_user()
    
    
    Library.lend_book(3,"003")
    Library.lend_book(1,"003")
    Library.return_book(3,"003")    
    
except ValueError as e:
    print("ValueError:", e)    



