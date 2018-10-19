from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api, Resource
from .models import all_Products, all_Sales, Products, Sales


app = Flask(__name__)
api = Api(app)

product = Products()
sale = Sales()

class All_Products_Endpoint(Resource): 

  def post(self):
    data = request.get_json()

    product_id = len(all_Products) + 1
    product_name = data.get("product_name")
    product_price = data.get("price")
    quantity = data.get("quantity")
    category = data.get("category")

    response = jsonify(product.create_new_product(product_name, product_id, product_price, quantity, category))
    response.status_code = 201
    return response

  def get(self):
    response = jsonify({"products": product.get_all_Products(), "message":"success"})
    response.status_code = 200
    return response


class One_Product_Endpoint(Resource):

  def get(self, product_id):
    response = jsonify(product.get_one_product(product_id))
    response.status_code = 200
    return response

class All_Sales_Endpoint(Resource):    #fetch all sales records

  def post(self, attendant_name,sale_id, total_worth, profit):
    data = request.get_json()

    sale_id = len(all_Sales) + 1
    attendant_name = data.get("attendant_name")
    total_worth = data.get("total_worth")
    profit = data.get("profit")    

    response = jsonify(sale.create_new_sale_record(attendant_name,sale_id, total_worth, profit))
    response.status_code = 201
    return response

  def get(self):
    response = jsonify(sale.get_all_Sales())
    response.status_code = 200
    return response

class One_Sale_Endpoint(Resource):      #fetch one sale record
 
  def get(self, sale_id):
    response = jsonify(sale.get_one_sale(sale_id))
    response.status_code = 200
    return response


  