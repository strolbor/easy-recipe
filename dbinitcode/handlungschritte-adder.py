#!/usr/bin/python
# -*- coding: ISO8859 -*-
from app import db
import sqlalchemy
from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags

handlungsschritt.query.delete()
AssociationRHhat.aiduery.delete()
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln und M�hren sch�len und in kleine St�cke schneiden. Die Paprikaschoten ebenfalls klein schneiden.  Das �l in einer Pfanne erhitzen und das Hackfleisch kr�melig braten. Mit den Dosentomaten, Tomatenmark und der Br�he abl�schen. Kartoffeln, M�hren und die Paprika hinzuf�gen. Alles zugedeckt ca. 40 min. bei mittlerer Hitze k�cheln lassen. Zum Reduzieren evtl. zus�tzlich ca. 10 min. ohne Deckel k�cheln lassen. Am Schluss mit den Gew�rzen abschmecken und den Schmand unterr�hren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 �C Umluft vorheizen.  Den Bl�tterteig auslegen und mit dem Frischk�se bestreichen. Den R�ucherlachs gleichm��ig darauf verteilen. Mit etwas Dill bestreuen und zu einer Schnecke rollen. Mit einem sehr scharfen Messer in gleichm��ige dicke Scheiben (ca. 1 cm) schneiden, dann nebeneinander auf einem mit Backpapier ausgelegten Backblech verteilen und mit dem verquirlten Ei bestreichen.  Im hei�en Backofen auf mittlerer Schiene ca. 20 - 25 Minuten backen. Vor dem Servieren abk�hlen lassen.  Tipp: Anstatt Lachs, Frischk�se und Dill kann man auch ger�ucherten Schinken verwenden. Dieser ist jedoch etwas trockener und ben�tigt nur 15 - 20 Minuten im Backofen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Bl�tterteig ausrollen und eine Teigh�lfte mit gut der H�lfte des Schmands bestreichen. Die H�lfte der Schinkenw�rfel und des K�ses darauf verteilen. Die Seite des Bl�tterteiges, die nicht belegt ist, �ber die andere Seite klappen.  Wiederum die H�lfte des Teiges mit dem restlichen Schmand bestreichen und die Schinkenw�rfel und K�seraspel darauf geben. Die unbestrichene Teigh�lfte dar�ber klappen. Den Bl�tterteig in Streifen schneiden. Vorsichtig spiralf�rmig drehen und auf ein mit Backpapier belegtes Blech legen.  Im hei�en Backofen bei 180 �C Ober-/Unterhitze ca. 25 Minuten backen.  Variante: Sehr gut schmecken diese Stangen auch, wenn man statt Schinken ger�ucherten Lachs verwendet. Daf�r braucht man dann ca. 180 g.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 180 �C Hei�luft vorheizen.  Den Bl�tterteig aus der Packung nehmen und in ca. 4 x 4 cm gro�e Quadrate schneiden. Die Quadrate auf ein mit Backpapier belegtes Blech legen. Mit etwas Milch bestreichen. Tomatenscheiben darauflegen, dabei einen kleinen Rand freilassen und pfeffern.  In den vorgeheizten Backofen auf die mittlere Einschubleiste schieben und ca. 15 - 20 Min. backen, bis die R�nder leicht gebr�unt sind.  In der Zwischenzeit Knoblauchw�rfelchen mit Oliven�l und Basilikum verr�hren.  Die fertig gebackenen Quadrate anschlie�end mit Fleur de Sel bestreuen und mit der Knoblauch-Basilikumpaste bestreichen. Entweder sofort servieren oder auch kalt genie�en.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die TULIP Bacon-Scheiben in etwa 5 cm gro�e St�ckchen schneiden. In eine Pfanne legen und 2 Min. bei kr�ftiger Hitze braten.  Kartoffeln, Zwiebeln und Butter dazugeben und weitere 7 Min. bei mittlerer Hitze braten, bis alles knusprig und goldbraun ist. Mit Salz und Pfeffer abschmecken und das Gericht warmhalten.  W�hrenddessen das �l in der Pfanne erhitzen, Eier in die Pfanne schlagen und etwa 6 Min. braten. Anschlie�end mit Salz w�rzen.  Das Gericht mit Parmesan und Thymian bestreuen und sofort mit den Spiegeleiern servieren.  Als Beilage passen eingelegte Rote Beete dazu.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Butterschmalz in einer tiefen Pfanne erhitzen. Das Gulasch im Butterschmalz scharf anbraten und mit Salz, Pfeffer und Paprikapulver w�rzen.  Wenn das Fleisch eine sch�ne Farbe angenommen hat und das Wasser verdampft ist, die gehackte Zwiebel, die gepresste Knoblauchzehe und die geriebene Karotte sowie den Senf und das Tomatenmark dazugeben und kurz weiterbraten.  Anschlie�end mit dem Bier abl�schen und einkochen lassen. Mit der Gem�sebr�he auff�llen und mit Deckel ca. 1 Stunde k�cheln lassen (bei Verwendung eines Schnellkochtopfes ca. 35 min).  Etwa 5 min. vor Ende der Garzeit die Cr�me fra�che einr�hren und nach Bedarf mit etwas So�enbinder andicken. Vor dem Servieren nochmal abschmecken.  Als Beilage passen Sp�tzle, Reis, Kartoffelbrei oder Salzkartoffeln")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gesch�lte Zwiebel w�rfeln und in einem gr��eren Topf in Oliven�l leicht anr�sten, Faschiertes dazugeben und kr�melig braten. Die gesch�lten Kartoffeln in kleine W�rfel schneiden, in den Topf geben und mit Br�he und Dosentomaten aufgie�en - die Kartoffeln und sp�ter das Gem�se sollten immer leicht bedeckt sein - ansonsten Br�he nachf�llen. Gepressten Knoblauch, viel gemahlenen Pfeffer und Kr�uter (z.B. getrockneten Majoran, Thymian, Oregano gemischt) dazugeben und leicht kochen lassen.  In der Zwischenzeit zuerst die Karotten in d�nne Scheibchen schneiden und nach ca. 15 Minuten in den Topf geben. Die Paprikaschote in kleine W�rfel oder Steifen schneiden und den geputzten Porree (ich verwende gerne den vorgeputzten) in Scheiben schneiden und nach weiteren 10 Minuten dazugeben und noch ca. 10 Minuten k�cheln lassen.  Den Eintopf gut mit Kr�utersalz abschmecken und mit Petersilie bestreut servieren.  Die Kochzeit richtet sich nat�rlich ein wenig nach der Gr��e der Kartoffel- und Gem�sest�ckchen und wie knackig man es mag.  Tipp: Wer m�chte, ersetzt das eine oder andere Gem�se durch Mais, Erbsen oder Brokkolir�schen oder gibt zus�tzlich etwas davon dazu und nimmt vom anderen Gem�se daf�r weniger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die frischen Kartoffeln werden ausgiebig gewaschen und dann wird ausprobiert, auf welcher Seite sie am stabilsten liegen. Jetzt von oben ca. alle drei Millimeter bis fast ganz durch mit einem scharfen und feinen Messer einschneiden. Die Kartoffeln nun auf ein Backblech mit Backpapier legen.  Die Butter wird vorsichtig im Topf bei schwacher Hitze geschmolzen. Sie darf auf keinen Fall braun werden oder verbrennen. In die Butter werden nun der Knoblauch, der Rosmarin, das Meersalz, der Kreuzk�mmel und der Cayennepfeffer gr�ndlich unterger�hrt. Leicht warm (und fl�ssig) halten und 5 Minuten durchziehen lassen.  Den Backofen auf 230 Grad (m�glichst Umluft) vorheizen.  Jetzt wird die Butter mit einem Teel�ffel oder Backpinsel �ber die Kartoffeln gegeben. Nicht alles verwenden, weil die zweite H�lfte nach ca. 25 Minuten Backzeit nochmal �ber die Kartoffeln gegeben wird. Jetzt kommt das Blech mit den Kartoffeln auf der mittleren Position in den vorgeheizten Backofen. Nach der H�lfte der Garzeit nochmals mit der Buttermarinade �bergie�en oder bepinseln. Gesamtbackzeit ca. 50 Minuten. Bei gr��eren Kartoffeln die Backzeit ggf. verl�ngern.  In der Zwischenzeit wird der Quark mit der Sahne, den Kr�utern gem�� Zutatenliste und der Schalotte verr�hrt und mit Salz und Pfeffer abgeschmeckt.  Jetzt werden die Kartoffeln auf Tellern angerichtet und zur Deko noch mit ein wenig grobem Meersalz �berstreut. Noch auf jeden Teller ein Klacks vom Kr�uterquark geben - FERTIG.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebel abziehen und in kleine W�rfel schneiden. Hackfleisch und Zwiebeln in erhitztem �l ca. 5 Minuten anbraten, mit Senf und Ketchup verr�hren, mit Salz und Pfeffer abschmecken und ausk�hlen lassen.  2. Tomaten waschen und vierteln, Gurken grob hacken. Pizzateig entrollen und in 12 Rechtecke schneiden (ca. 9 x 9 cm). Hackfleisch-Mischung, Cheddar, Tomaten und Gurken mittig auf den Teigst�cken verteilen und Teig �ber der F�llung zusammenfalten. Teigr�nder gut zusammendr�cken, sodass keine �ffnung mehr bleibt und mit der verschlossenen Seite nach unten in gefettete Mulden eines Muffinblechs legen.  3. Muffins mit Milch bestreichen, mit Sesam bestreuen und im vorgeheizten Backofen bei 180 �C (Umluft: 160 �C) ca. 35 Minuten backen. Cheese-Burger-Muffins etwas abk�hlen lassen, aus der Form l�sen und lauwarm, nach Wunsch mit Burgersauce und Ketchup, servieren.  Pro St�ck:  kJ/kcal: 917/220  EW: 10,9 g  F: 12,0 g  KH: 16,8 g  BE: 1,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="�l im Wok erhitzen, Knoblauch und Ingwer kurz darin anbraten. Dann die Fleischstreifen in den Wok geben und kr�ftig anbraten. Nun alle �brigen Zutaten, bis auf die Lauchzwiebeln dazugeben und ca. 10 Minuten durchgaren. Achtung bei 4 TL Sambal Oelek wird es ganz sch�n scharf!  Evtl. nochmals mit Zucker, Zitronensaft und Sojasauce abschmecken, nun die Lauchzwiebeln unterr�hren.  Als Beilage eignet sich Reis, ein Gem�securry und Raita oder Karottensalat mit Ingwer.  In Indien haben wir zu diesem Gericht extra Limettenachtel zum Nachw�rzen bekommen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 200 �C Ober-/Unterhitze (Umluft 180 �C) vorheizen.  Die Zwiebel und den Knoblauch sehr fein schneiden. Die Chilischote entkernen und ebenso fein hacken. Die Kirschtomaten waschen und halbieren. Den Parmesan reiben und den Mozzarella grob w�rfeln. Die Basilikumbl�tter abzupfen, waschen und trocken tupfen.  In einem gro�en Topf Salzwasser zum Kochen bringen und die Nudeln darin laut Packungsangabe al dente garen.  W�hrenddessen in einer gro�en Pfanne Oliven�l erhitzen und Zwiebel, Knoblauch und Chilischote darin anschwitzen. Die passierten Tomaten hinzuf�gen und die Sauce ein paar Minuten leicht k�cheln lassen. Dann die Sahne und den geriebenen Parmesan unterr�hren und die Sauce mit Salz, Pfeffer und einer ordentlichen Prise Zucker abschmecken.  Wenn die Nudeln soweit sind, diese abgie�en und in die Pfanne zur Sauce geben. Die Pfanne von der Hitze nehmen und die halbierten Kirschtomaten und die H�lfte der Mozzarellaw�rfel unterheben. Die Basilikumbl�tter in Streifen schneiden und ebenfalls unterheben.  Alles zusammen in eine Auflaufform geben, mit dem restlichen Mozzarella bestreuen und ca. 20 Minuten auf der mittleren Schiene im hei�en Backofen gratinieren.  Dazu passt zum Beispiel ein gr�ner Salat und Knoblauchbaguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Gratinform mit Butter einfetten. Den Knoblauch sch�len. Entweder fein w�rfeln und in der Form verteilen oder direkt in die Form pressen. Die Kartoffeln sch�len und in feine Scheiben schneiden (ich nehme daf�r einen Gurkenhobel, das geht am schnellsten).  Die H�lfte der Kartoffelscheiben in die Form schichten. Mit Kr�utersalz und frisch geriebenem Muskat leicht w�rzen, anschlie�end die restlichen Kartoffeln darauf schichten.  Die Sahne und die Milch mischen. Mit dem Gem�sebr�hepulver, Kr�utersalz, Muskat und Pfeffer kr�ftig w�rzen. Diese Mischung �ber die Kartoffeln geben. Butterfl�ckchen auf dem Gratin verteilen.  Im vorgeheizten Backofen bei 180 �C Ober-/Unterhitze ca. 1 Stunde backen. Hei� servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Rindfleischw�rfel im Butterschmalz 5 Minuten anbraten, dabei umr�hren, dann die Zwiebeln und Knoblauchst�cke dazugeben, weitere 5 Minuten mitd�nsten. Mit Rinderbouillon und Rotwein abl�schen, mit Salz, Pfeffer, Zucker, Paprikapulver, Lorbeerbl�ttern, Tomatenmark und Majoran w�rzen. Dann bei geschlossenem Deckel ca. 60 Minuten bei kleiner Hitze schmoren.  Die Kartoffel-, Paprika und Karottenst�cke zugeben und weitere ca. 20 Minuten k�cheln lassen, bis das Gem�se gar ist. Dann Petersilie unterr�hren und hei� servieren  Dazu schmeckt Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(13)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten f�r den Knetteig in eine Sch�ssel geben, rasch zusammenkneten und zur Seite stellen.  F�r die F�llung Margarine, Zucker, Vanillezucker, Puddingpulver und Eier in einer Sch�ssel verr�hren. Dann den Quark und die saure Sahne untermischen. Die s��e Sahne steif schlagen und unterheben.  Den Backofen auf 180 �C Ober-/Unterhitze vorheizen.  Den Knetteig in einer gefetteten 26er Springform auslegen, etwa 2 - 3 cm am Rand hochziehen. Nun die F�llung in die Form geben, glatt streichen und im hei�en Backofen 1 Stunde backen.  Achtung: Den Kuchen erst nach dem v�lligen Erkalten aus der Form nehmen, da unmittelbar nach dem Herausnehmen aus dem Backofen die Konsistenz der Quarkmasse noch zu weich ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach unz�hligen Feldversuchen, reichlich Google-Recherche und Restaurant-Spionage habe ich endlich ein Rezept entwickelt, das absolut authentisch und lecker schmeckt - eben wie in Bella Italia!  Zun�chst das Mehl mit dem Salz sieben und es in eine Teigr�hrmaschine oder einen Brotbackautomaten mit Teigfunktion f�llen. Nun die Hefe in dem lauwarmen Wasser aufl�sen und anschlie�end zum Mehl-Salz-Gemisch geben (Anmerkung des Chefkoch.de Teams Rezeptbearbeitung: Die angegebene Hefemenge stimmt und es handelt sich um frische Hefe).  Anschlie�end die Zutaten in 20 (!) Minuten zu einem elastischen, homogenen Teig verkneten.  Anmerkung: Eine elektrische Hilfe ist hier fast schon Pflicht, zur Not tut es auch ein Handr�hrger�t mit Knethaken. Bitte nicht verzweifelt mit der blo�en Hand kneten, der Teig erreicht so einfach nicht die gew�nschte Weichheit und Konsistenz.  Nach dem Kneten den Teig mit einem feuchten Tuch abdecken und zwei Stunden ruhen lassen. Anschlie�end in vier St�cke zu je 200 g teilen, diese zu Kugeln formen und wieder abgedeckt weitere sechs Stunden gehen lassen.  Was ist nun das Besondere an diesem Teig-Rezept? Das Geheimnis liegt nicht in erlesenen Zutaten wie teurem Pizzamehl oder hochwertigem Oliven�l und auch nicht in �berfl�ssigen Ingredienzen wie Bier, Zucker oder Eiern. Vielmehr erreicht man die geschmeidige Textur durch langes maschinelles Kneten! Die extrem geringe Menge Hefe sorgt zusammen mit der langen G�rung f�r einen �u�erst aromatischen Teig.  Abschlie�end noch ein paar Tipps f�r weitere Verarbeitung:  Den Teig so d�nn wie m�glich ausrollen oder ziehen! Alles unter 4 mm ist ideal.  F�r die Tomatenso�e einfach eine Dose Sch�ltomaten mit (viel) Knoblauch, Salz, Pfeffer, etwas Zucker, Basilikum und Oregano kalt p�rieren, nicht kochen. Anschlie�end mittig auf die Pizza auftragen und in kreisrunden Bewegungen mit der Kelle �ber die komplette Pizza verteilen. Nicht zu viel auftragen! Eine gute Pizza sollte man nicht in Tomatenso�e ertr�nken. Wenn einzelne Teigbereiche keine So�e abbekommen, macht das �berhaupt nichts. Lieber etwas weniger als etwas mehr.  Den Backofen auf H�chststufe vorheizen! Meiner schafft knapp 260 �C, das Ergebnis war super. Den Teig auf das hei�e Backblech legen (mit Backpapier ist das einfacher) und bereits nach 3 - 4 Minuten ist die Pizza fertig und kann genossen werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Butterkekse zerbr�seln, gut mit der fl�ssigen Butter vermischen und die Mischung auf den Boden einer Backform dr�cken. Bei 180 �C Ober-/Unterhitze im vorgeheizten Ofen 5 - 10 Minuten vorbacken, dann herausholen.  Den Zucker mit Speisest�rke, Frischk�se und Magerquark cremig r�hren. Das Ei, die Sahne und den Zitronensaft dazugeben und alles glatt r�hren. Nicht mit dem R�hrger�t schlagen, sondern langsam cremig r�hren, das ist ganz wichtig. Die Creme auf den vorgebackenen Boden streichen. Den Kuchen weitere ca. 45 Minuten backen. Wenn der Rand leicht braun ist, herausnehmen.  Die Zutaten f�r den Guss miteinander verr�hren, den Guss auf den Kuchen streichen und den Kuchen nochmal 5 Minuten backen.  Am besten �ber Nacht ausk�hlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln in Salzwasser al dente kochen und abk�hlen lassen.  Die getrockneten Tomaten in St�cke schneiden, die Pinienkerne in einer trockenen Pfanne ohne Fett anr�sten. Rucola und Basilikum waschen und etwas zerrupfen.  Alle Zutaten miteinander mischen und den Salat mindestens 1 Stunde ziehen lassen. Vor dem Servieren nochmal abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(17)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="F�r die Lasagneplatten zuerst die sechs Eier aufschlagen und verquirlen. Ein Backblech mit einem Backpapier auslegen, Eiermasse darauf geben und m�glichst gleichm��ig verteilen. Das Blech in den hei�en Ofen schieben und die Eier bei 80 bis 100 �C Ober-/Unterhitze stocken lassen. Immer wieder mal rein schauen und gerne die Masse zwischendurch wieder glatt auf dem gesamten Blech verteilen, damit eine gleichm��ige Platte entsteht.  F�r die Hackfleischf�llung inzwischen die Zwiebeln sch�len und hacken, dann glasig anbraten. Das Hackfleisch hinzugeben. Das Fleisch mit etwas Salz und Pfeffer w�rzen und braten. Anschlie�end mit den gehackten oder frischen Tomaten und den passierten Tomaten abl�schen. Jetzt nach Belieben abschmecken und ziehen lassen. Ich nutze gerne Oregano, Basilikum, Thymian, eigentlich alles, was gr�n ist und vorhanden ist.  F�r die B�chamelsauce ein wenig �l hei� werden lassen und mit der Messerspitze Mehl vermengen. Mit der Sahne und ggf einem Schuss Wasser abl�schen und cremig r�hren. Mit Salz, Pfeffer und Muskat w�rzen. Die Cr�me fra�che hinzugeben und zur Seite stellen.  Nun die Eiermasse in Scheiben schneiden, die der genutzten Auflaufform entsprechen. Jetzt abwechselnd mit der Hackfleischsauce, Sauce B�chamel und Lasagneplatten in der Auflaufform stapeln. Die letzte Schicht sollte die Bechamel sein, welche dann mit K�se �berstreut wird.  Alles dann so lange bei 180 �C Ober-/Unterhitze im hei�en Ofen backen, bis der K�se goldbraun ist. Da alle Zutaten bereits gar sind, ist die Backzeit variabel, am besten schmeckt es mir so nach circa 20 Minuten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Filet trocken tupfen und in 8 Medaillons schneiden. Mit Senf bestreichen, mit Schinken umwickeln und in eine kleine Auflaufform legen.  2. Champignons abtropfen lassen und in der Auflaufform zwischen den Medaillons verteilen. Mit Salz und Pfeffer w�rzen und Kr�uter �berstreuen.  3. F�r die Sauce Sahne und Cr�me fra�che verr�hren, mit Paprikapulver, Salz und Pfeffer w�rzen, �ber die Medaillons gie�en und im vorgeheizten Backofen bei 200 �C (Gas: Stufe 4, Umluft 180 �C) ca. 30 Minuten garen. Sp�tzle nach Packungsanweisung zubereiten und zu dem Filet servieren.  Pro Portion:  kJ/kcal: 2503/598  EW: 51,6 g  F: 29,3 g  KH: 30,2 g  BE: 2,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Schweinefilet die wei�e Haut entfernen. Das �l mit der Butter erhitzen, nicht zu hei� werden lassen. Das Fleisch mit Salz und Pfeffer w�rzen und ca. 10 Minuten von allen Seiten braten. Es soll innen noch rosa sein. Dann herausnehmen und auf einem Teller (damit der Fleischsaft aufgefangen wird) erkalten lassen.  Im Bratfett Zwiebeln, Knoblauch und Schinken gut br�unen. Die Champignons putzen und in Scheiben schneiden und mitbraten. Dann mit Br�he abl�schen und Sahne und Cr�me fra�che oder Schmand und den ausgetretenen Fleischsaft zugeben. Die So�e mit Salz, Pfeffer, Tomatenmark und Senf kr�ftig abschmecken. Sollte sie zu fl�ssig sein, etwas Speisest�rke in wenig kaltem Wasser anr�hren und unter R�hren zur kochenden So�e geben, bis zur gew�nschten Konsistenz. Die So�e abk�hlen lassen.  Das kalte Fleisch in 1 cm breite Scheiben schneiden und dann in Streifen. Dann in die So�e geben, die Petersilie dazu und durchr�hren, k�hl stellen.  Am n�chsten Tag das Gericht auf kleiner Flamme erhitzen, jedoch nicht mehr kochen. So bleibt das Fleisch rosa. Die So�e nochmals abschmecken.  Dazu schmeckt Baguette, aber auch Sp�tzle und Salat.  Tipp:  Sollte am Vortag zubereitet werden. Deshalb auch gut geeignet f�r Feste mit gr��erer Personenzahl.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln sch�len und zusammen mit dem Schinken w�rfeln. Mit dem Frischk�se mischen und mit etwas Salz und viel Pfeffer abschmecken. Man kann auch bei Bedarf noch ein wenig Kr�uter der Provence dazugeben.  Diese Masse gut auf dem ausgebreiteten Bl�tterteig verteilen. Nun den Teig vorsichtig zusammenrollen und in ca. 3 cm dicke Scheiben schneiden. Die Scheiben auf ein mit Backpapier belegtes Backblech legen.  Ca. 10 Min bei 180 �C Umluft in den vorgeheizten Backofen schieben - je nach gew�nschtem Br�unungsgrad l�nger oder k�rzer.  Bei uns gibt es diese kleinen K�stlichkeiten sonntags hei� oder kalt oft zum Brunch. Die Rollen lassen sich aber auch gut zu jeder Party mitnehmen. Den Belag kann man nach Geschmack auch jederzeit abwandeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Apfel sch�len, Kerngeh�use entfernen und mit Hilfe einer K�chenreibe grob raspeln. Bl�tterteig auspacken, mit Alsan/ Margarine bestreichen, Apfelraspel darauf verteilen, mit Zimt und Zucker bestreuen.  2. Hochkant aufwickeln. In 6 gleichgro�e St�cke schneiden. Mit einem Kochl�ffelstiel (oder �hnlichem) jedes St�ck mittig eindr�cken, sodass die Enden die typische Franzbr�tchen-Form bekommen.  3. Mit dem Backpapier auf ein Backblech geben und im vorgeheizten Backofen bei 200 �C Ober-/Unterhitze f�r 10 - 15 Minuten goldbraun backen.  N�hrwerte pro St�ck:  Energie kJ/kcal 1354/324  Eiwei� 2,3 g  Fett 13,3 g  Kohlenhydrate 47,2 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:  Spargel putzen, den wei�en Spargel ganz, bei dem gr�nen Spargel nur das untere Drittel sch�len und den Spargel in ca. 5 cm lange St�cke schneiden. 1,5 Liter Wasser mit 1 TL Salz, 1 Prise Zucker und Margarine aufkochen, Spargel dazugeben und ca. 10 Minuten garen. Gr�nen Spargel erst nach 5 Minuten Garzeit zuf�gen. Spargel abgie�en und dabei das Spargelwasser auffangen.  Backofen auf 180� C (Gas: Stufe 3, Umluft 160� C). vorheizen.  Mini-Kn�del nach Packungsanweisung ca. 8 Minuten garen. Schinken in Streifen schneiden.  F�r die So�e Margarine in einem Topf erhitzen, Mehl dazugeben und anschwitzen, Milch und 300 ml Spargelsud angie�en, aufkochen und mit Salz, Pfeffer und Muskat abschmecken. Fr�hlingszwiebeln putzen, waschen und in feine Ringe schneiden. Die H�lfte der Fr�hlingszwiebeln unter die So�e mischen.  Spargel, Kn�del und Schinken in eine Gratinform (24 x 28 cm) geben, So�e dar�ber gie�en, K�se �berstreuen und ca. 30-35 Minuten goldbraun backen Restliche Fr�hlingszwiebeln �ber das Gratin streuen und servieren.  Pro Portion:  kJ/kcal: 1500/358  EW: 19,9 g  F: 12,8 g  KH: 39,6 g  BE: 3,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 �C Ober-/Unterhitze vorheizen.  Ein Backblech mit Backpapier auslegen. Mit nicht zu wenig Oliven�l bestreichen. Die Kartoffeln in d�nne Scheiben gef�chert auf dem gefetteten Papier auslegen. Zwischen den Reihen etwas Platz lassen.  Gesch�lten Knoblauch waagerecht halbieren und wie den Rosmarin unter die Kartoffelscheiben legen. Salzen, pfeffern und die Kartoffelscheiben noch mal mit �l bestreichen.  Auf mittlerer H�he die Kartoffeln 35 min bei 200�C backen. Sie sollten leicht knusprig und leicht gebr�unt sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Gnocchi nach Packungsanweisung kochen.  Die Paprikaschote putzen und in einer K�chenmaschine p�rieren. Die Knoblauchzehe abziehen, pressen und in etwas Oliven�l anbraten. Das Paprikap�ree zuf�gen und kurz mitbraten. Die passierten Tomaten zugeben, dann den Frischk�se unterr�hren und aufkochen lassen. Mit Salz, Pfeffer, Oregano und Br�he abschmecken.  Eine Auflaufform einfetten und die Gnocchi darin verteilen, die Sauce dar�ber geben. Den Mozzarella in Scheiben schneiden, den Parmesan reiben und beides obendrauf verteilen.  Im vorgeheizten Backofen bei 180 �C ca. 15 Minuten �berbacken. Sofort servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Rezept stammt von einer Chinareise aus der Stadt Chongqing.  Zun�chst den Boden des Wok gro�z�gig mit �l bedecken und dieses auf h�chster Stufe erhitzen. Das Geschnetzelte rundherum mit Mehl best�uben und im Wok scharf anbraten, dann salzen. Das Fleisch herausnehmen, evtl. etwas �l nachgeben und die gehackten Erdn�sse leicht anbraten. Die Erdn�sse herausnehmen und die Zwiebeln anbraten. Anschlie�end den gehackten Knoblauch hinzugeben und ebenfalls anbraten. Die Fr�hlingszwiebeln und die Chilischoten in Streifen schneiden und hinzugeben. Den Zucker dar�ber streuen und karamellisieren lassen.  Fleisch und Erdn�sse wieder hinzugeben. Mit Wein abl�schen, aufkochen lassen und den Essig hinzugeben. Abschlie�end mit Sojasauce, Ingwer und Pfeffer (gut zerkleinern, sehr intensiv!) w�rzen und abschmecken.  Auf Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln in 0,5 cm gro�e W�rfel schneiden, Karotte und Sellerie w�rfeln. Alles in 2 EL Butterschmalz kr�ftig anbraten. Tomatenmark zugeben und and�nsten bis sich eine homogene Masse bildet, das Mark darf ruhig ein bisschen ansetzen. Paprikapulver kurz mitr�sten (Vorsicht, darf nicht verbrennen!). Mit dem Rotwein und der Br�he abl�schen und zum Kochen bringen. Jetzt erst das gew�rfelte Fleisch dazu geben, wieder aufkochen und bei kleiner Hitze mit den Lorbeerbl�ttern ca. 2 Stunden k�cheln lassen.  Durch das Gem�se ist es normalerweise nicht n�tig, die Sauce zu binden. Wenn sie allerdings zu fl�ssig ist, kann man das Gulasch mit 1 EL in kaltem Wasser aufgel�stem St�rkemehl andicken. Dann noch abschmecken mit Salz und Pfeffer. Die Lorbeerbl�tter fische ich nach M�glichkeit vor dem Servieren raus.  Dies ist ein Grundrezept f�r Gulasch, man kann es wunderbar abwandeln, indem man z. B. eine halbe Stunde vor Ende der Garzeit noch Sahne, Kartoffeln und/oder Paprikaschoten zugibt. Ich gebe auch immer noch Knoblauch dazu, den mochte aber meine Oma nicht.  Dazu schmecken Kn�del jeglicher Art, Kartoffeln oder Nudeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz und Pfeffer w�rzen. Evtl. noch Kr�uter wie Oregano, Thymian und/oder Basilikum und nach Geschmack Knoblauch dazugeben. Ca. 12 - 15 kleine B�llchen aus der Masse formen und in eine Auflaufform legen.  F�r die Tomatenso�e die st�ckigen Tomaten mit der Sahne, der Kr�utermischung, Tomatenmark und Zucker verr�hren, dann mit Salz und Pfeffer abschmecken. Alles �ber die Hackb�llchen geben. Den Mozzarella in Scheiben schneiden und dar�ber verteilen.  Im hei�en Backofen bei 175 �C Umluft ca. 30 - 40 min. garen. Aufpassen, dass der K�se nicht zu dunkel wird.  Dazu passt Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 180�C vorheizen.  Paprikaschoten halbieren, putzen, waschen und in St�cke schneiden. Zwiebeln abziehen und in feine Ringe schneiden. Sauerkraut abtropfen lassen und gut ausdr�cken.  Hackfleisch in erhitztem �l von allen Seiten anbraten. Paprika, Zwiebeln und Kartoffelnudeln hinzugeben, and�nsten und mit Sauerkraut in eine Auflaufform geben. Schmand mit Milch verr�hren, mit Salz und Pfeffer abschmecken, �ber die Zutaten gie�en, mit K�se bestreuen und im vorgeheizten Backofen ca. 20-30 Min. backen (Gas: Stufe 3, Umluft: 160�C).  Pro Portion:  kj/kcal: 3232/774  EW: 39,3 g  F: 47,0 g  KH: 45,0 g  BE: 3,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis nach Packungsanleitung kochen.  Das Fleisch h�uten, waschen und in spielw�rfelgro�e St�ckchen schneiden. Mit etwas �l in der Pfanne anbraten. Wenn es leicht Farbe bekommt, den Honig dazu geben. Fr�hlingszwiebeln und Knoblauch dazu, kurz mit anschwitzen. Die Ananas abtropfen lassen und den Saft auffangen, dann die Ananasst�cke mit in die Pfanne geben und auch kurz mit anschwitzen. Den Curry dazu geben und kurz alles durchr�sten.  Mit Sahne abl�schen. Den Schmelzk�se in St�ckchen dazu geben und schmelzen lassen. Alles aufkochen lassen, mit Salz, Pfeffer, Curry, Instantbr�he, etwas gemahlenem Chili und dem Ananassaft abschmecken und dann auf dem Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(30)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die H�hnchenbrust in St�cke schneiden. Aus 1 TL Paprikapulver, 1 EL Limonen- bzw. Zitronensaft, 1 TL Salz, 1 Becher Joghurt, 1 TL Cayennepfeffer, 1 EL Garam Masala Pulver, 1 St�ck Ingwer und 1 Knoblauchzehe eine Marinade herstellen. Das Fleisch mit der Marinade mischen.  Mindestens eine Stunde einziehen lassen. Besser ist es, das Fleisch bereits am Vortag zu marinieren und �ber Nacht in den K�hlschrank zu stellen.  Den Ofen auf 200 �C Ober-/Unterhitze vorheizen dann das Fleisch in einer Auflaufform f�r 25 Minuten garen.  Die Zwiebel klein hacken und in 2 EL Butter glasig anschwitzen. Die passierten Tomaten, den Zimt, 1 TL Salz, 2 TL Cayennepfeffer, 1 St�ck Ingwer und 1 Knoblauchzehe hinzugeben. Alles 20 Minuten mit Deckel und bei niedriger Temperatur k�cheln lassen. Gelegentlich umr�hren. Nun die restlichen 2 EL Butter, den Honig und die Sahne hinzuf�gen, weitere 3 Minuten k�cheln. Das Fleisch aus der Marinade nehmen, in die So�e geben, kurz umr�hren und 2 Minuten mitk�cheln lassen.  Dazu passt Reis oder Naan.  Wer gerne Koriandergr�n mag, der kann ganz am Ende noch ein paar frisch gehackte Bl�tter hinzuf�gen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das H�hnerfleisch in mundgerechte W�rfel schneiden, die Zwiebel klein hacken, die Knoblauchzehen fein hacken, die Kardamomkapseln zerdr�cken und mit den Nelken im M�rser klein mahlen.  Das �l in einem mittelgro�en Topf erhitzen, Zwiebeln und das Nelken-Kardamom-Gemisch darin and�nsten und glasig werden lassen. Jetzt H�hnerfleisch, Knoblauch und das Ingwerp�ree dazugeben und weitere 4 Minuten unter R�hren durchbraten. Die restlichen Gew�rze dazugeben, einige Minuten weiterr�hren und dabei das Ganze sehr gut durchmischen und durchkochen lassen. Tomatenp�ree, Mandelmehl, Br�he und Sahne nacheinander einr�hren, aufkochen und bei kleiner Flamme dann 15 - 20 Minuten k�cheln lassen, bis eine dick-cremige Konsistenz erreicht ist.  Dazu passen Reis oder Naan-Brot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(32)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln al dente kochen und erkalten lassen. Cocktailtomaten, getrocknete Tomaten und Oliven zerkleinern und mit den gekochten und erkalteten Nudeln mischen.  Aus den So�enzutaten eine Vinaigrette nach eigenem Geschmack herstellen und mit dem Salat vermengen. Dabei auf die Intensit�t des �ls aus dem Glas getrocknete Tomaten achten. Den Parmesan (am besten vom St�ck grob gehobelt) ebenfalls unter den Salat mengen.  Am besten 2 - 3 Stunden im K�hlschrank ziehen lassen. Nun evtl. nochmals nachw�rzen und wenn n�tig, das Verh�ltnis aus �l und Balsamico weiter verfeinern.  Den Rucola waschen, grob zerkleinern und erst vor dem Servieren mit dem Salat mischen. Zuletzt die Pinienkerne in der Pfanne kurz anr�sten und auf den bereits auf Tellern angerichteten Salat geben. Am besten mit frischem Ciabatta und einem leckeren Rotwein servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im lauwarmen Wasser und dem Oliven�l die Hefe mit dem Salz und Zucker aufl�sen. Dann das Mehl hinzuf�gen und einen glatten Teig kneten. Eine halbe Stunde an einem warmen Ort gehen lassen, zusammenkneten und abgedeckt im K�hlschrank 2 Tage ruhen lassen.  Nun kann man vom Teig eine herrlich frische Pizza herstellen.  Der Teig reicht f�r 6 runde Pizzen.  Anmerkungen: Belegen kann man diese nach Belieben, nat�rlich sollten die Tomatenso�e und der K�se nicht fehlen. Ich habe sie schon auf einem Blech sowie auf verschiedenen runden Pizzaformen gebacken. Sie wird immer supertoll und schmeckt original wie von meinem Lieblingsitaliener. Wenn man die Menge entsprechend reduzieren m�chte, ist das auch kein Problem. Die Menge der Hefe habe ich jedoch immer bei 40 g gelassen.  Am besten gelingt die Pizza, wenn man den Ofen sehr gut auf der h�chstm�glichen Temperatur vorheizt!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eier, Zucker, �l und Zimt mit dem Mixer verr�hren. Die Karotten und Mandeln hinzugeben. Mehl und Backpulver mischen, ebenfalls unterr�hren. Den Teig in eine gefettete 26er Springform f�llen, bei 180 �C Ober-/Unterhitze 40 - 50 Minuten backen. Man sollte eine St�bchenprobe machen und die Erfahrungswerte mit dem eigenen Backofen ber�cksichtigen.  F�r das Frosting Frischk�se und Zitronensaft mit dem Mixer auf niedriger Stufe glatt r�hren. Puderzucker und Vanillezucker einrieseln lassen.  Nach dem Backen den Kuchen abk�hlen lassen. Das Frosting mit der Streichpalette rundherum auftragen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(35)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln ungepellt und gewaschen ca. 15 min kochen. Sie sollen gar werden, aber nicht zu weich.  In der Zwischenzeit die Fr�hlingszwiebeln und den Schnittlauch waschen und in kleine St�cke schneiden. Die Fr�hlingszwiebeln zusammen mit dem Speck im Sonnenblumen�l ca. 5 min braten und mit Pfeffer w�rzen.  Den Backofen auf ca. 200 �C Ober/Unterhitze vorheizen. Das Speck-Fr�hlingszwiebel-Gemisch in einen tiefen Teller geben und die Cr�me fra�che und die H�lfte des Goudas hinzugeben. Mit etwas Salz und den Kr�utern der Provence w�rzen und gut mischen.  Die fertigen Kartoffeln abgie�en, in der Mitte l�ngs teilen und etwas abk�hlen lassen. Mit einem Teel�ffel mittelgro�e Mulden aush�hlen und die F�llung auf die H�lften verteilen. (Die F�llung darf gerne �ber die Mulden dr�ber gehen.)  Die Kartoffelh�lften auf ein Backblech auf Backfolie legen, sodass sie nicht umfallen. Den restlichen Gouda darauf verteilen. Auf der mittleren Schiene in 10 bis 15 min goldbraun �berbacken.  Die Kartoffeln aus dem Ofen nehmen und mit Schnittlauch bestreut servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz, Pfeffer, Tomatenmark, Ketchup, Oregano und einer halben klein gehackten Zwiebel vermengen. Die Hackfleischmasse dann in einer gro�en Pfanne mit etwas Oliven�l kr�melig braten und abk�hlen lassen.  Die Kritharaki (gibt es in jedem gut sortierten Supermarkt dort, wo auch Couscous und Bulgur zu finden sind) in Salzwasser ca. 14 Minuten garen und abgie�en.  Die Paprikaschoten sehr klein w�rfeln (Reiskorngr��e), die restliche halbe Zwiebel ebenfalls und in drei Beuteln Salatfix Gartenkr�uter mit etwas �l ziehen lassen.  Es m�ssen keine Fertigprodukte sein. Ein selbst gemachtes Kr�uterdressing auf Essigbasis tut es auch.  Die abgegossenen Nudeln mit den Hackfleischbr�seln vermengen. Dann die marinierten Paprikaw�rfel dazugeben. Alles vermengen und gut durchziehen lassen.  Der Salat schmeckt superlecker, frisch und ist schnell zuzubereiten. Auch rein optisch ein Hingucker, aufgrund der Reisnudeln. Wir essen den Salat - trotz des Fleischanteils - auch gern als Beilage zum Grillen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 175 �C Ober-/Unterhitze vorheizen.  Die Baguettes in den vorgeheizten Ofen legen und ca. 10 Minuten backen.  Derweil �l in einen gro�en Topf geben. Das Hackfleisch darin von allen Seiten gut anbraten und mit Salz und Pfeffer w�rzen. Den Lauch putzen, in kleine Ringe schneiden und zum Hackfleisch geben. Ca. 5 Minuten mit anbraten. Das Wasser zugie�en, Br�hw�rfel hineingeben und alles ca. 10 Minuten auf kleiner Flamme k�cheln lassen. Den Schmelzk�se einr�hren und schmelzen lassen. Cr�me fra�che untermengen und noch einmal kurz aufkochen lassen. Die Suppe mit Salz, Pfeffer, Muskat, Knoblauch- und Zwiebelpulver kr�ftig abschmecken.  Die Baguettes in Scheiben schneiden und zu der Suppe reichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="K�rbis, M�hren, Ingwer und Zwiebel sch�len und w�rfeln, in der Butter and�nsten. Mit der Br�he aufgie�en und in etwa 15 - 20 Minuten weich kochen. Dann sehr fein p�rieren, eventuell durch ein Sieb streichen. Die Kokosmilch unterr�hren, mit Salz, Pfeffer, Sojasauce und Zitronensaft abschmecken und noch mal erw�rmen. Mit Korianderbl�ttchen garniert servieren.  Eine schnelle, leicht exotische Suppe, sch�n im Men�. Ich benutze f�r diese Suppe immer einen Hokkaido, den muss man nicht sch�len. In Thailand isst man K�rbissuppe mit kleinen Garnelen als Einlage.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(39)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Rag� Bolognese:  In einem Topf das Oliven�l erhitzen, das Hackfleisch darin rundherum anbraten und die gehackten Zwiebeln und die gehackte Petersilie dazugeben. Knoblauch in feinen Scheiben und Tomatenmark dazu r�hren und mitbraten. Mit den Dosentomaten aufgie�en, salzen und pfeffern. Rotwein nach Belieben beif�gen. Das Rag� mindestens eine halbe Stunde lang bei ge�ffnetem Topf einkochen lassen.  B�chamelsauce:  Butter in einem kleinen Topf schmelzen und das Mehl mit dem Schneebesen unterr�hren und hellgelb anschwitzen. Die Milch dazugie�en und die Sauce glatt r�hren. Wer zu langsam ger�hrt hat und Kl�mpchen in der Sauce findet, kann die Sauce durch ein feines Haarsieb passieren und dann weiterkochen lassen. Die Sauce sollte fast eine halbe Stunde lang auf kleiner Flamme k�cheln, damit sie den Mehlgeschmack verliert. Mit Salz, Pfeffer und Zitronensaft sowie etwas Muskatnuss abschmecken.  Zubereitung der Lasagne:  In einer gebutterten, feuerfesten Form etwas Rag� Bolognese verteilen, eine Schicht Lasagneplatten darauf legen, die Nudelschicht wieder mit Rag� und dann mit einer Schicht B�chamel bedecken.  Anschlie�end wieder eine Schicht Nudeln, Rag� und B�chamel. So Schicht f�r Schicht die Form f�llen.  Die letzte Schicht sollte die B�chamelsauce bilden. Dick mit geriebenem K�se bestreuen und Butterfl�ckchen darauf setzen.  Die Lasagne im hei�en Backofen bei 180 �C Umluft ca. 30 - 40 Minuten backen, bis die Kruste goldbraun ist.  Tipp:  Die Lasagne kann man auch gut einen Tag vorher vorbereiten und im K�hlschrank ziehen lassen.  Als Vorspeise empfehle ich Honigmelone mit Parmaschinken und als Nachspeise einen Beerenmix an Quark-Joghurt-Sahne-Creme mit brauner Zuckerkruste.  Pro Portion 1122 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hackfleisch in einem gro�en Topf anbraten. Zwiebel und Knoblauch klein hacken und dazugeben. Karotten sch�len, in kleine Scheiben schneiden und zum Hackfleisch geben. Alles 5 Minuten unter gelegentlichem R�hren weiter braten. Tomatenmark hinzugeben und gut vermischen. Dann mit der Br�he abl�schen, aufkochen und bei geringer Hitze 40 Minuten zugedeckt k�cheln lassen.  Die Paprika in kleine Sticks schneiden und ca. 10 Minuten vor Ende der Kochzeit hinzuf�gen. Zum Schluss noch mit Salz und Pfeffer abschmecken.  Anrichten und auf jeden Teller einen Klecks Cr�me fra�che geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(41)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Gefl�gelfleisch, Champignons und Tomaten klein schneiden.  Das Fleisch in etwas �l anbraten und mit ein wenig Chiliflocken sowie Salz und Pfeffer w�rzen. Danach die Zwiebeln und Champignons dazugeben und 3 - 4 Minuten braten. Zum Schluss die restlichen Zutaten zugeben und umr�hren. Weitere 5 Minuten leicht k�cheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(42)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170 �C Ober-/Unterhitze vorheizen.  F�r den Boden Quark, Eier und 120 g K�se in einer Sch�ssel miteinander verr�hren und w�rzen. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im hei�en Ofen backen.  Das Backblech herausnehmen und den Boden beliebig belegen mit z. B. Tomatensauce, Salami, Schinken, Zucchini, Champignons oder Mais. Mit 60 g K�se bestreuen und erneut in den Ofen schieben, bis der K�se eine sch�ne Farbe hat.  Abk�hlen lassen, mit Rucola bestreuen und vorsichtig einrollen.  Eingerollt in Alufolie mehrere Tage im K�hlschrank haltbar.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170 �C Ober-/Unterhitze vorheizen.  F�r den Boden Quark, Eier und 80 g vom K�se in einer Sch�ssel miteinander verr�hren. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im Ofen backen.  Das Backblech herausnehmen, den Kuchenboden mit Cr�me fra�che bestreichen und mit Speckw�rfeln, Lauchzwiebeln und dem restlichen K�se bestreuen. Weitere 15 - 20 Minuten backen, bis der K�se eine sch�ne Farbe hat.  Kann als Flammkuchen oder als Rolle gegessen werden.  Der Flammkuchen hat ca. 6 g Kohlenhydrate.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Magerquark, Reibek�se und Eier zu einer dickfl�ssigen Masse verr�hren und auf einem mit Backpapier ausgelegten Backblech verteilen. Bei 180 �C Ober-/Unterhitze im hei�en Backofen ca. 20 Minuten backen. Den Teig ausk�hlen lassen.  Die Zutaten f�r die Sauce verr�hren.  Das Hackfleisch in einer Pfanne mit Salz und Pfeffer kr�melig anbraten. Die Gurken in Scheiben schneiden und zum Hackfleisch geben. 2/3 der Sauce auf dem gebackenen Teig verteilen. Das noch warme Hackfleisch dar�ber verteilen und den Toastk�se �ber dem Hackfleisch schmelzen lassen.  Anschlie�end Salat und evtl. Tomaten darauf legen und die restliche Sauce darauf verteilen. Den Teig mithilfe des Backpapiers einrollen, so dass die Big Mac Rolle aussieht wie eine Biskuitrolle.  Wichtig ist, nicht zu viel auf dem Teig zu verteilen, da die Rolle sonst zu dick wird und die F�llung an beiden Enden hervorquillt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="H�hnchenbrust s�ubern und in mundgerechte St�cke schneiden. In einer Pfanne mit etwas Pflanzenfett anbraten, bis das Fleisch sch�n knusprig ist. Mit etwas Salz, Pfeffer und Curry w�rzen.  In der Zwischenzeit Zucchini, Gurke und Tomaten klein schneiden. H�hnchen beiseitelegen und warm halten.  In der gleichen Pfanne Zwiebeln und Knoblauch anbraten. Zucchini dazugeben und d�nsten, bis diese weich aber noch bissfest sind. Gurke und Tomaten dazugeben und ca. 4 Minuten d�nsten. Evtl. einen Schuss Wasser dazugeben.  Frischk�se und Milch einr�hren. H�hnchenfleisch in die Pfanne geben und mit geschlossenem Deckel bei schwacher Hitze ca. 5 - 10 Minuten k�cheln lassen, bis die Sauce cremig wird. Mit Paprika abschmecken.  Tipp: Man kann auch eine rote Paprikaschote zusammen mit der Zucchini dazugeben.  Dazu passt sehr gut mein Erdbeer-Avocado-Salat: http://www.chefkoch.de/rezepte/2762181428080627/Erdbeer-Avocado-Salat.html")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Lachsfilet, falls TK, etwas antauen lassen. Waschen und trocken tupfen. Mit Salz und Pfeffer, nach Wunsch auch mit Kr�utern, w�rzen.  Schafsk�se in W�rfel schneiden. Die Zucchini und Pilze in d�nne Scheiben, die Paprika in Streifen schneiden. Tomaten halbieren oder vierteln. Knoblauch fein hacken. Das Gem�se mit Knoblauch, Salz und Pfeffer sowie ein paar Spritzern Chili�l in einer Sch�ssel vermengen.  Auf einem Backblech aus Alufolie* eine Sch�ssel formen, d.h. die R�nder an 4 Seiten hochschlagen. Ich empfehle 2 Schichten Alufolie zu nehmen, dann kann nichts auslaufen. Anschlie�end das Gem�se darauf verteilen. Dann den Lachs darauf legen, mit ein bisschen Chili-�l betr�ufeln und den Schafsk�se gro�z�gig dar�ber kr�meln.  Bei 180 �C Ober-/Unterhitze ca. 30 - 35 Minuten im hei�en Ofen garen.  *Anmerkung der Chefkoch.de Rezeptbearbeitung:  Wie auf vielen Bildern zu sehen ist, kann man auch eine Auflaufform verwenden. Das Gericht gelingt darin genau so gut.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Cashewkerne mit dem Currypulver in einer Pfanne bei schwacher Hitze 3 Minuten trocken r�sten. Den Ingwer sch�len und reiben, den Knoblauch in kleine St�cke schneiden.  Die Cashewkerne zusammen mit Ingwer, Knoblauch, Essig, Tomatenmark und Joghurt in einer K�chenmaschine oder im Mixer p�rieren. Die so entstandene Paste mit dem Fleisch in einer Sch�ssel vermischen und alles 24 Stunden im K�hlschrank durchziehen lassen.  In einer gro�en Pfanne oder einem gro�en Topf die Butter zerlassen. Zwiebel, Zimt, Salz und Kardamom bei mittlerer Hitze ca. 5 Minuten and�nsten, bis die Zwiebel weich ist. Das Fleisch mit der Marinade dazugeben und 10 Minuten kochen lassen. Die Chiliflocken, gehackte Tomaten aus der Dose und die Gem�sebr�he dazugeben und aufkochen lassen. Die Hitze reduzieren und ohne Deckel 40 - 45 Minuten k�cheln lassen. Kurz vor dem Servieren die Sahne unterr�hren und das Gericht mit dem gehackten Koriander bestreuen.  Dazu passt wunderbar Basmatireis oder Naanbrot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Teigzutaten verkneten und einen geschmeidigen, nicht mehr klebenden Teig herstellen. Zwei Muffinbackformen mit je 12 Muffinmulden fetten und den Teig in den Mulden verteilen, dabei jeweils auch einen kleinen Rand andr�cken.  Paprika und Lauch putzen und waschen, Zwiebel sch�len, alles fein hacken und in einer Pfanne mit etwas �l ca. 5 Minuten and�nsten. Die H�lfte des Gem�ses in eine Sch�ssel f�llen und abk�hlen lassen.  Getrocknete Tomaten abtropfen lassen, in kleine St�cke schneiden. Schinken w�rfeln. Die Tomaten zur einen, den Schinken zur anderen Gem�seh�lfte geben. So erh�lt man nachher 12 Miniquiches f�r Schinkenliebhaber und 12 f�r Vegetarier.  Die Gusszutaten miteinander verquirlen und jeweils wieder halb und halb mit dem Gem�se mischen.  Dieses dann auf den Teig in den Muffinmulden geben.  Im vorgeheizten Backofen bei 180 �C Ober-/Unterhitze ca. 20 - 25 Minuten backen.  Diese Mini-Quiches passen super zu einem kalten Bufett oder als Fingerfood auf einer Party.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fleisch waschen und trocken tupfen. Mit Salz und Pfeffer w�rzen. �l in einer Pfanne erhitzen. Filets darin von allen Seiten ca. 5 Min. kr�ftig anbraten.  Tomaten waschen und halbieren. Basilikumbl�tter abzupfen, waschen und fein hacken.  Sahne in einem Topf aufkochen lassen. Schmelzk�se hineinr�hren und schmelzen lassen. Mit Salz und Pfeffer w�rzen. 2/3 vom Basilikum unterr�hren.  Fleisch und Tomaten in eine gefettete Auflaufform geben. Sauce dar�ber gie�en. Mozzarella in kleine St�ckchen schneiden und auf dem Fleisch verteilen. Wer mag, kann noch geriebenen Parmesan und 1 EL Kr�uterbutter in kleine Fl�ckchen darauf verteilen.  Im vorgeheizten Ofen bei 200 �C Ober-/Unterhitze bzw. 175 �C Umluft ca. 30 Min. backen. Herausnehmen und mit restlichem Basilikum bestreuen.  Dazu schmecken Kroketten oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Platte (oder einen gro�en Teller) in den Backofen stellen und diesen mit 80 �C ca. eine halbe Stunde vorheizen. Temperatur wenn m�glich mit Backofenthermometer kontrollieren.  Schweinefilet 1 Stunde vor dem Anbraten aus dem K�hlschrank nehmen, damit das Fleisch auch im Kern Zimmertemperatur annimmt. Falls der Metzger es nicht schon vorher getan hat, das Fleisch parieren (d.h. von Sehnen, H�utchen, Fett etc. befreien). Hat man ein ganzes Schweinefilet, dann schl�gt man die Spitze soweit um, dass in etwa ein gleichm��ig dickes Fleischst�ck entsteht.  Filet salzen (nur wenig wegen des Speckmantels!) und pfeffern.  Baconscheiben �berlappt auslegen, in einer Breite, die der L�nge des Filetst�cks entspricht. Beide Enden des Filets je nach Dicke mit ein bis zwei (evtl. halbierten) Baconscheiben abdecken, das Filet auf die ausgelegten Scheiben legen und einrollen. Die Speckh�lle entweder mit K�chengarn oder (von mir aus Handhabungsgr�nden bevorzugt) mit Rouladennadeln fixieren.  In einem gro�en Schmortopf �l bzw. Butterschmalz erhitzen und das Filet in ca. 6 Minuten von allen Seiten braun/kross anbraten. Auch die beiden Kopfseiten sollten dabei angebraten werden, dabei das Filet mit Hilfe von einer K�chenzange oder gefaltetem K�chenpapier senkrecht halten. Anschlie�end das Fleisch mit einem Bratenthermometer versehen f�r ca. 2 Stunden in den vorgeheizten Backofen auf die Platte/den Teller legen und auf die gew�nschte Kerntemperatur bringen (ca. 60 �C f�r einen rosa Kern).  Den Bratensatz im Schmortopf entfetten und mit etwas Wei�wein oder Br�he l�sen, dann f�r den sp�teren Gebrauch beiseitestellen.  Eine halbe Stunde vor Garende des Fleisches die Zwiebeln sch�len und w�rfeln, Knoblauchzehen sch�len und in kleine Scheiben/W�rfel schneiden sowie die Pilze s�ubern und je nach Gr��e in 2, 4 oder 6 Teile schneiden.  In einer gro�en Pfanne die Butter zerlassen, den Schinkenspeck/Bacon anbraten, Zwiebeln und Knoblauch anschwitzen. Die Champignons und das Tomatenmark hinzuf�gen, etwas pfeffern und salzen und so lange braten, bis kaum noch Fl�ssigkeit �brig geblieben ist. W�hrenddessen Sahne, Cr�me fra�che, Br�he und Wein im Schmortopf mit dem gel�sten Bratensatz zusammen erhitzen. Gleichzeitig kann man auch schon das Wasser f�r die Sp�tzle aufsetzen.  Die gebratenen Champignons in den Schmortopf geben und ca. 5 Minuten leicht k�cheln lassen, dabei nach Belieben klein gehackte Kr�uter hinzuf�gen. Anschlie�end mit Worcesterso�e, Salz und Pfeffer abschmecken. Wem das Champignongem�se zu fl�ssig ist, kann gegebenenfalls noch mit Mehl/Mondamin andicken.  Die Sp�tzle nach Anweisung im Salzwasser mit 2 EL �l bissfest kochen, abgie�en und - wenn sie nicht direkt auf die vorgew�rmten Teller verteilt werden - kurz in etwas zerlassener Butter schwenken.  Das Fleisch aufschneiden (scharfes oder Elektromesser l�sst den krossen Schinkenspeck heil an den Fleischscheiben) und mit Champignongem�se und Sp�tzle servieren.  F�r Interessierte noch einige Tipps:  Es empfiehlt sich, die Essteller von vornherein mit der Fleischplatte mit vorzuw�rmen. Sie sind dann zwar relativ hei� (80 �C), das ist aber auch g�nstig, da beim NT-Garen das Fleisch naturgem�� nicht sehr hei� auf den Teller kommt und dann noch schneller ausk�hlen w�rde. Zwischendurch sollte man sie nicht in den Ofen zum Fleisch stellen, da das den NT-Garvorgang zu stark unterbricht.  Beim Anbraten der Filet-Enden hat sich bei mir das Halten des Filets mit K�chenpapier in der Hand durchgesetzt. Dazu faltet man ein Blatt K�chenpapier zweimal und achtet nur darauf, dass man sich nicht am hei�en Fett verbrennt bzw. das Papier das hei�e Fett aufsaugt. Man kann dann das Filet bequem ca. 30 sec. senkrecht halten, f�rs Anbraten des Endes. Das Problem bei der K�chenzange ist, dass man damit die Baconh�lle doch viel leichter verschiebt oder sogar zerst�rt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln kochen und mit kaltem Wasser abschrecken. Die Pinienkerne in einer Pfanne bei mittlerer Hitze ohne Fett leicht anbr�unen. Rucola gut waschen, trocken schleudern und etwas kleiner schneiden. Die getrockneten Tomaten gut abtropfen lassen und wie den Mozzarella und den Parmaschinken klein schneiden. Alles in eine gro�e Sch�ssel geben, salzen und pfeffern.  �l, Essig, klein gehackte oder gepresste Knoblauchzehe, Pesto, Senf und Honig miteinander vermischen und kurz vor dem Essen �ber den Salat geben. Alles noch einmal gut durchmischen und mit dem geriebenen Parmesan garnieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(52)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln im Salzwasser al dente kochen, abk�hlen lassen. In der Pfanne die gehackte Zwiebel mit dem Knoblauch anschwitzen, das Fleisch hinzu f�gen und gut anbraten. Die klein gew�rfelten Tomaten zuf�gen und mit Tomatenmark, den Gew�rzen, sch�n pikant abschmecken.  Nacheinander Nudeln, Joghurt sowie die Hackfleischmischung in die Sch�ssel f�llen und alles gut vermengen. Zum Schluss mit der klein gehackten Petersilie bestreuen, aber erst kurz vor dem Anrichten untermengen.  Den Salat im K�hlschrank gut durchk�hlen lassen. 1 Stunde vor dem Verzehr heraus nehmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(53)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln nach Packungsanweisung bissfest kochen.  In der Zwischenzeit die Tomaten klein schneiden und den Schafsk�se w�rfeln. Den Knoblauch abziehen, durchpressen oder winzig klein schneiden. Die Pinienkerne vorsichtig in einer Pfanne ohne Fett anr�sten (Vorsicht - sie werden schnell schwarz!). Die Basilikumbl�tter klein rei�en oder schneiden.  Die gekochten Nudeln abgie�en und nun alles zusammen in eine Sch�ssel geben. Nun das Oliven�l (die Menge ist gesch�tzt) dar�ber geben und mit Salz und Pfeffer abschmecken.  Tipp: Bei uns wird die erste Portion immer noch warm gegessen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Br�tchen in Wasser einweichen.  Die Zwiebel sch�len und in feine W�rfel schneiden. Wer m�chte, kann die Zwiebel auch kurz in Butter glasig d�nsten (ich bevorzuge die rohen Zwiebeln).  Das Ei, die Zwiebeln und die Gew�rze zur Hackmasse geben und sehr gut vermengen, entweder mit einem gro�en L�ffel oder mit den H�nden. Nicht mit dem Mixer arbeiten, dabei werden die Frikadellen oft z�h!  Die Br�tchenmasse sehr gut ausdr�cken, entweder mit den H�nden, oder auch zwischen zwei Brettchen, zur Hackmasse geben und wieder gut vermengen. Bis hierhin sollten diese Arbeitsschritte wenigstens 10 - 15 Minuten dauern, denn je ordentlicher vermengt und geknetet wird, umso besser und lockerer das Ergebnis!  Wer die rohe Masse abschmecken kann, sollte das jetzt tun, oder eine Probe braten. Jetzt gleichm��ige, nicht zu kleine B�llchen/Kl��e/Klopse formen und auf einer bemehlten Arbeitsfl�che flachdr�cken und gl�tten. Wer m�chte, kann sie in Mehl oder Semmelbr�sel wenden. Oma und ich braten sie ohne alles.  Eine schwere Pfanne mit guter Margarine stark erhitzen und die Frikadellen einlegen, kurz auf beiden Seiten scharf anbraten und dann ca. 15 - 20 Minuten (1 - 2-mal vorsichtig wenden) auf mittlerer/schwacher Hitze fertig braten. Nicht zu viele Frikadellen auf einmal in einer Pfanne braten, eher eine zweite benutzen oder nacheinander braten.  Dazu passt z. B. Kartoffelsalat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln w�rfeln und mit dem Hackfleisch in Oliven�l anbraten. Die Paprikaschoten ebenfalls w�rfeln und mit den Champignons sowie dem Mais zum Hackfleisch geben. Alles kurz anbraten, anschlie�end mit der Gem�sebr�he abl�schen. Die Sahne, die Tomatensauce und den Sahneschmelzk�se hinzugeben und ca. 10 Minuten k�cheln lassen. Zum Schluss mit Salz, Pfeffer und Oregano abschmecken.  Beim Servieren nach Belieben etwas geriebenen Parmesan auf die Suppe streuen.  Dazu passt am besten Baguette.  Tipp: Schmeckt auch als Nudelsauce gut, dann weniger Gem�sebr�he verwenden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis in der Gem�sebr�he garen (eine Tasse mit ca. 200 - 250 ml Inhalt als Ma� nehmen).  Die Chilischote l�ngs halbieren, von den Kernen befreien und hacken. Die Paprikaschoten putzen und w�rfeln. Die Zwiebeln fein w�rfeln und in einer Pfanne in etwas �l glasig d�nsten. Den gepressten Knoblauch, die Chilischote und das Tomatenmark hinzugeben und kurz mit anschwitzen. Die Paprikaw�rfel in die Pfanne geben und ein paar Minuten lang anbraten, dabei ab und zu die Pfanne schwenken. Mit Paprikapulver, Salz und Pfeffer w�rzen. Den Reis hinzugeben, untermengen und hei� werden lassen. Die Kr�uter hacken und zuletzt untermischen. Nochmals abschmecken.  Joghurt und gepressten Knoblauch verr�hren, mit Salz und Pfeffer abschmecken. Den Reis mit einem Klecks von der Joghurtsauce servieren.  Von der Menge werden ca. 3 - 4 Personen satt. Der Reis kann auch als Beilage gegessen werden.  Die Kr�utermenge kann nach Belieben erh�ht werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die H�hnchenfilets waschen und mit K�chenkrepp trocken tupfen. Mit Salz und Paprikapulver w�rzen und in einer Auflaufform dicht aneinanderlegen. Die Paprikaschoten waschen, entkernen, in schmale Streifen schneiden und auf den Filets verteilen.  Die Zwiebel in halbe Ringe schneiden und in einer Pfanne in etwas �l and�nsten. Die Chilischote hineinzupfen, den Knoblauch pressen und hinzugeben. Paprikapulver und Tomatenmark hinzuf�gen, mit der Br�he abl�schen und kurz aufkochen lassen. Anschlie�end Sahne und Schmand unter die So�e r�hren und mit Salz abschmecken. Die So�e in die Auflaufform gie�en, Fleisch und Paprikastreifen sollten ganz bedeckt sein. Den geriebenen K�se gleichm��ig darauf verteilen.  Im vorgeheizten Backofen bei 180 �C Ober-/Unterhitze ca. 1/2 Std. garen.  Beilagen: Bandnudeln oder Reis und Eisbergsalat mit Mandarinen und s��-saurer Vinaigrette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln in Spalten schneiden und in einer Sch�ssel mit Parmesan und Oliven�l vermischen. Die Gew�rze in einer separaten Sch�ssel vermengen und dann zu den Kartoffeln geben. Noch einmal kr�ftig durchmischen, die Kartoffelecken dann auf einem mit Backpapier ausgelegten Backblech verteilen und bei 200 �C Ober-/Unterhitze f�r ca. 40 Minuten backen.  Hinweis: Hei�hunger auf eine deftige Beilage oder einfach nur Appetit auf einen leckeren Snack? Diese Kartoffelecken sind genau das richtige f�r alle, die es gerne deftig m�gen und etwas Neues ausprobieren wollen. Dazu schmeckt Sour Cream mit ein paar frischen Kr�utern wirklich k�stlich, alternativ k�nnt ihr die Wedges nat�rlich auch als Beilage zu einem leckeren Steak oder gebratenem Fisch servieren. Eurer Kreativit�t sind keine Grenzen gesetzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(59)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vorbereitende Schritte:  Die Butter w�rfeln und bei Raumtemperatur weich werden lassen.  Gr�nes und rotes Pesto separat durch ein Sieb streichen und so etwas �l entfernen.  Mozzarella in St�cke rei�en.  Sonnengetrocknete Tomaten abtropfen lassen und fein hacken.  Die Oliven abtropfen lassen und grob hacken.  Erste Arbeitsschritte:  Zwei gro�e Backbleche mit Backpapier auslegen.  Die gr��ere R�hrsch�ssel einsetzen.  Den Spiral-Knethaken anbringen.  Schritt 1:  Die erste Zutat der Zutatenliste 1 (Milch) in einem kleinen Topf bei mittlerer Hitze erw�rmen.  Vom Herd nehmen und in eine Karaffe gie�en.  Die n�chsten vier Zutaten der Zutatenliste 1 (Mehl, Hefe, Zucker, Salz) in die R�hrsch�ssel geben. Den Spritzschutz anbringen.  20 Sekunden bei Geschwindigkeitsstufe 1 gut verr�hren.  W�hrend die K�chenmaschine langsam r�hrt, bei Geschwindigkeitsstufe 1 die warme Milch langsam dazugie�en.  Die n�chsten zwei Zutaten der Zutatenliste 1 (Ei, Eigelb) hineingeben.  2 Minuten bei Geschwindigkeitsstufe 1 r�hren.  Nach und nach bei Geschwindigkeitsstufe 1 die letzte Zutat der Zutatenliste 1 (Butter) in die R�hrsch�ssel geben.  6 bis 8 Minuten bei Geschwindigkeitsstufe 1 zu einem glatten und homogenen Teig r�hren.  Die R�hrsch�ssel aus der K�chenmaschine herausnehmen, mit Klarsichtfolie abdecken und an einem warmen Ort 1 Stunde gehen lassen.  Schritt 2:  Den Teig auf eine leicht bemehlte Arbeitsfl�che legen und flach dr�cken. Den Teig in 12 Portionen (je ca. 76 Gramm) teilen. Jedes Teigst�ck zu einem festen Teigball formen.  F�r die Pesto-Babki:  Sechs Teigb�lle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.  Die Zutaten der Zutatenliste 2 (Pesto, Mozzarella, schwarzer Pfeffer) �ber die Teigst�cke geben. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigst�cke vom langen Ende her zu einer Schlange fest aufrollen. Alle N�hte und Enden zusammendr�cken. Mit einem scharfen Messer die Teigschlangen der L�nge nach halbieren. Die beiden halbierten Teigschlangen mit der gef�llten Seite nach oben zu einem Zopf flechten.  Den Hefezopf langziehen (25 cm). Beide Enden zusammenf�hren, sodass sie sich �berlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendr�cken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.  Schritt 3:  Die kleinere R�hrsch�ssel einsetzen und den K-Haken anbringen.  Die Zutaten der Zutatenliste 3 (Pesto, Peperoni, sonnengetrocknete Tomaten, Oliven, Mozzarella, Oregano, schwarzen Pfeffer) in die R�hrsch�ssel geben. Geschwindigkeitsstufe 1 einstellen, 20 Sekunden r�hren und in dieser Zeit auf Geschwindigkeitsstufe 3 erh�hen, um die Zutaten zu einer Paste zu r�hren.  F�r die Pizza-Babki:  Die letzten sechs Teigb�lle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.  Die Paste gleichm��ig �ber die Teigst�cke verteilen. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigst�cke vom langen Ende her zu einer Schlange fest aufrollen. Alle N�hte und Enden zusammendr�cken. Mit einem scharfen Messer die Teigschlangen der L�nge nach halbieren. Die beiden halbierten Teigschlangen mit der gef�llten Seite nach oben zu einem Zopf flechten.  Den Hefezopf langziehen (25 cm). Beide Enden zusammenf�hren, sodass sie sich �berlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendr�cken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.  Schritt 4:  Den Backofen auf 190 �C Ober-/Unterhitze vorheizen.  Die Klarsichtfolie entfernen. Babki mit verquirltem Ei (Eistreiche) bestreichen.  Im Backofen 12 bis 15 Minuten goldbraun backen.  Warm servieren.  Die herzhaften Babki schmecken nicht nur k�stlich, sondern sind auch ein echter Hingucker auf dem Esstisch.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 170 �C Ober-/Unterhitze vorheizen.  Die TULIP Bacon-Scheiben auf ein mit Backpapier ausgelegtes Backblech legen.  Die Barbecuesauce mit braunem Zucker und Paprikapulver mischen. Die TULIP Bacon-Scheiben mit der Mischung gleichm��ig glasieren und im Ofen etwa 25 Min. auf der mittleren Einschubleiste kross backen. Anschlie�end auf K�chenpapier geben und 3 Min. ruhen lassen.  Mehl, Milch, Zucker, Eier, Butter und Salz zu einem glatten und dicken Pfannkuchenteig verr�hren.  Die Pfannkuchen in einer hei�en beschichteten Pfanne (Gr��e nach Belieben) bei mittlerer Hitze von beiden Seiten goldbraun backen.  Serviervorschlag: Pfannkuchen mit Frischk�se, Ahornsirup und den knusprigen, glasierten Baconstreifen servieren. Nach Belieben mit frischen Johannisbeeren dekorieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das H�hnerfleisch in kleine St�cke schneiden und im Topf kurz anbraten. Die Fr�hlingszwiebeln in Ringe schneiden und den Ingwer in kleine St�cke. Beides zuf�gen und kurz mitbraten.  Mit der H�hnerbr�he abl�schen. Kokosmilch, Sojasauce und Currypaste hinzuf�gen. Das Zitronengras l�ngs kreuzweise einschneiden, sodass es noch am St�ck bleibt, dann kann man es sp�ter einfacher wieder entnehmen, und in die Suppe geben.  5 Minuten kochen, das restliche Gem�se und die Gew�rze hinzuf�gen. Die Nudeln nach Packungsangabe kochen und hinzuf�gen.  Wer mag, kann noch ein wenig frischen Koriander aufheben und am Schluss �ber die Suppe streuen. Ich habe ab und zu noch getrocknete Chilif�den zum Garnieren verwendet.  Anmerkung der Redaktion:  Viki r�stet die Currypaste bereits zusammen mit Ingwer, Chili und etwas Speise�l an, dadurch wird der Geschmack intensiver. Anstatt Fr�hlingszwiebeln k�nnt ihr auch Schalotten oder Zwiebeln verwenden. Sie gibt die Paprikastreifen etwas fr�her, als die Pilze und die Nudeln in die Suppe, damit sie sch�n gar werden und so besser zu verdauen sind. Viki gibt zum Verfeinern noch zwei Prisen Zucker in die Suppe. Zum Anrichten drapiert Viki zun�chst ein paar Nudeln und etwas Gem�se in einen tiefen Teller, bevor sie ihn mit Suppe aufgie�t. Zum Schluss garniert sie die Suppe mit frischem Koriander und etwas Minze.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mehl, Quark, Backpulver, Milch, �l, Salz und Zucker gut verkneten. Die �brigen Zutaten zum Teig geben. Noch mal durchkneten und kleine B�llchen formen. Auf ein Backblech mit Backpapier legen.  F�r 30 - 40 Min. bei 180 �C Ober-/Unterhitze in den hei�en Ofen geben.  Tipp: F�r Feiern mache ich mindestens die doppelte Menge, kamen dort immer sehr gut an. Die Geschmackszutaten (R�stzwiebeln, Schinken, K�se) sind variabel, auf den K�se w�rde ich aber nicht verzichten!  Beim Backen muss man hin und wieder gucken, sie werden je nach Herd von unten auch sehr schnell dunkel, aber zu hell sollten sie auch nicht sein. Vorsicht, wenn sie noch warm sind, werden sie gerne stibitzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Teig reicht f�r 3 oder 4 runde Pizzen oder ein Blech.  Alle Zutaten in eine Sch�ssel geben und mindestens 5 Min. gut durchkneten. Den Teig ca. 30 Min. gehen lassen. Anschlie�end in 3 - 4 Portionen teilen, die jeweils zu Kugeln geformt werden.  Nun kann es losgehen mit dem Auswellen und Belegen.  Der Teig ist f�r jegliche Weiterverarbeitung geeignet - ob im Backofen (220�C, ca. 15 - 20 Min.), auf einem Pizzastein (250�C, ca. 10 - 15 Min.) oder in einer Elektropfanne (Stufe 3, erste Seite 3 Min., dann wenden, belegen und noch einmal 3 Min. von der anderen Seite). Sofort servieren.  Ich habe das Rezept von einer italienischen Freundin.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="F�r die Sauce das Oliven�l in einem Topf erhitzen. Das Hackfleisch hineingeben und unter R�hren so lange braten, bis es braun und kr�melig ist. 1 EL Tomatenmark unterr�hren und kurz anr�sten. Mit der Gem�sebr�he abl�schen, die Sahne hinzuf�gen und aufkochen lassen. Das restliche Tomatenmark unterr�hren und die Sauce mindestens 30 Minuten k�cheln lassen. Danach die Butter darin zerlassen und die Sauce mit Salz, Cayennepfeffer und Parmesan abschmecken.  Die Rigatoni nach Packungsanweisung in reichlich Salzwasser sehr bissfest kochen, dabei gelegentlich umr�hren. In ein Sieb abgie�en und abtropfen lassen, dann wieder in den Topf geben.  Den Schinken in 1/2 bis 1 cm breite Streifen schneiden. Die Sauce zu den Rigatoni geben und alles erhitzen. Die Schinkenstreifen unterr�hren und nur kurz darin erw�rmen.  Den Backofen auf 180 �C vorheizen. Die Nudelmischung in eine gro�e Auflaufform geben oder auf vier kleine ofenfeste Formen gleichm��ig verteilen. Den geriebenen Edamer dar�ber streuen. Auf der mittleren Schiene �berbacken, bis der K�se goldgelb ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Rinderrouladen aufrollen, waschen und mit K�chenkrepp trockentupfen. Zwiebeln in Halbmonde, Gurken in L�ngsstreifen schneiden. Schere und K�chengarn bereitstellen.  Die ausgebreiteten Rouladen d�nn mit Senf bestreichen, salzen und pfeffern. Auf jede Roulade mittig in der L�nge ca. 1/2 Zwiebel und 1 1/2 Scheiben Fr�hst�cksspeck sowie 1/2 (evtl. mehr) Gurke verteilen. Nun von beiden L�ngsseiten etwas einschlagen, dann aufrollen und mit dem K�chengarn wie ein Postpaket verschn�ren.  In einer Pfanne das Butterschmalz hei� werden lassen und die Rouladen dann rundherum darin anbraten. Herausnehmen und in einen Schmortopf umf�llen.  Den Sellerie, die restliche Zwiebel, Lauch und die M�hren kleinschneiden und in der Pfanne anbraten. Sobald sie halbwegs blond sind, kurz r�hren. Eine sehr d�nne Schicht vom Rotwein angie�en, nicht mehr r�hren und die Fl�ssigkeit verdampfen lassen. Sobald das Gem�se dann wieder trockenbr�t, wieder eine Schicht Wein angie�en, kurz r�hren und weiter verdampfen lassen. Dies wiederholen, bis die 1/2 Flasche Wein aufgebraucht ist. Auf diese Art wird das R�stgem�se sehr braun (gut f�r den Geschmack und die Farbe der So�e), aber nicht trocken. Am Schluss mit dem Rinderfond, etwas Salz und Pfeffer und einem guten Schuss Gurkensud auff�llen und dann in den Schmortopf zu den Rouladen geben. Den Topf entweder auf kleiner Flamme oder bei ca. 160 �C Ober-/Unterhitze im hei�en Backofen f�r 1 1/2 Stunden schmoren lassen. Ab und zu evtl. etwas Fl�ssigkeit zugie�en.  Nach 1 1/2 Stunden testen, ob die Rouladen weich sind (einfach mal mit den Kochl�ffel ein bisschen draufdr�cken, sie sollten sich willig eindr�cken lassen - wenn nicht, nochmal eine halbe Stunde weiterschmoren). Dann vorsichtig aus dem Topf heben, warmstellen.  Die So�e durch ein Sieb geben, aufkochen. Ca. 1 EL Senf mit etwas Wasser und der Speisest�rke gut verr�hren, in die kochende So�e nach und nach unter R�hren eingie�en, bis die gew�nschte Konsistenz erreicht ist. Die So�e evtl. nochmal mit Salz, Pfeffer, Rotwein, Gurkensud abschmecken.  Pro Portion 830 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln sch�len und in feine W�rfel schneiden. Im Sonnenblumen�l glasig anschwitzen. Rote Linsen, Tomaten mit Saft und Kokosmilch hinzuf�gen und gut umr�hren. Mit der Gem�sebr�he aufgie�en und die Suppe ca. 20 Minuten k�cheln.  Zum Schluss mit Salz, Chili- und Kurkumapulver abschmecken.  Die Suppe schmeckt am n�chsten Tag doppelt so gut. Dazu passen Garnelenspie�e und Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(67)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Mehl mit Kakao und Backpulver in einer R�hrsch�ssel mischen. Die �brigen Zutaten f�r den Teig hinzuf�gen und alles mit einem Mixer zu einem Teig verarbeiten. Anschlie�end zu einer Kugel formen und den Teig in Frischhaltefolie gewickelt mindestens 30 Minuten kaltstellen.  Inzwischen f�r die F�llung die Butter in einem Topf zerlassen und abk�hlen lassen. Den Boden der Springform fetten. Die H�lfte des Teiges mit einem Nudelholz ausrollen (wer lieber einen etwas dickeren Boden mag, kann auch 2/3 des Teiges verwenden) und eine 26er Springform damit auskleiden. Dabei sollte ein ca. 2 cm hoher Rand entstehen.  Den Quark mit Zucker, Vanillezucker, dem Mark einer Vanilleschote, den Eiern, dem Puddingpulver und der zerlassenen Butter mit einem Schneebesen zu einer gebundenen Masse verr�hren, in die Form geben und glatt streichen. Den restlichen Teig in kleine St�cke zupfen und auf der F�llung verteilen.  Die Form auf dem Rost im unteren Drittel in den vorgeheizten Backofen schieben und bei 180�C Ober-/Unterhitze ca. 60 Minuten backen. Nach dem Backen den Kuchen in der Form auf einem Kuchenrost erkalten lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gehackte Zwiebel in einer Pfanne mit etwas �l anschwitzen. Das Hackfleisch zugeben und kr�melig braten. Mit Salz, Pfeffer, Currypulver, Chilipulver und Knoblauch w�rzig abschmecken. Das Tomatenmark zugeben und kurz mitr�sten. Die Gem�sebr�he angie�en und den w�rfelig geschnittenen K�rbis ebenfalls zugeben. Zugedeckt ca. 5 Minuten d�nsten.  Danach Cr�me fra�che, Basilikum und die Gnocchi zugeben und alles gut miteinander vermischen. In eine Auflaufform f�llen. Den Mozzarella in Scheiben schneiden und dar�ber verteilen.  Im vorgeheiztem Backrohr bei 200 �C Ober-/Unterhitze ca. 15 Minuten �berbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(69)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 250 �C Ober-/Unterhitze vorheizen.  Knetteig bereiten, ganz d�nn ausrollen. Schmand und Cr�me double mischen, w�rzen und auf dem Teig verstreichen.  Zwiebeln mit ganz wenig Wasser 1 Minute bei 600 Watt in der Mikrowelle d�nsten (durch die hohen Temperaturen beim Backen kann es leicht passieren, dass die Zwiebeln verbrennen - das wird durch diesen Trick vermieden). Zusammen mit dem Speck auf dem Belag verteilen.  Nun 20 Minuten im hei�en Ofen auf der unteren Einschubleiste backen. Mit Schnittlauchr�llchen bestreut servieren.  Tipp: Wer Kalorien sparen m�chte, ersetzt Cr�me double durch 20%igen Quark.  Reicht f�r 2 - 3 Personen, je nach Hunger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch mit je 1 EL �l, Sojasauce und Ingwer gut vermischen und ca. 30 Minuten marinieren. In der Zwischenzeit das Gem�se putzen und schneiden. Das Fleisch in einer beschichteten Pfanne rasch braten und dann zur Seite stellen.  Im Wok oder einer gro�en Pfanne mit hohem Rand die Currypaste in 1 EL �l anr�sten. Die Erdnussbutter unterr�hren und schmelzen lassen. Mit Kokosmilch abl�schen, das Gem�se zugeben und alles ca. 15 Minuten k�cheln lassen.  In der Zwischenzeit den Reis zubereiten und ausd�mpfen lassen.  Kurz vor Ende der Garzeit (das Gem�se soll noch Biss haben) das Fleisch dazugeben und kurz wieder erhitzen. Das Curry mit Palmzucker, Fischsauce (notfalls etwas Salz nehmen) und Zitronengraspaste (soll nicht mitkochen) abschmecken. Nach Belieben Thai-Basilikum dar�berstreuen und mit dem Reis servieren.  Die Zusammenstellung des Gem�ses kann man ganz nach Geschmack und Verf�gbarkeit variieren/erg�nzen, z. B. fein geschnittene Wasserkastanien f�r noch mehr Biss, ein paar kleine Brokkolir�schen oder einige Zuckerschoten (diagonal geteilt, kurz blanchiert oder angebraten) als zus�tzlichen Farbtupfer. Es sollten (geputzt und geschnitten gemessen) insgesamt ca. 4 - 5 Handvoll Gem�se sein.  Zitronengraspaste ist geriebenes, in etwas Pflanzen�l eingelegtes Zitronengras. Das angebrochene Glas am besten im Tiefk�hlfach aufbewahren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:  Backofen auf 180�C vorheizen. Zwiebel abziehen und in W�rfel schneiden. Lauch putzen, waschen und in halbe Ringe schneiden. Zucchini und Tomaten waschen, halbieren und Zucchini zus�tzlich in Scheiben schneiden.  �l in einer Pfanne erhitzen und Zwiebelw�rfel darin anbraten. Hackfleisch dazugeben und kr�ftig anbraten. Lauch und Zucchini hinzuf�gen und mitd�nsten. Passierte Tomaten angie�en, Kirschtomaten unterheben, mit Salz und Cayennepfeffer abschmecken.  Kartoffelnudeln in Portionsauflaufformen geben und mit der Sauce �bergie�en.  Aufl�ufe mit K�se bestreuen und im vorgeheizten Backofen 15-20 Minuten backen (Gas: Stufe 3, Umluft 160�C).  Zubereitungszeit: 30 Minuten  Backzeit: 15-20 Minuten  Pro Portion (bei 3 Portionen):  kJ/kcal: 3647/871  EW: 46,5 g  F: 47,0 g  KH: 66,0 g  BE: 5,0")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Wirsing putzen, waschen und in Streifen, Kasseler in W�rfel schneiden. Zwiebeln abziehen und in Ringe schneiden. �l erhitzen, Zwiebeln dazugeben, goldbraun braten und herausnehmen. Wirsing in das verbliebene Bratfett geben und and�nsten. Br�he angie�en, Kasseler und gebratene Zwiebeln dazugeben und abgedeckt ca. 20 Min. garen.  2. Schupfnudeln und Schmand untermischen und alles mit Senf, Liebst�ckel, Salz, Pfeffer und K�mmel abschmecken.  3. Mischung in eine Gratinform (20 x 30 cm) geben, K�se �berstreuen und im vorgeheizten Backofen bei 200 �C (Gas: Stufe 4, Umluft 180 �C) ca. 25-30 Min. goldbraun �berbacken. Schnittlauch �berstreuen und servieren.  Pro Portion (bei 6 Portionen):  kJ/kcal: 2.322/555  EW: 24,3 g  F: 24,5 g  KH: 59,2 g  BE: 4,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Wirsing die groben �u�eren Bl�tter l�sen, den Wirsing vierteln und den Strunk herausschneiden. Den Wirsing absp�len und abtropfen lassen, dann in Streifen schneiden.  Die Zwiebel abziehen, halbieren und in feine Streifen schneiden. Etwas �l in einem gro�en Topf erhitzen und die Zwiebelstreifen darin unter gelegentlichem R�hren anschwitzen. Die Wirsingstreifen zuf�gen, salzen und mit geschlossenem Deckel d�nsten. Die Gem�sebr�he zugie�en und ca. 10 � 15 Minuten bissfest schmoren.  W�hrenddessen das Kasseler in kleine W�rfel schneiden, zusammen mit den Schupfnudeln unter den Wirsing mischen. Die Hitze reduzieren, die saure Sahne unterheben, alles mit Senf, Salz, Pfeffer und K�mmel abschmecken. Die Schupfnudel-Wirsing-Mischung in eine Auflaufform (ca. 20 x 30 cm) f�llen, mit dem geriebenen K�se und den Schnittlauchr�llchen bestreuen.  Im vorgeheizten Backofen bei 200 �C Ober-/Unterhitze ca. 25 Minuten goldbraun �berbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sauerrahm und Cr�me fra�che mit der Br�he verr�hren und diese Mischung in eine gro�e Auflaufform f�llen.  Die Kartoffeln gut waschen und mehrfach einschneiden, aber nicht ganz durchschneiden - sie sollen an der Unterseite noch zusammenh�ngen. Die Abst�nde zwischen den Schnitten sollten so �hnlich sein wie bei einem Eierschneider.  Die Kartoffeln mit der geschnittenen Seite nach oben in die Form setzen. Aber nur nebeneinander - nicht �bereinander - stapeln, sodass sie etwa zur H�lfte in der So�e sitzen.  Im hei�en Backofen bei 200 �C Ober-/Unterhitze ca. 45 - 60 Minuten backen, bis die Kartoffeln fast gar sind.  In der Zwischenzeit die Butter zerlassen. Katenschinken und Rosmarin hinzuf�gen sowie die Toastbrotw�rfel dazumischen. Diese Mischung auf den Kartoffeln verteilen und noch einmal so lange backen, bis die Brotw�rfel sch�n braun sind und die Kartoffeln gar.  Dazu Blattsalat servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln waschen, sch�len und in W�rfel schneiden. Den Lauch waschen und in Ringe schneiden. Beides in zerlassener Butter leicht anbraten. Die Gem�sebr�he dazugeben und alles 15 Min. kochen. Evtl. mit dem P�rierstab ganz leicht p�rieren (nur ein paar Impulse). Den Lachs in mundgerechte W�rfel schneiden und zu der Suppe geben. Alles noch einmal 5 Min. ziehen lassen. Die Suppe mit Sahne verfeinern und mit Dill bestreuen. Hei� servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(76)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="De Tomaten, die Waln�sse, eine Knoblauchzehe und einen guten Schuss Oliven�l in einen Mixer geben und daraus ein Pesto herstellen. Mit Salz und Pfeffer w�rzen.  Zwiebel und Knoblauch w�rfeln, in etwas Oliven�l in einer Pfanne glasig d�nsten und mit ein wenig Gem�sebr�he abl�schen. Dann Spinat dazugeben und einige Minuten mitd�nsten, bis er zusammenf�llt. Mit Salz und Pfeffer w�rzen.  Den Bl�tterteig auf einem Backblech ausbreiten und gro�z�gig mit dem Tomatenpesto bestreichen. Danach den Spinat darauf verteilen und von der langen Seite her zu einem Strudel rollen. Wichtig: Mit dem Schluss nach unten auf das Backblech legen, damit er sch�n zu bleibt.  Mit etwas Wasser bestreichen und bei 200 �C Ober-/Unterhitze backen, bis der Bl�tterteig goldbraun ist. Das dauert ca. 20 Minuten.  Optional bietet sich nat�rlich ein Knoblauchdip oder auch eine Tomatenso�e dazu an; uns hat es aber auch ohne sehr gut geschmeckt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="F�r den Reis 1 Teil Reis mit 2 Teilen kaltem Salzwasser in einem Topf mit Deckel aufkochen. Dann die Hitze reduzieren, sodass es gerade eben k�chelt. Abgedeckt quellen lassen, bis alles Wasser verkocht ist. Das dauert ca. 15 - 20 Minuten.  1 EL Erdnuss�l in eine hei�e Pfanne geben. Die H�hnerbrust scharf darin anbraten und aus der Pfanne nehmen. Wieder 1 EL Erdnuss�l in dieselbe hei�e Pfanne geben, die Currypaste kurz darin anschwitzen und mit der Kokosmilch aufgie�en.  Tipp: Es gibt 3 verschiedene Currypasten. Gr�ne (am sch�rfsten), rote (mittelscharf) und gelbe (am mildesten). Ich nehme auf jeden Fall einen sauberen Teel�ffel, um die Paste aus dem Glas zu nehmen und stelle das ge�ffnete Glas in den K�hlschrank. So h�lt es sich mehrere Monate.  Die Erdnussbutter dazugeben, den Knoblauch dazupressen, die gek�rnte Gem�sebr�he und die Zuckerschoten dazugeben. Wer keine Zuckerschoten bekommt, kann auch gr�ne Bohnen nehmen. Zuckerschoten schmecken aber besser.  Die Karotte sch�len, je nach Dicke l�ngs halbieren, in Scheiben schneiden und ebenfalls dazugeben. Alles mehrere Minuten k�cheln lassen, sodass die Zuckerschoten und die Karotte noch bissfest sind.  Danach die Bambussprossen und das Fleisch wieder dazugeben und noch ein paar Minuten k�cheln lassen. Die Speisest�rke in kaltem Wasser anr�hren und in die k�chelnde So�e geben, um sie etwas anzudicken. Zum Schluss die Zitronengraspaste unterr�hren und mit Salz w�rzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dieses Grundrezept kann je nach Lust und Laune durch Variieren des Fleisches (z. B. H�hnerbrust, Putenbrust, Rinderlende oder Schweinefilet) oder mit Fischfilet oder Garnelen und mit verschiedenem Gem�se (z. B. Bambussprossen in Streifen, Sojabohnenkeimlinge, Karotten, Babymais, Zuckerschoten, Thai-Auberginen, Pak Choi o. a.) zu immer neuem Genuss-Erlebnis f�hren. Lassen Sie Ihrer Kreativit�t freien Lauf! Es eignet sich auch f�r Vegetarier, da man es auch ausschlie�lich mit vielem verschiedenem Gem�se zubereiten kann.  Das Gericht muss nicht im Wok zubereitet werden, es geht genauso gut in einem breiten Topf, da es Suppencharakter hat.  Die Currypaste im hei�en �l sautieren, kurz mit etwas Wasser abl�schen, nach und nach die Kokosmilch dazugeben und immer erst gut verr�hren, bevor man mehr dazugibt (bringt eine sehr sch�ne rote Farbe). Das vorgesehene Fleisch (Fisch oder Garnelen) in mundgerechte St�cke schneiden, dazugeben und ca. 5 Minuten k�cheln lassen, bis es gar ist. Garnelen brauchen nur sehr kurze Zeit!  Das in Streifen geschnittene Gem�se der Wahl (egal welches und wie viele Sorten) dazugeben und alles wieder zum Kochen bringen. Alles sollte bissfest bleiben und die Farbe behalten (Pak Choi oder Chinakohl erst kurz vor Ende dazugeben).  Mit der Fischsauce, der hellen Sojasauce und dem Palmzucker abschmecken. Thai-Basilikum-Bl�tter und Peperoni dazuf�gen, eine Minute weiterkochen. Nach Belieben und Sch�rfe-Empfinden die kleingeschnittenen Chili-R�llchen einstreuen.  Das Gericht hei� mit Reis (Basmati, Jasminreis oder thail�ndischer Duftreis) servieren, als Variation kann man auch roten Reis aus dem Asialaden probieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Tortellini nach Packungsanweisung kochen.  Den gekochten Schinken in einer tiefen Pfanne in Butter kurz anbraten, dann 400 ml von der Sahne hineingeben und auf kleiner Stufe k�cheln lassen. Wenn die Tortellini gar sind, in die Pfanne zur Schinkensahne geben und weiter k�cheln lassen.  In der Zwischenzeit in einer kleinen Sch�ssel das Eigelb mit Parmesan, Muskatnuss, Salz und den restlichen 200 ml Sahne verr�hren. Dies dann in die Pfanne zu den Tortellini geben und so lange k�cheln lassen, bis die So�e dickfl�ssig wird. Sofort servieren.  Sehr gehaltvoll, aber der Geschmack ist fantastisch. Ab und zu kann man sich's mal g�nnen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die ersten sechs Zutaten f�r die Marinade mischen und die gewaschenen und getrockneten H�hnchenfilets hineinlegen. Mindestens 1 Std. darin marinieren (geht auch �ber Nacht).  Kartoffeln sch�len, gr��ere Knollen halbieren und in Oliven�l ca. 10 Min. von allen Seiten braun braten.  Die gebratenen Kartoffeln in eine mit Oliven�l ausgestrichene Auflaufform geben.  Knoblauch sch�len und klein hacken. Die Zwiebel sch�len, halbieren und die H�lften in Ringe schneiden. 1 Zweig Thymian und 1 Zweig Rosmarin waschen und hacken. Zwiebeln, Knoblauch und gehackte Kr�uter im Bratfett and�nsten, dann �ber die Kartoffeln geben.  Das Fleisch mit der Marinade auf die Kartoffeln geben und alles im Backofen bei 200 Grad ca. 15 Min. braten. Dann hei�e H�hnerbr�he angie�en, die Tomaten und zwei Rosmarinzweige im Auflauf verteilen und weitere 30 Min. im Ofen garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Aus dem Mehl, Zucker, Butter, Ei und Backpulver einen Knetteig herstellen. Den Boden einer 26 cm Springform mit Backpapier auslegen, den Rand einfetten. Den Teig ausrollen und die R�nder von Hand recht hoch dr�cken.  Den Backofen am besten jetzt auf 175�C Ober-/Unterhitze vorheizen.  Den Quark kurz geschmeidig r�hren, dann nach und nach alle Zutaten zugeben und gut verr�hren. Die sehr fl�ssige Masse in die Springform f�llen und den Kuchen 70 Minuten backen.  In der Zwischenzeit das Eiwei� mit dem Puderzucker steif schlagen. Nach 70 Minuten den Kuchen heraus holen und den Eischnee ca. 1 cm dick auf den Belag streichen. Es wird wohl nicht alles davon ben�tigt! Nochmals 10 Minuten bei gleicher Hitze backen.  Dann den Kuchen etwas abk�hlen lassen und den Rand der Springform vorsichtig mit einem Messer l�sen. Den Kuchen auf dem Boden der Springform mehrere Stunden abk�hlen lassen. Wenn alles funktioniert hat, dann sollten beim Abk�hlen auf dem Eiwei�guss die Tr�nen entstehen. Schmecken tut der Kuchen aber auch ohne!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Schafsk�sew�rfel in ein Sieb gie�en und das �l dabei auffangen. Die Champignons in Scheiben schneiden. Die Paprikaschoten putzen und in Streifen schneiden. Den Knoblauch fein hacken.  In ca. 3 EL von dem aufgefangenen �l das Hackfleisch braun und kr�melig braten. Die H�lfte der Champignons dazugeben und mit anbraten. Nun auch die Paprikastreifen und den Knoblauch dazugeben und anbraten.  Nach ca. 5 Minuten die Cr�me fra�che und den Oregano einr�hren und mit Salz und Pfeffer w�rzig abschmecken. Alles in eine feuerfeste Form geben und die restlichen Champignons darauf verteilen. Zuletzt die abgetropften Schafsk�sew�rfel sowie den zerbr�ckelten Schafsk�se darauf streuen.  Den Auflauf ca. 20 - 30 Minuten im hei�en Backofen bei 180 �C Umluft backen.  Dazu passt Tzatziki, Fladenbrot und/oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 �C Ober-/Unterhitze vorheizen.  F�r die F�llung 1 EL Sesam�l in einer ausreichend gro�en Pfanne erhitzen. Gem�se in mundgerechte St�cke schneiden, Sprossen abtropfen lassen. Das vegane �Hack� in der Pfanne kr�melig braten. Das Gem�se hinzugeben und alles vermengen. 3 Minuten bei hoher Hitze and�nsten und mit Chili Flocken, Salz und Pfeffer w�rzen.  Die Strudelteigbl�tter hochkant legen. Auf den unteren Teil mittig etwa 3 EL der F�llung geben. Seiten einklappen und das gesamte Strudelteigblatt vorsichtig einrollen. Auf ein mit Backpapier ausgelegtes Backblech legen. Mit den �brigen Bl�ttern gleich verfahren. Die fertigen Fr�hlingsrollen mit dem restlichen Sesam�l einpinseln. Wer mag kann etwas Sesam dr�berstreuen.  Die Fr�hlingsrollen im vorgeheizten Backofen 25 - 30 Minuten auf der mittleren einschubleiste goldbraun backen.  Pro St�ck  Energie kJ/kcal 1059/253  Eiwei� 12,1 g  Fett 7,6 g  Kohlenhydrate 32 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Br�he aufkochen lassen, den Reis hineingeben und 15 min kochen. Er sollte dann noch etwas al dente sein. Den Reis abgie�en und abk�hlen lassen.  Tipp: Man kann nat�rlich auch einen Rest vom Vortag nehmen. Dann aber sp�ter mit dem Salz nicht sparen. Der Reis sollte schon sch�n w�rzig sein.  Den K�se raspeln, die M�hren putzen und raspeln (ob man K�se und M�hren fein oder grob raspelt, bleibt dem eigenen Gusto �berlassen). Die Zwiebeln fein w�rfeln.  Reis, K�se, M�hren, Zwiebeln und Eier miteinander verr�hren. Pfeffer (ruhig reichlich), Salz und Kr�uter einr�hren. Nun Semmelbr�sel einr�hren, bis die Masse etwas Konsistenz hat. Dann ca. 15 min quellen lassen. Pr�fen, ob die Masse unter Druck in den H�nden zu einer Frikadelle geformt werden kann. Wenn ja, anschlie�end noch leicht in Semmelbr�seln w�lzen.  In reichlich Butterschmalz bei geringer Hitze vorsichtig von beiden Seiten goldbraun braten. Nach dem Braten auf K�chenkrepp das Fett abtropfen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebeln und Knoblauch sch�len und fein w�rfeln.  2. Kichererbsen abgie�en, absp�len und abtropfen lassen, Rosinen absp�len.  3. Wurzelgem�se sch�len und w�rfeln.  4. Koch-R�hrelement und R�hrhilfe einsetzen. Oliven�l in die R�hrsch�ssel geben und Programm Eintopf w�hlen.  5. Hackfleisch nach und nach dazu br�seln, Zwiebeln, Knoblauch und Zucker zugeben und Temperatur auf 160 �C erh�hen.  6. Wurzelgem�se (Suppengr�n), Zimt, Kreuzk�mmel, Cayennepfeffer zugeben. W�hrend die KCC l�uft, mit Tomaten, Kichererbsen, Rosinen und Gem�sebr�he auff�llen.  7. Ende des Programms abwarten und gegebenenfalls mit Salz und Pfeffer abschmecken. Vor dem Servieren Zitronenabrieb zugeben.  Gef�llt Dir dieses Rezept? Dann freuen wir uns auf Deine Bewertungs-Sternchen!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 175 �C - 195 �C vorheizen.  Zuerst die Schale von den 3 Zitronen abreiben, zwei Zitronen davon auspressen.  Dann Eier und Zucker schaumig r�hren. Das Mehl sieben und mit Vanillezucker, Backpulver, Zitronenschale und Margarine nach und nach dazugeben. Alles gut mixen. Den Teig auf ein mit Backpapier ausgelegtes Backblech streichen. In den vorgeheizten Backofen schieben und ca. 20 Min. auf der mittleren Schiene backen.  Nun aus dem Zitronensaft und dem Puderzucker nach und nach eine Glasur mischen - bitte sehr sparsam mit dem Zitronensaft umgehen, die Glasur muss sch�n dickfl�ssig sein.  Solange der Kuchen noch warm ist, mit einer Gabel �berall einstechen. Somit wird er sch�n saftig, denn die Glasur kann so einsickern. Dann schnell die Glasur auf dem warmen Kuchen verstreichen und ausk�hlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das H�hnchenbrustfilet waschen, mit K�chenpapier abtupfen und in mundgerechte St�cke schneiden. Das Oliven�l mit der roten Currypaste in einer beschichteten Pfanne erhitzen und das H�hnchenfleisch darin von allen Seiten knusprig braten.  W�hrenddessen die Zucchini waschen und die Karotten sch�len. Nun mit einem Sparsch�ler rundherum die �Bandnudeln� absch�len, bei den Zucchini m�glichst das innere Kerngeh�use �brig lassen, die Karotten k�nnen komplett verwendet werden. Sollten die Scheiben zu breit werden, kann man das Gem�se mit einem Messer vor dem Absch�len l�ngs einschneiden.  Das fertig gebratene H�hnchenfleisch herausnehmen und dabei m�glichst den Bratsaft in der Pfanne lassen. Die Gem�sebandnudeln in Wasser und Br�he mit dem Bratsaft aufkochen und einige Minuten garen lassen. Derweil die Tomaten w�rfeln und zusammen mit dem Tomatenmark zum Gem�se geben.  Zum Schluss den Ziegenfrischk�se und das H�hnchenfleisch zugeben und alles noch einmal unter R�hren erhitzen. Mit Salz und Pfeffer abschmecken und servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zucchini waschen und l�ngs in fingerdicke Scheiben schneiden. In einer Pfanne in Oliven�l von beiden Seiten anbraten, danach auf K�chenpapier abtropfen lassen. Oder alternativ die Scheiben mit Oliven�l bestreichen, ein wenig salzen und auf der obersten Schiene mit der Grillfunktion im Backofen br�unen. Das dauert allerdings l�nger.  Die Zwiebel in W�rfel schneiden und in der Pfanne in wenig Oliven�l glasig d�nsten. Die Knoblauchzehe dazu pressen und etwas mitd�nsten. Das Hackfleisch hinzugeben und kr�melig braten. Wenn das Fleisch Farbe bekommen hat, mit Salz, Pfeffer und Paprikapulver w�rzen, 1 EL Tomatenmark hinzugeben, unterr�hren und eine Minute mit anschwitzen. Die Tomaten hinzugeben und mit Oregano, Thymian, Salz, Pfeffer und Paprika w�rzen. 10 min auf kleiner Flamme k�cheln lassen, zum Schluss die gehackte Petersilie hinzugeben.  Den Frischk�se mit der Milch verr�hren, wahlweise auch Sauerrahm unterr�hren. Mit Salz, Pfeffer und etwas Muskat w�rzen, ca. 50 g Streuk�se unterr�hren.  Eine Lasagneform oder eine andere Auflaufform mit Zucchinischeiben auslegen. Darauf ein paar L�ffel Tomaten-Hack-So�e verteilen, darauf eine Schicht Frischk�seso�e, und darauf wieder Zucchinischeiben. Weiter so schichten, bis alle Zutaten verbraucht sind. Die oberste Schicht soll Tomaten-Hack-So�e sein. Diese mit dem restlichen K�se bestreuen.  Die Zucchini-Lasagne im vorgeheizten Backofen bei 200 �C Ober-/Unterhitze in ca. 30 min goldbraun backen.  Dazu passt ein kleiner frischer Salat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zucchini sch�len und anschlie�end mit einem Sch�lmesser in Streifen schneiden - also wie Spaghetti bzw. Bandnudeln.  Die Zucchini in etwas Oliven�l anbraten. Inzwischen die Tomaten klein schneiden und dazugeben. Dann das Mineralwasser hinzuf�gen (das sorgt daf�r, dass die Zucchini weicher werden und sich einfach besser um die Gabel wickeln lassen). Tomatenmark und eine beliebige Menge Frischk�se dazugeben (ich empfehle: 2 TL). Salzen, pfeffern und die Kr�uter hinzuf�gen. Eventuell noch w�rzen (z. B. mit Paprikapulver oder Gyrosgew�rz). Noch ein wenig k�cheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(90)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

