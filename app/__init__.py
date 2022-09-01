from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = ""
class Config(object):
    global basedir
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    print(basedir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REZEPTRANKINGS_PER_PAGE = 30


app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath(app.instance_path)
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SECRET_KEY"] ="bhjewjvhewhewhje"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ITEMS_PER_PAGE'] = 1000


app.debug = True

from app import forms, rezept, routesnutzer, \
    routesbackend,routesbackend_function, routes_handlung, routes_rezept, routes_tags, routes_zutat, \
        routesfrontend, routesdownload
