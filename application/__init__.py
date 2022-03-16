from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
db = SQLAlchemy(app)

url = 'mysql+pymysql://nathan:password@final-db.cbr9zealguel.eu-west-2.rds.amazonaws.com/movies_db'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)

engine= create_engine(url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()

import application.routes 