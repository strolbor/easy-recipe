from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_mysqldb import MySQL

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SECRET_KEY"] ="bhjewjvhewhewhje"
app.config["MYSQL_HOST"] = ''
app.config["MYSQL_USER"] = 's242501_3347116'
app.config["MYSQL_PASSWORD"] = 'gha@LfJYQBfYU1Q'
app.config["MYSQL_DB"] = 'db242501x3347116'


from app import routesbackend, routesfrontend, routesdownload, forms