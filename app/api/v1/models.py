from flask import jsonify
all_Products = {}
all_Sales = {}
new_Product = {}
new_Sale = {}


class Products(object):
  
  def create_new_product(self, product_name, product_id, price, quantity, category):
    
    for product in all_Products:
      if product_id == product["product_id"]: 
        return jsonify({"message":"The product you entered already exists"})

    new_Product["product_name"] = product_name
    new_Product["price"] = price
    new_Product["quantity"] = quantity
    new_Product["category"] = category

    all_Products[product_id] = new_Product
    return {"message":"new product created successfully"}

  def get_all_Products(self):
    return all_Products

  def get_one_product(self, product_id):
    for product_id in all_Products:
      return all_Products[product_id]
    return {"message":"Product doesn't exist"}



class Sales(object):

  def create_new_sale_record(self, attendant_name,sale_id, total_worth, profit):
   
    for sale_id in all_Sales:
      return {"message":"The sale you entered already exists"}

    new_Sale["attendant_name"] = attendant_name
    new_Sale["total_worth"] = total_worth
    new_Sale["profit"] = profit

    all_Sales[sale_id]=new_Sale  

    return {"message":"new sale added successfully"}
    
  def get_all_Sales(self):
    return all_Sales
  
  def get_one_sale(self, sale_id):
    for sale_id in all_Sales:
      return all_Sales[sale_id]
    return {"message":"The sale doesn't exist"}

