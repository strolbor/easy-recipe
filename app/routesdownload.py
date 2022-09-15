from app import app
from flask import send_from_directory


@app.route('/ctl/download/<path:filename>')
def downloadfoto(filename):
    #print(app.config['UPLOAD_FOLDER'], filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)