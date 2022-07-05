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
#    Beziehungen   #
####################

class Association(db.Model):
    __tablename__ = "association"
    rid = db.Column(db.ForeignKey("rezeptsql.id"), primary_key=True)
    zid = db.Column(db.ForeignKey("zutatsql.id"), primary_key=True)
    menge = db.Column(db.Integer())
    optional = db.Column(db.Boolean())

    hatzutat = db.relationship("zutat", back_populates="rezepte", cascade="save-update") # child relationship
    rezept = db.relationship("rezept", back_populates="zutaten", cascade="save-update") # parents relationship

    def __repr__(self) -> str:
        return "RZ-Verknüpfung mit {} und {}".format(self.rezept,self.hatzutat)

class AssociationRHhat(db.Model):
  """Many to Many Relationship Table bzgl. Rezept und Handlungschritten"""
  __tablename__ = "association_rhhat"
  rid = db.Column(db.ForeignKey("rezeptsql.id"),primary_key=True)
  hid = db.Column(db.ForeignKey("handlungsschritt.id"),primary_key=True)
  position = db.Column("position", db.Integer, unique=True)
  
  #Relationsship
  hatid = db.relationship("handlungsschritt", back_populates="rezepte", cascade="save-update") # child relationship
  rezept = db.relationship("rezept", back_populates="handlungsschritte", cascade="save-update") # parents relationship


rthat= db.Table("association_rthat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezeptsql.id")),
  db.Column("tags_id", db.ForeignKey("tags.id")),
)
"""Many to Many Relationship Table bzgl. Rezept und Tags"""

####################
#      Klassen     #
####################

class rezept(db.Model):
    """Rezept Klasse"""
    __tablename__ = "rezeptsql"
    id     = db.Column(db.Integer,primary_key=True)
    name    = db.Column(db.String)
    bild    = db.Column(db.String)
    # Relationsship zu den Assocation: Rezept <-> Zutat
    zutaten = db.relationship("Association", back_populates="rezept", cascade="all, delete-orphan")
    # Relationsship zu den Assocation: Rezept <-> Handlungsschritt
    handlungsschritte = db.relationship("AssociationRHhat", back_populates="rezept", cascade="all, delete-orphan")

    def __repre__(self):
        return "Rezept: {} mit der ID: {}".format(self.name,self.id)

class handlungsschritt(db.Model):
    """Handlungsschirtt Klasse"""
    __tablename__ = "handlungsschritt"
    id   = db.Column(db.Integer,primary_key=True)
    bild  = db.Column(db.String)
    bild2 = db.Column(db.String)
    text  = db.Column(db.String)
    # Relationsship zu den Assocation: Rezept <-> Handlungsschritt
    rezepte = db.relationship("AssociationRHhat",back_populates="hatid",cascade="all, delete-orphan")

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.id,self.text)

class zutat(db.Model):
    """Zutaten Klasse"""
    __tablename__ = "zutatsql"
    id     = db.Column(db.Integer,primary_key=True)
    einheit = db.Column(db.String)
    bild    = db.Column(db.String)
    name    = db.Column(db.String)
    #parents = db.relationship("Association", back_populates="child")
    rezepte = db.relationship("Association", back_populates="hatzutat",cascade="all, delete-orphan")
    
    def __repr__(self):
        return '{} in der Einheit: {} und der ID: {}'.format(self.name,self.einheit,self.id)

class tags(db.Model):
    """ Tags Klasse"""
    __tablename__ = "tags"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    def __repr__(self):
        return '{}'.format(self.name)


