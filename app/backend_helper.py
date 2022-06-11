import os

from sqlalchemy import desc

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