import unittest
import json
from app import create_app
import sys


class ProductsTestCase(unittest.TestCase):      
  #this class represents the products testcase for the client methods

  def setUp(self):
    #Define test variables and initialize app.
    self.app = create_app(config_name="testing")
    self.client= create_app('testing').test_client()
    self.data = {}
    

  #test if user can get all products by using get method
  def test_get_all_Products(self):
    response=self.client.get('api/v1/products',content_type="application/json")
    self.assertEqual(response.status_code,200)

  def test_create_new_product(self):
    data = {"product_name":"nivea","price":5000,"quantity":40, "category":"body lotion"}
    response = self.client.post("/api/v1/products",data = json.dumps(data),content_type="application/json")
    self.assertEqual(response.status_code,201)

  def test_get_one_product(self):
    response=self.client.get('api/v1/products/1',content_type="application/json")
    self.assertEqual(response.status_code,200)

 

if __name__ == '__main__':
    unittest.main()