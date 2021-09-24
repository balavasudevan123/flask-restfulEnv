from flask import Response, request, jsonify, Flask
from flask_restful import Resource
from db import *
import json
import os
from passlib.context import CryptContext
import math, random
from flask_jwt_extended import jwt_required, get_jwt_identity
import decimal

class SwaggerDemo(Resource):
    @jwt_required()  #use this to protect the function with JWT
    def get(self):
        """
        This API provides full details of an User
        It works also with swag_from, schemas and spec_dict
        ---
        tags:
         - User
        security:
        - Bearer: []
        responses:
          200:
           description: user Details
           schema:
             id: id
             properties:
               id:
                 type: array
                 description: Details of the User
        """
        user_id = get_jwt_identity() #to extract the user ID from JWT access token (Flask Jwt Extended package's predefined function)
        
        return user_id,200