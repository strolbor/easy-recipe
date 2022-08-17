from app import db
import sqlalchemy
from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags

handob = handlungsschritt(text="Die Kartoffeln und M�hren sch�len und in kleine St�cke schneiden. Die Paprikaschoten ebenfalls klein schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das �l in einer Pfanne erhitzen und das Hackfleisch kr�melig braten. Mit den Dosentomaten, Tomatenmark und der Br�he abl�schen. Kartoffeln, M�hren und die Paprika hinzuf�gen. Alles zugedeckt ca. 40 min. bei mittlerer Hitze k�cheln lassen. Zum Reduzieren evtl. zus�tzlich ca. 10 min. ohne Deckel k�cheln lassen. Am Schluss mit den Gew�rzen abschmecken und den Schmand unterr�hren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

