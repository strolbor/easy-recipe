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
    """Das ist die Verknüpfungstabelle zwischen Rezept und Zutat"""
    __tablename__   = "association"
    rid             = db.Column(db.ForeignKey("rezeptsql.id"), primary_key=True)
    zid             = db.Column(db.ForeignKey("zutatsql.id"), primary_key=True)

    # Extra Daten Einträge
    menge           = db.Column(db.String)
    optional        = db.Column(db.Boolean)
    
    # Relationships
    hatzutat        = db.relationship("zutat", back_populates="rezepte", cascade="save-update") # child relationship
    rezept          = db.relationship("rezept", back_populates="zutaten", cascade="save-update") # parents relationship

    def __repr__(self) -> str:
        return "Rezept-Zutat-Verknüpfung mit ({},{})".format(self.rezept,self.hatzutat)

class AssociationRHhat(db.Model):
  """Many to Many Relationship Table bzgl. Rezept und Handlungschritten"""
  __tablename__     = "association_rhhat"
  aid               = db.Column(db.Integer,primary_key=True)
  rid               = db.Column(db.ForeignKey("rezeptsql.id"))
  hid               = db.Column(db.ForeignKey("handlungsschritt.id"))

  # Extra Daten
  position          = db.Column("position", db.Integer())
  
  #Relationsship
  hatid             = db.relationship("handlungsschritt", back_populates="rezepte", cascade="save-update") # child relationship
  rezept            = db.relationship("rezept", back_populates="handlungsschritte", cascade="save-update") # parents relationship

  def __repr__(self) -> str:
    return "Rezept-Handlungsschritt-Verknüpfung: ({},{}) mit ID: {}".format(self.rid,self.hid,self.aid)


rthat= db.Table("association_rthat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezeptsql.id")),
  db.Column("tags_id", db.ForeignKey("tags.id")),
)
"""Many to Many Relationship Table bzgl. Rezept und Tags"""

zkhat= db.Table("association_zkhat",
  db.Model.metadata,
  db.Column("zutat_id",db.ForeignKey("zutatsql.id")),
  db.Column("kategorie_id", db.ForeignKey("kategorie.id")),
)

####################
#      Klassen     #
####################

class rezept(db.Model):
    """Rezept Klasse"""
    __tablename__       = "rezeptsql"
    id                  = db.Column(db.Integer,primary_key=True)
    name                = db.Column(db.String)
    bild                = db.Column(db.String)

    # Extra Attribute
    kurzbeschreibung    = db.Column(db.String)

    # Relationsship zu den Assocation: Rezept <-> Zutat
    zutaten             = db.relationship("Association", back_populates="rezept", cascade="all, delete-orphan")
    
    # Relationsship zu den Assocation: Rezept <-> Handlungsschritt
    handlungsschritte   = db.relationship("AssociationRHhat", back_populates="rezept", cascade="all, delete-orphan")
    
    # Relationsship Rezepte <-> Tags
    tags                = db.relationship('tags', secondary=rthat, # rthat => Rezept-Tags-Many-Many-Relationship
        backref = db.backref('belongs'))

    def __repre__(self):
        return "Rezept: {} mit der ID: {}".format(self.name,self.id)

class handlungsschritt(db.Model):
    """Handlungsschirtt Klasse"""
    __tablename__       = "handlungsschritt"
    id                  = db.Column(db.Integer,primary_key=True)
    bild                = db.Column(db.String)
    bild2               = db.Column(db.String)
    text                = db.Column(db.String)

    # Relationsship zu den Assocation: Rezept <-> Handlungsschritt
    rezepte             = db.relationship("AssociationRHhat",back_populates="hatid",cascade="all, delete-orphan")

    def __repr__(self):
        return '<handlungsschritt {}; Text: {}>'.format(self.id,self.text)

class zutat(db.Model):
    """Zutaten Klasse"""
    __tablename__       = "zutatsql"
    id                  = db.Column(db.Integer,primary_key=True)
    einheit             = db.Column(db.String)
    bild                = db.Column(db.String)
    name                = db.Column(db.String)

    # Relationship
    rezepte             = db.relationship("Association", back_populates="hatzutat",cascade="all, delete-orphan")
    kategorie           = db.relationship('kategorie', secondary=zkhat, backref = db.backref('bkat'))
    
    def __repr__(self):
        return 'Zutat: {} in der Einheit: {} und der ID: {}'.format(self.name,self.einheit,self.id)

class tags(db.Model):
    """ Tags Klasse"""
    __tablename__       = "tags"
    id                  = db.Column(db.Integer,primary_key=True)
    name                = db.Column(db.String)

    def __repr__(self):
        return '{}'.format(self.name)

class kategorie(db.Model):
    """ Kategorie für Zutat Klasse"""
    __tablename__       = "kategorie"
    id                  = db.Column(db.Integer,primary_key=True)
    name                = db.Column(db.String)

    def __repr__(self):
        return '{}'.format(self.name)


