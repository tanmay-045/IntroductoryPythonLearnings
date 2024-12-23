# Implementing Product Class
class Product:
    def __init__(self,p_id,p_name,p_price,p_quantity):
        self.p_name=p_name
        self.p_id=p_id
        self.p_price=p_price
        self.p_quantity=p_quantity
        self.p_discount=None

    
# Implementing CartItem Class
class CartItem:
    def __init__(self):
        self.p_id=None
        self.p_quantity=None

    def add_products_in_cart(self,p_id,p_quantity):
        self.p_id=p_id
        self.p_quantity=p_quantity

    def update_quantity(self,strr,p_quantity):          # 'a': add      'r': remove
        if strr == 'a':
            self.p_quantity+=p_quantity
        if strr == 'r':
            self.p_quantity-=p_quantity


# Implementing ShoppingCart class
class ShoppingCart():
    def __init__(self):
        self.p_id=None  
        self.p_name=None
        self.p_price=None
        self.p_quantity_to_buy=None
        self.products_list=[]
        
    def add_products_in_cart(self,product,p_quantity_to_buy):
        self.products_list.append((product))
        self.p_id=product.p_id
        self.p_name=product.p_name
        self.p_quantity_to_buy=p_quantity_to_buy
        self.p_price=product.p_price*p_quantity_to_buy
        print(f"{p_quantity_to_buy} '{product.p_name}' has been added to Cart. ")
        print("Total Amount : ",self.p_price)


    def update_quantity_in_cart(self,product,strr,p_quantity):          # 'a': add      'r': remove
        if product in self.products_list:
            if strr == 'a':
                self.p_quantity_to_buy+=p_quantity
            if strr == 'r':
                self.p_quantity_to_buy-=p_quantity
            print("Quantity Updated")
            return
        print("No such item found in Cart")

        
    def apply_discount(self,product,discount_percent):
        if discount_percent<50:                                             # assuming no to give discount more than 50%
            self.p_price = self.p_price - self.p_price*discount_percent*0.01
            print("Wohoo! Discount Applied")
            print("Discount Price : ",self.p_price)

    def cart_details(self):
        print(f"---Items in Cart---")
        print(f"{self.p_quantity_to_buy} {self.products_list[0].p_name} are in the cart.")
        print(f"Total Amount : ",self.p_price)


import random 

class Orders:
    def __init__(self):
        self.order_number=None

    def checkout(self,cart,money):
         if cart.p_price==money:             
             self.order_number=int(random.random())
             print("Transaction Succesfull")
             print("Your order number is : ",self.order_number)         
         else:
             print("Please enter correct amount")



product1 = Product(101,"Mouse",200,50)
product1 = Product(101,"Keyboard",300,50)

cart1 = ShoppingCart()

cart1.add_products_in_cart(product1,2)

cart1.apply_discount(product1,10)

cart1.cart_details()

order1=Orders

order1.checkout(cart1,540)

    

        
