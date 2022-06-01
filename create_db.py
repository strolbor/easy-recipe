from app import db
from app.rezept import rezept, zutat, handlungsschritt

r1 = rezept(name="Omlett")
r2 = rezept(name="Kartoffelsalat mit Mayonnaise")
r3 = rezept(name="Apfelkuchen")

z1=zutat(name='Ei', einheit='Normalgröße',rezept_id=[r1,r3])
z2=zutat(name='Apfel', einheit='Normalgröße',rezept_id=r3)
z3=zutat(name= 'Mehl', einheit='Gramm',rezept_id=[r3,r2])
z4=zutat(name='Kartoffeln', einheit='Kilogramm',rezept_id=r2)
z5=zutat(name='Zwiebeln', einheit='Gramm',rezept_id=r2)
z6=zutat(name='Gemüsebrühe', einheit='Milliliter',rezept_id=r2)
z7=zutat(name= 'Essig', einheit='Esslöffel',rezept_id=r2)
z8=zutat(name= 'Senf', einheit='Teelöffel',rezept_id=r2)
z9=zutat(name= 'Salz', einheit='Teelöffel',rezept_id=r2)
z10=zutat(name='Pfeffer', einheit='Teelöffel',rezept_id=r2)
z11=zutat(name= 'Zucker', einheit='Teelöffel',rezept_id=r2)
z12=zutat(name= 'Mayonnaise', einheit='Gramm',rezept_id=r2)
z13=zutat(name= 'Fleischwurst', einheit='Gramm',rezept_id=r2)
z14=zutat(name= 'Gewürzgurke(n)', einheit='Gramm',rezept_id=r2)