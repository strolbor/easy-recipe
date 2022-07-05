from tkinter.messagebox import NO
from app import db
from app.rezept import rezept,handlungsschritt,AssociationRHhat
import sqlalchemy

print("[Add Assoc]")
rezept1 = rezept.query.get(1)
print("Rezept:",rezept1)
hand1 = handlungsschritt.query.filter_by(id=1).first()
print("Zutat:",hand1)

if rezept1 is None:
    r1 = rezept(name="Test 1")
    db.session.add(r1)
    db.session.commit()

if hand1 is None:
    h1 = handlungsschritt(text="Lorum ipsum")
    db.session.add(h1)
    db.session.commit()
    hand1 = h1

assoc1 = AssociationRHhat(position=1) # Extra Daten hinzufügen
assoc1.hatid = hand1 # Verknüpfung
print(assoc1)
try:
    with db.session.no_autoflush:
        rezept1.handlungsschritte.append(assoc1)
    print("Rezept handlungsschritte",rezept1.handlungsschritte)
    db.session.commit()
except sqlalchemy.exc.IntegrityError:
    print("Rolling back")
    db.session.rollback()

print("\r\nTest Assoc")
# iterate through child objects via association, including association
# attributes
for assoc in rezept1.handlungsschritte:
    print(">",assoc.position)
    print(">",assoc.rid) 
    print(">",assoc.hid)
    print(">---")

ass = AssociationRHhat.query.get((1,1))
print("\r\nAssociation (1)",ass)

print("rezept1.zutaten",rezept1.handlungsschritte)

print("Remove Assoc")
# Remove Association
rezept1.handlungsschritte.remove(assoc)
print(rezept1.handlungsschritte)
db.session.commit()