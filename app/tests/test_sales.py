import unittest
import json
from app import create_app
import sys


class SalesTestCase(unittest.TestCase):      
  #this class represents the products testcase for the client methods

  def setUp(self):
    #Define test variables and initialize app.
    self.app = create_app(config_name="testing")
    self.client= create_app('testing').test_client()
    self.data = {}
    

  #test if user can get all products by using get method
  def test_get_all_Sales(self):
    response=self.client.get('api/v1/sales',content_type="application/json")
    self.assertEqual(response.status_code,200)

  def test_create_new_sale(self):
    data = {"product_id":1}
    response = self.client.post("/api/v1/sales",data = json.dumps(data),content_type="application/json")
    self.assertEqual(response.status_code,201)

  def test_get_one_sale(self):
    response=self.client.get('api/v1/sales/1',content_type="application/json")
    self.assertEqual(response.status_code,200)

  # def test_wrong_product(self):
  #   response=self.client.get("/api/v1/products/50", content_type = "application/json")
  #   response.status_code = 404
  #   self.assertEqual(response)
    

if __name__ == '__main__':
    unittest.main()