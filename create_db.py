from app import db
from app.rezept import rezept, zutat, handlungsschritt

r1 = rezept(name="Omlett",tags="",bild="")
r2 = rezept(name="Kartoffelsalat mit Mayonnaise",tags="",bild="")
r3 = rezept(name="Apfelkuchen",tags="",bild="")
db.session.add(r1)
db.session.add(r2)
db.session.add(r3)
print(r1)
print(rezept.query.all())

def addZutat(name, einheit, bild):
    new_zutat = zutat(name, einheit, bild)
    db.session.add(new_zutat)
    db.session.commit()

def deleteZutat(zid):
    db.session.delete(zutat.query.get(zid))
    db.session.commit()

if 1 == 0:
    addZutat(name='Ei', einheit='Normalgröße', bild="none")
    addZutat(name='Apfel', einheit='Normalgröße', bild="none")
    addZutat(name='Mehl', einheit='Gramm', bild="none")
    addZutat(name='Kartoffeln', einheit='Kilogramm', bild="none")
    addZutat(name='Zwiebeln', einheit='Gramm', bild="none")
    addZutat(name='Gemüsebrühe', einheit='Milliliter', bild="none")
    addZutat(name='Essig', einheit='Esslöffel', bild="none")
    addZutat(name='Senf', einheit='Teelöffel', bild="none")
    addZutat(name='Salz', einheit='Teelöffel', bild="none")
    addZutat(name='Pfeffer', einheit='Teelöffel', bild="none")
    addZutat(nam1e='Zucker', einheit='Teelöffel', bild="none")
    addZutat(name='Mayonnaise', einheit='Gramm', bild="none")
    addZutat(name='Fleischwurst', einheit='Gramm', bild="none")
    addZutat(name='Gewürzgurken', einheit='Gramm', bild="none")
