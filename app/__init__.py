from flask import Flask, Blueprint
from flask_restful import Api, Resource
from ..instance.config import app_config



def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True) 
  '''loads the right configurations from config.py given a config name'''
  
  app.config.from_object(app_config[config_name])

  from .api.v1 import api_v1 as v1
  app.register_blueprint(v1)
  
  return app
    