from flask import Flask, Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from .models import all_Products, all_Sales, Products, Sales


app = Flask(__name__)
api = Api(app)

class All_Products_Endpoint(Resource): 

  def post(self):
    data = request.get_json()
    product_id = len(all_Products) + 1
    product_name = data["product_name"]
    product_price = data["price"]
    quantity = data["quantity"]
    category = data["category"]

    product = Products(product_name, product_id, product_price, quantity, category)
    response = product.create_new_product()

    if product_name == "" or not product_name:
      return {"message":"please enter the product_name"},400
    if quantity == "":
      return {"message":"Please specify a quantity"},400
    if product_price == "":
      return {"message":"please enter the price"},400
    if category == "":
      return{"message":"please enter the category"},400
    if quantity == 0:
      return{"message":"invalid quantity"},400

    return make_response(jsonify({"message":"success","products":all_Products}), 201)

  def get(self):
    return make_response(jsonify({"message":"success","products":all_Products}), 200)


class One_Product_Endpoint(Resource):
  def get(self, product_id):
    for product in all_Products:
        if product["product_id"] == product_id:
          return product

class All_Sales_Endpoint(Resource):    #fetch all sales records

  def post(self):
    data = request.get_json()
    sale_id = len(all_Sales) + 1
    product_id = data["product_id"]
    for prod in all_Products:
      if product_id == prod["product_id"]:
        new_Sale={
            "sale_id": prod
        }
        all_Sales.append(new_Sale)
        return make_response(jsonify({"message":"successfully sold"}), 201)
    return make_response(jsonify({"message":"No product to sell"}), 404)

  def get(self):
    return make_response(jsonify({"message":"success","sales":all_Sales}), 200)

class One_Sale_Endpoint(Resource):      #fetch one sale record
 
  def get(self, sale_id):
    for sale in all_Sales:
      if sale["sale_id"] == sale_id:
        return sale


  