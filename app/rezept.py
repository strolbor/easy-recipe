from app import db

class rezept(db.Model):
    __tablename__ = "rezept"
    rid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    tags = db.Column(db.String)
    bild = db.Column(db.String)

    def __repr__(self):
        return '<Rezept {}>'.format(self.name)

class zutat(db.Model):
    __tablename__ = "zutat"
    zid = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild = db.Column(db.String)
    name = db.Column(db.String)
    rezept_id = db.Column(db.Integer, db.ForeignKey('rezept.rid'))
    
    def __repr__(self):
        return '<Rezept {}; Einheit: {}>'.format(self.name,self.einheit)

class handlungsschritt(db.Model):
    __tablename__ = "handlungsschritt"
    hid = db.Column(db.Integer,primary_key=True)
    bild = db.Column(db.String)
    bild2 = db.Column(db.String)
    text=db.Column(db.String)
    #relation = db.relationship("Handlungsschritt gehört zum Rezept", db.ForeignKey('rezept.handlungsschritte'))

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

