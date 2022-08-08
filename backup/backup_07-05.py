# 05.07.2021 BAckup

from app import db
from app.rezept import rezept, zutat, tags, handlungsschritt

def addZutat(name, einheit, bild, id):
    new = zutat(name=name, einheit=einheit, bild=bild,id=id)
    db.session.add(new)
    db.session.commit()

def addRezept(name, bild,id):
    new = rezept(name=name, bild=bild,id=id)
    db.session.add(new)
    db.session.commit()

def addHandlung(bild, bild2,text,id):
    new = handlungsschritt(bild=bild, bild2=bild2,text=text,id=id)
    db.session.add(new)
    db.session.commit()

def addTags(name,id):
    new = tags(name=name,id=id)
    db.session.add(new)
    db.session.commit()

# Es werden alle Rezepte angelegt
addRezept(name="Omlett",bild="rezept1\1600x1200_omelett-grundrezept.jpg",id=1)
addRezept(name="Kartoffelsalat mit Mayonnaise",bild="",id=2)
addRezept(name="Apfelkuchen",bild="",id=3)
addRezept(name="Rührei",bild="rezept4/Screenshot_2022-05-26_000200.png",id=4)

# Es werden alle Zutaten angelegt
addZutat(name="Mehl",bild="None",einheit="Gramm",id=1)
addZutat(name="Zwiebeln",bild="None",einheit="Gramm",id=2)
addZutat(name="Gemüsebrühe",bild="None",einheit="Milliliter",id=3)
addZutat(name="Essig",bild="None",einheit="Esslöffel",id=4)
addZutat(name="Senf",bild="None",einheit="Teelöffel",id=5)
addZutat(name="Salz",bild="None",einheit="Teelöffel",id=6)
addZutat(name="Pfeffer",bild="None",einheit="Teelöffel",id=7)
addZutat(name="Zucker",bild="None",einheit="Teelöffel",id=8)
addZutat(name="Mayonnaise",bild="None",einheit="Gramm",id=9)
addZutat(name="Fleischwurst",bild="None",einheit="Gramm",id=10)
addZutat(name="Gewürzgurken",bild="None",einheit="Gramm",id=11)
addZutat(name="Ei (mit Bild)",bild="zutat12\egg.jpg",einheit="Normalgröße",id=12)

# Es werden alle handlungsschritte angelegt
addHandlung(text="Handlungsschritt mit Bildern",bild="hand1\Screenshot_2022-05-25_235554.png",bild2="hand1\Screenshot_2022-05-26_000200.png",id=1)
addHandlung(text="Handlungsschritt ohne Bildern",bild="",bild2="",id=2)

# Es werden alle Tags angelegt
addTags(name="Keine Angabe",id=1)
addTags(name="Vegan",id=2)
addTags(name="Ei",id=4)


# Das Rezept Omlett hat folgende Zutaten: [Zwiebeln in der Einheit: Gramm und der ID: 2, Ei (mit Bild) in der Einheit: Normalgröße und der ID: 12]
r = rezept.query.get(1)
r.zutaten.append(zutat.query.get(2))
db.session.commit()
r = rezept.query.get(1)
r.zutaten.append(zutat.query.get(12))
db.session.commit()
# Das Rezept Kartoffelsalat mit Mayonnaise hat folgende Zutaten: [Essig in der Einheit: Esslöffel und der ID: 4, Senf in der Einheit: Teelöffel und der ID: 5, Salz in der Einheit: Teelöffel und der ID: 6, Gewürzgurken in der Einheit: Gramm und der ID: 11, Ei (mit Bild) in der Einheit: Normalgröße und der ID: 12]
r = rezept.query.get(2)
r.zutaten.append(zutat.query.get(4))
db.session.commit()
r = rezept.query.get(2)
r.zutaten.append(zutat.query.get(5))
db.session.commit()
r = rezept.query.get(2)
r.zutaten.append(zutat.query.get(6))
db.session.commit()
r = rezept.query.get(2)
r.zutaten.append(zutat.query.get(11))
db.session.commit()
r = rezept.query.get(2)
r.zutaten.append(zutat.query.get(12))
db.session.commit()
# Das Rezept Apfelkuchen hat folgende Zutaten: [Zwiebeln in der Einheit: Gramm und der ID: 2, Zucker in der Einheit: Teelöffel und der ID: 8, Fleischwurst in der Einheit: Gramm und der ID: 10]
r = rezept.query.get(3)
r.zutaten.append(zutat.query.get(2))
db.session.commit()
r = rezept.query.get(3)
r.zutaten.append(zutat.query.get(8))
db.session.commit()
r = rezept.query.get(3)
r.zutaten.append(zutat.query.get(10))
db.session.commit()
# Das Rezept Rührei hat folgende Zutaten: [Mayonnaise in der Einheit: Gramm und der ID: 9, Ei (mit Bild) in der Einheit: Normalgröße und der ID: 12]
r = rezept.query.get(4)
r.zutaten.append(zutat.query.get(9))
db.session.commit()
r = rezept.query.get(4)
r.zutaten.append(zutat.query.get(12))
db.session.commit()

# Das Rezept Omlett hat folgende Tags: [Ei]
r = rezept.query.get(1)
r.tags.append(tags.query.get(4))
db.session.commit()
# Das Rezept Kartoffelsalat mit Mayonnaise hat folgende Tags: []
# Das Rezept Apfelkuchen hat folgende Tags: [Keine Angabe]
r = rezept.query.get(3)
r.tags.append(tags.query.get(1))
db.session.commit()
# Das Rezept Rührei hat folgende Tags: [Keine Angabe, Ei]
r = rezept.query.get(4)
r.tags.append(tags.query.get(1))
db.session.commit()
r = rezept.query.get(4)
r.tags.append(tags.query.get(4))
db.session.commit()

db.session.commit() 