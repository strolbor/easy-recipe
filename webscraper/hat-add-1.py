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

