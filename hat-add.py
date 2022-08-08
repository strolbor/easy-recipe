from app import db
from app.rezept import Association, rezept, zutat
import sqlalchemy

db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
try:
   print('Rezept: Bauerntopf wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
try:
   print('Rezept: Bauerntopf wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
try:
   print('Rezept: Bauerntopf wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
try:
   print('Rezept: Bauerntopf wird Möhre hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
try:
   print('Rezept: Bauerntopf wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()

except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
