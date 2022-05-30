from app import db

class rezept(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    tags = db.Column(db.String)
    bild = db.Column(db.String)

    def __repr__(self):
        return '<Rezept {}>'.format(self.name)

class zutat(db.Model):
    zid = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild = db.Column(db.String)
    name = db.Column(db.String)
    
    def __repr__(self):
        return '<Rezept {}; Einheit: {}>'.format(self.name,self.einheit)

class handlungsschritt(db.Model):
    hid = db.Column(db.Integer,primary_key=True)
    bild = db.Column(db.String)
    bild2 = db.Column(db.String)
    text=db.Column(db.String)

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.hid,self.text)


    
"""
class rezept(db.Model):
    zutaten = ""
    def __init__(self, bildurl, titel, tags, rezeptid):
        self.bildurl = bildurl
        self.titel = titel
        self.tags = tags
        self.rezeptid = rezeptid
"""

