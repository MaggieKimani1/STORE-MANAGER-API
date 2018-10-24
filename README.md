# STORE-MANAGER-API
Api endpoints for inventory management in store manager

[![Build Status](https://travis-ci.com/MaggieKimani1/STORE-MANAGER-API.svg?branch=ch-add-travis-161340662)](https://travis-ci.com/MaggieKimani1/STORE-MANAGER-API)

[![Coverage Status](https://coveralls.io/repos/github/MaggieKimani1/STORE-MANAGER-API/badge.svg?branch=master)](https://coveralls.io/github/MaggieKimani1/STORE-MANAGER-API?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

# STORE-MANAGER-API
⋅⋅*Admin can add a product
⋅⋅*Admin/store attendant can get all products
⋅⋅*Admin/store attendant can get a specific product
⋅⋅*Store attendant can add a sale order
⋅⋅*Admin can get all sale order records

###Endpoints

| HTTP Method   |     Endpoint                |     Function            |
| ------------- |:--------------------------: | -----------------------:|
| GET           | /api/v1/products            |   Get all products      |
| GET           | /api/v1/products/product_id |   Get one product       |
| GET           | /api/v1/sales               |   Get all sales         |
| GET           | /api/v1/products/saleid     |   Get one sale record   |
| POST          | /api/v1/products            |   Create a new sale     |
| POST          | /api/v1/sales               |   Create a new product  |

###Prerequisites
⋅⋅*pip
⋅⋅*virtualenv
⋅⋅*python 3 or python 2.7

##Setting Up Locally
⋅⋅*Clone the repo
⋅⋅*git clone https://github.com/MaggieKimani1/STORE-MANAGER-API
⋅⋅*create a virtual environment and activate it 
⋅⋅*virtualenv env
⋅⋅*install dependencies 
⋅⋅*pip install -r requirements.txt