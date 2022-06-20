from app import app
from flask import render_template

@app.route('/nutzer/')
def nutzerhome():
    return render_template('nutzer_home.html')