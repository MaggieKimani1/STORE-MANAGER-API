from flask import Flask, Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from .models import all_Products, all_Sales, Products, Sales


app = Flask(__name__)
api = Api(app)

class All_Products_Endpoint(Resource): 

  def post(self):
    '''Creating a new product'''
    try:

      data = request.get_json()
      # product_id = len(all_Products) + 1
      product_name = data["product_name"]
      product_price = data["price"]
      quantity = data["quantity"]
      category = data["category"]

      

      product = Products(product_name,product_price, quantity, category)
      products=product.create_new_product(product_name,product_price, quantity, category)

      if product_name == "" or not product_name:
        return {"message":"please enter the product_name"},400
      if quantity == "" or not quantity:
        return {"message":"Please specify a quantity"},400
      if product_price == "" or not product_price:
        return {"message":"please enter the price"},400
      if category == "" or not category:
        return{"message":"please enter the category"},400
      if quantity == 0:
        return{"message":"invalid quantity"},400

      # all_Products.append()
      return make_response(jsonify({"message":"success","products":products}), 201)

      

    except:
      return make_response(jsonify({"message":"include all details"}), 400)


    

    

  def get(self):
    products=Products.get_all_Products()
    '''Fetching a specific product'''
    return make_response(jsonify({"message":"success","products":products}), 200)


class One_Product_Endpoint(Resource):
  
  def get(self, product_id):
    '''Fetching a product'''
    products=Products.get_all_Products()
    for product in products:
      if product["product_id"] == product_id:
        return product
      return make_response(jsonify({"message":"no product found"}), 404)

class All_Sales_Endpoint(Resource):   
  
  def post(self, product_id):
    '''Creating a new sale'''

    data = request.get_json() #retrieving the data using the request in json format
    product_name = data["product_name"]
    product_price = data["price"]

    

    products=Products.get_all_Products()
    for prod in products:
      if product_id == prod["product_id"]:
        # new_Sale={
        #     "sale_id": prod
        # }
        # all_Sales.append(new_Sale)
        sale = Sales(product_name,product_price)
        sales=sale.create_new_sale_record(product_name,product_price,product_id)

        return make_response(jsonify({"message":"successfully sold" ,"sales": sales}), 201)
      return make_response(jsonify({"message":"No product to sell"}), 404)

  def get(self):
    '''Fetching all sale records'''

    return make_response(jsonify({"message":"success","sales":all_Sales}), 200)

class One_Sale_Endpoint(Resource):    

   def get(self, sale_id):
    '''Fetching a sale record'''

    for sale in all_Sales:
      if sale["sale_id"] == sale_id:
        return sale


  