# project\__init__.py

from project.core.views import core
from project.error.handlers import error_pages

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os


app = Flask(__name__)

# ! WTForms Secret Key
app.config['SECRET_KEY'] = 'mysecretkey'

# ! Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
database_dir = os.path.join(basedir, "static/database/")

# sqlite 3
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(database_dir, "data.sqlite3")
# mysql
# app.config["SQLALCHEMY_DATABASE_URI"] = \
#     "mysql+pymysql://root:Nooby123@localhost:3306/test_db?charset=utf8"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

# ! Blueprint Import
app.register_blueprint(core)
app.register_blueprint(error_pages)
