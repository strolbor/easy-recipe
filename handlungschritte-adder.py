from app import db
import sqlalchemy
from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags

handob = handlungsschritt(text="1. Apfel schälen, Kerngehäuse entfernen und mit Hilfe einer Küchenreibe grob raspeln. Blätterteig auspacken, mit Alsan/ Margarine bestreichen, Apfelraspel darauf verteilen, mit Zimt und Zucker bestreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2. Hochkant aufwickeln. In 6 gleichgroße Stücke schneiden. Mit einem Kochlöffelstiel (oder ähnlichem) jedes Stück mittig eindrücken, sodass die Enden die typische Franzbrötchen-Form bekommen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="3. Mit dem Backpapier auf ein Backblech geben und im vorgeheizten Backofen bei 200 °C Ober-/Unterhitze für 10 - 15 Minuten goldbraun backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nährwerte pro Stück:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Energie kJ/kcal 1354/324")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eiweiß 2,3 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fett 13,3 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kohlenhydrate 47,2 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Spargel putzen, den weißen Spargel ganz, bei dem grünen Spargel nur das untere Drittel schälen und den Spargel in ca. 5 cm lange Stücke schneiden. 1,5 Liter Wasser mit 1 TL Salz, 1 Prise Zucker und Margarine aufkochen, Spargel dazugeben und ca. 10 Minuten garen. Grünen Spargel erst nach 5 Minuten Garzeit zufügen. Spargel abgießen und dabei das Spargelwasser auffangen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 180° C (Gas: Stufe 3, Umluft 160° C). vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mini-Knödel nach Packungsanweisung ca. 8 Minuten garen. Schinken in Streifen schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Soße Margarine in einem Topf erhitzen, Mehl dazugeben und anschwitzen, Milch und 300 ml Spargelsud angießen, aufkochen und mit Salz, Pfeffer und Muskat abschmecken. Frühlingszwiebeln putzen, waschen und in feine Ringe schneiden. Die Hälfte der Frühlingszwiebeln unter die Soße mischen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Spargel, Knödel und Schinken in eine Gratinform (24 x 28 cm) geben, Soße darüber gießen, Käse überstreuen und ca. 30-35 Minuten goldbraun backen Restliche Frühlingszwiebeln über das Gratin streuen und servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kJ/kcal: 1500/358")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 19,9 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 39,6 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Ein Backblech mit Backpapier auslegen. Mit nicht zu wenig Olivenöl bestreichen. Die Kartoffeln in dünne Scheiben gefächert auf dem gefetteten Papier auslegen. Zwischen den Reihen etwas Platz lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Geschälten Knoblauch waagerecht halbieren und wie den Rosmarin unter die Kartoffelscheiben legen. Salzen, pfeffern und die Kartoffelscheiben noch mal mit Öl bestreichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Auf mittlerer Höhe die Kartoffeln 35 min bei 200°C backen. Sie sollten leicht knusprig und leicht gebräunt sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Gnocchi nach Packungsanweisung kochen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Paprikaschote putzen und in einer Küchenmaschine pürieren. Die Knoblauchzehe abziehen, pressen und in etwas Olivenöl anbraten. Das Paprikapüree zufügen und kurz mitbraten. Die passierten Tomaten zugeben, dann den Frischkäse unterrühren und aufkochen lassen. Mit Salz, Pfeffer, Oregano und Brühe abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine Auflaufform einfetten und die Gnocchi darin verteilen, die Sauce darüber geben. Den Mozzarella in Scheiben schneiden, den Parmesan reiben und beides obendrauf verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Backofen bei 180 °C ca. 15 Minuten überbacken. Sofort servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Rezept stammt von einer Chinareise aus der Stadt Chongqing.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zunächst den Boden des Wok großzügig mit Öl bedecken und dieses auf höchster Stufe erhitzen. Das Geschnetzelte rundherum mit Mehl bestäuben und im Wok scharf anbraten, dann salzen. Das Fleisch herausnehmen, evtl. etwas Öl nachgeben und die gehackten Erdnüsse leicht anbraten. Die Erdnüsse herausnehmen und die Zwiebeln anbraten. Anschließend den gehackten Knoblauch hinzugeben und ebenfalls anbraten. Die Frühlingszwiebeln und die Chilischoten in Streifen schneiden und hinzugeben. Den Zucker darüber streuen und karamellisieren lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fleisch und Erdnüsse wieder hinzugeben. Mit Wein ablöschen, aufkochen lassen und den Essig hinzugeben. Abschließend mit Sojasauce, Ingwer und Pfeffer (gut zerkleinern, sehr intensiv!) würzen und abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Auf Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln in 0,5 cm große Würfel schneiden, Karotte und Sellerie würfeln. Alles in 2 EL Butterschmalz kräftig anbraten. Tomatenmark zugeben und andünsten bis sich eine homogene Masse bildet, das Mark darf ruhig ein bisschen ansetzen. Paprikapulver kurz mitrösten (Vorsicht, darf nicht verbrennen!). Mit dem Rotwein und der Brühe ablöschen und zum Kochen bringen. Jetzt erst das gewürfelte Fleisch dazu geben, wieder aufkochen und bei kleiner Hitze mit den Lorbeerblättern ca. 2 Stunden köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Durch das Gemüse ist es normalerweise nicht nötig, die Sauce zu binden. Wenn sie allerdings zu flüssig ist, kann man das Gulasch mit 1 EL in kaltem Wasser aufgelöstem Stärkemehl andicken. Dann noch abschmecken mit Salz und Pfeffer. Die Lorbeerblätter fische ich nach Möglichkeit vor dem Servieren raus.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dies ist ein Grundrezept für Gulasch, man kann es wunderbar abwandeln, indem man z. B. eine halbe Stunde vor Ende der Garzeit noch Sahne, Kartoffeln und/oder Paprikaschoten zugibt. Ich gebe auch immer noch Knoblauch dazu, den mochte aber meine Oma nicht.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu schmecken Knödel jeglicher Art, Kartoffeln oder Nudeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz und Pfeffer würzen. Evtl. noch Kräuter wie Oregano, Thymian und/oder Basilikum und nach Geschmack Knoblauch dazugeben. Ca. 12 - 15 kleine Bällchen aus der Masse formen und in eine Auflaufform legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Tomatensoße die stückigen Tomaten mit der Sahne, der Kräutermischung, Tomatenmark und Zucker verrühren, dann mit Salz und Pfeffer abschmecken. Alles über die Hackbällchen geben. Den Mozzarella in Scheiben schneiden und darüber verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im heißen Backofen bei 175 °C Umluft ca. 30 - 40 min. garen. Aufpassen, dass der Käse nicht zu dunkel wird.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 180°C vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Paprikaschoten halbieren, putzen, waschen und in Stücke schneiden. Zwiebeln abziehen und in feine Ringe schneiden. Sauerkraut abtropfen lassen und gut ausdrücken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hackfleisch in erhitztem Öl von allen Seiten anbraten. Paprika, Zwiebeln und Kartoffelnudeln hinzugeben, andünsten und mit Sauerkraut in eine Auflaufform geben. Schmand mit Milch verrühren, mit Salz und Pfeffer abschmecken, über die Zutaten gießen, mit Käse bestreuen und im vorgeheizten Backofen ca. 20-30 Min. backen (Gas: Stufe 3, Umluft: 160°C).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kj/kcal: 3232/774")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 39,3 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 45,0 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis nach Packungsanleitung kochen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(30)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch häuten, waschen und in spielwürfelgroße Stückchen schneiden. Mit etwas Öl in der Pfanne anbraten. Wenn es leicht Farbe bekommt, den Honig dazu geben. Frühlingszwiebeln und Knoblauch dazu, kurz mit anschwitzen. Die Ananas abtropfen lassen und den Saft auffangen, dann die Ananasstücke mit in die Pfanne geben und auch kurz mit anschwitzen. Den Curry dazu geben und kurz alles durchrösten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(30)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mit Sahne ablöschen. Den Schmelzkäse in Stückchen dazu geben und schmelzen lassen. Alles aufkochen lassen, mit Salz, Pfeffer, Curry, Instantbrühe, etwas gemahlenem Chili und dem Ananassaft abschmecken und dann auf dem Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(30)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Hähnchenbrust in Stücke schneiden. Aus 1 TL Paprikapulver, 1 EL Limonen- bzw. Zitronensaft, 1 TL Salz, 1 Becher Joghurt, 1 TL Cayennepfeffer, 1 EL Garam Masala Pulver, 1 Stück Ingwer und 1 Knoblauchzehe eine Marinade herstellen. Das Fleisch mit der Marinade mischen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mindestens eine Stunde einziehen lassen. Besser ist es, das Fleisch bereits am Vortag zu marinieren und über Nacht in den Kühlschrank zu stellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 200 °C Ober-/Unterhitze vorheizen dann das Fleisch in einer Auflaufform für 25 Minuten garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel klein hacken und in 2 EL Butter glasig anschwitzen. Die passierten Tomaten, den Zimt, 1 TL Salz, 2 TL Cayennepfeffer, 1 Stück Ingwer und 1 Knoblauchzehe hinzugeben. Alles 20 Minuten mit Deckel und bei niedriger Temperatur köcheln lassen. Gelegentlich umrühren. Nun die restlichen 2 EL Butter, den Honig und die Sahne hinzufügen, weitere 3 Minuten köcheln. Das Fleisch aus der Marinade nehmen, in die Soße geben, kurz umrühren und 2 Minuten mitköcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt Reis oder Naan.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wer gerne Koriandergrün mag, der kann ganz am Ende noch ein paar frisch gehackte Blätter hinzufügen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hühnerfleisch in mundgerechte Würfel schneiden, die Zwiebel klein hacken, die Knoblauchzehen fein hacken, die Kardamomkapseln zerdrücken und mit den Nelken im Mörser klein mahlen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(32)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Öl in einem mittelgroßen Topf erhitzen, Zwiebeln und das Nelken-Kardamom-Gemisch darin andünsten und glasig werden lassen. Jetzt Hühnerfleisch, Knoblauch und das Ingwerpüree dazugeben und weitere 4 Minuten unter Rühren durchbraten. Die restlichen Gewürze dazugeben, einige Minuten weiterrühren und dabei das Ganze sehr gut durchmischen und durchkochen lassen. Tomatenpüree, Mandelmehl, Brühe und Sahne nacheinander einrühren, aufkochen und bei kleiner Flamme dann 15 - 20 Minuten köcheln lassen, bis eine dick-cremige Konsistenz erreicht ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(32)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passen Reis oder Naan-Brot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(32)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln al dente kochen und erkalten lassen. Cocktailtomaten, getrocknete Tomaten und Oliven zerkleinern und mit den gekochten und erkalteten Nudeln mischen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Aus den Soßenzutaten eine Vinaigrette nach eigenem Geschmack herstellen und mit dem Salat vermengen. Dabei auf die Intensität des Öls aus dem Glas getrocknete Tomaten achten. Den Parmesan (am besten vom Stück grob gehobelt) ebenfalls unter den Salat mengen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Am besten 2 - 3 Stunden im Kühlschrank ziehen lassen. Nun evtl. nochmals nachwürzen und wenn nötig, das Verhältnis aus Öl und Balsamico weiter verfeinern.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Rucola waschen, grob zerkleinern und erst vor dem Servieren mit dem Salat mischen. Zuletzt die Pinienkerne in der Pfanne kurz anrösten und auf den bereits auf Tellern angerichteten Salat geben. Am besten mit frischem Ciabatta und einem leckeren Rotwein servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im lauwarmen Wasser und dem Olivenöl die Hefe mit dem Salz und Zucker auflösen. Dann das Mehl hinzufügen und einen glatten Teig kneten. Eine halbe Stunde an einem warmen Ort gehen lassen, zusammenkneten und abgedeckt im Kühlschrank 2 Tage ruhen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nun kann man vom Teig eine herrlich frische Pizza herstellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Teig reicht für 6 runde Pizzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anmerkungen: Belegen kann man diese nach Belieben, natürlich sollten die Tomatensoße und der Käse nicht fehlen. Ich habe sie schon auf einem Blech sowie auf verschiedenen runden Pizzaformen gebacken. Sie wird immer supertoll und schmeckt original wie von meinem Lieblingsitaliener. Wenn man die Menge entsprechend reduzieren möchte, ist das auch kein Problem. Die Menge der Hefe habe ich jedoch immer bei 40 g gelassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Am besten gelingt die Pizza, wenn man den Ofen sehr gut auf der höchstmöglichen Temperatur vorheizt!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eier, Zucker, Öl und Zimt mit dem Mixer verrühren. Die Karotten und Mandeln hinzugeben. Mehl und Backpulver mischen, ebenfalls unterrühren. Den Teig in eine gefettete 26er Springform füllen, bei 180 °C Ober-/Unterhitze 40 - 50 Minuten backen. Man sollte eine Stäbchenprobe machen und die Erfahrungswerte mit dem eigenen Backofen berücksichtigen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(35)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für das Frosting Frischkäse und Zitronensaft mit dem Mixer auf niedriger Stufe glatt rühren. Puderzucker und Vanillezucker einrieseln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(35)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach dem Backen den Kuchen abkühlen lassen. Das Frosting mit der Streichpalette rundherum auftragen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(35)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln ungepellt und gewaschen ca. 15 min kochen. Sie sollen gar werden, aber nicht zu weich.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit die Frühlingszwiebeln und den Schnittlauch waschen und in kleine Stücke schneiden. Die Frühlingszwiebeln zusammen mit dem Speck im Sonnenblumenöl ca. 5 min braten und mit Pfeffer würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf ca. 200 °C Ober/Unterhitze vorheizen. Das Speck-Frühlingszwiebel-Gemisch in einen tiefen Teller geben und die Crème fraîche und die Hälfte des Goudas hinzugeben. Mit etwas Salz und den Kräutern der Provence würzen und gut mischen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die fertigen Kartoffeln abgießen, in der Mitte längs teilen und etwas abkühlen lassen. Mit einem Teelöffel mittelgroße Mulden aushöhlen und die Füllung auf die Hälften verteilen. (Die Füllung darf gerne über die Mulden drüber gehen.)")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffelhälften auf ein Backblech auf Backfolie legen, sodass sie nicht umfallen. Den restlichen Gouda darauf verteilen. Auf der mittleren Schiene in 10 bis 15 min goldbraun überbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln aus dem Ofen nehmen und mit Schnittlauch bestreut servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz, Pfeffer, Tomatenmark, Ketchup, Oregano und einer halben klein gehackten Zwiebel vermengen. Die Hackfleischmasse dann in einer großen Pfanne mit etwas Olivenöl krümelig braten und abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kritharaki (gibt es in jedem gut sortierten Supermarkt dort, wo auch Couscous und Bulgur zu finden sind) in Salzwasser ca. 14 Minuten garen und abgießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Paprikaschoten sehr klein würfeln (Reiskorngröße), die restliche halbe Zwiebel ebenfalls und in drei Beuteln Salatfix Gartenkräuter mit etwas Öl ziehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Es müssen keine Fertigprodukte sein. Ein selbst gemachtes Kräuterdressing auf Essigbasis tut es auch.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die abgegossenen Nudeln mit den Hackfleischbröseln vermengen. Dann die marinierten Paprikawürfel dazugeben. Alles vermengen und gut durchziehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Salat schmeckt superlecker, frisch und ist schnell zuzubereiten. Auch rein optisch ein Hingucker, aufgrund der Reisnudeln. Wir essen den Salat - trotz des Fleischanteils - auch gern als Beilage zum Grillen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 175 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Baguettes in den vorgeheizten Ofen legen und ca. 10 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Derweil Öl in einen großen Topf geben. Das Hackfleisch darin von allen Seiten gut anbraten und mit Salz und Pfeffer würzen. Den Lauch putzen, in kleine Ringe schneiden und zum Hackfleisch geben. Ca. 5 Minuten mit anbraten. Das Wasser zugießen, Brühwürfel hineingeben und alles ca. 10 Minuten auf kleiner Flamme köcheln lassen. Den Schmelzkäse einrühren und schmelzen lassen. Crème fraîche untermengen und noch einmal kurz aufkochen lassen. Die Suppe mit Salz, Pfeffer, Muskat, Knoblauch- und Zwiebelpulver kräftig abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Baguettes in Scheiben schneiden und zu der Suppe reichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kürbis, Möhren, Ingwer und Zwiebel schälen und würfeln, in der Butter andünsten. Mit der Brühe aufgießen und in etwa 15 - 20 Minuten weich kochen. Dann sehr fein pürieren, eventuell durch ein Sieb streichen. Die Kokosmilch unterrühren, mit Salz, Pfeffer, Sojasauce und Zitronensaft abschmecken und noch mal erwärmen. Mit Korianderblättchen garniert servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(39)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine schnelle, leicht exotische Suppe, schön im Menü. Ich benutze für diese Suppe immer einen Hokkaido, den muss man nicht schälen. In Thailand isst man Kürbissuppe mit kleinen Garnelen als Einlage.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(39)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Ragú Bolognese:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einem Topf das Olivenöl erhitzen, das Hackfleisch darin rundherum anbraten und die gehackten Zwiebeln und die gehackte Petersilie dazugeben. Knoblauch in feinen Scheiben und Tomatenmark dazu rühren und mitbraten. Mit den Dosentomaten aufgießen, salzen und pfeffern. Rotwein nach Belieben beifügen. Das Ragú mindestens eine halbe Stunde lang bei geöffnetem Topf einkochen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Béchamelsauce:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Butter in einem kleinen Topf schmelzen und das Mehl mit dem Schneebesen unterrühren und hellgelb anschwitzen. Die Milch dazugießen und die Sauce glatt rühren. Wer zu langsam gerührt hat und Klümpchen in der Sauce findet, kann die Sauce durch ein feines Haarsieb passieren und dann weiterkochen lassen. Die Sauce sollte fast eine halbe Stunde lang auf kleiner Flamme köcheln, damit sie den Mehlgeschmack verliert. Mit Salz, Pfeffer und Zitronensaft sowie etwas Muskatnuss abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung der Lasagne:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einer gebutterten, feuerfesten Form etwas Ragú Bolognese verteilen, eine Schicht Lasagneplatten darauf legen, die Nudelschicht wieder mit Ragú und dann mit einer Schicht Béchamel bedecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anschließend wieder eine Schicht Nudeln, Ragú und Béchamel. So Schicht für Schicht die Form füllen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die letzte Schicht sollte die Béchamelsauce bilden. Dick mit geriebenem Käse bestreuen und Butterflöckchen darauf setzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Lasagne im heißen Backofen bei 180 °C Umluft ca. 30 - 40 Minuten backen, bis die Kruste goldbraun ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Lasagne kann man auch gut einen Tag vorher vorbereiten und im Kühlschrank ziehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Als Vorspeise empfehle ich Honigmelone mit Parmaschinken und als Nachspeise einen Beerenmix an Quark-Joghurt-Sahne-Creme mit brauner Zuckerkruste.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="11")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion 1122 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position="12")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hackfleisch in einem großen Topf anbraten. Zwiebel und Knoblauch klein hacken und dazugeben. Karotten schälen, in kleine Scheiben schneiden und zum Hackfleisch geben. Alles 5 Minuten unter gelegentlichem Rühren weiter braten. Tomatenmark hinzugeben und gut vermischen. Dann mit der Brühe ablöschen, aufkochen und bei geringer Hitze 40 Minuten zugedeckt köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(41)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Paprika in kleine Sticks schneiden und ca. 10 Minuten vor Ende der Kochzeit hinzufügen. Zum Schluss noch mit Salz und Pfeffer abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(41)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anrichten und auf jeden Teller einen Klecks Crème fraîche geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(41)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Geflügelfleisch, Champignons und Tomaten klein schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(42)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch in etwas Öl anbraten und mit ein wenig Chiliflocken sowie Salz und Pfeffer würzen. Danach die Zwiebeln und Champignons dazugeben und 3 - 4 Minuten braten. Zum Schluss die restlichen Zutaten zugeben und umrühren. Weitere 5 Minuten leicht köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(42)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für den Boden Quark, Eier und 120 g Käse in einer Schüssel miteinander verrühren und würzen. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im heißen Ofen backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Backblech herausnehmen und den Boden beliebig belegen mit z. B. Tomatensauce, Salami, Schinken, Zucchini, Champignons oder Mais. Mit 60 g Käse bestreuen und erneut in den Ofen schieben, bis der Käse eine schöne Farbe hat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Abkühlen lassen, mit Rucola bestreuen und vorsichtig einrollen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eingerollt in Alufolie mehrere Tage im Kühlschrank haltbar.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für den Boden Quark, Eier und 80 g vom Käse in einer Schüssel miteinander verrühren. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im Ofen backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Backblech herausnehmen, den Kuchenboden mit Crème fraîche bestreichen und mit Speckwürfeln, Lauchzwiebeln und dem restlichen Käse bestreuen. Weitere 15 - 20 Minuten backen, bis der Käse eine schöne Farbe hat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kann als Flammkuchen oder als Rolle gegessen werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Flammkuchen hat ca. 6 g Kohlenhydrate.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Magerquark, Reibekäse und Eier zu einer dickflüssigen Masse verrühren und auf einem mit Backpapier ausgelegten Backblech verteilen. Bei 180 °C Ober-/Unterhitze im heißen Backofen ca. 20 Minuten backen. Den Teig auskühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten für die Sauce verrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch in einer Pfanne mit Salz und Pfeffer krümelig anbraten. Die Gurken in Scheiben schneiden und zum Hackfleisch geben. 2/3 der Sauce auf dem gebackenen Teig verteilen. Das noch warme Hackfleisch darüber verteilen und den Toastkäse über dem Hackfleisch schmelzen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anschließend Salat und evtl. Tomaten darauf legen und die restliche Sauce darauf verteilen. Den Teig mithilfe des Backpapiers einrollen, so dass die Big Mac Rolle aussieht wie eine Biskuitrolle.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wichtig ist, nicht zu viel auf dem Teig zu verteilen, da die Rolle sonst zu dick wird und die Füllung an beiden Enden hervorquillt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Lachsfilet, falls TK, etwas antauen lassen. Waschen und trocken tupfen. Mit Salz und Pfeffer, nach Wunsch auch mit Kräutern, würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schafskäse in Würfel schneiden. Die Zucchini und Pilze in dünne Scheiben, die Paprika in Streifen schneiden. Tomaten halbieren oder vierteln. Knoblauch fein hacken. Das Gemüse mit Knoblauch, Salz und Pfeffer sowie ein paar Spritzern Chiliöl in einer Schüssel vermengen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Auf einem Backblech aus Alufolie* eine Schüssel formen, d.h. die Ränder an 4 Seiten hochschlagen. Ich empfehle 2 Schichten Alufolie zu nehmen, dann kann nichts auslaufen. Anschließend das Gemüse darauf verteilen. Dann den Lachs darauf legen, mit ein bisschen Chili-Öl beträufeln und den Schafskäse großzügig darüber krümeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Bei 180 °C Ober-/Unterhitze ca. 30 - 35 Minuten im heißen Ofen garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="*Anmerkung der Chefkoch.de Rezeptbearbeitung:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wie auf vielen Bildern zu sehen ist, kann man auch eine Auflaufform verwenden. Das Gericht gelingt darin genau so gut.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hähnchenbrust säubern und in mundgerechte Stücke schneiden. In einer Pfanne mit etwas Pflanzenfett anbraten, bis das Fleisch schön knusprig ist. Mit etwas Salz, Pfeffer und Curry würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit Zucchini, Gurke und Tomaten klein schneiden. Hähnchen beiseitelegen und warm halten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der gleichen Pfanne Zwiebeln und Knoblauch anbraten. Zucchini dazugeben und dünsten, bis diese weich aber noch bissfest sind. Gurke und Tomaten dazugeben und ca. 4 Minuten dünsten. Evtl. einen Schuss Wasser dazugeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Frischkäse und Milch einrühren. Hähnchenfleisch in die Pfanne geben und mit geschlossenem Deckel bei schwacher Hitze ca. 5 - 10 Minuten köcheln lassen, bis die Sauce cremig wird. Mit Paprika abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Man kann auch eine rote Paprikaschote zusammen mit der Zucchini dazugeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt sehr gut mein Erdbeer-Avocado-Salat: http://www.chefkoch.de/rezepte/2762181428080627/Erdbeer-Avocado-Salat.html")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Cashewkerne mit dem Currypulver in einer Pfanne bei schwacher Hitze 3 Minuten trocken rösten. Den Ingwer schälen und reiben, den Knoblauch in kleine Stücke schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Cashewkerne zusammen mit Ingwer, Knoblauch, Essig, Tomatenmark und Joghurt in einer Küchenmaschine oder im Mixer pürieren. Die so entstandene Paste mit dem Fleisch in einer Schüssel vermischen und alles 24 Stunden im Kühlschrank durchziehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einer großen Pfanne oder einem großen Topf die Butter zerlassen. Zwiebel, Zimt, Salz und Kardamom bei mittlerer Hitze ca. 5 Minuten andünsten, bis die Zwiebel weich ist. Das Fleisch mit der Marinade dazugeben und 10 Minuten kochen lassen. Die Chiliflocken, gehackte Tomaten aus der Dose und die Gemüsebrühe dazugeben und aufkochen lassen. Die Hitze reduzieren und ohne Deckel 40 - 45 Minuten köcheln lassen. Kurz vor dem Servieren die Sahne unterrühren und das Gericht mit dem gehackten Koriander bestreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt wunderbar Basmatireis oder Naanbrot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Teigzutaten verkneten und einen geschmeidigen, nicht mehr klebenden Teig herstellen. Zwei Muffinbackformen mit je 12 Muffinmulden fetten und den Teig in den Mulden verteilen, dabei jeweils auch einen kleinen Rand andrücken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Paprika und Lauch putzen und waschen, Zwiebel schälen, alles fein hacken und in einer Pfanne mit etwas Öl ca. 5 Minuten andünsten. Die Hälfte des Gemüses in eine Schüssel füllen und abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Getrocknete Tomaten abtropfen lassen, in kleine Stücke schneiden. Schinken würfeln. Die Tomaten zur einen, den Schinken zur anderen Gemüsehälfte geben. So erhält man nachher 12 Miniquiches für Schinkenliebhaber und 12 für Vegetarier.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Gusszutaten miteinander verquirlen und jeweils wieder halb und halb mit dem Gemüse mischen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dieses dann auf den Teig in den Muffinmulden geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Backofen bei 180 °C Ober-/Unterhitze ca. 20 - 25 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Diese Mini-Quiches passen super zu einem kalten Bufett oder als Fingerfood auf einer Party.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fleisch waschen und trocken tupfen. Mit Salz und Pfeffer würzen. Öl in einer Pfanne erhitzen. Filets darin von allen Seiten ca. 5 Min. kräftig anbraten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tomaten waschen und halbieren. Basilikumblätter abzupfen, waschen und fein hacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sahne in einem Topf aufkochen lassen. Schmelzkäse hineinrühren und schmelzen lassen. Mit Salz und Pfeffer würzen. 2/3 vom Basilikum unterrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fleisch und Tomaten in eine gefettete Auflaufform geben. Sauce darüber gießen. Mozzarella in kleine Stückchen schneiden und auf dem Fleisch verteilen. Wer mag, kann noch geriebenen Parmesan und 1 EL Kräuterbutter in kleine Flöckchen darauf verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Ofen bei 200 °C Ober-/Unterhitze bzw. 175 °C Umluft ca. 30 Min. backen. Herausnehmen und mit restlichem Basilikum bestreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu schmecken Kroketten oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Platte (oder einen großen Teller) in den Backofen stellen und diesen mit 80 °C ca. eine halbe Stunde vorheizen. Temperatur wenn möglich mit Backofenthermometer kontrollieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schweinefilet 1 Stunde vor dem Anbraten aus dem Kühlschrank nehmen, damit das Fleisch auch im Kern Zimmertemperatur annimmt. Falls der Metzger es nicht schon vorher getan hat, das Fleisch parieren (d.h. von Sehnen, Häutchen, Fett etc. befreien). Hat man ein ganzes Schweinefilet, dann schlägt man die Spitze soweit um, dass in etwa ein gleichmäßig dickes Fleischstück entsteht.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Filet salzen (nur wenig wegen des Speckmantels!) und pfeffern.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Baconscheiben überlappt auslegen, in einer Breite, die der Länge des Filetstücks entspricht. Beide Enden des Filets je nach Dicke mit ein bis zwei (evtl. halbierten) Baconscheiben abdecken, das Filet auf die ausgelegten Scheiben legen und einrollen. Die Speckhülle entweder mit Küchengarn oder (von mir aus Handhabungsgründen bevorzugt) mit Rouladennadeln fixieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einem großen Schmortopf Öl bzw. Butterschmalz erhitzen und das Filet in ca. 6 Minuten von allen Seiten braun/kross anbraten. Auch die beiden Kopfseiten sollten dabei angebraten werden, dabei das Filet mit Hilfe von einer Küchenzange oder gefaltetem Küchenpapier senkrecht halten. Anschließend das Fleisch mit einem Bratenthermometer versehen für ca. 2 Stunden in den vorgeheizten Backofen auf die Platte/den Teller legen und auf die gewünschte Kerntemperatur bringen (ca. 60 °C für einen rosa Kern).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Bratensatz im Schmortopf entfetten und mit etwas Weißwein oder Brühe lösen, dann für den späteren Gebrauch beiseitestellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine halbe Stunde vor Garende des Fleisches die Zwiebeln schälen und würfeln, Knoblauchzehen schälen und in kleine Scheiben/Würfel schneiden sowie die Pilze säubern und je nach Größe in 2, 4 oder 6 Teile schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einer großen Pfanne die Butter zerlassen, den Schinkenspeck/Bacon anbraten, Zwiebeln und Knoblauch anschwitzen. Die Champignons und das Tomatenmark hinzufügen, etwas pfeffern und salzen und so lange braten, bis kaum noch Flüssigkeit übrig geblieben ist. Währenddessen Sahne, Crème fraîche, Brühe und Wein im Schmortopf mit dem gelösten Bratensatz zusammen erhitzen. Gleichzeitig kann man auch schon das Wasser für die Spätzle aufsetzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gebratenen Champignons in den Schmortopf geben und ca. 5 Minuten leicht köcheln lassen, dabei nach Belieben klein gehackte Kräuter hinzufügen. Anschließend mit Worcestersoße, Salz und Pfeffer abschmecken. Wem das Champignongemüse zu flüssig ist, kann gegebenenfalls noch mit Mehl/Mondamin andicken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Spätzle nach Anweisung im Salzwasser mit 2 EL Öl bissfest kochen, abgießen und - wenn sie nicht direkt auf die vorgewärmten Teller verteilt werden - kurz in etwas zerlassener Butter schwenken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch aufschneiden (scharfes oder Elektromesser lässt den krossen Schinkenspeck heil an den Fleischscheiben) und mit Champignongemüse und Spätzle servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="11")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für Interessierte noch einige Tipps:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="12")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Es empfiehlt sich, die Essteller von vornherein mit der Fleischplatte mit vorzuwärmen. Sie sind dann zwar relativ heiß (80 °C), das ist aber auch günstig, da beim NT-Garen das Fleisch naturgemäß nicht sehr heiß auf den Teller kommt und dann noch schneller auskühlen würde. Zwischendurch sollte man sie nicht in den Ofen zum Fleisch stellen, da das den NT-Garvorgang zu stark unterbricht.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="13")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Beim Anbraten der Filet-Enden hat sich bei mir das Halten des Filets mit Küchenpapier in der Hand durchgesetzt. Dazu faltet man ein Blatt Küchenpapier zweimal und achtet nur darauf, dass man sich nicht am heißen Fett verbrennt bzw. das Papier das heiße Fett aufsaugt. Man kann dann das Filet bequem ca. 30 sec. senkrecht halten, fürs Anbraten des Endes. Das Problem bei der Küchenzange ist, dass man damit die Baconhülle doch viel leichter verschiebt oder sogar zerstört.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position="14")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln kochen und mit kaltem Wasser abschrecken. Die Pinienkerne in einer Pfanne bei mittlerer Hitze ohne Fett leicht anbräunen. Rucola gut waschen, trocken schleudern und etwas kleiner schneiden. Die getrockneten Tomaten gut abtropfen lassen und wie den Mozzarella und den Parmaschinken klein schneiden. Alles in eine große Schüssel geben, salzen und pfeffern.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(52)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Öl, Essig, klein gehackte oder gepresste Knoblauchzehe, Pesto, Senf und Honig miteinander vermischen und kurz vor dem Essen über den Salat geben. Alles noch einmal gut durchmischen und mit dem geriebenen Parmesan garnieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(52)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln im Salzwasser al dente kochen, abkühlen lassen. In der Pfanne die gehackte Zwiebel mit dem Knoblauch anschwitzen, das Fleisch hinzu fügen und gut anbraten. Die klein gewürfelten Tomaten zufügen und mit Tomatenmark, den Gewürzen, schön pikant abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(53)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nacheinander Nudeln, Joghurt sowie die Hackfleischmischung in die Schüssel füllen und alles gut vermengen. Zum Schluss mit der klein gehackten Petersilie bestreuen, aber erst kurz vor dem Anrichten untermengen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(53)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Salat im Kühlschrank gut durchkühlen lassen. 1 Stunde vor dem Verzehr heraus nehmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(53)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln nach Packungsanweisung bissfest kochen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit die Tomaten klein schneiden und den Schafskäse würfeln. Den Knoblauch abziehen, durchpressen oder winzig klein schneiden. Die Pinienkerne vorsichtig in einer Pfanne ohne Fett anrösten (Vorsicht - sie werden schnell schwarz!). Die Basilikumblätter klein reißen oder schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gekochten Nudeln abgießen und nun alles zusammen in eine Schüssel geben. Nun das Olivenöl (die Menge ist geschätzt) darüber geben und mit Salz und Pfeffer abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Bei uns wird die erste Portion immer noch warm gegessen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln würfeln und mit dem Hackfleisch in Olivenöl anbraten. Die Paprikaschoten ebenfalls würfeln und mit den Champignons sowie dem Mais zum Hackfleisch geben. Alles kurz anbraten, anschließend mit der Gemüsebrühe ablöschen. Die Sahne, die Tomatensauce und den Sahneschmelzkäse hinzugeben und ca. 10 Minuten köcheln lassen. Zum Schluss mit Salz, Pfeffer und Oregano abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Beim Servieren nach Belieben etwas geriebenen Parmesan auf die Suppe streuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt am besten Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Schmeckt auch als Nudelsauce gut, dann weniger Gemüsebrühe verwenden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Brötchen in Wasser einweichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel schälen und in feine Würfel schneiden. Wer möchte, kann die Zwiebel auch kurz in Butter glasig dünsten (ich bevorzuge die rohen Zwiebeln).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Ei, die Zwiebeln und die Gewürze zur Hackmasse geben und sehr gut vermengen, entweder mit einem großen Löffel oder mit den Händen. Nicht mit dem Mixer arbeiten, dabei werden die Frikadellen oft zäh!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Brötchenmasse sehr gut ausdrücken, entweder mit den Händen, oder auch zwischen zwei Brettchen, zur Hackmasse geben und wieder gut vermengen. Bis hierhin sollten diese Arbeitsschritte wenigstens 10 - 15 Minuten dauern, denn je ordentlicher vermengt und geknetet wird, umso besser und lockerer das Ergebnis!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wer die rohe Masse abschmecken kann, sollte das jetzt tun, oder eine Probe braten. Jetzt gleichmäßige, nicht zu kleine Bällchen/Klöße/Klopse formen und auf einer bemehlten Arbeitsfläche flachdrücken und glätten. Wer möchte, kann sie in Mehl oder Semmelbrösel wenden. Oma und ich braten sie ohne alles.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine schwere Pfanne mit guter Margarine stark erhitzen und die Frikadellen einlegen, kurz auf beiden Seiten scharf anbraten und dann ca. 15 - 20 Minuten (1 - 2-mal vorsichtig wenden) auf mittlerer/schwacher Hitze fertig braten. Nicht zu viele Frikadellen auf einmal in einer Pfanne braten, eher eine zweite benutzen oder nacheinander braten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt z. B. Kartoffelsalat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis in der Gemüsebrühe garen (eine Tasse mit ca. 200 - 250 ml Inhalt als Maß nehmen).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Chilischote längs halbieren, von den Kernen befreien und hacken. Die Paprikaschoten putzen und würfeln. Die Zwiebeln fein würfeln und in einer Pfanne in etwas Öl glasig dünsten. Den gepressten Knoblauch, die Chilischote und das Tomatenmark hinzugeben und kurz mit anschwitzen. Die Paprikawürfel in die Pfanne geben und ein paar Minuten lang anbraten, dabei ab und zu die Pfanne schwenken. Mit Paprikapulver, Salz und Pfeffer würzen. Den Reis hinzugeben, untermengen und heiß werden lassen. Die Kräuter hacken und zuletzt untermischen. Nochmals abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Joghurt und gepressten Knoblauch verrühren, mit Salz und Pfeffer abschmecken. Den Reis mit einem Klecks von der Joghurtsauce servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Von der Menge werden ca. 3 - 4 Personen satt. Der Reis kann auch als Beilage gegessen werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kräutermenge kann nach Belieben erhöht werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Hähnchenfilets waschen und mit Küchenkrepp trocken tupfen. Mit Salz und Paprikapulver würzen und in einer Auflaufform dicht aneinanderlegen. Die Paprikaschoten waschen, entkernen, in schmale Streifen schneiden und auf den Filets verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel in halbe Ringe schneiden und in einer Pfanne in etwas Öl andünsten. Die Chilischote hineinzupfen, den Knoblauch pressen und hinzugeben. Paprikapulver und Tomatenmark hinzufügen, mit der Brühe ablöschen und kurz aufkochen lassen. Anschließend Sahne und Schmand unter die Soße rühren und mit Salz abschmecken. Die Soße in die Auflaufform gießen, Fleisch und Paprikastreifen sollten ganz bedeckt sein. Den geriebenen Käse gleichmäßig darauf verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Backofen bei 180 °C Ober-/Unterhitze ca. 1/2 Std. garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Beilagen: Bandnudeln oder Reis und Eisbergsalat mit Mandarinen und süß-saurer Vinaigrette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln in Spalten schneiden und in einer Schüssel mit Parmesan und Olivenöl vermischen. Die Gewürze in einer separaten Schüssel vermengen und dann zu den Kartoffeln geben. Noch einmal kräftig durchmischen, die Kartoffelecken dann auf einem mit Backpapier ausgelegten Backblech verteilen und bei 200 °C Ober-/Unterhitze für ca. 40 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(59)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hinweis: Heißhunger auf eine deftige Beilage oder einfach nur Appetit auf einen leckeren Snack? Diese Kartoffelecken sind genau das richtige für alle, die es gerne deftig mögen und etwas Neues ausprobieren wollen. Dazu schmeckt Sour Cream mit ein paar frischen Kräutern wirklich köstlich, alternativ könnt ihr die Wedges natürlich auch als Beilage zu einem leckeren Steak oder gebratenem Fisch servieren. Eurer Kreativität sind keine Grenzen gesetzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(59)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vorbereitende Schritte:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Butter würfeln und bei Raumtemperatur weich werden lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Grünes und rotes Pesto separat durch ein Sieb streichen und so etwas Öl entfernen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mozzarella in Stücke reißen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sonnengetrocknete Tomaten abtropfen lassen und fein hacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Oliven abtropfen lassen und grob hacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Erste Arbeitsschritte:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zwei große Backbleche mit Backpapier auslegen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die größere Rührschüssel einsetzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Spiral-Knethaken anbringen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schritt 1:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="11")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die erste Zutat der Zutatenliste 1 (Milch) in einem kleinen Topf bei mittlerer Hitze erwärmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="12")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Herd nehmen und in eine Karaffe gießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="13")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die nächsten vier Zutaten der Zutatenliste 1 (Mehl, Hefe, Zucker, Salz) in die Rührschüssel geben. Den Spritzschutz anbringen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="14")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="20 Sekunden bei Geschwindigkeitsstufe 1 gut verrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="15")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Während die Küchenmaschine langsam rührt, bei Geschwindigkeitsstufe 1 die warme Milch langsam dazugießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="16")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die nächsten zwei Zutaten der Zutatenliste 1 (Ei, Eigelb) hineingeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="17")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2 Minuten bei Geschwindigkeitsstufe 1 rühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="18")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach und nach bei Geschwindigkeitsstufe 1 die letzte Zutat der Zutatenliste 1 (Butter) in die Rührschüssel geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="19")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="6 bis 8 Minuten bei Geschwindigkeitsstufe 1 zu einem glatten und homogenen Teig rühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="20")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Rührschüssel aus der Küchenmaschine herausnehmen, mit Klarsichtfolie abdecken und an einem warmen Ort 1 Stunde gehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="21")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schritt 2:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="22")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Teig auf eine leicht bemehlte Arbeitsfläche legen und flach drücken. Den Teig in 12 Portionen (je ca. 76 Gramm) teilen. Jedes Teigstück zu einem festen Teigball formen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="23")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Pesto-Babki:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="24")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sechs Teigbälle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="25")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten der Zutatenliste 2 (Pesto, Mozzarella, schwarzer Pfeffer) über die Teigstücke geben. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigstücke vom langen Ende her zu einer Schlange fest aufrollen. Alle Nähte und Enden zusammendrücken. Mit einem scharfen Messer die Teigschlangen der Länge nach halbieren. Die beiden halbierten Teigschlangen mit der gefüllten Seite nach oben zu einem Zopf flechten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="26")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Hefezopf langziehen (25 cm). Beide Enden zusammenführen, sodass sie sich überlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendrücken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="27")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schritt 3:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="28")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die kleinere Rührschüssel einsetzen und den K-Haken anbringen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="29")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten der Zutatenliste 3 (Pesto, Peperoni, sonnengetrocknete Tomaten, Oliven, Mozzarella, Oregano, schwarzen Pfeffer) in die Rührschüssel geben. Geschwindigkeitsstufe 1 einstellen, 20 Sekunden rühren und in dieser Zeit auf Geschwindigkeitsstufe 3 erhöhen, um die Zutaten zu einer Paste zu rühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="30")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Pizza-Babki:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="31")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die letzten sechs Teigbälle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="32")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Paste gleichmäßig über die Teigstücke verteilen. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigstücke vom langen Ende her zu einer Schlange fest aufrollen. Alle Nähte und Enden zusammendrücken. Mit einem scharfen Messer die Teigschlangen der Länge nach halbieren. Die beiden halbierten Teigschlangen mit der gefüllten Seite nach oben zu einem Zopf flechten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="33")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Hefezopf langziehen (25 cm). Beide Enden zusammenführen, sodass sie sich überlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendrücken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="34")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Schritt 4:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="35")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 190 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="36")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Klarsichtfolie entfernen. Babki mit verquirltem Ei (Eistreiche) bestreichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="37")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im Backofen 12 bis 15 Minuten goldbraun backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="38")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Warm servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="39")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die herzhaften Babki schmecken nicht nur köstlich, sondern sind auch ein echter Hingucker auf dem Esstisch.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position="40")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 170 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die TULIP Bacon-Scheiben auf ein mit Backpapier ausgelegtes Backblech legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Barbecuesauce mit braunem Zucker und Paprikapulver mischen. Die TULIP Bacon-Scheiben mit der Mischung gleichmäßig glasieren und im Ofen etwa 25 Min. auf der mittleren Einschubleiste kross backen. Anschließend auf Küchenpapier geben und 3 Min. ruhen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mehl, Milch, Zucker, Eier, Butter und Salz zu einem glatten und dicken Pfannkuchenteig verrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Pfannkuchen in einer heißen beschichteten Pfanne (Größe nach Belieben) bei mittlerer Hitze von beiden Seiten goldbraun backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Serviervorschlag: Pfannkuchen mit Frischkäse, Ahornsirup und den knusprigen, glasierten Baconstreifen servieren. Nach Belieben mit frischen Johannisbeeren dekorieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hühnerfleisch in kleine Stücke schneiden und im Topf kurz anbraten. Die Frühlingszwiebeln in Ringe schneiden und den Ingwer in kleine Stücke. Beides zufügen und kurz mitbraten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mit der Hühnerbrühe ablöschen. Kokosmilch, Sojasauce und Currypaste hinzufügen. Das Zitronengras längs kreuzweise einschneiden, sodass es noch am Stück bleibt, dann kann man es später einfacher wieder entnehmen, und in die Suppe geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="5 Minuten kochen, das restliche Gemüse und die Gewürze hinzufügen. Die Nudeln nach Packungsangabe kochen und hinzufügen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wer mag, kann noch ein wenig frischen Koriander aufheben und am Schluss über die Suppe streuen. Ich habe ab und zu noch getrocknete Chilifäden zum Garnieren verwendet.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anmerkung der Redaktion:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Viki röstet die Currypaste bereits zusammen mit Ingwer, Chili und etwas Speiseöl an, dadurch wird der Geschmack intensiver. Anstatt Frühlingszwiebeln könnt ihr auch Schalotten oder Zwiebeln verwenden. Sie gibt die Paprikastreifen etwas früher, als die Pilze und die Nudeln in die Suppe, damit sie schön gar werden und so besser zu verdauen sind. Viki gibt zum Verfeinern noch zwei Prisen Zucker in die Suppe. Zum Anrichten drapiert Viki zunächst ein paar Nudeln und etwas Gemüse in einen tiefen Teller, bevor sie ihn mit Suppe aufgießt. Zum Schluss garniert sie die Suppe mit frischem Koriander und etwas Minze.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mehl, Quark, Backpulver, Milch, Öl, Salz und Zucker gut verkneten. Die übrigen Zutaten zum Teig geben. Noch mal durchkneten und kleine Bällchen formen. Auf ein Backblech mit Backpapier legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für 30 - 40 Min. bei 180 °C Ober-/Unterhitze in den heißen Ofen geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Für Feiern mache ich mindestens die doppelte Menge, kamen dort immer sehr gut an. Die Geschmackszutaten (Röstzwiebeln, Schinken, Käse) sind variabel, auf den Käse würde ich aber nicht verzichten!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Beim Backen muss man hin und wieder gucken, sie werden je nach Herd von unten auch sehr schnell dunkel, aber zu hell sollten sie auch nicht sein. Vorsicht, wenn sie noch warm sind, werden sie gerne stibitzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Teig reicht für 3 oder 4 runde Pizzen oder ein Blech.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Alle Zutaten in eine Schüssel geben und mindestens 5 Min. gut durchkneten. Den Teig ca. 30 Min. gehen lassen. Anschließend in 3 - 4 Portionen teilen, die jeweils zu Kugeln geformt werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nun kann es losgehen mit dem Auswellen und Belegen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Teig ist für jegliche Weiterverarbeitung geeignet - ob im Backofen (220°C, ca. 15 - 20 Min.), auf einem Pizzastein (250°C, ca. 10 - 15 Min.) oder in einer Elektropfanne (Stufe 3, erste Seite 3 Min., dann wenden, belegen und noch einmal 3 Min. von der anderen Seite). Sofort servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Ich habe das Rezept von einer italienischen Freundin.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Sauce das Olivenöl in einem Topf erhitzen. Das Hackfleisch hineingeben und unter Rühren so lange braten, bis es braun und krümelig ist. 1 EL Tomatenmark unterrühren und kurz anrösten. Mit der Gemüsebrühe ablöschen, die Sahne hinzufügen und aufkochen lassen. Das restliche Tomatenmark unterrühren und die Sauce mindestens 30 Minuten köcheln lassen. Danach die Butter darin zerlassen und die Sauce mit Salz, Cayennepfeffer und Parmesan abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Rigatoni nach Packungsanweisung in reichlich Salzwasser sehr bissfest kochen, dabei gelegentlich umrühren. In ein Sieb abgießen und abtropfen lassen, dann wieder in den Topf geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Schinken in 1/2 bis 1 cm breite Streifen schneiden. Die Sauce zu den Rigatoni geben und alles erhitzen. Die Schinkenstreifen unterrühren und nur kurz darin erwärmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 180 °C vorheizen. Die Nudelmischung in eine große Auflaufform geben oder auf vier kleine ofenfeste Formen gleichmäßig verteilen. Den geriebenen Edamer darüber streuen. Auf der mittleren Schiene überbacken, bis der Käse goldgelb ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Rinderrouladen aufrollen, waschen und mit Küchenkrepp trockentupfen. Zwiebeln in Halbmonde, Gurken in Längsstreifen schneiden. Schere und Küchengarn bereitstellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die ausgebreiteten Rouladen dünn mit Senf bestreichen, salzen und pfeffern. Auf jede Roulade mittig in der Länge ca. 1/2 Zwiebel und 1 1/2 Scheiben Frühstücksspeck sowie 1/2 (evtl. mehr) Gurke verteilen. Nun von beiden Längsseiten etwas einschlagen, dann aufrollen und mit dem Küchengarn wie ein Postpaket verschnüren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einer Pfanne das Butterschmalz heiß werden lassen und die Rouladen dann rundherum darin anbraten. Herausnehmen und in einen Schmortopf umfüllen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Sellerie, die restliche Zwiebel, Lauch und die Möhren kleinschneiden und in der Pfanne anbraten. Sobald sie halbwegs blond sind, kurz rühren. Eine sehr dünne Schicht vom Rotwein angießen, nicht mehr rühren und die Flüssigkeit verdampfen lassen. Sobald das Gemüse dann wieder trockenbrät, wieder eine Schicht Wein angießen, kurz rühren und weiter verdampfen lassen. Dies wiederholen, bis die 1/2 Flasche Wein aufgebraucht ist. Auf diese Art wird das Röstgemüse sehr braun (gut für den Geschmack und die Farbe der Soße), aber nicht trocken. Am Schluss mit dem Rinderfond, etwas Salz und Pfeffer und einem guten Schuss Gurkensud auffüllen und dann in den Schmortopf zu den Rouladen geben. Den Topf entweder auf kleiner Flamme oder bei ca. 160 °C Ober-/Unterhitze im heißen Backofen für 1 1/2 Stunden schmoren lassen. Ab und zu evtl. etwas Flüssigkeit zugießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach 1 1/2 Stunden testen, ob die Rouladen weich sind (einfach mal mit den Kochlöffel ein bisschen draufdrücken, sie sollten sich willig eindrücken lassen - wenn nicht, nochmal eine halbe Stunde weiterschmoren). Dann vorsichtig aus dem Topf heben, warmstellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Soße durch ein Sieb geben, aufkochen. Ca. 1 EL Senf mit etwas Wasser und der Speisestärke gut verrühren, in die kochende Soße nach und nach unter Rühren eingießen, bis die gewünschte Konsistenz erreicht ist. Die Soße evtl. nochmal mit Salz, Pfeffer, Rotwein, Gurkensud abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion 830 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln schälen und in feine Würfel schneiden. Im Sonnenblumenöl glasig anschwitzen. Rote Linsen, Tomaten mit Saft und Kokosmilch hinzufügen und gut umrühren. Mit der Gemüsebrühe aufgießen und die Suppe ca. 20 Minuten köcheln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(67)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zum Schluss mit Salz, Chili- und Kurkumapulver abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(67)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Suppe schmeckt am nächsten Tag doppelt so gut. Dazu passen Garnelenspieße und Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(67)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Mehl mit Kakao und Backpulver in einer Rührschüssel mischen. Die übrigen Zutaten für den Teig hinzufügen und alles mit einem Mixer zu einem Teig verarbeiten. Anschließend zu einer Kugel formen und den Teig in Frischhaltefolie gewickelt mindestens 30 Minuten kaltstellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Inzwischen für die Füllung die Butter in einem Topf zerlassen und abkühlen lassen. Den Boden der Springform fetten. Die Hälfte des Teiges mit einem Nudelholz ausrollen (wer lieber einen etwas dickeren Boden mag, kann auch 2/3 des Teiges verwenden) und eine 26er Springform damit auskleiden. Dabei sollte ein ca. 2 cm hoher Rand entstehen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Quark mit Zucker, Vanillezucker, dem Mark einer Vanilleschote, den Eiern, dem Puddingpulver und der zerlassenen Butter mit einem Schneebesen zu einer gebundenen Masse verrühren, in die Form geben und glatt streichen. Den restlichen Teig in kleine Stücke zupfen und auf der Füllung verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Form auf dem Rost im unteren Drittel in den vorgeheizten Backofen schieben und bei 180°C Ober-/Unterhitze ca. 60 Minuten backen. Nach dem Backen den Kuchen in der Form auf einem Kuchenrost erkalten lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gehackte Zwiebel in einer Pfanne mit etwas Öl anschwitzen. Das Hackfleisch zugeben und krümelig braten. Mit Salz, Pfeffer, Currypulver, Chilipulver und Knoblauch würzig abschmecken. Das Tomatenmark zugeben und kurz mitrösten. Die Gemüsebrühe angießen und den würfelig geschnittenen Kürbis ebenfalls zugeben. Zugedeckt ca. 5 Minuten dünsten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(69)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Danach Crème fraîche, Basilikum und die Gnocchi zugeben und alles gut miteinander vermischen. In eine Auflaufform füllen. Den Mozzarella in Scheiben schneiden und darüber verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(69)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheiztem Backrohr bei 200 °C Ober-/Unterhitze ca. 15 Minuten überbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(69)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 250 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Knetteig bereiten, ganz dünn ausrollen. Schmand und Crème double mischen, würzen und auf dem Teig verstreichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zwiebeln mit ganz wenig Wasser 1 Minute bei 600 Watt in der Mikrowelle dünsten (durch die hohen Temperaturen beim Backen kann es leicht passieren, dass die Zwiebeln verbrennen - das wird durch diesen Trick vermieden). Zusammen mit dem Speck auf dem Belag verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nun 20 Minuten im heißen Ofen auf der unteren Einschubleiste backen. Mit Schnittlauchröllchen bestreut servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Wer Kalorien sparen möchte, ersetzt Crème double durch 20%igen Quark.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Reicht für 2 - 3 Personen, je nach Hunger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch mit je 1 EL Öl, Sojasauce und Ingwer gut vermischen und ca. 30 Minuten marinieren. In der Zwischenzeit das Gemüse putzen und schneiden. Das Fleisch in einer beschichteten Pfanne rasch braten und dann zur Seite stellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im Wok oder einer großen Pfanne mit hohem Rand die Currypaste in 1 EL Öl anrösten. Die Erdnussbutter unterrühren und schmelzen lassen. Mit Kokosmilch ablöschen, das Gemüse zugeben und alles ca. 15 Minuten köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit den Reis zubereiten und ausdämpfen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kurz vor Ende der Garzeit (das Gemüse soll noch Biss haben) das Fleisch dazugeben und kurz wieder erhitzen. Das Curry mit Palmzucker, Fischsauce (notfalls etwas Salz nehmen) und Zitronengraspaste (soll nicht mitkochen) abschmecken. Nach Belieben Thai-Basilikum darüberstreuen und mit dem Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zusammenstellung des Gemüses kann man ganz nach Geschmack und Verfügbarkeit variieren/ergänzen, z. B. fein geschnittene Wasserkastanien für noch mehr Biss, ein paar kleine Brokkoliröschen oder einige Zuckerschoten (diagonal geteilt, kurz blanchiert oder angebraten) als zusätzlichen Farbtupfer. Es sollten (geputzt und geschnitten gemessen) insgesamt ca. 4 - 5 Handvoll Gemüse sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zitronengraspaste ist geriebenes, in etwas Pflanzenöl eingelegtes Zitronengras. Das angebrochene Glas am besten im Tiefkühlfach aufbewahren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 180°C vorheizen. Zwiebel abziehen und in Würfel schneiden. Lauch putzen, waschen und in halbe Ringe schneiden. Zucchini und Tomaten waschen, halbieren und Zucchini zusätzlich in Scheiben schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Öl in einer Pfanne erhitzen und Zwiebelwürfel darin anbraten. Hackfleisch dazugeben und kräftig anbraten. Lauch und Zucchini hinzufügen und mitdünsten. Passierte Tomaten angießen, Kirschtomaten unterheben, mit Salz und Cayennepfeffer abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kartoffelnudeln in Portionsauflaufformen geben und mit der Sauce übergießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Aufläufe mit Käse bestreuen und im vorgeheizten Backofen 15-20 Minuten backen (Gas: Stufe 3, Umluft 160°C).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitungszeit: 30 Minuten")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backzeit: 15-20 Minuten")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion (bei 3 Portionen):")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kJ/kcal: 3647/871")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 46,5 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 66,0 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position="11")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Wirsing die groben äußeren Blätter lösen, den Wirsing vierteln und den Strunk herausschneiden. Den Wirsing abspülen und abtropfen lassen, dann in Streifen schneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel abziehen, halbieren und in feine Streifen schneiden. Etwas Öl in einem großen Topf erhitzen und die Zwiebelstreifen darin unter gelegentlichem Rühren anschwitzen. Die Wirsingstreifen zufügen, salzen und mit geschlossenem Deckel dünsten. Die Gemüsebrühe zugießen und ca. 10  15 Minuten bissfest schmoren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Währenddessen das Kasseler in kleine Würfel schneiden, zusammen mit den Schupfnudeln unter den Wirsing mischen. Die Hitze reduzieren, die saure Sahne unterheben, alles mit Senf, Salz, Pfeffer und Kümmel abschmecken. Die Schupfnudel-Wirsing-Mischung in eine Auflaufform (ca. 20 x 30 cm) füllen, mit dem geriebenen Käse und den Schnittlauchröllchen bestreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Backofen bei 200 °C Ober-/Unterhitze ca. 25 Minuten goldbraun überbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Wirsing putzen, waschen und in Streifen, Kasseler in Würfel schneiden. Zwiebeln abziehen und in Ringe schneiden. Öl erhitzen, Zwiebeln dazugeben, goldbraun braten und herausnehmen. Wirsing in das verbliebene Bratfett geben und andünsten. Brühe angießen, Kasseler und gebratene Zwiebeln dazugeben und abgedeckt ca. 20 Min. garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2. Schupfnudeln und Schmand untermischen und alles mit Senf, Liebstöckel, Salz, Pfeffer und Kümmel abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="3. Mischung in eine Gratinform (20 x 30 cm) geben, Käse überstreuen und im vorgeheizten Backofen bei 200 °C (Gas: Stufe 4, Umluft 180 °C) ca. 25-30 Min. goldbraun überbacken. Schnittlauch überstreuen und servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion (bei 6 Portionen):")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kJ/kcal: 2.322/555")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 24,3 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 59,2 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sauerrahm und Crème fraîche mit der Brühe verrühren und diese Mischung in eine große Auflaufform füllen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln gut waschen und mehrfach einschneiden, aber nicht ganz durchschneiden - sie sollen an der Unterseite noch zusammenhängen. Die Abstände zwischen den Schnitten sollten so ähnlich sein wie bei einem Eierschneider.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln mit der geschnittenen Seite nach oben in die Form setzen. Aber nur nebeneinander - nicht übereinander - stapeln, sodass sie etwa zur Hälfte in der Soße sitzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im heißen Backofen bei 200 °C Ober-/Unterhitze ca. 45 - 60 Minuten backen, bis die Kartoffeln fast gar sind.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit die Butter zerlassen. Katenschinken und Rosmarin hinzufügen sowie die Toastbrotwürfel dazumischen. Diese Mischung auf den Kartoffeln verteilen und noch einmal so lange backen, bis die Brotwürfel schön braun sind und die Kartoffeln gar.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu Blattsalat servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln waschen, schälen und in Würfel schneiden. Den Lauch waschen und in Ringe schneiden. Beides in zerlassener Butter leicht anbraten. Die Gemüsebrühe dazugeben und alles 15 Min. kochen. Evtl. mit dem Pürierstab ganz leicht pürieren (nur ein paar Impulse). Den Lachs in mundgerechte Würfel schneiden und zu der Suppe geben. Alles noch einmal 5 Min. ziehen lassen. Die Suppe mit Sahne verfeinern und mit Dill bestreuen. Heiß servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(76)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="De Tomaten, die Walnüsse, eine Knoblauchzehe und einen guten Schuss Olivenöl in einen Mixer geben und daraus ein Pesto herstellen. Mit Salz und Pfeffer würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zwiebel und Knoblauch würfeln, in etwas Olivenöl in einer Pfanne glasig dünsten und mit ein wenig Gemüsebrühe ablöschen. Dann Spinat dazugeben und einige Minuten mitdünsten, bis er zusammenfällt. Mit Salz und Pfeffer würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Blätterteig auf einem Backblech ausbreiten und großzügig mit dem Tomatenpesto bestreichen. Danach den Spinat darauf verteilen und von der langen Seite her zu einem Strudel rollen. Wichtig: Mit dem Schluss nach unten auf das Backblech legen, damit er schön zu bleibt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mit etwas Wasser bestreichen und bei 200 °C Ober-/Unterhitze backen, bis der Blätterteig goldbraun ist. Das dauert ca. 20 Minuten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Optional bietet sich natürlich ein Knoblauchdip oder auch eine Tomatensoße dazu an; uns hat es aber auch ohne sehr gut geschmeckt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für den Reis 1 Teil Reis mit 2 Teilen kaltem Salzwasser in einem Topf mit Deckel aufkochen. Dann die Hitze reduzieren, sodass es gerade eben köchelt. Abgedeckt quellen lassen, bis alles Wasser verkocht ist. Das dauert ca. 15 - 20 Minuten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1 EL Erdnussöl in eine heiße Pfanne geben. Die Hühnerbrust scharf darin anbraten und aus der Pfanne nehmen. Wieder 1 EL Erdnussöl in dieselbe heiße Pfanne geben, die Currypaste kurz darin anschwitzen und mit der Kokosmilch aufgießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Es gibt 3 verschiedene Currypasten. Grüne (am schärfsten), rote (mittelscharf) und gelbe (am mildesten). Ich nehme auf jeden Fall einen sauberen Teelöffel, um die Paste aus dem Glas zu nehmen und stelle das geöffnete Glas in den Kühlschrank. So hält es sich mehrere Monate.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Erdnussbutter dazugeben, den Knoblauch dazupressen, die gekörnte Gemüsebrühe und die Zuckerschoten dazugeben. Wer keine Zuckerschoten bekommt, kann auch grüne Bohnen nehmen. Zuckerschoten schmecken aber besser.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Karotte schälen, je nach Dicke längs halbieren, in Scheiben schneiden und ebenfalls dazugeben. Alles mehrere Minuten köcheln lassen, sodass die Zuckerschoten und die Karotte noch bissfest sind.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Danach die Bambussprossen und das Fleisch wieder dazugeben und noch ein paar Minuten köcheln lassen. Die Speisestärke in kaltem Wasser anrühren und in die köchelnde Soße geben, um sie etwas anzudicken. Zum Schluss die Zitronengraspaste unterrühren und mit Salz würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dieses Grundrezept kann je nach Lust und Laune durch Variieren des Fleisches (z. B. Hühnerbrust, Putenbrust, Rinderlende oder Schweinefilet) oder mit Fischfilet oder Garnelen und mit verschiedenem Gemüse (z. B. Bambussprossen in Streifen, Sojabohnenkeimlinge, Karotten, Babymais, Zuckerschoten, Thai-Auberginen, Pak Choi o. a.) zu immer neuem Genuss-Erlebnis führen. Lassen Sie Ihrer Kreativität freien Lauf! Es eignet sich auch für Vegetarier, da man es auch ausschließlich mit vielem verschiedenem Gemüse zubereiten kann.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Gericht muss nicht im Wok zubereitet werden, es geht genauso gut in einem breiten Topf, da es Suppencharakter hat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Currypaste im heißen Öl sautieren, kurz mit etwas Wasser ablöschen, nach und nach die Kokosmilch dazugeben und immer erst gut verrühren, bevor man mehr dazugibt (bringt eine sehr schöne rote Farbe). Das vorgesehene Fleisch (Fisch oder Garnelen) in mundgerechte Stücke schneiden, dazugeben und ca. 5 Minuten köcheln lassen, bis es gar ist. Garnelen brauchen nur sehr kurze Zeit!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das in Streifen geschnittene Gemüse der Wahl (egal welches und wie viele Sorten) dazugeben und alles wieder zum Kochen bringen. Alles sollte bissfest bleiben und die Farbe behalten (Pak Choi oder Chinakohl erst kurz vor Ende dazugeben).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mit der Fischsauce, der hellen Sojasauce und dem Palmzucker abschmecken. Thai-Basilikum-Blätter und Peperoni dazufügen, eine Minute weiterkochen. Nach Belieben und Schärfe-Empfinden die kleingeschnittenen Chili-Röllchen einstreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Gericht heiß mit Reis (Basmati, Jasminreis oder thailändischer Duftreis) servieren, als Variation kann man auch roten Reis aus dem Asialaden probieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Tortellini nach Packungsanweisung kochen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den gekochten Schinken in einer tiefen Pfanne in Butter kurz anbraten, dann 400 ml von der Sahne hineingeben und auf kleiner Stufe köcheln lassen. Wenn die Tortellini gar sind, in die Pfanne zur Schinkensahne geben und weiter köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit in einer kleinen Schüssel das Eigelb mit Parmesan, Muskatnuss, Salz und den restlichen 200 ml Sahne verrühren. Dies dann in die Pfanne zu den Tortellini geben und so lange köcheln lassen, bis die Soße dickflüssig wird. Sofort servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sehr gehaltvoll, aber der Geschmack ist fantastisch. Ab und zu kann man sich's mal gönnen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die ersten sechs Zutaten für die Marinade mischen und die gewaschenen und getrockneten Hähnchenfilets hineinlegen. Mindestens 1 Std. darin marinieren (geht auch über Nacht).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kartoffeln schälen, größere Knollen halbieren und in Olivenöl ca. 10 Min. von allen Seiten braun braten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gebratenen Kartoffeln in eine mit Olivenöl ausgestrichene Auflaufform geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Knoblauch schälen und klein hacken. Die Zwiebel schälen, halbieren und die Hälften in Ringe schneiden. 1 Zweig Thymian und 1 Zweig Rosmarin waschen und hacken. Zwiebeln, Knoblauch und gehackte Kräuter im Bratfett andünsten, dann über die Kartoffeln geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch mit der Marinade auf die Kartoffeln geben und alles im Backofen bei 200 Grad ca. 15 Min. braten. Dann heiße Hühnerbrühe angießen, die Tomaten und zwei Rosmarinzweige im Auflauf verteilen und weitere 30 Min. im Ofen garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Aus dem Mehl, Zucker, Butter, Ei und Backpulver einen Knetteig herstellen. Den Boden einer 26 cm Springform mit Backpapier auslegen, den Rand einfetten. Den Teig ausrollen und die Ränder von Hand recht hoch drücken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen am besten jetzt auf 175°C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Quark kurz geschmeidig rühren, dann nach und nach alle Zutaten zugeben und gut verrühren. Die sehr flüssige Masse in die Springform füllen und den Kuchen 70 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit das Eiweiß mit dem Puderzucker steif schlagen. Nach 70 Minuten den Kuchen heraus holen und den Eischnee ca. 1 cm dick auf den Belag streichen. Es wird wohl nicht alles davon benötigt! Nochmals 10 Minuten bei gleicher Hitze backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dann den Kuchen etwas abkühlen lassen und den Rand der Springform vorsichtig mit einem Messer lösen. Den Kuchen auf dem Boden der Springform mehrere Stunden abkühlen lassen. Wenn alles funktioniert hat, dann sollten beim Abkühlen auf dem Eiweißguss die Tränen entstehen. Schmecken tut der Kuchen aber auch ohne!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Schafskäsewürfel in ein Sieb gießen und das Öl dabei auffangen. Die Champignons in Scheiben schneiden. Die Paprikaschoten putzen und in Streifen schneiden. Den Knoblauch fein hacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In ca. 3 EL von dem aufgefangenen Öl das Hackfleisch braun und krümelig braten. Die Hälfte der Champignons dazugeben und mit anbraten. Nun auch die Paprikastreifen und den Knoblauch dazugeben und anbraten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach ca. 5 Minuten die Crème fraîche und den Oregano einrühren und mit Salz und Pfeffer würzig abschmecken. Alles in eine feuerfeste Form geben und die restlichen Champignons darauf verteilen. Zuletzt die abgetropften Schafskäsewürfel sowie den zerbröckelten Schafskäse darauf streuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Auflauf ca. 20 - 30 Minuten im heißen Backofen bei 180 °C Umluft backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt Tzatziki, Fladenbrot und/oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Füllung 1 EL Sesamöl in einer ausreichend großen Pfanne erhitzen. Gemüse in mundgerechte Stücke schneiden, Sprossen abtropfen lassen. Das vegane Hack in der Pfanne krümelig braten. Das Gemüse hinzugeben und alles vermengen. 3 Minuten bei hoher Hitze andünsten und mit Chili Flocken, Salz und Pfeffer würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Strudelteigblätter hochkant legen. Auf den unteren Teil mittig etwa 3 EL der Füllung geben. Seiten einklappen und das gesamte Strudelteigblatt vorsichtig einrollen. Auf ein mit Backpapier ausgelegtes Backblech legen. Mit den übrigen Blättern gleich verfahren. Die fertigen Frühlingsrollen mit dem restlichen Sesamöl einpinseln. Wer mag kann etwas Sesam drüberstreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Frühlingsrollen im vorgeheizten Backofen 25 - 30 Minuten auf der mittleren einschubleiste goldbraun backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Energie kJ/kcal 1059/253")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eiweiß 12,1 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fett 7,6 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kohlenhydrate 32 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Brühe aufkochen lassen, den Reis hineingeben und 15 min kochen. Er sollte dann noch etwas al dente sein. Den Reis abgießen und abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Man kann natürlich auch einen Rest vom Vortag nehmen. Dann aber später mit dem Salz nicht sparen. Der Reis sollte schon schön würzig sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Käse raspeln, die Möhren putzen und raspeln (ob man Käse und Möhren fein oder grob raspelt, bleibt dem eigenen Gusto überlassen). Die Zwiebeln fein würfeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Reis, Käse, Möhren, Zwiebeln und Eier miteinander verrühren. Pfeffer (ruhig reichlich), Salz und Kräuter einrühren. Nun Semmelbrösel einrühren, bis die Masse etwas Konsistenz hat. Dann ca. 15 min quellen lassen. Prüfen, ob die Masse unter Druck in den Händen zu einer Frikadelle geformt werden kann. Wenn ja, anschließend noch leicht in Semmelbröseln wälzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In reichlich Butterschmalz bei geringer Hitze vorsichtig von beiden Seiten goldbraun braten. Nach dem Braten auf Küchenkrepp das Fett abtropfen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebeln und Knoblauch schälen und fein würfeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2. Kichererbsen abgießen, abspülen und abtropfen lassen, Rosinen abspülen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="3. Wurzelgemüse schälen und würfeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="4. Koch-Rührelement und Rührhilfe einsetzen. Olivenöl in die Rührschüssel geben und Programm Eintopf wählen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="5. Hackfleisch nach und nach dazu bröseln, Zwiebeln, Knoblauch und Zucker zugeben und Temperatur auf 160 °C erhöhen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="6. Wurzelgemüse (Suppengrün), Zimt, Kreuzkümmel, Cayennepfeffer zugeben. Während die KCC läuft, mit Tomaten, Kichererbsen, Rosinen und Gemüsebrühe auffüllen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="7. Ende des Programms abwarten und gegebenenfalls mit Salz und Pfeffer abschmecken. Vor dem Servieren Zitronenabrieb zugeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Gefällt Dir dieses Rezept? Dann freuen wir uns auf Deine Bewertungs-Sternchen!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 175 °C - 195 °C vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zuerst die Schale von den 3 Zitronen abreiben, zwei Zitronen davon auspressen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dann Eier und Zucker schaumig rühren. Das Mehl sieben und mit Vanillezucker, Backpulver, Zitronenschale und Margarine nach und nach dazugeben. Alles gut mixen. Den Teig auf ein mit Backpapier ausgelegtes Backblech streichen. In den vorgeheizten Backofen schieben und ca. 20 Min. auf der mittleren Schiene backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nun aus dem Zitronensaft und dem Puderzucker nach und nach eine Glasur mischen - bitte sehr sparsam mit dem Zitronensaft umgehen, die Glasur muss schön dickflüssig sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Solange der Kuchen noch warm ist, mit einer Gabel überall einstechen. Somit wird er schön saftig, denn die Glasur kann so einsickern. Dann schnell die Glasur auf dem warmen Kuchen verstreichen und auskühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hähnchenbrustfilet waschen, mit Küchenpapier abtupfen und in mundgerechte Stücke schneiden. Das Olivenöl mit der roten Currypaste in einer beschichteten Pfanne erhitzen und das Hähnchenfleisch darin von allen Seiten knusprig braten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Währenddessen die Zucchini waschen und die Karotten schälen. Nun mit einem Sparschäler rundherum die Bandnudeln abschälen, bei den Zucchini möglichst das innere Kerngehäuse übrig lassen, die Karotten können komplett verwendet werden. Sollten die Scheiben zu breit werden, kann man das Gemüse mit einem Messer vor dem Abschälen längs einschneiden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das fertig gebratene Hähnchenfleisch herausnehmen und dabei möglichst den Bratsaft in der Pfanne lassen. Die Gemüsebandnudeln in Wasser und Brühe mit dem Bratsaft aufkochen und einige Minuten garen lassen. Derweil die Tomaten würfeln und zusammen mit dem Tomatenmark zum Gemüse geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zum Schluss den Ziegenfrischkäse und das Hähnchenfleisch zugeben und alles noch einmal unter Rühren erhitzen. Mit Salz und Pfeffer abschmecken und servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zucchini waschen und längs in fingerdicke Scheiben schneiden. In einer Pfanne in Olivenöl von beiden Seiten anbraten, danach auf Küchenpapier abtropfen lassen. Oder alternativ die Scheiben mit Olivenöl bestreichen, ein wenig salzen und auf der obersten Schiene mit der Grillfunktion im Backofen bräunen. Das dauert allerdings länger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel in Würfel schneiden und in der Pfanne in wenig Olivenöl glasig dünsten. Die Knoblauchzehe dazu pressen und etwas mitdünsten. Das Hackfleisch hinzugeben und krümelig braten. Wenn das Fleisch Farbe bekommen hat, mit Salz, Pfeffer und Paprikapulver würzen, 1 EL Tomatenmark hinzugeben, unterrühren und eine Minute mit anschwitzen. Die Tomaten hinzugeben und mit Oregano, Thymian, Salz, Pfeffer und Paprika würzen. 10 min auf kleiner Flamme köcheln lassen, zum Schluss die gehackte Petersilie hinzugeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Frischkäse mit der Milch verrühren, wahlweise auch Sauerrahm unterrühren. Mit Salz, Pfeffer und etwas Muskat würzen, ca. 50 g Streukäse unterrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine Lasagneform oder eine andere Auflaufform mit Zucchinischeiben auslegen. Darauf ein paar Löffel Tomaten-Hack-Soße verteilen, darauf eine Schicht Frischkäsesoße, und darauf wieder Zucchinischeiben. Weiter so schichten, bis alle Zutaten verbraucht sind. Die oberste Schicht soll Tomaten-Hack-Soße sein. Diese mit dem restlichen Käse bestreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zucchini-Lasagne im vorgeheizten Backofen bei 200 °C Ober-/Unterhitze in ca. 30 min goldbraun backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt ein kleiner frischer Salat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zucchini schälen und anschließend mit einem Schälmesser in Streifen schneiden - also wie Spaghetti bzw. Bandnudeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(90)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zucchini in etwas Olivenöl anbraten. Inzwischen die Tomaten klein schneiden und dazugeben. Dann das Mineralwasser hinzufügen (das sorgt dafür, dass die Zucchini weicher werden und sich einfach besser um die Gabel wickeln lassen). Tomatenmark und eine beliebige Menge Frischkäse dazugeben (ich empfehle: 2 TL). Salzen, pfeffern und die Kräuter hinzufügen. Eventuell noch würzen (z. B. mit Paprikapulver oder Gyrosgewürz). Noch ein wenig köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(90)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

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
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 °C Umluft vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Blätterteig auslegen und mit dem Frischkäse bestreichen. Den Räucherlachs gleichmäßig darauf verteilen. Mit etwas Dill bestreuen und zu einer Schnecke rollen. Mit einem sehr scharfen Messer in gleichmäßige dicke Scheiben (ca. 1 cm) schneiden, dann nebeneinander auf einem mit Backpapier ausgelegten Backblech verteilen und mit dem verquirlten Ei bestreichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im heißen Backofen auf mittlerer Schiene ca. 20 - 25 Minuten backen. Vor dem Servieren abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Anstatt Lachs, Frischkäse und Dill kann man auch geräucherten Schinken verwenden. Dieser ist jedoch etwas trockener und benötigt nur 15 - 20 Minuten im Backofen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Blätterteig ausrollen und eine Teighälfte mit gut der Hälfte des Schmands bestreichen. Die Hälfte der Schinkenwürfel und des Käses darauf verteilen. Die Seite des Blätterteiges, die nicht belegt ist, über die andere Seite klappen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wiederum die Hälfte des Teiges mit dem restlichen Schmand bestreichen und die Schinkenwürfel und Käseraspel darauf geben. Die unbestrichene Teighälfte darüber klappen. Den Blätterteig in Streifen schneiden. Vorsichtig spiralförmig drehen und auf ein mit Backpapier belegtes Blech legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im heißen Backofen bei 180 °C Ober-/Unterhitze ca. 25 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Variante: Sehr gut schmecken diese Stangen auch, wenn man statt Schinken geräucherten Lachs verwendet. Dafür braucht man dann ca. 180 g.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 180 °C Heißluft vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Blätterteig aus der Packung nehmen und in ca. 4 x 4 cm große Quadrate schneiden. Die Quadrate auf ein mit Backpapier belegtes Blech legen. Mit etwas Milch bestreichen. Tomatenscheiben darauflegen, dabei einen kleinen Rand freilassen und pfeffern.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In den vorgeheizten Backofen auf die mittlere Einschubleiste schieben und ca. 15 - 20 Min. backen, bis die Ränder leicht gebräunt sind.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit Knoblauchwürfelchen mit Olivenöl und Basilikum verrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die fertig gebackenen Quadrate anschließend mit Fleur de Sel bestreuen und mit der Knoblauch-Basilikumpaste bestreichen. Entweder sofort servieren oder auch kalt genießen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die TULIP Bacon-Scheiben in etwa 5 cm große Stückchen schneiden. In eine Pfanne legen und 2 Min. bei kräftiger Hitze braten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kartoffeln, Zwiebeln und Butter dazugeben und weitere 7 Min. bei mittlerer Hitze braten, bis alles knusprig und goldbraun ist. Mit Salz und Pfeffer abschmecken und das Gericht warmhalten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Währenddessen das Öl in der Pfanne erhitzen, Eier in die Pfanne schlagen und etwa 6 Min. braten. Anschließend mit Salz würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Gericht mit Parmesan und Thymian bestreuen und sofort mit den Spiegeleiern servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Als Beilage passen eingelegte Rote Beete dazu.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Butterschmalz in einer tiefen Pfanne erhitzen. Das Gulasch im Butterschmalz scharf anbraten und mit Salz, Pfeffer und Paprikapulver würzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wenn das Fleisch eine schöne Farbe angenommen hat und das Wasser verdampft ist, die gehackte Zwiebel, die gepresste Knoblauchzehe und die geriebene Karotte sowie den Senf und das Tomatenmark dazugeben und kurz weiterbraten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anschließend mit dem Bier ablöschen und einkochen lassen. Mit der Gemüsebrühe auffüllen und mit Deckel ca. 1 Stunde köcheln lassen (bei Verwendung eines Schnellkochtopfes ca. 35 min).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Etwa 5 min. vor Ende der Garzeit die Crème fraîche einrühren und nach Bedarf mit etwas Soßenbinder andicken. Vor dem Servieren nochmal abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Als Beilage passen Spätzle, Reis, Kartoffelbrei oder Salzkartoffeln")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die geschälte Zwiebel würfeln und in einem größeren Topf in Olivenöl leicht anrösten, Faschiertes dazugeben und krümelig braten. Die geschälten Kartoffeln in kleine Würfel schneiden, in den Topf geben und mit Brühe und Dosentomaten aufgießen - die Kartoffeln und später das Gemüse sollten immer leicht bedeckt sein - ansonsten Brühe nachfüllen. Gepressten Knoblauch, viel gemahlenen Pfeffer und Kräuter (z.B. getrockneten Majoran, Thymian, Oregano gemischt) dazugeben und leicht kochen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit zuerst die Karotten in dünne Scheibchen schneiden und nach ca. 15 Minuten in den Topf geben. Die Paprikaschote in kleine Würfel oder Steifen schneiden und den geputzten Porree (ich verwende gerne den vorgeputzten) in Scheiben schneiden und nach weiteren 10 Minuten dazugeben und noch ca. 10 Minuten köcheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Eintopf gut mit Kräutersalz abschmecken und mit Petersilie bestreut servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kochzeit richtet sich natürlich ein wenig nach der Größe der Kartoffel- und Gemüsestückchen und wie knackig man es mag.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Tipp: Wer möchte, ersetzt das eine oder andere Gemüse durch Mais, Erbsen oder Brokkoliröschen oder gibt zusätzlich etwas davon dazu und nimmt vom anderen Gemüse dafür weniger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die frischen Kartoffeln werden ausgiebig gewaschen und dann wird ausprobiert, auf welcher Seite sie am stabilsten liegen. Jetzt von oben ca. alle drei Millimeter bis fast ganz durch mit einem scharfen und feinen Messer einschneiden. Die Kartoffeln nun auf ein Backblech mit Backpapier legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Butter wird vorsichtig im Topf bei schwacher Hitze geschmolzen. Sie darf auf keinen Fall braun werden oder verbrennen. In die Butter werden nun der Knoblauch, der Rosmarin, das Meersalz, der Kreuzkümmel und der Cayennepfeffer gründlich untergerührt. Leicht warm (und flüssig) halten und 5 Minuten durchziehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 230 Grad (möglichst Umluft) vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Jetzt wird die Butter mit einem Teelöffel oder Backpinsel über die Kartoffeln gegeben. Nicht alles verwenden, weil die zweite Hälfte nach ca. 25 Minuten Backzeit nochmal über die Kartoffeln gegeben wird. Jetzt kommt das Blech mit den Kartoffeln auf der mittleren Position in den vorgeheizten Backofen. Nach der Hälfte der Garzeit nochmals mit der Buttermarinade übergießen oder bepinseln. Gesamtbackzeit ca. 50 Minuten. Bei größeren Kartoffeln die Backzeit ggf. verlängern.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In der Zwischenzeit wird der Quark mit der Sahne, den Kräutern gemäß Zutatenliste und der Schalotte verrührt und mit Salz und Pfeffer abgeschmeckt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Jetzt werden die Kartoffeln auf Tellern angerichtet und zur Deko noch mit ein wenig grobem Meersalz überstreut. Noch auf jeden Teller ein Klacks vom Kräuterquark geben - FERTIG.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebel abziehen und in kleine Würfel schneiden. Hackfleisch und Zwiebeln in erhitztem Öl ca. 5 Minuten anbraten, mit Senf und Ketchup verrühren, mit Salz und Pfeffer abschmecken und auskühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2. Tomaten waschen und vierteln, Gurken grob hacken. Pizzateig entrollen und in 12 Rechtecke schneiden (ca. 9 x 9 cm). Hackfleisch-Mischung, Cheddar, Tomaten und Gurken mittig auf den Teigstücken verteilen und Teig über der Füllung zusammenfalten. Teigränder gut zusammendrücken, sodass keine Öffnung mehr bleibt und mit der verschlossenen Seite nach unten in gefettete Mulden eines Muffinblechs legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="3. Muffins mit Milch bestreichen, mit Sesam bestreuen und im vorgeheizten Backofen bei 180 °C (Umluft: 160 °C) ca. 35 Minuten backen. Cheese-Burger-Muffins etwas abkühlen lassen, aus der Form lösen und lauwarm, nach Wunsch mit Burgersauce und Ketchup, servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Stück:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kJ/kcal: 917/220")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 10,9 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 16,8 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Öl im Wok erhitzen, Knoblauch und Ingwer kurz darin anbraten. Dann die Fleischstreifen in den Wok geben und kräftig anbraten. Nun alle übrigen Zutaten, bis auf die Lauchzwiebeln dazugeben und ca. 10 Minuten durchgaren. Achtung bei 4 TL Sambal Oelek wird es ganz schön scharf!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Evtl. nochmals mit Zucker, Zitronensaft und Sojasauce abschmecken, nun die Lauchzwiebeln unterrühren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Als Beilage eignet sich Reis, ein Gemüsecurry und Raita oder Karottensalat mit Ingwer.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In Indien haben wir zu diesem Gericht extra Limettenachtel zum Nachwürzen bekommen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 200 °C Ober-/Unterhitze (Umluft 180 °C) vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebel und den Knoblauch sehr fein schneiden. Die Chilischote entkernen und ebenso fein hacken. Die Kirschtomaten waschen und halbieren. Den Parmesan reiben und den Mozzarella grob würfeln. Die Basilikumblätter abzupfen, waschen und trocken tupfen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="In einem großen Topf Salzwasser zum Kochen bringen und die Nudeln darin laut Packungsangabe al dente garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Währenddessen in einer großen Pfanne Olivenöl erhitzen und Zwiebel, Knoblauch und Chilischote darin anschwitzen. Die passierten Tomaten hinzufügen und die Sauce ein paar Minuten leicht köcheln lassen. Dann die Sahne und den geriebenen Parmesan unterrühren und die Sauce mit Salz, Pfeffer und einer ordentlichen Prise Zucker abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Wenn die Nudeln soweit sind, diese abgießen und in die Pfanne zur Sauce geben. Die Pfanne von der Hitze nehmen und die halbierten Kirschtomaten und die Hälfte der Mozzarellawürfel unterheben. Die Basilikumblätter in Streifen schneiden und ebenfalls unterheben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Alles zusammen in eine Auflaufform geben, mit dem restlichen Mozzarella bestreuen und ca. 20 Minuten auf der mittleren Schiene im heißen Backofen gratinieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu passt zum Beispiel ein grüner Salat und Knoblauchbaguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Gratinform mit Butter einfetten. Den Knoblauch schälen. Entweder fein würfeln und in der Form verteilen oder direkt in die Form pressen. Die Kartoffeln schälen und in feine Scheiben schneiden (ich nehme dafür einen Gurkenhobel, das geht am schnellsten).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Hälfte der Kartoffelscheiben in die Form schichten. Mit Kräutersalz und frisch geriebenem Muskat leicht würzen, anschließend die restlichen Kartoffeln darauf schichten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Sahne und die Milch mischen. Mit dem Gemüsebrühepulver, Kräutersalz, Muskat und Pfeffer kräftig würzen. Diese Mischung über die Kartoffeln geben. Butterflöckchen auf dem Gratin verteilen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im vorgeheizten Backofen bei 180 °C Ober-/Unterhitze ca. 1 Stunde backen. Heiß servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Rindfleischwürfel im Butterschmalz 5 Minuten anbraten, dabei umrühren, dann die Zwiebeln und Knoblauchstücke dazugeben, weitere 5 Minuten mitdünsten. Mit Rinderbouillon und Rotwein ablöschen, mit Salz, Pfeffer, Zucker, Paprikapulver, Lorbeerblättern, Tomatenmark und Majoran würzen. Dann bei geschlossenem Deckel ca. 60 Minuten bei kleiner Hitze schmoren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(13)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffel-, Paprika und Karottenstücke zugeben und weitere ca. 20 Minuten köcheln lassen, bis das Gemüse gar ist. Dann Petersilie unterrühren und heiß servieren")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(13)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu schmeckt Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(13)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten für den Knetteig in eine Schüssel geben, rasch zusammenkneten und zur Seite stellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Füllung Margarine, Zucker, Vanillezucker, Puddingpulver und Eier in einer Schüssel verrühren. Dann den Quark und die saure Sahne untermischen. Die süße Sahne steif schlagen und unterheben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 180 °C Ober-/Unterhitze vorheizen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Knetteig in einer gefetteten 26er Springform auslegen, etwa 2 - 3 cm am Rand hochziehen. Nun die Füllung in die Form geben, glatt streichen und im heißen Backofen 1 Stunde backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Achtung: Den Kuchen erst nach dem völligen Erkalten aus der Form nehmen, da unmittelbar nach dem Herausnehmen aus dem Backofen die Konsistenz der Quarkmasse noch zu weich ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach unzähligen Feldversuchen, reichlich Google-Recherche und Restaurant-Spionage habe ich endlich ein Rezept entwickelt, das absolut authentisch und lecker schmeckt - eben wie in Bella Italia!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zunächst das Mehl mit dem Salz sieben und es in eine Teigrührmaschine oder einen Brotbackautomaten mit Teigfunktion füllen. Nun die Hefe in dem lauwarmen Wasser auflösen und anschließend zum Mehl-Salz-Gemisch geben (Anmerkung des Chefkoch.de Teams Rezeptbearbeitung: Die angegebene Hefemenge stimmt und es handelt sich um frische Hefe).")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anschließend die Zutaten in 20 (!) Minuten zu einem elastischen, homogenen Teig verkneten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Anmerkung: Eine elektrische Hilfe ist hier fast schon Pflicht, zur Not tut es auch ein Handrührgerät mit Knethaken. Bitte nicht verzweifelt mit der bloßen Hand kneten, der Teig erreicht so einfach nicht die gewünschte Weichheit und Konsistenz.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach dem Kneten den Teig mit einem feuchten Tuch abdecken und zwei Stunden ruhen lassen. Anschließend in vier Stücke zu je 200 g teilen, diese zu Kugeln formen und wieder abgedeckt weitere sechs Stunden gehen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Was ist nun das Besondere an diesem Teig-Rezept? Das Geheimnis liegt nicht in erlesenen Zutaten wie teurem Pizzamehl oder hochwertigem Olivenöl und auch nicht in überflüssigen Ingredienzen wie Bier, Zucker oder Eiern. Vielmehr erreicht man die geschmeidige Textur durch langes maschinelles Kneten! Die extrem geringe Menge Hefe sorgt zusammen mit der langen Gärung für einen äußerst aromatischen Teig.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Abschließend noch ein paar Tipps für weitere Verarbeitung:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Teig so dünn wie möglich ausrollen oder ziehen! Alles unter 4 mm ist ideal.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="8")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Tomatensoße einfach eine Dose Schältomaten mit (viel) Knoblauch, Salz, Pfeffer, etwas Zucker, Basilikum und Oregano kalt pürieren, nicht kochen. Anschließend mittig auf die Pizza auftragen und in kreisrunden Bewegungen mit der Kelle über die komplette Pizza verteilen. Nicht zu viel auftragen! Eine gute Pizza sollte man nicht in Tomatensoße ertränken. Wenn einzelne Teigbereiche keine Soße abbekommen, macht das überhaupt nichts. Lieber etwas weniger als etwas mehr.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="9")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf Höchststufe vorheizen! Meiner schafft knapp 260 °C, das Ergebnis war super. Den Teig auf das heiße Backblech legen (mit Backpapier ist das einfacher) und bereits nach 3 - 4 Minuten ist die Pizza fertig und kann genossen werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position="10")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Butterkekse zerbröseln, gut mit der flüssigen Butter vermischen und die Mischung auf den Boden einer Backform drücken. Bei 180 °C Ober-/Unterhitze im vorgeheizten Ofen 5 - 10 Minuten vorbacken, dann herausholen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Zucker mit Speisestärke, Frischkäse und Magerquark cremig rühren. Das Ei, die Sahne und den Zitronensaft dazugeben und alles glatt rühren. Nicht mit dem Rührgerät schlagen, sondern langsam cremig rühren, das ist ganz wichtig. Die Creme auf den vorgebackenen Boden streichen. Den Kuchen weitere ca. 45 Minuten backen. Wenn der Rand leicht braun ist, herausnehmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten für den Guss miteinander verrühren, den Guss auf den Kuchen streichen und den Kuchen nochmal 5 Minuten backen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Am besten über Nacht auskühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln in Salzwasser al dente kochen und abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(17)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die getrockneten Tomaten in Stücke schneiden, die Pinienkerne in einer trockenen Pfanne ohne Fett anrösten. Rucola und Basilikum waschen und etwas zerrupfen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(17)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Alle Zutaten miteinander mischen und den Salat mindestens 1 Stunde ziehen lassen. Vor dem Servieren nochmal abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(17)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Lasagneplatten zuerst die sechs Eier aufschlagen und verquirlen. Ein Backblech mit einem Backpapier auslegen, Eiermasse darauf geben und möglichst gleichmäßig verteilen. Das Blech in den heißen Ofen schieben und die Eier bei 80 bis 100 °C Ober-/Unterhitze stocken lassen. Immer wieder mal rein schauen und gerne die Masse zwischendurch wieder glatt auf dem gesamten Blech verteilen, damit eine gleichmäßige Platte entsteht.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Hackfleischfüllung inzwischen die Zwiebeln schälen und hacken, dann glasig anbraten. Das Hackfleisch hinzugeben. Das Fleisch mit etwas Salz und Pfeffer würzen und braten. Anschließend mit den gehackten oder frischen Tomaten und den passierten Tomaten ablöschen. Jetzt nach Belieben abschmecken und ziehen lassen. Ich nutze gerne Oregano, Basilikum, Thymian, eigentlich alles, was grün ist und vorhanden ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Für die Béchamelsauce ein wenig Öl heiß werden lassen und mit der Messerspitze Mehl vermengen. Mit der Sahne und ggf einem Schuss Wasser ablöschen und cremig rühren. Mit Salz, Pfeffer und Muskat würzen. Die Crème fraîche hinzugeben und zur Seite stellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nun die Eiermasse in Scheiben schneiden, die der genutzten Auflaufform entsprechen. Jetzt abwechselnd mit der Hackfleischsauce, Sauce Béchamel und Lasagneplatten in der Auflaufform stapeln. Die letzte Schicht sollte die Bechamel sein, welche dann mit Käse überstreut wird.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Alles dann so lange bei 180 °C Ober-/Unterhitze im heißen Ofen backen, bis der Käse goldbraun ist. Da alle Zutaten bereits gar sind, ist die Backzeit variabel, am besten schmeckt es mir so nach circa 20 Minuten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Filet trocken tupfen und in 8 Medaillons schneiden. Mit Senf bestreichen, mit Schinken umwickeln und in eine kleine Auflaufform legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="2. Champignons abtropfen lassen und in der Auflaufform zwischen den Medaillons verteilen. Mit Salz und Pfeffer würzen und Kräuter überstreuen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="3. Für die Sauce Sahne und Crème fraîche verrühren, mit Paprikapulver, Salz und Pfeffer würzen, über die Medaillons gießen und im vorgeheizten Backofen bei 200 °C (Gas: Stufe 4, Umluft 180 °C) ca. 30 Minuten garen. Spätzle nach Packungsanweisung zubereiten und zu dem Filet servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Pro Portion:")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="kJ/kcal: 2503/598")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="EW: 51,6 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="KH: 30,2 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position="7")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Schweinefilet die weiße Haut entfernen. Das Öl mit der Butter erhitzen, nicht zu heiß werden lassen. Das Fleisch mit Salz und Pfeffer würzen und ca. 10 Minuten von allen Seiten braten. Es soll innen noch rosa sein. Dann herausnehmen und auf einem Teller (damit der Fleischsaft aufgefangen wird) erkalten lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im Bratfett Zwiebeln, Knoblauch und Schinken gut bräunen. Die Champignons putzen und in Scheiben schneiden und mitbraten. Dann mit Brühe ablöschen und Sahne und Crème fraîche oder Schmand und den ausgetretenen Fleischsaft zugeben. Die Soße mit Salz, Pfeffer, Tomatenmark und Senf kräftig abschmecken. Sollte sie zu flüssig sein, etwas Speisestärke in wenig kaltem Wasser anrühren und unter Rühren zur kochenden Soße geben, bis zur gewünschten Konsistenz. Die Soße abkühlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das kalte Fleisch in 1 cm breite Scheiben schneiden und dann in Streifen. Dann in die Soße geben, die Petersilie dazu und durchrühren, kühl stellen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Am nächsten Tag das Gericht auf kleiner Flamme erhitzen, jedoch nicht mehr kochen. So bleibt das Fleisch rosa. Die Soße nochmals abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dazu schmeckt Baguette, aber auch Spätzle und Salat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="5")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sollte am Vortag zubereitet werden. Deshalb auch gut geeignet für Feste mit größerer Personenzahl.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position="6")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln schälen und zusammen mit dem Schinken würfeln. Mit dem Frischkäse mischen und mit etwas Salz und viel Pfeffer abschmecken. Man kann auch bei Bedarf noch ein wenig Kräuter der Provence dazugeben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position="1")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Diese Masse gut auf dem ausgebreiteten Blätterteig verteilen. Nun den Teig vorsichtig zusammenrollen und in ca. 3 cm dicke Scheiben schneiden. Die Scheiben auf ein mit Backpapier belegtes Backblech legen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position="2")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Ca. 10 Min bei 180 °C Umluft in den vorgeheizten Backofen schieben - je nach gewünschtem Bräunungsgrad länger oder kürzer.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position="3")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Bei uns gibt es diese kleinen Köstlichkeiten sonntags heiß oder kalt oft zum Brunch. Die Rollen lassen sich aber auch gut zu jeder Party mitnehmen. Den Belag kann man nach Geschmack auch jederzeit abwandeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position="4")
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

