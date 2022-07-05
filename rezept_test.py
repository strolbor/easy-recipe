from app import db
from app.rezept import rezept,zutat,  Association
import sqlalchemy

print("[Add Assoc]")
rezept1 = rezept.query.filter_by(id=1).first()
print("Rezept:",rezept1)
zutat1 = zutat.query.filter_by(id=1).first()
print("Zutat:",zutat1)

#Assoc erstellen
assoc1 = Association(menge=2,optional=True) # Extra Daten hinzufügen
assoc1.hatzutat= zutat1 # Zutat verknüpfen
print(assoc1)
try:
    with db.session.no_autoflush:
        rezept1.zutaten.append(assoc1)
    print("Rezept Zutaten",rezept1.zutaten)
    db.session.commit()
except sqlalchemy.exc.IntegrityError:
    print("Rolling back")
    db.session.rollback()

print("\r\nTest Assoc")
# iterate through child objects via association, including association
# attributes
for assoc in rezept1.zutaten:
    print(">",assoc.menge)
    print(">",assoc.hatzutat)
    print(">",assoc.menge)
    print(">",assoc.optional)
    print(">---")

ass = Association.query.get((1,1))
print("\r\nAssociation (1)",ass)

print("rezept1.zutaten",rezept1.zutaten)

print("Remove Assoc")
# Remove Association
rezept1.zutaten.remove(assoc)
print(rezept1.zutaten)
db.session.commit()