from app import db

####################
#        Nutzer    #
####################

class konto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    rights = db.Column(db.String)
    def __repr__(self):
        return '{}'.format(self.name)


####################
#    Beziehungen   #
####################

rzhat = db.Table("association_rzhat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezept.id")),
  db.Column("zutat_id", db.ForeignKey("zutat.id")),
  db.Column("optional", db.Boolean),
  db.Column("Menge", db.Integer),
)
"""Many to Many Relationship Table bzgl. Rezept und Zutaten"""

rhhat= db.Table("association_rhhat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezept.id")),
  db.Column("handlungsschrit_id", db.ForeignKey("handlungsschritt.id")),
  db.Column("position", db.Integer),
)
"""Many to Many Relationship Table bzgl. Rezept und Handlungschritten"""

rthat= db.Table("association_rthat",
  db.Model.metadata,
  db.Column("rezept_id",db.ForeignKey("rezept.id")),
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

class rezept(db.Model):
    """Rezept Klasse"""
    __tablename__ = "rezept"
    id     = db.Column(db.Integer,primary_key=True)
    name    = db.Column(db.String)
    bild    = db.Column(db.String)
    # Relationsships
    zutaten = db.relationship('zutat', secondary=rzhat, # rzhat => Rezept-Zutat-Many-Many-Relationship
        backref=db.backref('inhalte'))
    tags    = db.relationship('tags', secondary=rthat, # rthat => Rezept-Tags-Many-Many-Relationship
        backref = db.backref('belongs'))
    handlungsschritte    = db.relationship('handlungsschritt', secondary=rhhat, # rhhat => Rezept-Handlungsschritt-Many-Many-Relationship
        backref = db.backref('handlungen'))
    

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
