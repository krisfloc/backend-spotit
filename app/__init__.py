from app.config import Config
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


"This can be changed to your local setup, if you use a different set of variables"
#POSTGRES = {
   # 'user': 'postgres',
   # 'pw': 'password',
   # 'db': 'postgres',
   # 'host': 'localhost',
   # 'port': '5432',
#}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lgzazgjiscblnh:b817d88f94aefcf2c4b892a5aea7f8b996b01550225c500423e7fabde63a18ca@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d3ntkg8sda8oq1'

app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes, models
