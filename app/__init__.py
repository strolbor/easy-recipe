

from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jsglue import JSGlue

basedir = ""


class Config(object):
    global basedir
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    print(basedir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REZEPTRANKINGS_PER_PAGE = 1000


jsglue = JSGlue()

app = Flask(__name__)
jsglue.init_app(app)
UPLOAD_FOLDER = os.path.abspath(app.instance_path)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SECRET_KEY"] = "bhjewjvhewhewhje"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ITEMS_PER_PAGE'] = 9
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg']

app.debug = True

from app import forms, rezept, routesbackend, routesbackend_function,  routes_rezept, routes_tags, routes_zutat, routesfrontend, routesdownload