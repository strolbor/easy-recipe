from app import db
from app.rezept import Association, rezept, zutat
import sqlalchemy

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
   db.session.rollback()

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
   db.session.rollback()

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
   db.session.rollback()

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
   db.session.rollback()

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
   db.session.rollback()

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
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Schmand hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Zuckerschote hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(260)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Lachs-Schnecken wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Lachs-Schnecken wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Lachs-Schnecken wird Räucherlachs in Scheiben hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(188)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Lachs-Schnecken wird Dill hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Lachs-Schnecken wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Schinken-Käse-Stangen wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Schinken-Käse-Stangen wird Schmand hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Schinken-Käse-Stangen wird Räucherschinken hinzugefügt.')
   assoc1 = Association(menge=80,optional=False)
   zutat = zutat.query.get(189)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Schinken-Käse-Stangen wird Käse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Milch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Blätterteig-Tomaten-Quadrate wird Fleur de Sel hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(55)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird TULIP Bacon-Scheiben hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(236)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Butter hinzugefügt.')
   assoc1 = Association(menge=25,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Ei hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=25,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Gulasch vom Schwein hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(70)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Butterschmalz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Senf hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Karotte hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Bier hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(12)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Saucenbinder hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(196)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Öl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Karotte hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Porree hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(170)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gemüse-Eintopf wird Kräutersalz und Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(119)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Butter hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Rosmarin hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Meersalz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(140)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Kreuzkümmel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(113)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Meersalz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(140)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Quark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Petersilie hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Schnittlauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Schalotte hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(202)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kräuterquark wird Sahne hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Pflanzenöl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(166)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Tomatenketchup hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(230)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Kirschtomate hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Gewürzgurke hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Pizzatomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(169)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Cheddarkäse hinzugefügt.')
   assoc1 = Association(menge=120,optional=False)
   zutat = zutat.query.get(25)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Milch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Sesam hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(214)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Ingwer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Zitrone hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Zucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Sambal Oelek hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(195)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Hühnerbrühe hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Lauchzwiebel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(127)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Cherrytomate hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(26)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Rigatoni hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(176)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Zucker hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Butter hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Sahne hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Vollmilch hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(241)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Kräutersalz und Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(119)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Muskat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Butterflöckchen hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(19)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rindergulasch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(179)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Butterschmalz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rinderbrühe hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(177)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rotwein hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Zucker hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Majoran hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Lorbeerblätter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(131)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Karotte hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Petersilie oder TK hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(162)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Mehl hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Zucker hinzugefügt.')
   assoc1 = Association(menge=75,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Margarine hinzugefügt.')
   assoc1 = Association(menge=75,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Margarine hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Zucker hinzugefügt.')
   assoc1 = Association(menge=225,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Vanillepuddingpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Ei hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird Quark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird saure Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(199)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Käsekuchen der Welt wird süße Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(225)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Mehl hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Wasser hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Salz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Frischhefe hinzugefügt.')
   assoc1 = Association(menge=5,optional=False)
   zutat = zutat.query.get(56)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Pizzatomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(169)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Zucker hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Butterkeks hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(20)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Butter hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zucker hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Speisestärke hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Magerquark hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Sahne hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zitronensaft hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Schmand hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zucker hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zitronensaft hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()



from app import db
from app.rezept import Association, rezept, zutat

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Penne hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(159)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Pinienkerne hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Rucola hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Cocktailtomaten hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Pesto hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Ei hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Mehl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Sahne hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Muskat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Käse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird HENGLEIN Eierspätzle hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(76)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Schweinefilet hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Senf hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Schinken hinzugefügt.')
   assoc1 = Association(menge=8,optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Champignons hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Majoran hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Dill hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Petersilie oder TK hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(162)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Spätzle wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Schweinefilet hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Butter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Katenschinken hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(100)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Champignons hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Fleischbrühe hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(54)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Sahne hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Speisestärke hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Petersilie hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Schinken hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Franzbrötchen wird Henglein Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(75)
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
   print('Rezept: Franzbrötchen wird Äpfel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(263)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

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
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Rosmarin hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=60,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Gnocchi hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(68)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Brühe hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(16)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Hühnerfleisch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(87)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Mehl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Erdnüsse hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(47)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Zucker hinzugefügt.')
   assoc1 = Association(menge=25,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Weißwein hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(245)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Essig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(48)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Szechuanpfeffer hinzugefügt.')
   assoc1 = Association(menge=10,optional=False)
   zutat = zutat.query.get(224)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Ingwer hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=20,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Butterschmalz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Karotte hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Knollensellerie hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(107)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rotwein hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rindfleisch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(182)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rinderbrühe hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(177)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Lorbeerblätter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(131)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Saucenbinder hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(196)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird süße Sahne hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(225)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Kräuter hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Zucker hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackbällchen Toscana wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird HENGLEIN Kartoffelnudeln hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Sauerkraut hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(197)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Öl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Schmand hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Milch hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Käse hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Ananasstücke hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(3)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Sahne hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Sahne-Schmelzkäse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Honig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Currypulver hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Hühnerbrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Reis hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Hähnchen-Ananas-Curry mit Reis wird Chilipulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Hühnerbrust hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Limonensaft oder Zitronensaft hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(129)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Joghurt hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Garam Masala hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(60)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Ingwerpaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(89)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Butter hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Tomatenketchup hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(230)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Zimtpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(252)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Ingwerpaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(89)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Honig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Sahne hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Korianderblätter hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(111)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Hühnerbrüste hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(86)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kardamomkapsel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(95)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Nelke hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(149)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Pflanzenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(166)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Ingwerpaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(89)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Koriander hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(110)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Piment hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(167)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kreuzkümmel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(113)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kurkuma hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(120)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Chiliflocken hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Tomatenpüree hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(232)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Mandelmehl hinzugefügt.')
   assoc1 = Association(menge=75,optional=False)
   zutat = zutat.query.get(138)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Hühnerbrühe hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Schlagsahne hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(206)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Nudeln hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Cocktailtomaten hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Rucola hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Oliven hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(151)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Pinienkerne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Öl von den Tomaten hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(264)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Aceto balsamico hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(1)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Senf hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Wasser hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=25,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Frischhefe hinzugefügt.')
   assoc1 = Association(menge=40,optional=False)
   zutat = zutat.query.get(56)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Salz hinzugefügt.')
   assoc1 = Association(menge=20,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Zucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Mehl hinzugefügt.')
   assoc1 = Association(menge=925,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Möhre hinzugefügt.')
   assoc1 = Association(menge=375,optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Zimtpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(252)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Öl hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Ei hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Mandel hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(137)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Puderzucker hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, Rüblikuchen oder Möhrenkuchen wird Zitronensaft hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Speck hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(219)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Gouda hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(69)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Sonnenblumenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(217)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Schnittlauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Kritharaki hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(115)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Tomatenketchup hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(230)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Oregano hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Fertigmischung für Salatsauce hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(50)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Baguette hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(6)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Öl hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Lauch hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Wasser hinzugefügt.')
   assoc1 = Association(menge=700,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Schmelzkäse hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(208)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Muskat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Knoblauchpulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(106)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Käse-Lauch-Suppe mit Hackfleisch wird Zwiebelpulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(262)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Hokkaidokürbis hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(81)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Möhre hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Ingwer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Zwiebelpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(262)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Butter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Zitrone hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Kürbissuppe mit Ingwer und Kokosmilch wird Koriandergrün hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(112)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Petersilie oder TK hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(162)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Rotwein hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Milch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Butter hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Mehl hinzugefügt.')
   assoc1 = Association(menge=40,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Zitronensaft hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Muskat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Lasagneplatte hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(125)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Käse hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Butterflöckchen hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(19)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Karotte hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Geflügelfleisch hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(61)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Champignons hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Kirschtomate hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Chiliflocken hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kräuter-Tomatenpfanne mit saftigem Geflügelfleisch wird Gemüsezwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(65)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Quark hinzugefügt.')
   assoc1 = Association(menge=120,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Ei hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Käse hinzugefügt.')
   assoc1 = Association(menge=120,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Käse hinzugefügt.')
   assoc1 = Association(menge=60,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Tomatensauce hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(233)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Fleisch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(53)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Gemüse hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(63)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Rucola hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Quark hinzugefügt.')
   assoc1 = Association(menge=120,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Käse hinzugefügt.')
   assoc1 = Association(menge=160,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Lauchzwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(127)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Speckwürfel hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(220)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Magerquark hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Käse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Ei hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Ketchup hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(101)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Naturjoghurt hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(148)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Schmelzkäse hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(208)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Gewürzgurke hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Salat hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(193)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Lachsfilet hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(124)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Schafskäse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(201)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Champignons hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Cherrytomate hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(26)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengemüse wird Chiliöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(32)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Hühnerbrust hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Gurke hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(71)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Strauchtomate hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(223)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Schalotte hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(202)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Milch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Currypulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb Hähnchenbrust mit Zucchini und Tomaten in cremiger Frischkäsesauce wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Cashewkerne hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(22)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Currypulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Ingwer hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Weißweinessig hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(246)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Joghurt hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=750,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Butter hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Zimtstange hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(253)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Kardamompulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(96)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Chiliflocken hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Sahne hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Makhani Hähnchen wird Koriandergrün hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(112)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Mehl hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Quark hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Milch hinzugefügt.')
   assoc1 = Association(menge=70,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Öl hinzugefügt.')
   assoc1 = Association(menge=5,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Lauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Schinken hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Schmand hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Käse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Cocktailtomaten hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Sahne hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Sahne-Schmelzkäse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-Hähnchen in Basilikum-Sahnesauce wird Kräuterbutter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(118)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Schweinefilet hinzugefügt.')
   assoc1 = Association(menge=650,optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Bacon hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(5)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Öl hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Champignons hinzugefügt.')
   assoc1 = Association(menge=750,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Butter hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Schinkenspeck hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(204)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Sahne hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Brühepulver hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(17)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Weißwein hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(245)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Worcestersauce hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(248)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Mehl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Spätzle hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(222)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Öl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Spätzle wird Butter hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Penne hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(159)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Pinienkerne hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Rucola hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Parmaschinken hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(157)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=70,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Balsamico hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(7)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Pesto hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Honig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Nudeln hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Wasser hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Naturjoghurt hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(148)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Petersilie hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf türkische Art wird Thymian hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Farfalle hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(49)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Schafskäse am Stück hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(200)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Pinienkerne hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Basilikumblätter hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(11)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafskäse und Basilikum wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Champignons hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Mais hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(134)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Tomatensauce hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(233)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Sahne-Schmelzkäse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Brötchen hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(15)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Majoran hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Pfeffer aus der Mühle hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(164)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Petersilie hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Maggi hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(133)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Margarine hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Reis hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Kräuter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Joghurt hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Sahne hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Schmand hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Käse hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-Hähnchen wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Knoblauchgranulat hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(105)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Kräuter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Milch hinzugefügt.')
   assoc1 = Association(menge=240,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mehl hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Trockenhefe hinzugefügt.')
   assoc1 = Association(menge=10,optional=False)
   zutat = zutat.query.get(235)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Zucker hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Salz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Butter hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pesto hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pesto hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Peperoni hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(160)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Oliven hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(151)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Bacon hinzugefügt.')
   assoc1 = Association(menge=12,optional=False)
   zutat = zutat.query.get(5)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Barbecuesauce hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(9)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Zucker hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Mehl hinzugefügt.')
   assoc1 = Association(menge=240,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Zucker hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Milch hinzugefügt.')
   assoc1 = Association(menge=480,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Butter hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Ahornsirup hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(2)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischkäse wird Johannisbeeren hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(93)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Hühnerbrust hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Ingwerwurzel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(90)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Hühnerbrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Currypaste hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Champignons hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Zitronengras hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(255)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird chinesische Eiernudeln hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(33)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Öl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Koriandergrün hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(112)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und Hühnchen wird Chilifäden hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(28)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Quark hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Milch hinzugefügt.')
   assoc1 = Association(menge=8,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Öl hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Röstzwiebeln hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(190)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Käse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-Bällchen wird Schinkenwürfel hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(205)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Mehl hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Hefe hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(74)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Wasser hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Salz hinzugefügt.')
   assoc1 = Association(menge=10,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Sahne hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Butter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Rigatoni hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(176)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Kochschinken hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(108)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Edamer Käse hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(42)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rinderroulade hinzugefügt.')
   assoc1 = Association(menge=8,optional=False)
   zutat = zutat.query.get(181)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=5,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Gewürzgurke hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Senf hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Frühstücksspeck hinzugefügt.')
   assoc1 = Association(menge=12,optional=False)
   zutat = zutat.query.get(59)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Butterschmalz hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Knollensellerie hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(107)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Möhre hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Lauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rotwein hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rinderfond hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(178)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Speisestärke hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Gurkenflüssigkeit hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(72)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Linsen hinzugefügt.')
   assoc1 = Association(menge=175,optional=False)
   zutat = zutat.query.get(130)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Chilipulver hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Kurkuma hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(120)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Sonnenblumenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(217)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Kakaopulver hinzugefügt.')
   assoc1 = Association(menge=30,optional=False)
   zutat = zutat.query.get(94)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Butter hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Fett hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Butter hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Magerquark hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Ei hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillepuddingpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanilleschote hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(238)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Öl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Currypulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Chilipulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Hokkaidokürbis hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(81)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Basilikum hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Gnocchi hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(68)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger Kürbis-Gnocchi-Auflauf wird Mozzarella hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Öl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Wasser hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Crème double hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(35)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Speckwürfel hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(220)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Schmand hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Schnittlauch hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Pflanzenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(166)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Ingwerwurzel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(90)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Currypaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Erdnussbutter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(45)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Frühlingszwiebel hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Bambussprosse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(8)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Maiskölbchen hinzugefügt.')
   assoc1 = Association(menge=10,optional=False)
   zutat = zutat.query.get(135)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Fischsauce hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(52)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Palmzucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(154)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Zitronengraspaste  hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(256)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Thai-Basilikum hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(226)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Jasminreis oder Duftreis hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(91)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Lauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Kirschtomate hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Pflanzenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(166)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Hackfleisch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gemüse wird Käse hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Wirsing hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(247)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Kasseler hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(99)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Schupfnudeln aus dem Kühlregal hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(210)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird saure Sahne hinzugefügt.')
   assoc1 = Association(menge=125,optional=False)
   zutat = zutat.query.get(199)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Käse hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Kümmelpulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(123)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Schnittlauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird HENGLEIN Kartoffelnudeln hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Wirsing hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(247)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Kasseler hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(99)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Pflanzenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(166)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Brühe hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(16)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Schmand hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Senf hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Liebstöckel - Blättchen hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(128)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Kümmel hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(122)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Käse hinzugefügt.')
   assoc1 = Association(menge=60,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Schnittlauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Sauerrahm hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(198)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Fleischbrühe hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(54)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Drillinge hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(40)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Butter hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Katenschinken hinzugefügt.')
   assoc1 = Association(menge=75,optional=False)
   zutat = zutat.query.get(100)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Rosmarinnadeln hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(185)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Toastbrot hinzugefügt.')
   assoc1 = Association(menge=5,optional=False)
   zutat = zutat.query.get(228)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Lauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Butter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Lachsfilet hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(124)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Sahne hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Dill hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Blätterteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=8,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Walnüsse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(242)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Blattspinat hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(13)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Walnüssen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Erdnussöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(46)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Hühnerbrust hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Currypaste hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Erdnussbutter hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(45)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Zuckerschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(260)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Karotte hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Bambussprosse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(8)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Speisestärke hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Wasser hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Zitronengraspaste  hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(256)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Duftreis hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(41)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Wasser hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-Hühnchen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Fleisch hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(53)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Currypaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Wasser hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Kokosmilch hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Gemüse nach Wahl hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(62)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Fischsauce hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(52)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Palmzucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(154)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Peperoni hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(160)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Chilischote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Thai-Basilikum hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(226)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry für mehrere Variationen wird Rapskernöl oder Erdnussöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(174)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Tortellini hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(234)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Kochschinken hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(108)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Butter hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Sahne hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Parmesan hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Muskat hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Salz hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Honig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Sojasauce hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Chilisauce hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(30)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Preiselbeeren hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(171)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Ketchup hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(101)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Kartoffel hinzugefügt.')
   assoc1 = Association(menge=800,optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Rosmarin hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Thymian hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Hühnerbrühe hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer Hähnchen-Auflauf wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Mehl hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Zucker hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Butter hinzugefügt.')
   assoc1 = Association(menge=70,optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Magerquark hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Zucker hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Vanillepuddingpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Ei hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Sahne hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Milch hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Öl hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Tränenkuchen - der beste Käsekuchen der Welt! wird Puderzucker hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Schafskäse am Stück hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(200)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=600,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Champignons hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Crème fraîche hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Oregano hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Schafskäse am Stück hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(200)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Türkischer Hackfleischauflauf mit Schafskäse wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird HENGLEIN Strudelteig hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(80)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Veggie-Hack hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(240)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Gemüsezwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(65)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Paprikaschote hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Zuckerschote hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(260)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Mungobohnensprossen hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(145)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Sesamöl hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(215)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Chiliflocken hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Frühlingsrollen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Reis hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Emmentaler hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(44)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Möhre hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Ei hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Semmelbrösel hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(212)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Butterschmalz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Kichererbsen aus der Dose hinzugefügt.')
   assoc1 = Association(menge=250,optional=False)
   zutat = zutat.query.get(102)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=200,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Wurzelgemüse hinzugefügt.')
   assoc1 = Association(menge=80,optional=False)
   zutat = zutat.query.get(249)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=400,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Rosinen hinzugefügt.')
   assoc1 = Association(menge=50,optional=False)
   zutat = zutat.query.get(183)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Zucker hinzugefügt.')
   assoc1 = Association(menge=20,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Gemüsebrühe hinzugefügt.')
   assoc1 = Association(menge=350,optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Cayennepfeffer hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Kreuzkümmelpulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(114)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Zimtpulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(252)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Würziger Kichererbseneintopf wird Zitrone hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Margarine hinzugefügt.')
   assoc1 = Association(menge=350,optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Mehl hinzugefügt.')
   assoc1 = Association(menge=350,optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Zucker hinzugefügt.')
   assoc1 = Association(menge=350,optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Vanillezucker hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Backpulver hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Ei hinzugefügt.')
   assoc1 = Association(menge=6,optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Zitrone hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Puderzucker hinzugefügt.')
   assoc1 = Association(menge=300,optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Hühnerbrustfilet hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Currypaste hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Karotte hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Wasser hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Brühepulver hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(17)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=4,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Ziegenfrischkäse hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(250)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit Hähnchen und Tomate wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Zwiebel hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Knoblauch hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Rinderhackfleisch hinzugefügt.')
   assoc1 = Association(menge=500,optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Milch hinzugefügt.')
   assoc1 = Association(menge=100,optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Sauerrahm hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(198)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Käse hinzugefügt.')
   assoc1 = Association(menge=150,optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Paprikapulver hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Oregano hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Thymian hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Petersilie hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Zucchini hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Olivenöl hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Tomaten hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Mineralwasser hinzugefügt.')
   assoc1 = Association(menge=2,optional=False)
   zutat = zutat.query.get(143)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Tomatenmark hinzugefügt.')
   assoc1 = Association(menge=3,optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Frischkäse hinzugefügt.')
   assoc1 = Association(menge=1,optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Salz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Kräuter der Provence hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Gewürz hinzugefügt.')
   assoc1 = Association(menge=0,optional=False)
   zutat = zutat.query.get(66)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier über mir')
   db.session.rollback()

