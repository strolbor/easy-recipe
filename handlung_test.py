from app import db
from app.rezept import rezept,zutat,  Association,handlungsschritt
import sqlalchemy

print("[Add Assoc]")
rezept1 = rezept.query.get(1)
print("Rezept:",rezept1)
hand1 = handlungsschritt.query.filter_by(id=1).first()
print("Zutat:",hand1)

