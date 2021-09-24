from flask import Response, request, jsonify, Flask
from flask_restful import Resource
from db import *
import json
import os
from passlib.context import CryptContext
import math, random
from flask_mail import Mail, Message
from flask_jwt_extended import create_access_token
import datetime
from datetime import date

appSrc = Flask(__name__)
mail = Mail(appSrc)

class UserValidate(Resource):
  def post(self):
    """
      JWT Token Generate
      It works also with swag_from, schemas and spec_dict
      ---
      tags:
        - User Authentication
      parameters:
      - name: body
        in: body
        required: true
        description: Jwt token generate
      responses:
        200:
          description: Success message
          schema:
            id: id
            properties:
              id:
                type: array
                description: JWT token and acknowledge with Status
    """
    json_data = request.get_json(force=True)

    #check username and password received as json request and validate the credentials with database table password.
    #after that follow the below code to generate the JWT token for the particular user based on date, expiry date, etc.,
    #We use Flask JWT Extended package for JWT

    #if condition to validate the username and password:
    todayStr = str(date.today())
    expires = datetime.timedelta(days=7)

    #following code returns JWT access token as response
    access_token = create_access_token(identity=str(mobileCheckquery.cus_id), expires_delta=expires)
    response = {
      "code" : "200",
      "jwtToken": access_token,
    }
    return response,200