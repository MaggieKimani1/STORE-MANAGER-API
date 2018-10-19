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

  