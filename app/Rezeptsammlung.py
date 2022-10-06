
import app
from app.rezept import zutat, rezept, kategorie
import random
from sqlalchemy.sql.expression import func

class Rezeptsammlung:
    rid = -1
    name = ""
    """speichere Arrays wie Tags,vorhandene/fehlendeZutatenNamen als String, damit auf Website schöner angezeigt wird"""
    tags = ""
    bild = ""

    def __init__(self, _rid, _name, _tags, _bild):
        self.rid=_rid
        self.name = _name

        r_tags = ""
        for tag in _tags:
            r_tags += f"{str(tag).replace('Tag','')}, "
        r_tags = r_tags[:-2]

        if len(r_tags) > 0:
            self.tags = r_tags
        self.bild = _bild


    def __repr__(self):
        return 'Rezept {} mit ID:{} Tags:{} Bild-URL:{} '.format(
            self.name,self.rid,self.tags,self.bild
        )

    def __eq__(self, other):
        return self.rid == other.rid


def isVegan(rez):
    for zut in rez.zutaten:
        fleischkat = kategorie.query.get(5)
        kaesekat = kategorie.query.get(4)
        milchkat = kategorie.query.get(11)

        for katzut in fleischkat.bkat:
            if katzut.id == zut.hatzutat.id:
                return False

        for katzut in kaesekat.bkat:
            if katzut.id == zut.hatzutat.id:
                return False

        for katzut in milchkat.bkat:
            if katzut.id == zut.hatzutat.id:
                return False
    return True

def isVegetarisch(rez):
    for zut in rez.zutaten:
        fleischkat = kategorie.query.get(5)

        for katzut in fleischkat.bkat:
            if katzut.id == zut.hatzutat.id:
                return False
    return True


def isFleisch(rez):
    for zut in rez.zutaten:
        fleischkat = kategorie.query.get(5)

        for katzut in fleischkat.bkat:
            if katzut.id == zut.hatzutat.id:
                return True
    return False

def isEinfach(rez):
    return len(rez.zutaten) < 6


"""BISHER EIGENSCHAFT vegan, vegetarisch, fleisch, einfach"""
def getRezeptByEigenschaft(anzahl, eigenschaft):
    passendeRezepte = []
    alleRez = rezept.query.all()
    for rez in random.sample( alleRez, len(alleRez)):
        bedingung=False

        if eigenschaft=="vegan":
            bedingung = isVegan(rez)
        elif eigenschaft=="vegetarisch":
            bedingung = isVegetarisch(rez)
        elif eigenschaft=="fleisch":
            bedingung = isFleisch(rez)
        elif eigenschaft=="einfach":
            bedingung = isEinfach(rez)

        if bedingung:
            neuesRezept = Rezeptsammlung(_rid=rez.id, _name=rez.name, _tags=rez.tags, _bild=rez.bild)
            passendeRezepte.append(neuesRezept)

        if len(passendeRezepte) >= anzahl:
            return passendeRezepte
    return passendeRezepte

def getRezepteByTag(tag):
    passendeRezepte = []
    for rez in rezept.query.all():
        for _tag in rez.tags:
            if _tag.name == tag:
                neuesRezept = Rezeptsammlung(_rid=rez.id, _name=rez.name, _tags=rez.tags, _bild=rez.bild)
                passendeRezepte.append(neuesRezept)

    return passendeRezepte

def getRezepteByMaxZutaten(anzahl):
    passendeRezepte = []
    for rez in rezept.query.all():
        if len(rez.zutaten) <= anzahl:
            r_tags=""
            for tag in rez.tags:
                r_tags += f"{tag.name}, "
            r_tags = r_tags[:-2]
            neuesRezept = Rezeptsammlung(_rid=rez.id, _name=rez.name, _tags=r_tags, _bild=rez.bild)
            passendeRezepte.append(neuesRezept)

    return passendeRezepte


