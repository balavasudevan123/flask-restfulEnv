from flask import Flask,jsonify,request,render_template,session,redirect
from flask_restful import Api,Resource,fields,marshal_with,abort,reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import random
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root''@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


base = automap_base()
base.prepare(db.engine,reflect=True)

occupation = base.classes.tbl_occupation
