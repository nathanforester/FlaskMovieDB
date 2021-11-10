from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\workspaceBackup\\DevOps\\BasicProjectExample\\FlaskMovieDB\\flask.sqlite3'
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)

import application.routes 

