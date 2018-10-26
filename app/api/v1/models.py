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

  def get_all_Products(self):

    
    return all_Products

  def get_one_product(self, product_id):

    for product in all_Products:
      return product[product_id]

      
    return {"message":"Product doesn't exist"}



class Sales(object):

  def create_new_sale_record(self, attendant_name,sale_id, total_worth, profit):
   
   for sale_id in all_Sales:
      return {"message":"The sale you entered already exists"}

      new_Sale["attendant_name"] = attendant_name
      new_Sale["total_worth"] = total_worth
      new_Sale["profit"] = profit

   return {"message":"new sale added successfully"}
    

  def get_all_Sales(self):
    return all_Sales
  
  
