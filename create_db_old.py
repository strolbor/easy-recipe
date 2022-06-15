from app import db
from app.rezept import rezept, zutat

r1 = rezept(name="Omlett",bild="")
r2 = rezept(name="Kartoffelsalat mit Mayonnaise",bild="")
r3 = rezept(name="Apfelkuchen",bild="")

db.session.add_all([r1,r2,r3])
db.session.commit()
print(r1)
print(rezept.query.all())

def addZutat(name, einheit, bild):
    new = zutat(name, einheit, bild)
    db.session.add(new)
    db.session.commit()

def addRezept(name, bild):
    new = rezept(name, bild)
    db.session.add(new)
    db.session.commit()

def addHandlung(bild, bild2,text):
    new = rezept(bild, bild2,text)
    db.session.add(new)
    db.session.commit()

def addTags(bild, bild2,text):
    new = rezept(bild, bild2,text)
    db.session.add(new)
    db.session.commit()

if 1 == 0:
    addZutat(name='Mehl', einheit='Gramm', bild='none')
    addZutat(name='Kartoffeln', einheit='Kilogramm', bild='none')
    addZutat(name='Zwiebeln', einheit='Gramm', bild='none')
    addZutat(name='Gemüsebrühe', einheit='Milliliter', bild='none')
    addZutat(name='Essig', einheit='Esslöffel', bild='none')
    addZutat(name='Senf', einheit='Teelöffel', bild='none')
    addZutat(name='Salz', einheit='Teelöffel', bild='none')
    addZutat(name='Pfeffer', einheit='Teelöffel', bild='none')
    addZutat(name='Zucker', einheit='Teelöffel', bild='none')
    addZutat(name='Mayonnaise', einheit='Gramm', bild='none')
    addZutat(name='Fleischwurst', einheit='Gramm', bild='none')
    addZutat(name='Gewürzgurken', einheit='Gramm', bild='none')

if 1 == 1:
    z1= zutat(name='Mehl', einheit='Gramm', bild='none')
    z2= zutat(name='Kartoffeln', einheit='Kilogramm', bild='none')
    z3= zutat(name='Zwiebeln', einheit='Gramm', bild='none')
    z4= zutat(name='Gemüsebrühe', einheit='Milliliter', bild='none')
    z5= zutat(name='Essig', einheit='Esslöffel', bild='none')
    z6= zutat(name='Senf', einheit='Teelöffel', bild='none')
    z7= zutat(name='Salz', einheit='Teelöffel', bild='none')
    z8= zutat(name='Pfeffer', einheit='Teelöffel', bild='none')
    z9= zutat(name='Zucker', einheit='Teelöffel', bild='none')
    z10= zutat(name='Mayonnaise', einheit='Gramm', bild='none')
    z11 = zutat(name='Fleischwurst', einheit='Gramm', bild='none')
    z12 = zutat(name='Gewürzgurken', einheit='Gramm', bild='none')
    db.session.add(z1)
    db.session.add(z2)
    db.session.add(z3)
    db.session.add(z4)
    db.session.add(z5)
    db.session.add(z6)
    db.session.add(z7)
    db.session.add(z8)
    db.session.add(z9)
    db.session.add(z10)
    db.session.add(z11)
    db.session.add(z12)
    db.session.commit()
