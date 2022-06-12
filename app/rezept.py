from app import db

rzhat = db.Table("association_rzhat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezept.id")),
  db.Column("zutat_id", db.ForeignKey("zutat.id")),
  db.Column("optional", db.Boolean),
  db.Column("Menge", db.Boolean),
)
"""Many to Many Relationship Table"""

class rezept(db.Model):
    """Rezept Klasse"""
    __tablename__ = "rezept"
    id     = db.Column(db.Integer,primary_key=True)
    name    = db.Column(db.String)
    tags    = db.Column(db.String)
    bild    = db.Column(db.String)
    zutaten = db.relationship('zutat', secondary=rzhat,
        backref=db.backref('inhalte'))

    def __repr__(self):
        return '{} mit ID:{}'.format(self.name,self.id)

class zutat(db.Model):
    """Zutaten Klasse"""
    __tablename__ = "zutat"
    id     = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild    = db.Column(db.String)
    name    = db.Column(db.String)
    
    def __repr__(self):
        return '{} in der Einheit: {} und der ID: {}'.format(self.name,self.einheit,self.id)

class handlungsschritt(db.Model):
    """Handlungsschirtt Klasse"""
    __tablename__ = "handlungsschritt"
    id   = db.Column(db.Integer,primary_key=True)
    bild  = db.Column(db.String)
    bild2 = db.Column(db.String)
    text  = db.Column(db.String)

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.id,self.text)
