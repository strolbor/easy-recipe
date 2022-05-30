
class rezept(db.Model):
    zutaten = ""
    def __init__(self, bildurl, titel, tags, rezeptid):
        self.bildurl = bildurl
        self.titel = titel
        self.tags = tags
        self.rezeptid = rezeptid


