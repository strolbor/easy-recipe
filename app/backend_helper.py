import os
from app import app
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from flask import request
from flask.helpers import flash, url_for
import cv2


def createFolderIfNotExists(name):
    """Ordner erstellen"""
    if not os.path.exists(name):
        os.makedirs(name)


def getNewID(classes):
    """Mithilfe dieser Funktion erhalten wir die neue ID des Rezepts"""
    queryobj = classes.query.order_by(desc(classes.id)).first()
    idneu = 0
    if not queryobj is None:
        idneu = int(queryobj.id)+1
    """ Wir suchen die nächste ID"""
    return idneu


def createArrayHelper(arrayeingabe: list):
    """Mithilfe dieser Funktion wird ein Array der Form [id, {name}] erstellt"""
    array = []
    for entry in arrayeingabe:
        try:
            array.append([entry.id, entry.name])
        except AttributeError:
            array.append([entry.id, entry.text])
    return array


def createArrayHelper2(arrayeingabe: list):
    """Mithilfe dieser Funktion wird ein Array der Form [id, {name} (einheit)] erstellt"""
    array = []
    for entry in arrayeingabe:
        try:
            array.append([entry.id, str(f"{entry.name} ({entry.einheit})")])
        except AttributeError:
            array.append([entry.id, entry.text])
    return array


def savepic(feldname, rfiles, ordner) -> str:
    """Diese Funktion speichert unser Bild ab und anschließend wird es resized."""
    if feldname not in rfiles:
        """ Bild wurde garnicht erst hochgeladen"""
        return "A"
    file = rfiles[feldname]
    if file.filename == '':
        """ Es wurde kein Bild genommen."""
        return "B"
    if file:
        """ Bild ist vorhanden"""
        filename = secure_filename(file.filename)
        print()
        #Dateiendung erfragen, ob es ein Bild ist
        if filename.split(".")[1] not in app.config['ALLOWED_EXTENSIONS']:
            flash(
                f"Es wurde keine Bilddatei im Format {', '.join(app.config['ALLOWED_EXTENSIONS'])} erkannt")
            return "B"
            # Wenn es keine Bilddatei ist, verwirf es
        createFolderIfNotExists(os.path.join(app.instance_path, ordner))
        # Checken, ob es ein Bild ist
        path = os.path.join(app.instance_path, ordner, filename)
        # bild_url=filename
        bild_url = os.path.join(ordner, filename)
        file.save(path)

        img = cv2.imread(path)  # 496 x 370
        width = 496
        height = 370
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, resized)

        print("Bild gespeichert @", bild_url)
        return bild_url
