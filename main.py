from flask import Flask
from db import db
from flask_restful import Api
from resources.routes import initialize_routes
from flasgger import Swagger
import os
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root''@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config.from_pyfile('settings.py')
api = Api(app)
jwt = JWTManager(app)

template = {
  "swagger": "2.0",
  "info": {
    "title": "Title",
    "description": "APIs for project name",
    "contact": {
      "responsibleOrganization": "Organization Name",
      "responsibleDeveloper": "Developer name",
      "email": "email@gmail.com",
      "url": "www.website.com",
    },
    "termsOfService": "www.website.com",
    "version": "1.0.0"
  },
  "host": "127.0.0.1:5000",  # overrides localhost:500
  "basePath": "",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "securityDefinitions":
    {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}}
  ,
  "operationId": "getmyData"
}

swagger = Swagger(app, template=template)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

if __name__ == "__main__":
  # print("__name__ : ",__name__)
  init_db()
  initialize_routes(api)

  app.run(debug=True)
#   port = int(os.environ.get("PORT", 5000))
#   app.run(host='0.0.0.0', port=port, debug=True)