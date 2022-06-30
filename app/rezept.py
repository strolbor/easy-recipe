from app import db

####################
#        Nutzer    #
####################
"""
class konto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    rights = db.Column(db.String)
    def __repr__(self):
        return '{}'.format(self.name)
"""

####################
#                  #
####################

class Association(db.Model):
    __tablename__ = "association"
    rid = db.Column(db.ForeignKey("rezeptsql.id"), primary_key=True)
    zid = db.Column(db.ForeignKey("zutatsql.id"), primary_key=True)
    menge = db.Column(db.Integer())
    optional = db.Column(db.Boolean())
    hatzutat = db.relationship("zutat", back_populates="rezepte") # child relationship
    rezept = db.relationship("rezept", back_populates="zutaten") # parents relationship

class rezept(db.Model):
    """Rezept Klasse"""
    __tablename__ = "rezeptsql"
    id     = db.Column(db.Integer,primary_key=True)
    name    = db.Column(db.String)
    bild    = db.Column(db.String)
    zutaten = db.relationship("Association", back_populates="rezept")


class zutat(db.Model):
    """Zutaten Klasse"""
    __tablename__ = "zutatsql"
    id     = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild    = db.Column(db.String)
    name    = db.Column(db.String)
    #parents = db.relationship("Association", back_populates="child")
    rezepte = db.relationship("Association", back_populates="hatzutat")
    
    def __repr__(self):
        return '{} in der Einheit: {} und der ID: {}'.format(self.name,self.einheit,self.id)

####################
#    Beziehungen   #
####################

rhhat= db.Table("association_rhhat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezeptsql.id")),
  db.Column("handlungsschrit_id", db.ForeignKey("handlungsschritt.id")),
  db.Column("position", db.Integer),
)
"""Many to Many Relationship Table bzgl. Rezept und Handlungschritten"""

rthat= db.Table("association_rthat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezeptsql.id")),
  db.Column("tags_id", db.ForeignKey("tags.id")),
)
"""Many to Many Relationship Table bzgl. Rezept und Tags"""

####################
#      Klassen     #
####################

class tags(db.Model):
    """ Tags Klasse"""
    __tablename__ = "tags"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    def __repr__(self):
        return '{}'.format(self.name)

class handlungsschritt(db.Model):
    """Handlungsschirtt Klasse"""
    __tablename__ = "handlungsschritt"
    id   = db.Column(db.Integer,primary_key=True)
    bild  = db.Column(db.String)
    bild2 = db.Column(db.String)
    text  = db.Column(db.String)

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.id,self.text)
