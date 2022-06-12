import os

from sqlalchemy import desc
from werkzeug.utils import secure_filename
from flask import request

def createFolderIfNotExists(name):
    if not os.path.exists(name):
        os.makedirs(name)

def getNewID(classes):
    queryobj = classes.query.order_by(desc(classes.id)).first()
    idneu=0
    if not queryobj is None:
        idneu = int(queryobj.id)+1
    """ Wir suchen die nächste ID"""
    return idneu

def createArrayHelper(arrayeingabe: list) :
    array = []
    for entry in arrayeingabe:
        array.append([entry.id,entry.name])
    return array

def savepic(feldname, rfiles ,ordner) -> str:
    if feldname not in rfiles:
        """ Bild wurde garnicht erst hochgeladen"""
        return "A"
    file = rfiles[feldname]
    if file.filename == '':
        """ Es wurde kein Bild genommen."""
        return "B"
    if file:
        """ Bild ist vorhanden"""
        file = request.files[feldname]
        filename = secure_filename(file.filename)
        createFolderIfNotExists(os.path.join(app.instance_path,ordner))
        path = os.path.join(app.instance_path,ordner,filename)
        bild_url=filename
        file.save(path)
        print("Bild gespeichert")
        return bild_url