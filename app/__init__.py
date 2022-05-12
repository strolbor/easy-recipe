from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config["MYSQL_HOST"] = ''
app.config["MYSQL_USER"] = 's242501_3347116'
app.config["MYSQL_PASSWORD"] = 'gha@LfJYQBfYU1Q'
app.config["MYSQL_DB"] = 'db242501x3347116'


from app import routesbackend, routesfrontend, routesdownload, forms