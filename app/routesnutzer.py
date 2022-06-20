from app import app
from flask import render_template, send_from_directory

@app.route('/nutzer/')
def nutzerhome():
    return render_template('nutzer_base.html')