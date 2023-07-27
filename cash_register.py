# For this project, you will need to program a cash register for a warehouse.

# The system must be able to:
# Show a list of all added products.
# Add/update/remove products of the order from the customer.
# All updates must be affecting the stock of the product.
# Delete order. Restore product stock.

# Once the purchase is completed, the system must show a list of all products ordered and the total amount to be paid.
# In case the customer, the system should display the change to be returned to the customer. 

import time


class Products:

    # all_products list is a class-level variable that will store all the instances of the Products class.       
    all_products = []

    def __init__(self,id,name,quantity,price):
        self.__id     = id
        self.__name   = name
        self.quantity = quantity 
        self.__price  = price

        Products.all_products.append(self)

    def __str__(self):
        return f"id: {self.__id}, name: {self.__name}, quantity: {self.quantity}, price: {self.__price}" 
    
    
    # get_all_products class method allows you to retrieve the list of all added products. 
    # cls is often used as a convention for the first parameter of a class method.It stands for "class" and is similar toself for instance methods.  
    @classmethod
    def get_all_products(cls):   
        return cls.all_products


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price   


class CashRegister(Products):

    cart_list   = []
    cart_total = 0

    def __init__(self,product,quantity):
        self.product  = product
        self.quantity = quantity  
        self.product_instance = None  # Variable to store the product instance if found  
        self.total_order = None


    @classmethod
    def get_cart(cls): 
        return cls.cart_list
        
    @classmethod
    def check_if_cart_not_empty(cls):
        if len(cls.get_cart()) == 0:
            print("Your cart is currently empty.")
            return False
        return True
    
    @classmethod
    def get_cart_list(cls):
        if cls.check_if_cart_not_empty():
            total = 0            
            for product in cls.get_cart():                 
                total += product['total']
                print(product)
            cls.cart_total = total
        
    
    @classmethod
    def get_cart_total(cls):  
        return print(cls.cart_total)    




    @classmethod
    def remove_product(cls,product_id):
        if  cls.check_if_cart_not_empty():
            for product in CashRegister.cart_list:
                if product["id"] == product_id:
                    CashRegister.cart_list.remove(product)
                    return True
            return False  


    @classmethod
    def payment(cls,amount):
        print(amount, cls.cart_total)
        if amount < cls.cart_total:
            print("Please enter a valid amount.") 
            return False       
        elif amount > cls.cart_total:
            change = amount - cls.cart_total
            print("Payment successful!")             
            print(f"Your change: {change}")            
        else:
            print("Payment successful!") 
        return True            




    def check_product_exists(self):
        all_products = Products.get_all_products()
        for product in all_products:            
            if product.get_id() == self.product:                 
                self.product_instance = product                 
                return True
        print("\nProduct not found.")
        return False


    def check_stock_available(self):        
        if self.product_instance.quantity < self.quantity:   
            print("\nThe quantity requested is not available.")             
            return False 
        return True        

    
    def add_product_order(self): 
        if self.check_product_exists() and self.check_stock_available(): 
            register = {}        
            register["id"]       = self.product_instance.get_id()
            register["name"]     = self.product_instance.get_name()
            register["quantity"] = self.quantity   
            register["price"]    = self.product_instance.get_price()             
            register["total"]    = self.quantity * self.product_instance.get_price() 

            
            if self.remove_product(register["id"]):
                CashRegister.cart_list.append(register)
                print("\nCart updated.") 
            else:    
                CashRegister.cart_list.append(register)
                print("\nNew product added.")
                               
        return True  

class ValidateInputs:
    def __init__(self,option):
        self.option = option

    def check_input(self):
        if self.option is None or self.option.isdigit() != True:
           print("\nPlease enter a valid option.")
           return False
        else:
            return True         

    def check_range(self):        
        if int(self.option) not in range(1, 6) :
            print("\nPlease enter a number within the valid options.")
            return False
        else:
            return True    

    


products_available = [
    {"id":1,"name":"Apple","quantity":30,"price":8.0},
    {"id":2,"name":"Orange","quantity":40,"price":7.0},
    {"id":3,"name":"Pineapple","quantity":20,"price":10.0},
    {"id":4,"name":"Banano","quantity":30,"price":6.0},
    {"id":5,"name":"Tangerines","quantity":10,"price":4.5},
    {"id":6,"name":"Kiwi","quantity":12,"price":7.8},
    {"id":7,"name":"Peach","quantity":15,"price":9.0},
    {"id":8,"name":"Watermelon","quantity":45,"price":15.5},
    {"id":9,"name":"Grapes","quantity":5,"price":10.0},
    {"id":10,"name":"Melon","quantity":10,"price":17.0},    
    ]



if __name__ == "__main__":

    [Products(i["id"],i["name"],i["quantity"],i["price"]) for i in products_available] 
    
    print("Welcome to the Warehouse.")   

    options = [
        "\nOptions:",
        "1) View products.",
        "2) Add product to the cart.",
        "3) View your cart.",
        "4) Remove product of your cart.",
        "5) Checkout cart.",
        "6) Exit the program.",
        ]

    start = True
    while start:
     
        [print(i) for i in options]

        option = input("Enter your answer:")         
        
        valide = ValidateInputs(option) 

        if valide.check_input() and valide.check_range():
            option = int(option)

            if option == 1:
                print("\nList of Products:")
                [print(i) for i in Products.get_all_products()] 


            if option == 2: 
                product  =  input("Enter the id of the product that you want:")
                quantity =  input("Enter the amount you want to carry:")

                valid_product  = ValidateInputs(product)
                valid_quantity = ValidateInputs(quantity)

                if valid_product.check_input() and valid_quantity.check_input():
                    cash_register = CashRegister(int(product), int(quantity))    
                    if cash_register.add_product_order(): 
                        CashRegister.get_cart_list() 
                        CashRegister.get_cart_total()


            if option == 3:                
                CashRegister.get_cart_list()
                CashRegister.get_cart_total() 


            if option == 4:
                product = input("Enter the id of the product that you remove:")
                if ValidateInputs(product).check_input():
                    if CashRegister.remove_product(product_id=int(product)):
                        print("The product was successfully removed.")
                        CashRegister.get_cart_list()    
                        CashRegister.get_cart_total()    
                    else:
                        print("Product not found.")



            if option == 5:
                
                CashRegister.get_cart_list()
                CashRegister.get_cart_total()
                amount = input("Please enter the amount to pay:")                
                if ValidateInputs(amount).check_input(): 
                    if CashRegister.payment(int(amount)):
                        time.sleep(3)                        
                        start = False 

            if option == 6:
                start = False 
    
    

