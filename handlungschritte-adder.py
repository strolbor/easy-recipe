from app import db
import sqlalchemy
from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags

handob = handlungsschritt(text="Die Kartoffeln und Möhren schälen und in kleine Stücke schneiden. Die Paprikaschoten ebenfalls klein schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Öl in einer Pfanne erhitzen und das Hackfleisch krümelig braten. Mit den Dosentomaten, Tomatenmark und der Brühe ablöschen. Kartoffeln, Möhren und die Paprika hinzufügen. Alles zugedeckt ca. 40 min. bei mittlerer Hitze köcheln lassen. Zum Reduzieren evtl. zusätzlich ca. 10 min. ohne Deckel köcheln lassen. Am Schluss mit den Gewürzen abschmecken und den Schmand unterrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

