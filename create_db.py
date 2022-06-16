from app import db
from app.rezept import handlungsschritt, rezept, zutat, tags

def addZutat(name, einheit, bild):
<<<<<<< HEAD
    new = zutat(name=name, einheit=einheit, bild=bild)
    db.session.add(new)
    db.session.commit()

def addRezept(name, bild):
    new = rezept(name=name, bild=bild)
    db.session.add(new)
=======
    new_zutat = zutat(name=name, einheit=einheit, bild=bild)
    db.session.add(new_zutat)
>>>>>>> 2aa6afb2d6e48c766fed1bc595b8bdc38cf7f24b
    db.session.commit()

def addHandlung(bild, bild2,text):
    new = handlungsschritt(bild=bild, bild2=bild2,text=text)
    db.session.add(new)
    db.session.commit()

def addTags(name):
    new = rezept(name=name)
    db.session.add(new)
    db.session.commit()

# Es werden alle Rezepte angelegt
addRezept(name="Omlett",bild="")
addRezept(name="Kartoffelsalat mit Mayonnaise",bild="")
addRezept(name="Apfelkuchen",bild="")

# Es werden alle Zutaten angelegt
addZutat(name="Mehl",bild="none",einheit="Gramm")
addZutat(name="Zwiebeln",bild="none",einheit="Gramm")
addZutat(name="Gemüsebrühe",bild="none",einheit="Milliliter")
addZutat(name="Essig",bild="none",einheit="Esslöffel")
addZutat(name="Senf",bild="none",einheit="Teelöffel")
addZutat(name="Salz",bild="none",einheit="Teelöffel")
addZutat(name="Pfeffer",bild="none",einheit="Teelöffel")
addZutat(name="Zucker",bild="none",einheit="Teelöffel")
addZutat(name="Mayonnaise",bild="none",einheit="Gramm")
addZutat(name="Fleischwurst",bild="none",einheit="Gramm")
addZutat(name="Gewürzgurken",bild="none",einheit="Gramm")
addZutat(name="Ei",bild="",einheit="Normalgröße")

# Es werden alle handlungsschritte angelegt
addHandlung(text="reer",bild="Screenshot_2022-05-25_235554.png",bild2="Screenshot_2022-05-26_000200.png")

# Es werden alle Tags angelegt
addTags(name="Keine Angabe")
addTags(name="Vegan")
addTags(name="Vegetarisch")


# Das Rezept Omlett hat folgende Zutaten: [Ei in der Einheit: Normalgröße und der ID: 14, Mehl in der Einheit: Gramm und der ID: 2]
rezept.query.get(1).zutaten.append(zutat.query.get(14))
rezept.query.get(1).zutaten.append(zutat.query.get(2))
# Das Rezept Kartoffelsalat mit Mayonnaise hat folgende Zutaten: [Zwiebeln in der Einheit: Gramm und der ID: 4, Gemüsebrühe in der Einheit: Milliliter und der ID: 5, Essig in der Einheit: Esslöffel und der ID: 6, Mayonnaise in der Einheit: Gramm und der ID: 11, Fleischwurst in der Einheit: Gramm und der ID: 12, Gewürzgurken in der Einheit: Gramm und der ID: 13]
rezept.query.get(2).zutaten.append(zutat.query.get(4))
rezept.query.get(2).zutaten.append(zutat.query.get(5))
rezept.query.get(2).zutaten.append(zutat.query.get(6))
rezept.query.get(2).zutaten.append(zutat.query.get(11))
rezept.query.get(2).zutaten.append(zutat.query.get(12))
rezept.query.get(2).zutaten.append(zutat.query.get(13))
# Das Rezept Apfelkuchen hat folgende Zutaten: [Mehl in der Einheit: Gramm und der ID: 2, Salz in der Einheit: Teelöffel und der ID: 8, Zucker in der Einheit: Teelöffel und der ID: 10, Ei in der Einheit: Normalgröße und der ID: 14]
rezept.query.get(3).zutaten.append(zutat.query.get(2))
rezept.query.get(3).zutaten.append(zutat.query.get(8))
rezept.query.get(3).zutaten.append(zutat.query.get(10))
rezept.query.get(3).zutaten.append(zutat.query.get(14))

# Es werden alle Tags angelegt

# Das Rezept Omlett hat folgende Tags: []
# Das Rezept Kartoffelsalat mit Mayonnaise hat folgende Tags: []
# Das Rezept Apfelkuchen hat folgende Tags: [<tags 1>]
rezept.query.get(3).tags.append(tags.query.get(1))

db.session.commit()