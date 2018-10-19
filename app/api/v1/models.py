all_Products = {}
all_Sales = {}
product_Description = {}
new_Sale = {}


class Products(object):
  
  def create_new_product(self, product_name, product_id, price, quantity, category):
    
    for product_id in all_Products:
      return {"message":"The product you entered already exists"}

      product_Description["product_name"] = product_name
      product_Description["price"] = price
      product_Description["quantity"] = quantity
      product_Description["category"] = category

      all_Products[product_id] = product_Description
      return {"message":"new product created successfully"}

  