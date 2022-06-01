from app import db
from app.rezept import rezept, zutat, handlungsschritt

r1 = rezept(name="Omlett",tags="",bild="")
db.session.add(r1)
r2 = rezept(name="Kartoffelsalat mit Mayonnaise",tags="",bild="")
db.session.add(r2)
r3 = rezept(name="Apfelkuchen",tags="",bild="")
db.session.add(r3)
print(r1)
print(rezept.query.all())

z1=zutat(name='Ei', einheit='Normalgröße',bild="none",rezept_id=r1)
z1a=zutat(name='Ei', einheit='Normalgröße',bild="none",rezept_id=r3)
z2=zutat(name='Apfel', einheit='Normalgröße',bild="none",rezept_id=r3)
z3=zutat(name= 'Mehl', einheit='Gramm',rezept_id=r3,bild="none")
z3a=zutat(name= 'Mehl', einheit='Gramm',rezept_id=r2,bild="none")
z4=zutat(name='Kartoffeln', einheit='Kilogramm',rezept_id=r2,bild="none")
z5=zutat(name='Zwiebeln', einheit='Gramm',rezept_id=r2,bild="none")
z6=zutat(name='Gemüsebrühe', einheit='Milliliter',rezept_id=r2,bild="none")
z7=zutat(name= 'Essig', einheit='Esslöffel',rezept_id=r2,bild="none")
z8=zutat(name= 'Senf', einheit='Teelöffel',rezept_id=r2,bild="none")
z9=zutat(name= 'Salz', einheit='Teelöffel',rezept_id=r2,bild="none")
z10=zutat(name='Pfeffer', einheit='Teelöffel',rezept_id=r2,bild="none")
z11=zutat(name= 'Zucker', einheit='Teelöffel',rezept_id=r2,bild="none")
z12=zutat(name= 'Mayonnaise', einheit='Gramm',rezept_id=r2,bild="none")
z13=zutat(name= 'Fleischwurst', einheit='Gramm',rezept_id=r2,bild="none")
z14=zutat(name= 'Gewürzgurke(n)', einheit='Gramm',rezept_id=r2,bild="none")


if 1 == 0:
    db.session.rollback()


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
    db.session.add(z13)
    db.session.add(z14)
    db.session.commit()
