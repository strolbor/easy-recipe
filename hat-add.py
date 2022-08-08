from app import db
import sqlalchemy
from app.rezept import Association, rezept, zutat

try:
   print('Rezept: Franzbrötchen wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Franzbrötchen wird Margarine hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Franzbrötchen wird Apfel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(266)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Franzbrötchen wird Zimt hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(251)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Franzbrötchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=5,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird HENGLEIN Mini-Knödel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(79)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Spargel hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(218)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Spargel hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(218)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Zucker hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Margarine hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Parmaschinken hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(157)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Margarine hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Mehl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Milch hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Muskat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Frühlingshaftes Spargel-Knödel-Gratin wird Käse hinzugefügt.')
   assoc1 = Association(menge=60,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Kartoffel hinzugefügt.')
