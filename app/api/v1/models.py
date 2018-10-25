all_Products = []
all_Sales = []

All_Users= {}
user_details={}


class Products(object):
  all_Products = []

  def __init__(self, product_name , price, quantity, category):
    '''constructor method that is called when an object is created'''
    self.product_name = product_name
    self.product_id = len(Products.all_Products) + 1
    self.price = price
    self.quantity= quantity
    self.category = category
  
  def create_new_product(self,product_name,product_price, quantity, category):
    for product in all_Products:
      if self.product_name == product["product_name"]:
        return "message The product you entered already exists"

    product_Description = {}
    product_Description["product_id"] = self.product_id
    product_Description["product_name"] = product_name
    product_Description["price"] = product_price
    product_Description["quantity"] = quantity
    product_Description["category"] = category

    Products.all_Products.append(product_Description)
    return Products.all_Products
  @classmethod
  def get_all_Products(cls):
    return cls.all_Products

  

class Sales(object):
  all_Sales = []

  def __init__(self,product_name, product_price):
    self.product_name = product_name
    self.product_price= product_price
    self.sale_id =  len(Sales.all_Sales) + 1

  def create_new_sale_record(self, product_name, product_price, product_id):
    new_Sale = {}
    new_Sale["product_id"] = product_id
    new_Sale["product_name"] = product_name
    new_Sale["price"] = product_price
    new_Sale["sale_id"] = self.sale_id

    Sales.all_Sales.append(new_Sale)
    return Sales.all_Sales

    # for prod in all_Products:
    #   if self.product_id == prod["product_id"]:

    #     new_Sale={
    #         self.sale_id: prod
    #     }

    #     all_Sales.append(new_Sale)
    #     return "success"
    
  def get_all_Sales(self):
    return all_Sales
  
  def get_one_sale(self, sale_id):
    for sale in all_Sales:
      if sale_id == sale["id"]:
        return sale
    return "message The sale doesn't exist"

# class Users(object):
#   '''class for handling user data'''

#   def __init__(self,username, email, password):
#     self.username = username
#     self.email = email
#     self.password = password

#   def register(self):
#     if email in All_Users:
#       return "message already exists"
#     else:

#       user_details["username"] = self.username
#       user_details["email"] = self.email
#       user_details["password"] = self.password

#     All_Users.append(user_details)
#     return "message successfully registered"

#   def get_one_user(self):
#     for user in All_Users:
#       if email in All_Users:
#         return All_Users[email]
#       return "user not found"

#   def get_all_users(self):
#     return All_Users