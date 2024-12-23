from datetime import datetime

class Product:
    def __init__(self,p_name,p_sku,p_price,p_quantity,p_category):
        self.p_name=p_name
        self.p_sku=p_sku
        self.p_price=p_price
        self.p_quantity=p_quantity
        self.p_category=p_category

    
class Categories:
    def __init__(self,c_name):
        self.items_list=[]


class Inventory:
    def __init__(self):
        self.categories_list=[]
        self.product_list=[]
        self.sell_report=[]
        self.stock=0

    def add_products(self,p_name,p_sku,p_price,p_quantity,p_category):
        product = Product(p_name,p_sku,p_price,p_quantity,p_category)
        self.categories_list.append(p_category)
        self.product_list.append(product)
        self.stock+=p_quantity
        print(f"Product '{p_name}' added.")

    def find_product(self,p_sku):
        for pro in self.product_list:
            if pro.p_sku==p_sku:
                return pro
        print(f'No product found with SKU {p_sku}')

    def add_category(self,category_name):
        # category = Categories(category_name)
        self.categories_list.append(category_name)
        print(f"New category '{category_name}' added")

    def print_category_wise_product(self,category_name):
        if category_name in self.categories_list:
            print(f'Product in {category_name} :')
            for product in self.product_list:
                if category_name==product.p_category:
                    print(product.p_name)
        else:
            print('No such category exists')

    def print_all_product(self):
        print('All Products Details: ')
        for product in self.product_list:
            print(f'{product.p_sku}  {product.p_price}   {product.p_name} {product.p_quantity}')
        
    def print_no_stock(self):
        print('Number of items in Stock :',self.stock)
    
    def sale_product(self,p_sku,discount,date_sold):
        ch=True
        for product in self.product_list:
            if product.p_sku==p_sku and product.p_quantity>0:
                ch=False
                product.p_quantity-=1
                self.stock-=1
                price = product.p_price * (1- (discount/100))
                self.sell_report.append((p_sku, 'Sold', date_sold,' at price ',price))
                return print(f"{product.p_name} sold at ruprees {price}")
        if ch:
            print('Product Not Available')

    def inventory_details(self):
        print('----INVENTORY DETAILS-----\n')
        self.print_all_product()
        print('\n----SELL REPORT----\n')
        for item in self.sell_report:
            print(item)
        print('\n-----STOCK----\n')
        self.print_no_stock()

    def temp_report(self):
        tups=list(set(self.categories_list))
        for category in tups:
            self.print_category_wise_product(category)


inventory = Inventory()


inventory.add_category('Electronic')
inventory.add_category('Furniture')
inventory.add_category('Clothing')

print()

inventory.add_products('Iphone','E001',10000,5,'Electronic')
inventory.add_products('HeadPhone','E002',950,3,'Electronic')
inventory.add_products('Chair','F001',670,10,'Furniture')
inventory.add_products('T-Shirt','C001',550,7,'Clothing')
inventory.add_products('Table','F002',870,6,'Furniture')

print()

inventory.print_all_product()

print()

inventory.print_no_stock()

print()

inventory.print_category_wise_product('Electronic')

print()

inventory.sale_product('C001',10, datetime(2024,11,15))
inventory.sale_product('E001',50, datetime(2024,11,18))
inventory.sale_product('G001',50, datetime(2024,11,20))

print()

inventory.inventory_details()

print()

inventory.temp_report()



