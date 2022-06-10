from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_mysqldb import MySQL

basedir = ""
class Config(object):
    global basedir
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    print(basedir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath(app.instance_path)
print("uploadfolder:",UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.debug = True

from app import routesbackend, routesfrontend, routesdownload, forms, rezept
