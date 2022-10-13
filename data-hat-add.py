from app import db
import sqlalchemy
from app.rezept import Association, rezept, zutat

Association.query.delete()

try:
   print('Rezept: Bauerntopf wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird M�hre hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="300 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bauerntopf wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(1)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Lachs-Schnecken wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Rolle(n)",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Lachs-Schnecken wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Lachs-Schnecken wird R�ucherlachs in Scheiben hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(188)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Lachs-Schnecken wird Dill hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Lachs-Schnecken wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(2)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Schinken-K�se-Stangen wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Schinken-K�se-Stangen wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Schinken-K�se-Stangen wird R�ucherschinken hinzugef�gt.')
   assoc1 = Association(menge="80 g",optional=False)
   zutat = zutat.query.get(189)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Schinken-K�se-Stangen wird K�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(3)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Pkt.",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Milch hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bl�tterteig-Tomaten-Quadrate wird Fleur de Sel hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(55)
   rezept1 = rezept.query.get(4)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird TULIP Bacon-Scheiben hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(236)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Butter hinzugef�gt.')
   assoc1 = Association(menge="25 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Ei hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="25 g",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bratkartoffeln mit Bacon und Parmesan wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="1 Prise(n)",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(5)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Gulasch vom Schwein hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(70)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Butterschmalz hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Senf hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Bier hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(12)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="600 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Brauhaus-Gulasch wird Saucenbinder hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(196)
   rezept1 = rezept.query.get(6)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 m.-gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="4 gro�e",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 gr. Dose/n",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Rinderbr�he hinzugef�gt.')
   assoc1 = Association(menge="500 ml",optional=False)
   zutat = zutat.query.get(177)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="4 m.-gro�e",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1 m.-gro�e",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Porree hinzugef�gt.')
   assoc1 = Association(menge="1 Stange/n",optional=False)
   zutat = zutat.query.get(170)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Bunter Hackfleisch-Gem�se-Eintopf wird Kr�utersalz und Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(119)
   rezept1 = rezept.query.get(7)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="800 g",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Butter hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="3 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Rosmarin hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL, gestr.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Kreuzk�mmel hinzugef�gt.')
   assoc1 = Association(menge="1 Msp.",optional=False)
   zutat = zutat.query.get(113)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Meersalz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(140)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Quark hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="� Bund",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Schnittlauch hinzugef�gt.')
   assoc1 = Association(menge="� Bund",optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Schalotte hinzugef�gt.')
   assoc1 = Association(menge="1 kleine",optional=False)
   zutat = zutat.query.get(202)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Catharinas Ofenkartoffeln nach Fiefhusener Art mit Kr�uterquark wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(8)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="�",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Tomatenketchup hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(230)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Kirschtomate hinzugef�gt.')
   assoc1 = Association(menge="6",optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Gew�rzgurke hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Pizzateig hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(77)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Cheddark�se hinzugef�gt.')
   assoc1 = Association(menge="120 g",optional=False)
   zutat = zutat.query.get(25)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Milch hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cheese-Burger-Muffins wird Sesam hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(214)
   rezept1 = rezept.query.get(9)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Schweinefilet hinzugef�gt.')
   assoc1 = Association(menge="600 g",optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="1 St�ck(e)",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Zitrone hinzugef�gt.')
   assoc1 = Association(menge="�",optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Sambal Oelek hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(195)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird Lauchzwiebel hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(127)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Chili-Lemon-Chicken wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(10)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Cherrytomate hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(26)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="125 g",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Cremiger Nudelauflauf mit Tomaten und Mozzarella wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(11)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Butter hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="800 g",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Milch hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Kr�utersalz und Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(119)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Das beste Kartoffelgratin wird Butterfl�ckchen hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(19)
   rezept1 = rezept.query.get(12)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rindergulasch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(179)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Butterschmalz hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rinderbr�he hinzugef�gt.')
   assoc1 = Association(menge="800 ml",optional=False)
   zutat = zutat.query.get(177)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Rotwein hinzugef�gt.')
   assoc1 = Association(menge="150 ml",optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="3 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Majoran hinzugef�gt.')
   assoc1 = Association(menge="4 Zweig/e",optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Lorbeerbl�tter hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(131)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="3 gro�e",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Deftige Gulaschsuppe wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="� Bund",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(13)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="75 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="75 g",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="� Pck.",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="125 g",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="225 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Beutel",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Vanillepuddingpulver hinzugef�gt.')
   assoc1 = Association(menge="1 Beutel",optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Ei hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird Quark hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird saure Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(199)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste K�sekuchen der Welt wird s��e Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(225)
   rezept1 = rezept.query.get(14)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Weizenmehl hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(244)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="300 ml",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Salz hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Frischhefe hinzugef�gt.')
   assoc1 = Association(menge="5 g",optional=False)
   zutat = zutat.query.get(56)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Pizzatomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose/n",optional=False)
   zutat = zutat.query.get(169)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der beste Pizzateig wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(15)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Butterkeks hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(20)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Butter hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Speisest�rke hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="600 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Magerquark hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zitronensaft hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Der unglaublich cremige NY Cheese Cake wird Zitronensaft hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(16)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Glas",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Pinienkerne hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Rucola hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="einige Stiele",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Cocktailtomaten hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Pesto hinzugef�gt.')
   assoc1 = Association(menge="1 Glas",optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Kr�uter der Provence hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eckis italienischer Nudelsalat mit Pesto wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(17)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Ei hinzugef�gt.')
   assoc1 = Association(menge="6",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Kr�uter der Provence hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird �l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="1 Msp.",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird K�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Eierlasagne low carb wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(18)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Eiersp�tzle hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(76)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Schweinefilet hinzugef�gt.')
   assoc1 = Association(menge="600 g",optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Senf hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Schinken hinzugef�gt.')
   assoc1 = Association(menge="8 Scheibe/n",optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="1 Glas",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Majoran hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Dill hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="� Becher",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filet im Speckmantel mit Sp�tzle wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(19)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Schweinefilet hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Butter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2 m.-gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Katenschinken hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(100)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Fleischbr�he hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(54)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Speisest�rke hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Filettopf wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(20)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Rolle(n)",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Schinken hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Flammkuchenrolle wird Salz hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(21)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Franzbr�tchen wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Rolle(n)",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Franzbr�tchen wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Franzbr�tchen wird Apfel hinzugef�gt.')
   assoc1 = Association(menge="2 m.-gro�e",optional=False)
   zutat = zutat.query.get(266)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Franzbr�tchen wird Zimt hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(251)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Franzbr�tchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="5 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(22)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Mini-Kn�del hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(79)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Spargel hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(218)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Spargel hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(218)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Parmaschinken hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(157)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Milch hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="6",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Fr�hlingshaftes Spargel-Kn�del-Gratin wird K�se hinzugef�gt.')
   assoc1 = Association(menge="60 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(23)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Rosmarin hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="6",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="60 ml",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gebackene Knoblauch-Kartoffelscheiben wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(24)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Gnocchi hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(68)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="1 Kugel",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Br�he hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(16)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gnocchi aus dem Ofen in Paprika-Tomaten-Sauce wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(25)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird H�hnerfleisch hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(87)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Erdn�sse hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(47)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="25 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Wei�wein hinzugef�gt.')
   assoc1 = Association(menge="50 ml",optional=False)
   zutat = zutat.query.get(245)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Essig hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(48)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Szechuanpfeffer hinzugef�gt.')
   assoc1 = Association(menge="10 K�rner",optional=False)
   zutat = zutat.query.get(224)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="2 g",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="20 ml",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gong Bao Chicken wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(26)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Butterschmalz hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="4 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Knollensellerie hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(107)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rotwein hinzugef�gt.')
   assoc1 = Association(menge="0,7 Liter",optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rindfleisch hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(182)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Rinderbr�he hinzugef�gt.')
   assoc1 = Association(menge="300 ml",optional=False)
   zutat = zutat.query.get(177)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL, geh�uft",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL, geh�uft",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Lorbeerbl�tter hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(131)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Gulasch nach Oma Magda wird Saucenbinder hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(196)
   rezept1 = rezept.query.get(27)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Kr�uter der Provence hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose/n",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird s��e Sahne hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(225)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="1 Kugel/n",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackb�llchen Toscana wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(28)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Sauerkraut hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(197)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Milch hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Hackfleisch - Sauerkraut - Auflauf mit Schupfnudeln wird K�se hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(29)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Ananasst�cke hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(3)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="� Becher",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Sahne-Schmelzk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Honig hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Currypulver hinzugef�gt.')
   assoc1 = Association(menge="3 TL",optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird H�hnerbr�he hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Reis hinzugef�gt.')
   assoc1 = Association(menge="2 Beutel",optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird �l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: H�hnchen-Ananas-Curry mit Reis wird Chilipulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(30)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Limonensaft hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(129)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Joghurt hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Garam Masala hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(60)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="1 St�ck(e)",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Butter hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Zimt hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(251)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="1 St�ck(e)",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Honig hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="150 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Butter Chicken aus dem Ofen wird Korianderbl�tter hinzugef�gt.')
   assoc1 = Association(menge="einige",optional=False)
   zutat = zutat.query.get(111)
   rezept1 = rezept.query.get(31)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="3 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kardamomkapsel hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(95)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Nelke hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(149)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Ingwerpaste hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(89)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Koriander hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(110)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Piment hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(167)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kreuzk�mmel hinzugef�gt.')
   assoc1 = Association(menge="1 � TL",optional=False)
   zutat = zutat.query.get(113)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Kurkuma hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(120)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Chiliflocken hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Tomatenp�ree hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(232)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Mandelmehl hinzugef�gt.')
   assoc1 = Association(menge="75 g",optional=False)
   zutat = zutat.query.get(138)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird H�hnerbr�he hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Schlagsahne hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(206)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Indisches Chicken Korma wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(32)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Cocktailtomaten hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Rucola hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Glas",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Oliven hinzugef�gt.')
   assoc1 = Association(menge="1 kl. Glas",optional=False)
   zutat = zutat.query.get(151)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Pinienkerne hinzugef�gt.')
   assoc1 = Association(menge="1 Beutel",optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="1 Teil/e",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 Teil/e",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Aceto balsamico hinzugef�gt.')
   assoc1 = Association(menge="1 Teil/e",optional=False)
   zutat = zutat.query.get(1)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Senf hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Nudelsalat mit Rucola und getrockneten Tomaten wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(33)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="500 ml",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="25 ml",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Frischhefe hinzugef�gt.')
   assoc1 = Association(menge="40 g",optional=False)
   zutat = zutat.query.get(56)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Salz hinzugef�gt.')
   assoc1 = Association(menge="20 g",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="1 Prise(n)",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Italienischer Pizzateig wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="925 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(34)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird M�hre hinzugef�gt.')
   assoc1 = Association(menge="375 g",optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Zimtpulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(252)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird �l hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Mandel hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(137)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Puderzucker hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Karottenkuchen, R�blikuchen oder M�hrenkuchen wird Zitronensaft hinzugef�gt.')
   assoc1 = Association(menge="1 Spritzer",optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(35)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="4 m.-gro�e",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Speck hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(219)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Gouda hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(69)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Kr�uter der Provence hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kartoffeln Lorraine wird Schnittlauch hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(36)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Kritharaki hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(115)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Tomatenketchup hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(230)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Salatsaucemischung hinzugef�gt.')
   assoc1 = Association(menge="3 Beutel",optional=False)
   zutat = zutat.query.get(50)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Kritharaki-Salat mit Hackfleisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(37)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Baguette hinzugef�gt.')
   assoc1 = Association(menge="2 kleine",optional=False)
   zutat = zutat.query.get(6)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird �l hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Lauch hinzugef�gt.')
   assoc1 = Association(menge="3 Stange/n",optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="700 ml",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Schmelzk�se hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(208)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Knoblauchpulver hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(106)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�se-Lauch-Suppe mit Hackfleisch wird Zwiebelpulver hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(262)
   rezept1 = rezept.query.get(38)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Hokkaidok�rbis hinzugef�gt.')
   assoc1 = Association(menge="800 g",optional=False)
   zutat = zutat.query.get(81)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird M�hre hinzugef�gt.')
   assoc1 = Association(menge="600 g",optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="1 St�ck(e)",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Butter hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="1 Liter",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="500 ml",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Zitrone hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: K�rbissuppe mit Ingwer und Kokosmilch wird Koriander hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(110)
   rezept1 = rezept.query.get(39)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Rotwein hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Milch hinzugef�gt.')
   assoc1 = Association(menge="� Liter",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Butter hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="40 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Zitronensaft hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(257)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Lasagneplatte hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(125)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird K�se hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Lasagne wird Butterfl�ckchen hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(19)
   rezept1 = rezept.query.get(40)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="600 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2 m.-gro�e",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 m.-gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Bauerntopf wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(41)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Gefl�gelfleisch hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(61)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Kirschtomate hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 etwas",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Chiliflocken hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Kr�uter-Tomatenpfanne mit saftigem Gefl�gelfleisch wird Gem�sezwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(65)
   rezept1 = rezept.query.get(42)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Quark hinzugef�gt.')
   assoc1 = Association(menge="120 g",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Ei hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird K�se hinzugef�gt.')
   assoc1 = Association(menge="120 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird K�se hinzugef�gt.')
   assoc1 = Association(menge="60 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Tomatensauce hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(233)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Fleisch hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(53)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Gem�se hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(63)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb Pizzarolle wird Rucola hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(43)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Quark hinzugef�gt.')
   assoc1 = Association(menge="120 g",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird K�se hinzugef�gt.')
   assoc1 = Association(menge="160 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Lauchzwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(127)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low Carb-Keto-Flammkuchen wird Speck hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(219)
   rezept1 = rezept.query.get(44)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Magerquark hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird K�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Ei hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Ketchup hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(101)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Naturjoghurt hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(148)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Schmelzk�se hinzugef�gt.')
   assoc1 = Association(menge="3 Scheibe/n",optional=False)
   zutat = zutat.query.get(208)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Gew�rzgurke hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Salat hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(193)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb Big Mac Rolle wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(45)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Gurke hinzugef�gt.')
   assoc1 = Association(menge="�",optional=False)
   zutat = zutat.query.get(71)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Strauchtomate hinzugef�gt.')
   assoc1 = Association(menge="3 m.-gro�e",optional=False)
   zutat = zutat.query.get(223)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Schalotte hinzugef�gt.')
   assoc1 = Association(menge="2 kleine",optional=False)
   zutat = zutat.query.get(202)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Milch hinzugef�gt.')
   assoc1 = Association(menge="1 Schuss",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Currypulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-carb H�hnchenbrust mit Zucchini und Tomaten in cremiger Frischk�sesauce wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(46)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Lachsfilet hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(124)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Schafsk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(201)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="1 m.-gro�e",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1 m.-gro�e",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Cherrytomate hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(26)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Salz hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Low-Carb-Lachs mit Ofengem�se wird Chili�l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(32)
   rezept1 = rezept.query.get(47)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Cashewkerne hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(22)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Currypulver hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Ingwer hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(88)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Wei�wein hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(245)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Joghurt hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="750 g",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Butter hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Zimtstange hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(253)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Kardamompulver hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(96)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 Prise(n)",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Chiliflocken hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="150 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Makhani H�hnchen wird Koriandergr�n hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(112)
   rezept1 = rezept.query.get(48)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Quark hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Milch hinzugef�gt.')
   assoc1 = Association(menge="70 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird �l hinzugef�gt.')
   assoc1 = Association(menge="5 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Lauch hinzugef�gt.')
   assoc1 = Association(menge="1 Stange/n",optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 kleine",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Schinken hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird K�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mini-Party-Quiches wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(49)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Cocktailtomaten hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(34)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="� Topf",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Sahne-Schmelzk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="125 g",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Mozzarella-H�hnchen in Basilikum-Sahnesauce wird Kr�uterbutter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(118)
   rezept1 = rezept.query.get(50)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Schweinefilet hinzugef�gt.')
   assoc1 = Association(menge="650 g",optional=False)
   zutat = zutat.query.get(211)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Bacon hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(5)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird �l hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="750 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Butter hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Schinkenspeck hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(204)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2 m.-gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Br�he hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(16)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Wei�wein hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(245)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Worcestersauce hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(248)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Salz hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Kr�uter der Provence hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(116)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Sp�tzle hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(222)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL, geh�uft",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: NT-Schweinefilet im Speckmantel mit Champignons und Sp�tzle wird Butter hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(51)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Pinienkerne hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Rucola hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(187)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Parmaschinken hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(157)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="70 ml",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Balsamico hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(7)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Pesto hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Honig hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf italienisch wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(52)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="1 Paket",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Naturjoghurt hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(148)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="1 Bund",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat auf t�rkische Art wird Thymian hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(53)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Schafsk�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(201)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Pinienkerne hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(168)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="30",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="50 ml",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Nudelsalat mit getrockneten Tomaten, Pinienkernen, Schafsk�se und Basilikum wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(54)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Br�tchen hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(15)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Majoran hinzugef�gt.')
   assoc1 = Association(menge="1 TL, gestr.",optional=False)
   zutat = zutat.query.get(136)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="viel",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Maggi hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(133)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas beste Frikadellen wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(55)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Mais hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(134)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="� Liter",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Tomatensauce hinzugef�gt.')
   assoc1 = Association(menge="2 Pkt.",optional=False)
   zutat = zutat.query.get(233)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Sahne-Schmelzk�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(192)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Omas Pizzasuppe wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(56)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Reis hinzugef�gt.')
   assoc1 = Association(menge="2 Tasse/n",optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="4 Tasse/n",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="1 Handvoll",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Joghurt hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(92)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Reispfanne mit Joghurtsauce wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(57)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="125 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird K�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Paprika-Sahne-H�hnchen wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(58)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Knoblauchgranulat hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(105)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Parmesan-Knoblauch-Kartoffelecken wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(59)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Milch hinzugef�gt.')
   assoc1 = Association(menge="240 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Trockenhefe hinzugef�gt.')
   assoc1 = Association(menge="10 g",optional=False)
   zutat = zutat.query.get(235)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Salz hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Butter hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pesto hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pesto hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(161)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Peperoni hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(160)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Oliven hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(151)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Pfeffer hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(165)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pesto- und Pizza-Babka wird Ei hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(60)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Bacon hinzugef�gt.')
   assoc1 = Association(menge="12",optional=False)
   zutat = zutat.query.get(5)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Barbecuesauce hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(9)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="240 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 Prise(n)",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Milch hinzugef�gt.')
   assoc1 = Association(menge="480 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Butter hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Ahornsirup hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(2)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pfannkuchen mit glasiertem Bacon und Frischk�se wird Johannisbeeren hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(93)
   rezept1 = rezept.query.get(61)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 kl. Bund",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Ingwerwurzel hinzugef�gt.')
   assoc1 = Association(menge="2 cm",optional=False)
   zutat = zutat.query.get(90)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird H�hnerbr�he hinzugef�gt.')
   assoc1 = Association(menge="1 Liter",optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Currypaste hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Zitronengras hinzugef�gt.')
   assoc1 = Association(menge="1 St�ngel",optional=False)
   zutat = zutat.query.get(255)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird chinesische Eiernudeln hinzugef�gt.')
   assoc1 = Association(menge="125 g",optional=False)
   zutat = zutat.query.get(33)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird �l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Koriandergr�n hinzugef�gt.')
   assoc1 = Association(menge="1 Handvoll",optional=False)
   zutat = zutat.query.get(112)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pikante Thai-Suppe mit Kokos und H�hnchen wird Chilif�den hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(28)
   rezept1 = rezept.query.get(62)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Quark hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(173)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Milch hinzugef�gt.')
   assoc1 = Association(menge="8 EL",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird �l hinzugef�gt.')
   assoc1 = Association(menge="6 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird R�stzwiebeln hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(190)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird K�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizza-B�llchen wird Schinken hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(203)
   rezept1 = rezept.query.get(63)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Hefe hinzugef�gt.')
   assoc1 = Association(menge="4 g",optional=False)
   zutat = zutat.query.get(74)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="300 ml",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Pizzateig wird Salz hinzugef�gt.')
   assoc1 = Association(menge="10 g",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(64)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="200 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Butter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Nudeln hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(150)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Kochschinken hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(108)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rigatoni al forno wird Edamer K�se hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(42)
   rezept1 = rezept.query.get(65)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rinderroulade hinzugef�gt.')
   assoc1 = Association(menge="8",optional=False)
   zutat = zutat.query.get(181)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="5",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Gew�rzgurke hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(67)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Senf hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Speck hinzugef�gt.')
   assoc1 = Association(menge="12 Scheibe/n",optional=False)
   zutat = zutat.query.get(219)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Butterschmalz hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Knollensellerie hinzugef�gt.')
   assoc1 = Association(menge="1 St�ck(e)",optional=False)
   zutat = zutat.query.get(107)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird M�hre hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Lauch hinzugef�gt.')
   assoc1 = Association(menge="� Stange/n",optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rotwein hinzugef�gt.')
   assoc1 = Association(menge="� Flasche",optional=False)
   zutat = zutat.query.get(186)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Rinderfond hinzugef�gt.')
   assoc1 = Association(menge="� Liter",optional=False)
   zutat = zutat.query.get(178)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Speisest�rke hinzugef�gt.')
   assoc1 = Association(menge="TL",optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rinderrouladen klassisch wird Gurkenfl�ssigkeit hinzugef�gt.')
   assoc1 = Association(menge="1 Schuss",optional=False)
   zutat = zutat.query.get(72)
   rezept1 = rezept.query.get(66)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Pizzatomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(169)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Linsen hinzugef�gt.')
   assoc1 = Association(menge="175 g",optional=False)
   zutat = zutat.query.get(130)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Chilipulver hinzugef�gt.')
   assoc1 = Association(menge="3 TL",optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Kurkuma hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(120)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="600 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird �l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Rote Linsen-Kokos-Suppe wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(67)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Kakaopulver hinzugef�gt.')
   assoc1 = Association(menge="30 g",optional=False)
   zutat = zutat.query.get(94)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="2 TL, gestr.",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Butter hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Fett hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(51)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Butter hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Magerquark hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanillepuddingpulver hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Russischer Zupfkuchen wird Vanilleschote hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(238)
   rezept1 = rezept.query.get(68)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird �l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Currypulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(38)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Chilipulver hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(29)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Hokkaidok�rbis hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(81)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Basilikum hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(10)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Gnocchi hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(68)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Saftiger K�rbis-Gnocchi-Auflauf wird Mozzarella hinzugef�gt.')
   assoc1 = Association(menge="1 Kugel",optional=False)
   zutat = zutat.query.get(144)
   rezept1 = rezept.query.get(69)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="125 ml",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 Prise(n)",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Cr�me double hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(35)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Speck hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(219)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="1 Becher",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schneller Flammkuchen wird Schnittlauch hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(70)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Ingwerwurzel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(90)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Currypaste hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Erdnussbutter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(45)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="400 ml",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Fr�hlingszwiebel hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(58)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Bambussprosse hinzugef�gt.')
   assoc1 = Association(menge="1 kl. Glas",optional=False)
   zutat = zutat.query.get(8)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Maisk�lbchen hinzugef�gt.')
   assoc1 = Association(menge="10",optional=False)
   zutat = zutat.query.get(135)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Fischsauce hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(52)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Palmzucker hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(154)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Zitronengraspaste  hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(256)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Thai-Basilikum hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(226)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schnelles Thai-Curry mit Huhn, Paprika und feiner Erdnussnote wird Jasminreis oder Duftreis hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(91)
   rezept1 = rezept.query.get(71)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Lauch hinzugef�gt.')
   assoc1 = Association(menge="1 Stange/n",optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Kirschtomate hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(103)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Hackfleisch hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(73)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel - Hackfleisch - Auflauf mit Gem�se wird K�se hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(72)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="2 Pck.",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Wirsing hinzugef�gt.')
   assoc1 = Association(menge="1 kleiner",optional=False)
   zutat = zutat.query.get(247)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Kasseler hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(99)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Br�he hinzugef�gt.')
   assoc1 = Association(menge="500 ml",optional=False)
   zutat = zutat.query.get(16)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Schmand hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(207)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Liebst�ckel - Bl�ttchen hinzugef�gt.')
   assoc1 = Association(menge="einige",optional=False)
   zutat = zutat.query.get(128)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird K�mmel hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(122)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird K�se hinzugef�gt.')
   assoc1 = Association(menge="60 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin wird Schnittlauch hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(73)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Wirsing hinzugef�gt.')
   assoc1 = Association(menge="1 kl. Kopf",optional=False)
   zutat = zutat.query.get(247)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Kasseler hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(99)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="125 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Schupfnudeln aus dem K�hlregal hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(210)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird saure Sahne hinzugef�gt.')
   assoc1 = Association(menge="125 g",optional=False)
   zutat = zutat.query.get(199)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Senf hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(213)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird K�se hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird K�mmelpulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(123)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schupfnudel-Wirsing-Gratin mit Kasseler wird Schnittlauch hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(209)
   rezept1 = rezept.query.get(74)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Sauerrahm hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(198)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Fleischbr�he hinzugef�gt.')
   assoc1 = Association(menge="400 ml",optional=False)
   zutat = zutat.query.get(54)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Drillinge hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(40)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Butter hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Katenschinken hinzugef�gt.')
   assoc1 = Association(menge="75 g",optional=False)
   zutat = zutat.query.get(100)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Rosmarinnadeln hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(185)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Kartoffeln wird Toastbrot hinzugef�gt.')
   assoc1 = Association(menge="5 Scheibe/n",optional=False)
   zutat = zutat.query.get(228)
   rezept1 = rezept.query.get(75)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Kartoffel hinzugef�gt.')
   assoc1 = Association(menge="3 gro�e",optional=False)
   zutat = zutat.query.get(98)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Lauch hinzugef�gt.')
   assoc1 = Association(menge="1 Stange/n",optional=False)
   zutat = zutat.query.get(126)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Butter hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="� Liter",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Lachsfilet hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(124)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Schwedische Sommersuppe wird Dill hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(39)
   rezept1 = rezept.query.get(76)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Bl�tterteig hinzugef�gt.')
   assoc1 = Association(menge="1 Rolle(n)",optional=False)
   zutat = zutat.query.get(14)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="8",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Waln�sse hinzugef�gt.')
   assoc1 = Association(menge="1 Handvoll",optional=False)
   zutat = zutat.query.get(242)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Blattspinat hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(13)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Spinatstrudel mit getrockneten Tomaten und Waln�ssen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(77)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Erdnuss�l hinzugef�gt.')
   assoc1 = Association(menge="2 TL",optional=False)
   zutat = zutat.query.get(46)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird H�hnerbrust hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(83)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Currypaste hinzugef�gt.')
   assoc1 = Association(menge="2 TL, geh�uft",optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="400 ml",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Erdnussbutter hinzugef�gt.')
   assoc1 = Association(menge="2 TL, geh�uft",optional=False)
   zutat = zutat.query.get(45)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="1 TL, geh�uft",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Zuckerschote hinzugef�gt.')
   assoc1 = Association(menge="2 Handvoll",optional=False)
   zutat = zutat.query.get(260)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Bambussprosse hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(8)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Speisest�rke hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(221)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Zitronengraspaste  hinzugef�gt.')
   assoc1 = Association(menge="2 TL, geh�uft",optional=False)
   zutat = zutat.query.get(256)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Reis hinzugef�gt.')
   assoc1 = Association(menge="1 Tasse",optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="2 Tasse/n",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai Curry Erdnuss-Kokos-H�hnchen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(78)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Fleisch hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(53)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Currypaste hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="1 kl. Glas",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Kokosmilch hinzugef�gt.')
   assoc1 = Association(menge="400 ml",optional=False)
   zutat = zutat.query.get(109)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Gem�se hinzugef�gt.')
   assoc1 = Association(menge="800 g",optional=False)
   zutat = zutat.query.get(63)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Fischsauce hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(52)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Palmzucker hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(154)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Peperoni hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(160)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Chilischote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(31)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird Thai-Basilikum hinzugef�gt.')
   assoc1 = Association(menge="6 Bl�tter",optional=False)
   zutat = zutat.query.get(226)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Thai-Red-Curry f�r mehrere Variationen wird �l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(79)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Tortellini hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(234)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Kochschinken hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(108)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Butter hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="600 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Parmesan hinzugef�gt.')
   assoc1 = Association(menge="4 EL",optional=False)
   zutat = zutat.query.get(158)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Muskat hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(146)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tortellini alla panna wird Salz hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(80)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Honig hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(82)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Sojasauce hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(216)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Chilisauce hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(30)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Preiselbeeren hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(171)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Ketchup hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(101)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Kartoffelnudeln hinzugef�gt.')
   assoc1 = Association(menge="800 g",optional=False)
   zutat = zutat.query.get(78)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2 Zehe/n",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Rosmarin hinzugef�gt.')
   assoc1 = Association(menge="3 Zweig/e",optional=False)
   zutat = zutat.query.get(184)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Thymian hinzugef�gt.')
   assoc1 = Association(menge="1 Zweig/e",optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird H�hnerbr�he hinzugef�gt.')
   assoc1 = Association(menge="� Liter",optional=False)
   zutat = zutat.query.get(85)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Toskanischer H�hnchen-Auflauf wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(81)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Butter hinzugef�gt.')
   assoc1 = Association(menge="70 g",optional=False)
   zutat = zutat.query.get(18)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Magerquark hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(132)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Vanillepuddingpulver hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(237)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Ei hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Sahne hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(191)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Milch hinzugef�gt.')
   assoc1 = Association(menge="250 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird �l hinzugef�gt.')
   assoc1 = Association(menge="150 ml",optional=False)
   zutat = zutat.query.get(265)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Tr�nenkuchen - der beste K�sekuchen der Welt! wird Puderzucker hinzugef�gt.')
   assoc1 = Association(menge="6 EL",optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(82)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Schafsk�se hinzugef�gt.')
   assoc1 = Association(menge="1 Glas",optional=False)
   zutat = zutat.query.get(201)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="600 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Champignons hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(24)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Cr�me fra�che hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(36)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Schafsk�se hinzugef�gt.')
   assoc1 = Association(menge="100 g",optional=False)
   zutat = zutat.query.get(201)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: T�rkischer Hackfleischauflauf mit Schafsk�se wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(83)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Strudelteig hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(80)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Veggie-Hack hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(240)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Gem�sezwiebel hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(65)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Paprikaschote hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(156)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Zuckerschote hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(260)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Mungobohnensprossen hinzugef�gt.')
   assoc1 = Association(menge="� Glas",optional=False)
   zutat = zutat.query.get(145)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Sesam�l hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(215)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Chiliflocken hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(27)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegane Fr�hlingsrollen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(84)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="1 Liter",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Reis hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(175)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Emmentaler hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(44)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird M�hre hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(147)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2 m.-gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Semmelbr�sel hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(212)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Vegetarische Frikadellen wird Butterschmalz hinzugef�gt.')
   assoc1 = Association(menge="n. B.",optional=False)
   zutat = zutat.query.get(21)
   rezept1 = rezept.query.get(85)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Kichererbsen aus der Dose hinzugef�gt.')
   assoc1 = Association(menge="250 g",optional=False)
   zutat = zutat.query.get(102)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="200 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Wurzelgem�se hinzugef�gt.')
   assoc1 = Association(menge="80 g",optional=False)
   zutat = zutat.query.get(249)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="400 g",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Rosinen hinzugef�gt.')
   assoc1 = Association(menge="50 g",optional=False)
   zutat = zutat.query.get(183)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="20 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Gem�sebr�he hinzugef�gt.')
   assoc1 = Association(menge="350 ml",optional=False)
   zutat = zutat.query.get(64)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Cayennepfeffer hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(23)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Kreuzk�mmelpulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(114)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Zimtpulver hinzugef�gt.')
   assoc1 = Association(menge="� TL",optional=False)
   zutat = zutat.query.get(252)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: W�rziger Kichererbseneintopf wird Zitrone hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(86)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Margarine hinzugef�gt.')
   assoc1 = Association(menge="350 g",optional=False)
   zutat = zutat.query.get(139)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Mehl hinzugef�gt.')
   assoc1 = Association(menge="350 g",optional=False)
   zutat = zutat.query.get(141)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Zucker hinzugef�gt.')
   assoc1 = Association(menge="350 g",optional=False)
   zutat = zutat.query.get(259)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Vanillezucker hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(239)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Backpulver hinzugef�gt.')
   assoc1 = Association(menge="2 TL, geh�uft",optional=False)
   zutat = zutat.query.get(4)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Ei hinzugef�gt.')
   assoc1 = Association(menge="6",optional=False)
   zutat = zutat.query.get(43)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Zitrone hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(254)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zitronenkuchen wird Puderzucker hinzugef�gt.')
   assoc1 = Association(menge="300 g",optional=False)
   zutat = zutat.query.get(172)
   rezept1 = rezept.query.get(87)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird H�hnerbrustfilet hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(84)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Currypaste hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(37)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="3",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Karotte hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(97)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Br�hepulver hinzugef�gt.')
   assoc1 = Association(menge="1 TL",optional=False)
   zutat = zutat.query.get(17)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="4",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Ziegenfrischk�se hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(250)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Karotten-Bandnudeln mit H�hnchen und Tomate wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(88)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="1 kg",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Zwiebel hinzugef�gt.')
   assoc1 = Association(menge="1 gro�e",optional=False)
   zutat = zutat.query.get(261)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Knoblauch hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(104)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Rinderhackfleisch hinzugef�gt.')
   assoc1 = Association(menge="500 g",optional=False)
   zutat = zutat.query.get(180)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="1 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="1 Dose",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="1 Pck.",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Milch hinzugef�gt.')
   assoc1 = Association(menge="100 ml",optional=False)
   zutat = zutat.query.get(142)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Sauerrahm hinzugef�gt.')
   assoc1 = Association(menge="evtl.",optional=False)
   zutat = zutat.query.get(198)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird K�se hinzugef�gt.')
   assoc1 = Association(menge="150 g",optional=False)
   zutat = zutat.query.get(121)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Paprikapulver hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(155)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Oregano hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(153)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Thymian hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(227)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Lasagne wird Petersilie hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(163)
   rezept1 = rezept.query.get(89)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Zucchini hinzugef�gt.')
   assoc1 = Association(menge="1",optional=False)
   zutat = zutat.query.get(258)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Oliven�l hinzugef�gt.')
   assoc1 = Association(menge="etwas",optional=False)
   zutat = zutat.query.get(152)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Tomaten hinzugef�gt.')
   assoc1 = Association(menge="2",optional=False)
   zutat = zutat.query.get(229)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Wasser hinzugef�gt.')
   assoc1 = Association(menge="2 EL",optional=False)
   zutat = zutat.query.get(243)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Tomatenmark hinzugef�gt.')
   assoc1 = Association(menge="3 EL",optional=False)
   zutat = zutat.query.get(231)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Frischk�se hinzugef�gt.')
   assoc1 = Association(menge="1 TL, geh�uft",optional=False)
   zutat = zutat.query.get(57)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Salz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(194)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Kr�uter hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(117)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

try:
   print('Rezept: Zucchini-Spaghetti wird Gew�rz hinzugef�gt.')
   assoc1 = Association(menge="",optional=False)
   zutat = zutat.query.get(66)
   rezept1 = rezept.query.get(90)
   assoc1.hatzutat= zutat
   with db.session.no_autoflush:
       rezept1.zutaten.append(assoc1)
   db.session.commit()
except sqlalchemy.exc.IntegrityError:
   print('Fehler: hier �ber mir')
   db.session.rollback()

