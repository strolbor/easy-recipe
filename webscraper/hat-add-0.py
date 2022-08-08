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



