all_Products = []
all_Sales = []
product_Description = {}

class Products(object):

  def __init__(self, product_name, product_id, price, quantity, category):
    self.product_name = product_name
    self.product_id = product_id
    self.price = price
    self.quantity= quantity
    self.category = category
  
  def create_new_product(self):
    for product in all_Products:
      if self.product_name == product["product_name"]:
          return "message The product you entered already exists"
    product_Description["product_id"] = self.product_id
    product_Description["product_name"] = self.product_name
    product_Description["price"] = self.price
    product_Description["quantity"] = self.quantity
    product_Description["category"] = self.category

    all_Products.append(product_Description)

  def get_all_Products(self):
    return all_Products

  

class Sales(object):

  def __init__(self,product_id, sale_id):
    self.product_id = product_id
    self.sale_id = sale_id
  def create_new_sale_record(self):
    for prod in all_Products:
      if self.product_id == prod["product_id"]:
        new_Sale={
            self.sale_id: prod
        }
        all_Sales.append(new_Sale)
        return "success"
    
  def get_all_Sales(self):
    return all_Sales
  
  def get_one_sale(self, sale_id):
    for sale in all_Sales:
      if sale_id == sale["id"]:
        return sale
    return "message The sale doesn't exist"