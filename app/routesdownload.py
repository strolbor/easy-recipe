from flask import send_from_directory
from app import app
import os

@app.route('/file/<path:name>')
def showfile(name):
    path = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(path+"/files/",name,as_attachment=False)

@app.route('/dfile/<path:name>')
def downfile(name):
    path = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(path+"/files/",name,as_attachment=True)