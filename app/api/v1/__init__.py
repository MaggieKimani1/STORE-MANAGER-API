from flask import Blueprint
from flask_restful import Api, Resource
from .views import All_Products_Endpoint, One_Product_Endpoint, All_Sales_Endpoint,One_Sale_Endpoint


api_v1 = Blueprint('api_v1',__name__,url_prefix='/api/v1')
api = Api(api_v1)

api.add_resource(All_Products_Endpoint,'/products')
api.add_resource(One_Product_Endpoint,'/products/<int:product_id>')
api.add_resource(All_Sales_Endpoint,'/products/<int:product_id>/sales')
api.add_resource(One_Sale_Endpoint,'/sales/<int:sale_id>')

   
