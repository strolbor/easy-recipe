from app import db

rzhat = db.Table("association",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezept.rid")),
  db.Column("zutat_id", db.ForeignKey("zutat.zid")),
)

class rzhat2(db.Model):
    rid=db.Column("rezept_id",db.ForeignKey("rezept.rid"),primary_key=True)
    zid=db.Column("zutat_id", db.ForeignKey("zutat.zid"),primary_key=True)
    
    def __repr__(self):
        return '[rzhat: RID {} <-> ZID: {}]'.format(self.rid,self.zid)


class rezept(db.Model):
    __tablename__ = "rezept"
    rid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    tags = db.Column(db.String)
    bild = db.Column(db.String)
    zutaten = db.relationship('zutat', secondary=rzhat,
        backref=db.backref('rezepte'))

    def __repr__(self):
        return '<Rezept {}> ID:{}'.format(self.name,self.rid)

class zutat(db.Model):
    __tablename__ = "zutat"
    zid = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild = db.Column(db.String)
    name = db.Column(db.String)
    
    def __repr__(self):
        return '<Rezept {}; Einheit: {}> ID={}'.format(self.name,self.einheit,self.zid)

class handlungsschritt(db.Model):
    __tablename__ = "handlungsschritt"
    hid = db.Column(db.Integer,primary_key=True)
    bild = db.Column(db.String)
    bild2 = db.Column(db.String)
    text=db.Column(db.String)

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.hid,self.text)


"""
"""
