from app import db
import sqlalchemy
from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags

AssociationRHhat.query.delete()
handlungsschritt.query.delete()
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln und Moehren schaelen und in kleine Stuecke schneiden. Die Paprikaschoten ebenfalls klein schneiden.  Das oel in einer Pfanne erhitzen und das Hackfleisch kruemelig braten. Mit den Dosentomaten, Tomatenmark und der Bruehe abloeschen. Kartoffeln, Moehren und die Paprika hinzufuegen. Alles zugedeckt ca. 40 min. bei mittlerer Hitze koecheln lassen. Zum Reduzieren evtl. zusaetzlich ca. 10 min. ohne Deckel koecheln lassen. Am Schluss mit den Gewuerzen abschmecken und den Schmand unterruehren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(1)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200 Grad C Umluft vorheizen.  Den Blaetterteig auslegen und mit dem Frischkaese bestreichen. Den Raeucherlachs gleichmaessig darauf verteilen. Mit etwas Dill bestreuen und zu einer Schnecke rollen. Mit einem sehr scharfen Messer in gleichmaessige dicke Scheiben (ca. 1 cm) schneiden, dann nebeneinander auf einem mit Backpapier ausgelegten Backblech verteilen und mit dem verquirlten Ei bestreichen.  Im heissen Backofen auf mittlerer Schiene ca. 20 - 25 Minuten backen. Vor dem Servieren abkuehlen lassen.  Tipp: Anstatt Lachs, Frischkaese und Dill kann man auch geraeucherten Schinken verwenden. Dieser ist jedoch etwas trockener und benoetigt nur 15 - 20 Minuten im Backofen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(2)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Blaetterteig ausrollen und eine Teighaelfte mit gut der Haelfte des Schmands bestreichen. Die Haelfte der Schinkenwuerfel und des Kaeses darauf verteilen. Die Seite des Blaetterteiges, die nicht belegt ist, ueber die andere Seite klappen.  Wiederum die Haelfte des Teiges mit dem restlichen Schmand bestreichen und die Schinkenwuerfel und Kaeseraspel darauf geben. Die unbestrichene Teighaelfte darueber klappen. Den Blaetterteig in Streifen schneiden. Vorsichtig spiralfoermig drehen und auf ein mit Backpapier belegtes Blech legen.  Im heissen Backofen bei 180  Grad C Ober-/Unterhitze ca. 25 Minuten backen.  Variante: Sehr gut schmecken diese Stangen auch, wenn man statt Schinken geraeucherten Lachs verwendet. Dafuer braucht man dann ca. 180 g.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(3)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 180  Grad C Heissluft vorheizen.  Den Blaetterteig aus der Packung nehmen und in ca. 4 x 4 cm grosse Quadrate schneiden. Die Quadrate auf ein mit Backpapier belegtes Blech legen. Mit etwas Milch bestreichen. Tomatenscheiben darauflegen, dabei einen kleinen Rand freilassen und pfeffern.  In den vorgeheizten Backofen auf die mittlere Einschubleiste schieben und ca. 15 - 20 Min. backen, bis die Raender leicht gebraeunt sind.  In der Zwischenzeit Knoblauchwuerfelchen mit Olivenoel und Basilikum verruehren.  Die fertig gebackenen Quadrate anschliessend mit Fleur de Sel bestreuen und mit der Knoblauch-Basilikumpaste bestreichen. Entweder sofort servieren oder auch kalt geniessen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(4)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die TULIP Bacon-Scheiben in etwa 5 cm grosse Stueckchen schneiden. In eine Pfanne legen und 2 Min. bei kraeftiger Hitze braten.  Kartoffeln, Zwiebeln und Butter dazugeben und weitere 7 Min. bei mittlerer Hitze braten, bis alles knusprig und goldbraun ist. Mit Salz und Pfeffer abschmecken und das Gericht warmhalten.  Waehrenddessen das oel in der Pfanne erhitzen, Eier in die Pfanne schlagen und etwa 6 Min. braten. Anschliessend mit Salz wuerzen.  Das Gericht mit Parmesan und Thymian bestreuen und sofort mit den Spiegeleiern servieren.  Als Beilage passen eingelegte Rote Beete dazu.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(5)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Butterschmalz in einer tiefen Pfanne erhitzen. Das Gulasch im Butterschmalz scharf anbraten und mit Salz, Pfeffer und Paprikapulver wuerzen.  Wenn das Fleisch eine schoene Farbe angenommen hat und das Wasser verdampft ist, die gehackte Zwiebel, die gepresste Knoblauchzehe und die geriebene Karotte sowie den Senf und das Tomatenmark dazugeben und kurz weiterbraten.  Anschliessend mit dem Bier abloeschen und einkochen lassen. Mit der Gemuesebruehe auffuellen und mit Deckel ca. 1 Stunde koecheln lassen (bei Verwendung eines Schnellkochtopfes ca. 35 min).  Etwa 5 min. vor Ende der Garzeit die Crème fraîche einruehren und nach Bedarf mit etwas Sossenbinder andicken. Vor dem Servieren nochmal abschmecken.  Als Beilage passen Spaetzle, Reis, Kartoffelbrei oder Salzkartoffeln")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(6)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die geschaelte Zwiebel wuerfeln und in einem groesseren Topf in Olivenoel leicht anroesten, Faschiertes dazugeben und kruemelig braten. Die geschaelten Kartoffeln in kleine Wuerfel schneiden, in den Topf geben und mit Bruehe und Dosentomaten aufgiessen - die Kartoffeln und spaeter das Gemuese sollten immer leicht bedeckt sein - ansonsten Bruehe nachfuellen. Gepressten Knoblauch, viel gemahlenen Pfeffer und Kraeuter (z.B. getrockneten Majoran, Thymian, Oregano gemischt) dazugeben und leicht kochen lassen.  In der Zwischenzeit zuerst die Karotten in duenne Scheibchen schneiden und nach ca. 15 Minuten in den Topf geben. Die Paprikaschote in kleine Wuerfel oder Steifen schneiden und den geputzten Porree (ich verwende gerne den vorgeputzten) in Scheiben schneiden und nach weiteren 10 Minuten dazugeben und noch ca. 10 Minuten koecheln lassen.  Den Eintopf gut mit Kraeutersalz abschmecken und mit Petersilie bestreut servieren.  Die Kochzeit richtet sich natuerlich ein wenig nach der Groesse der Kartoffel- und Gemuesestueckchen und wie knackig man es mag.  Tipp: Wer moechte, ersetzt das eine oder andere Gemuese durch Mais, Erbsen oder Brokkoliroeschen oder gibt zusaetzlich etwas davon dazu und nimmt vom anderen Gemuese dafuer weniger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(7)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die frischen Kartoffeln werden ausgiebig gewaschen und dann wird ausprobiert, auf welcher Seite sie am stabilsten liegen. Jetzt von oben ca. alle drei Millimeter bis fast ganz durch mit einem scharfen und feinen Messer einschneiden. Die Kartoffeln nun auf ein Backblech mit Backpapier legen.  Die Butter wird vorsichtig im Topf bei schwacher Hitze geschmolzen. Sie darf auf keinen Fall braun werden oder verbrennen. In die Butter werden nun der Knoblauch, der Rosmarin, das Meersalz, der Kreuzkuemmel und der Cayennepfeffer gruendlich untergeruehrt. Leicht warm (und fluessig) halten und 5 Minuten durchziehen lassen.  Den Backofen auf 230 Grad (moeglichst Umluft) vorheizen.  Jetzt wird die Butter mit einem Teeloeffel oder Backpinsel ueber die Kartoffeln gegeben. Nicht alles verwenden, weil die zweite Haelfte nach ca. 25 Minuten Backzeit nochmal ueber die Kartoffeln gegeben wird. Jetzt kommt das Blech mit den Kartoffeln auf der mittleren Position in den vorgeheizten Backofen. Nach der Haelfte der Garzeit nochmals mit der Buttermarinade uebergiessen oder bepinseln. Gesamtbackzeit ca. 50 Minuten. Bei groesseren Kartoffeln die Backzeit ggf. verlaengern.  In der Zwischenzeit wird der Quark mit der Sahne, den Kraeutern gemaess Zutatenliste und der Schalotte verruehrt und mit Salz und Pfeffer abgeschmeckt.  Jetzt werden die Kartoffeln auf Tellern angerichtet und zur Deko noch mit ein wenig grobem Meersalz ueberstreut. Noch auf jeden Teller ein Klacks vom Kraeuterquark geben - FERTIG.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(8)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebel abziehen und in kleine Wuerfel schneiden. Hackfleisch und Zwiebeln in erhitztem oel ca. 5 Minuten anbraten, mit Senf und Ketchup verruehren, mit Salz und Pfeffer abschmecken und auskuehlen lassen.  2. Tomaten waschen und vierteln, Gurken grob hacken. Pizzateig entrollen und in 12 Rechtecke schneiden (ca. 9 x 9 cm). Hackfleisch-Mischung, Cheddar, Tomaten und Gurken mittig auf den Teigstuecken verteilen und Teig ueber der Fuellung zusammenfalten. Teigraender gut zusammendruecken, sodass keine oeffnung mehr bleibt und mit der verschlossenen Seite nach unten in gefettete Mulden eines Muffinblechs legen.  3. Muffins mit Milch bestreichen, mit Sesam bestreuen und im vorgeheizten Backofen bei 180  Grad C (Umluft: 160  Grad C) ca. 35 Minuten backen. Cheese-Burger-Muffins etwas abkuehlen lassen, aus der Form loesen und lauwarm, nach Wunsch mit Burgersauce und Ketchup, servieren.  Pro Stueck:  kJ/kcal: 917/220  EW: 10,9 g  F: 12,0 g  KH: 16,8 g  BE: 1,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(9)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="oel im Wok erhitzen, Knoblauch und Ingwer kurz darin anbraten. Dann die Fleischstreifen in den Wok geben und kraeftig anbraten. Nun alle uebrigen Zutaten, bis auf die Lauchzwiebeln dazugeben und ca. 10 Minuten durchgaren. Achtung bei 4 TL Sambal Oelek wird es ganz schoen scharf!  Evtl. nochmals mit Zucker, Zitronensaft und Sojasauce abschmecken, nun die Lauchzwiebeln unterruehren.  Als Beilage eignet sich Reis, ein Gemuesecurry und Raita oder Karottensalat mit Ingwer.  In Indien haben wir zu diesem Gericht extra Limettenachtel zum Nachwuerzen bekommen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(10)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 200  Grad C Ober-/Unterhitze (Umluft 180  Grad C) vorheizen.  Die Zwiebel und den Knoblauch sehr fein schneiden. Die Chilischote entkernen und ebenso fein hacken. Die Kirschtomaten waschen und halbieren. Den Parmesan reiben und den Mozzarella grob wuerfeln. Die Basilikumblaetter abzupfen, waschen und trocken tupfen.  In einem grossen Topf Salzwasser zum Kochen bringen und die Nudeln darin laut Packungsangabe al dente garen.  Waehrenddessen in einer grossen Pfanne Olivenoel erhitzen und Zwiebel, Knoblauch und Chilischote darin anschwitzen. Die passierten Tomaten hinzufuegen und die Sauce ein paar Minuten leicht koecheln lassen. Dann die Sahne und den geriebenen Parmesan unterruehren und die Sauce mit Salz, Pfeffer und einer ordentlichen Prise Zucker abschmecken.  Wenn die Nudeln soweit sind, diese abgiessen und in die Pfanne zur Sauce geben. Die Pfanne von der Hitze nehmen und die halbierten Kirschtomaten und die Haelfte der Mozzarellawuerfel unterheben. Die Basilikumblaetter in Streifen schneiden und ebenfalls unterheben.  Alles zusammen in eine Auflaufform geben, mit dem restlichen Mozzarella bestreuen und ca. 20 Minuten auf der mittleren Schiene im heissen Backofen gratinieren.  Dazu passt zum Beispiel ein gruener Salat und Knoblauchbaguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(11)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Gratinform mit Butter einfetten. Den Knoblauch schaelen. Entweder fein wuerfeln und in der Form verteilen oder direkt in die Form pressen. Die Kartoffeln schaelen und in feine Scheiben schneiden (ich nehme dafuer einen Gurkenhobel, das geht am schnellsten).  Die Haelfte der Kartoffelscheiben in die Form schichten. Mit Kraeutersalz und frisch geriebenem Muskat leicht wuerzen, anschliessend die restlichen Kartoffeln darauf schichten.  Die Sahne und die Milch mischen. Mit dem Gemuesebruehepulver, Kraeutersalz, Muskat und Pfeffer kraeftig wuerzen. Diese Mischung ueber die Kartoffeln geben. Butterfloeckchen auf dem Gratin verteilen.  Im vorgeheizten Backofen bei 180  Grad C Ober-/Unterhitze ca. 1 Stunde backen. Heiss servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(12)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Rindfleischwuerfel im Butterschmalz 5 Minuten anbraten, dabei umruehren, dann die Zwiebeln und Knoblauchstuecke dazugeben, weitere 5 Minuten mitduensten. Mit Rinderbouillon und Rotwein abloeschen, mit Salz, Pfeffer, Zucker, Paprikapulver, Lorbeerblaettern, Tomatenmark und Majoran wuerzen. Dann bei geschlossenem Deckel ca. 60 Minuten bei kleiner Hitze schmoren.  Die Kartoffel-, Paprika und Karottenstuecke zugeben und weitere ca. 20 Minuten koecheln lassen, bis das Gemuese gar ist. Dann Petersilie unterruehren und heiss servieren  Dazu schmeckt Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(13)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zutaten fuer den Knetteig in eine Schuessel geben, rasch zusammenkneten und zur Seite stellen.  Fuer die Fuellung Margarine, Zucker, Vanillezucker, Puddingpulver und Eier in einer Schuessel verruehren. Dann den Quark und die saure Sahne untermischen. Die suesse Sahne steif schlagen und unterheben.  Den Backofen auf 180  Grad C Ober-/Unterhitze vorheizen.  Den Knetteig in einer gefetteten 26er Springform auslegen, etwa 2 - 3 cm am Rand hochziehen. Nun die Fuellung in die Form geben, glatt streichen und im heissen Backofen 1 Stunde backen.  Achtung: Den Kuchen erst nach dem voelligen Erkalten aus der Form nehmen, da unmittelbar nach dem Herausnehmen aus dem Backofen die Konsistenz der Quarkmasse noch zu weich ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(14)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Nach unzaehligen Feldversuchen, reichlich Google-Recherche und Restaurant-Spionage habe ich endlich ein Rezept entwickelt, das absolut authentisch und lecker schmeckt - eben wie in Bella Italia!  Zunaechst das Mehl mit dem Salz sieben und es in eine Teigruehrmaschine oder einen Brotbackautomaten mit Teigfunktion fuellen. Nun die Hefe in dem lauwarmen Wasser aufloesen und anschliessend zum Mehl-Salz-Gemisch geben (Anmerkung des Chefkoch.de Teams Rezeptbearbeitung: Die angegebene Hefemenge stimmt und es handelt sich um frische Hefe).  Anschliessend die Zutaten in 20 (!) Minuten zu einem elastischen, homogenen Teig verkneten.  Anmerkung: Eine elektrische Hilfe ist hier fast schon Pflicht, zur Not tut es auch ein Handruehrgeraet mit Knethaken. Bitte nicht verzweifelt mit der blossen Hand kneten, der Teig erreicht so einfach nicht die gewuenschte Weichheit und Konsistenz.  Nach dem Kneten den Teig mit einem feuchten Tuch abdecken und zwei Stunden ruhen lassen. Anschliessend in vier Stuecke zu je 200 g teilen, diese zu Kugeln formen und wieder abgedeckt weitere sechs Stunden gehen lassen.  Was ist nun das Besondere an diesem Teig-Rezept? Das Geheimnis liegt nicht in erlesenen Zutaten wie teurem Pizzamehl oder hochwertigem Olivenoel und auch nicht in ueberfluessigen Ingredienzen wie Bier, Zucker oder Eiern. Vielmehr erreicht man die geschmeidige Textur durch langes maschinelles Kneten! Die extrem geringe Menge Hefe sorgt zusammen mit der langen Gaerung fuer einen aeusserst aromatischen Teig.  Abschliessend noch ein paar Tipps fuer weitere Verarbeitung:  Den Teig so duenn wie moeglich ausrollen oder ziehen! Alles unter 4 mm ist ideal.  Fuer die Tomatensosse einfach eine Dose Schaeltomaten mit (viel) Knoblauch, Salz, Pfeffer, etwas Zucker, Basilikum und Oregano kalt puerieren, nicht kochen. Anschliessend mittig auf die Pizza auftragen und in kreisrunden Bewegungen mit der Kelle ueber die komplette Pizza verteilen. Nicht zu viel auftragen! Eine gute Pizza sollte man nicht in Tomatensosse ertraenken. Wenn einzelne Teigbereiche keine Sosse abbekommen, macht das ueberhaupt nichts. Lieber etwas weniger als etwas mehr.  Den Backofen auf Hoechststufe vorheizen! Meiner schafft knapp 260  Grad C, das Ergebnis war super. Den Teig auf das heisse Backblech legen (mit Backpapier ist das einfacher) und bereits nach 3 - 4 Minuten ist die Pizza fertig und kann genossen werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(15)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Butterkekse zerbroeseln, gut mit der fluessigen Butter vermischen und die Mischung auf den Boden einer Backform druecken. Bei 180  Grad C Ober-/Unterhitze im vorgeheizten Ofen 5 - 10 Minuten vorbacken, dann herausholen.  Den Zucker mit Speisestaerke, Frischkaese und Magerquark cremig ruehren. Das Ei, die Sahne und den Zitronensaft dazugeben und alles glatt ruehren. Nicht mit dem Ruehrgeraet schlagen, sondern langsam cremig ruehren, das ist ganz wichtig. Die Creme auf den vorgebackenen Boden streichen. Den Kuchen weitere ca. 45 Minuten backen. Wenn der Rand leicht braun ist, herausnehmen.  Die Zutaten fuer den Guss miteinander verruehren, den Guss auf den Kuchen streichen und den Kuchen nochmal 5 Minuten backen.  Am besten ueber Nacht auskuehlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(16)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln in Salzwasser al dente kochen und abkuehlen lassen.  Die getrockneten Tomaten in Stuecke schneiden, die Pinienkerne in einer trockenen Pfanne ohne Fett anroesten. Rucola und Basilikum waschen und etwas zerrupfen.  Alle Zutaten miteinander mischen und den Salat mindestens 1 Stunde ziehen lassen. Vor dem Servieren nochmal abschmecken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(17)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fuer die Lasagneplatten zuerst die sechs Eier aufschlagen und verquirlen. Ein Backblech mit einem Backpapier auslegen, Eiermasse darauf geben und moeglichst gleichmaessig verteilen. Das Blech in den heissen Ofen schieben und die Eier bei 80 bis 100  Grad C Ober-/Unterhitze stocken lassen. Immer wieder mal rein schauen und gerne die Masse zwischendurch wieder glatt auf dem gesamten Blech verteilen, damit eine gleichmaessige Platte entsteht.  Fuer die Hackfleischfuellung inzwischen die Zwiebeln schaelen und hacken, dann glasig anbraten. Das Hackfleisch hinzugeben. Das Fleisch mit etwas Salz und Pfeffer wuerzen und braten. Anschliessend mit den gehackten oder frischen Tomaten und den passierten Tomaten abloeschen. Jetzt nach Belieben abschmecken und ziehen lassen. Ich nutze gerne Oregano, Basilikum, Thymian, eigentlich alles, was gruen ist und vorhanden ist.  Fuer die Béchamelsauce ein wenig oel heiss werden lassen und mit der Messerspitze Mehl vermengen. Mit der Sahne und ggf einem Schuss Wasser abloeschen und cremig ruehren. Mit Salz, Pfeffer und Muskat wuerzen. Die Crème fraîche hinzugeben und zur Seite stellen.  Nun die Eiermasse in Scheiben schneiden, die der genutzten Auflaufform entsprechen. Jetzt abwechselnd mit der Hackfleischsauce, Sauce Béchamel und Lasagneplatten in der Auflaufform stapeln. Die letzte Schicht sollte die Bechamel sein, welche dann mit Kaese ueberstreut wird.  Alles dann so lange bei 180  Grad C Ober-/Unterhitze im heissen Ofen backen, bis der Kaese goldbraun ist. Da alle Zutaten bereits gar sind, ist die Backzeit variabel, am besten schmeckt es mir so nach circa 20 Minuten.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(18)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Filet trocken tupfen und in 8 Medaillons schneiden. Mit Senf bestreichen, mit Schinken umwickeln und in eine kleine Auflaufform legen.  2. Champignons abtropfen lassen und in der Auflaufform zwischen den Medaillons verteilen. Mit Salz und Pfeffer wuerzen und Kraeuter ueberstreuen.  3. Fuer die Sauce Sahne und Crème fraîche verruehren, mit Paprikapulver, Salz und Pfeffer wuerzen, ueber die Medaillons giessen und im vorgeheizten Backofen bei 200  Grad C (Gas: Stufe 4, Umluft 180  Grad C) ca. 30 Minuten garen. Spaetzle nach Packungsanweisung zubereiten und zu dem Filet servieren.  Pro Portion:  kJ/kcal: 2503/598  EW: 51,6 g  F: 29,3 g  KH: 30,2 g  BE: 2,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(19)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Schweinefilet die weisse Haut entfernen. Das oel mit der Butter erhitzen, nicht zu heiss werden lassen. Das Fleisch mit Salz und Pfeffer wuerzen und ca. 10 Minuten von allen Seiten braten. Es soll innen noch rosa sein. Dann herausnehmen und auf einem Teller (damit der Fleischsaft aufgefangen wird) erkalten lassen.  Im Bratfett Zwiebeln, Knoblauch und Schinken gut braeunen. Die Champignons putzen und in Scheiben schneiden und mitbraten. Dann mit Bruehe abloeschen und Sahne und Crème fraîche oder Schmand und den ausgetretenen Fleischsaft zugeben. Die Sosse mit Salz, Pfeffer, Tomatenmark und Senf kraeftig abschmecken. Sollte sie zu fluessig sein, etwas Speisestaerke in wenig kaltem Wasser anruehren und unter Ruehren zur kochenden Sosse geben, bis zur gewuenschten Konsistenz. Die Sosse abkuehlen lassen.  Das kalte Fleisch in 1 cm breite Scheiben schneiden und dann in Streifen. Dann in die Sosse geben, die Petersilie dazu und durchruehren, kuehl stellen.  Am naechsten Tag das Gericht auf kleiner Flamme erhitzen, jedoch nicht mehr kochen. So bleibt das Fleisch rosa. Die Sosse nochmals abschmecken.  Dazu schmeckt Baguette, aber auch Spaetzle und Salat.  Tipp:  Sollte am Vortag zubereitet werden. Deshalb auch gut geeignet fuer Feste mit groesserer Personenzahl.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(20)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln schaelen und zusammen mit dem Schinken wuerfeln. Mit dem Frischkaese mischen und mit etwas Salz und viel Pfeffer abschmecken. Man kann auch bei Bedarf noch ein wenig Kraeuter der Provence dazugeben.  Diese Masse gut auf dem ausgebreiteten Blaetterteig verteilen. Nun den Teig vorsichtig zusammenrollen und in ca. 3 cm dicke Scheiben schneiden. Die Scheiben auf ein mit Backpapier belegtes Backblech legen.  Ca. 10 Min bei 180  Grad C Umluft in den vorgeheizten Backofen schieben - je nach gewuenschtem Braeunungsgrad laenger oder kuerzer.  Bei uns gibt es diese kleinen Koestlichkeiten sonntags heiss oder kalt oft zum Brunch. Die Rollen lassen sich aber auch gut zu jeder Party mitnehmen. Den Belag kann man nach Geschmack auch jederzeit abwandeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(21)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Apfel schaelen, Kerngehaeuse entfernen und mit Hilfe einer Kuechenreibe grob raspeln. Blaetterteig auspacken, mit Alsan/ Margarine bestreichen, Apfelraspel darauf verteilen, mit Zimt und Zucker bestreuen.  2. Hochkant aufwickeln. In 6 gleichgrosse Stuecke schneiden. Mit einem Kochloeffelstiel (oder aehnlichem) jedes Stueck mittig eindruecken, sodass die Enden die typische Franzbroetchen-Form bekommen.  3. Mit dem Backpapier auf ein Backblech geben und im vorgeheizten Backofen bei 200  Grad C Ober-/Unterhitze fuer 10 - 15 Minuten goldbraun backen.  Naehrwerte pro Stueck:  Energie kJ/kcal 1354/324  Eiweiss 2,3 g  Fett 13,3 g  Kohlenhydrate 47,2 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(22)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:  Spargel putzen, den weissen Spargel ganz, bei dem gruenen Spargel nur das untere Drittel schaelen und den Spargel in ca. 5 cm lange Stuecke schneiden. 1,5 Liter Wasser mit 1 TL Salz, 1 Prise Zucker und Margarine aufkochen, Spargel dazugeben und ca. 10 Minuten garen. Gruenen Spargel erst nach 5 Minuten Garzeit zufuegen. Spargel abgiessen und dabei das Spargelwasser auffangen.  Backofen auf 180 Grad C (Gas: Stufe 3, Umluft 160 Grad C). vorheizen.  Mini-Knoedel nach Packungsanweisung ca. 8 Minuten garen. Schinken in Streifen schneiden.  Fuer die Sosse Margarine in einem Topf erhitzen, Mehl dazugeben und anschwitzen, Milch und 300 ml Spargelsud angiessen, aufkochen und mit Salz, Pfeffer und Muskat abschmecken. Fruehlingszwiebeln putzen, waschen und in feine Ringe schneiden. Die Haelfte der Fruehlingszwiebeln unter die Sosse mischen.  Spargel, Knoedel und Schinken in eine Gratinform (24 x 28 cm) geben, Sosse darueber giessen, Kaese ueberstreuen und ca. 30-35 Minuten goldbraun backen Restliche Fruehlingszwiebeln ueber das Gratin streuen und servieren.  Pro Portion:  kJ/kcal: 1500/358  EW: 19,9 g  F: 12,8 g  KH: 39,6 g  BE: 3,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(23)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200  Grad C Ober-/Unterhitze vorheizen.  Ein Backblech mit Backpapier auslegen. Mit nicht zu wenig Olivenoel bestreichen. Die Kartoffeln in duenne Scheiben gefaechert auf dem gefetteten Papier auslegen. Zwischen den Reihen etwas Platz lassen.  Geschaelten Knoblauch waagerecht halbieren und wie den Rosmarin unter die Kartoffelscheiben legen. Salzen, pfeffern und die Kartoffelscheiben noch mal mit oel bestreichen.  Auf mittlerer Hoehe die Kartoffeln 35 min bei 200 Grad C backen. Sie sollten leicht knusprig und leicht gebraeunt sein.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(24)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Gnocchi nach Packungsanweisung kochen.  Die Paprikaschote putzen und in einer Kuechenmaschine puerieren. Die Knoblauchzehe abziehen, pressen und in etwas Olivenoel anbraten. Das Paprikapueree zufuegen und kurz mitbraten. Die passierten Tomaten zugeben, dann den Frischkaese unterruehren und aufkochen lassen. Mit Salz, Pfeffer, Oregano und Bruehe abschmecken.  Eine Auflaufform einfetten und die Gnocchi darin verteilen, die Sauce darueber geben. Den Mozzarella in Scheiben schneiden, den Parmesan reiben und beides obendrauf verteilen.  Im vorgeheizten Backofen bei 180  Grad C ca. 15 Minuten ueberbacken. Sofort servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(25)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Rezept stammt von einer Chinareise aus der Stadt Chongqing.  Zunaechst den Boden des Wok grosszuegig mit oel bedecken und dieses auf hoechster Stufe erhitzen. Das Geschnetzelte rundherum mit Mehl bestaeuben und im Wok scharf anbraten, dann salzen. Das Fleisch herausnehmen, evtl. etwas oel nachgeben und die gehackten Erdnuesse leicht anbraten. Die Erdnuesse herausnehmen und die Zwiebeln anbraten. Anschliessend den gehackten Knoblauch hinzugeben und ebenfalls anbraten. Die Fruehlingszwiebeln und die Chilischoten in Streifen schneiden und hinzugeben. Den Zucker darueber streuen und karamellisieren lassen.  Fleisch und Erdnuesse wieder hinzugeben. Mit Wein abloeschen, aufkochen lassen und den Essig hinzugeben. Abschliessend mit Sojasauce, Ingwer und Pfeffer (gut zerkleinern, sehr intensiv!) wuerzen und abschmecken.  Auf Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(26)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln in 0,5 cm grosse Wuerfel schneiden, Karotte und Sellerie wuerfeln. Alles in 2 EL Butterschmalz kraeftig anbraten. Tomatenmark zugeben und anduensten bis sich eine homogene Masse bildet, das Mark darf ruhig ein bisschen ansetzen. Paprikapulver kurz mitroesten (Vorsicht, darf nicht verbrennen!). Mit dem Rotwein und der Bruehe abloeschen und zum Kochen bringen. Jetzt erst das gewuerfelte Fleisch dazu geben, wieder aufkochen und bei kleiner Hitze mit den Lorbeerblaettern ca. 2 Stunden koecheln lassen.  Durch das Gemuese ist es normalerweise nicht noetig, die Sauce zu binden. Wenn sie allerdings zu fluessig ist, kann man das Gulasch mit 1 EL in kaltem Wasser aufgeloestem Staerkemehl andicken. Dann noch abschmecken mit Salz und Pfeffer. Die Lorbeerblaetter fische ich nach Moeglichkeit vor dem Servieren raus.  Dies ist ein Grundrezept fuer Gulasch, man kann es wunderbar abwandeln, indem man z. B. eine halbe Stunde vor Ende der Garzeit noch Sahne, Kartoffeln und/oder Paprikaschoten zugibt. Ich gebe auch immer noch Knoblauch dazu, den mochte aber meine Oma nicht.  Dazu schmecken Knoedel jeglicher Art, Kartoffeln oder Nudeln.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(27)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz und Pfeffer wuerzen. Evtl. noch Kraeuter wie Oregano, Thymian und/oder Basilikum und nach Geschmack Knoblauch dazugeben. Ca. 12 - 15 kleine Baellchen aus der Masse formen und in eine Auflaufform legen.  Fuer die Tomatensosse die stueckigen Tomaten mit der Sahne, der Kraeutermischung, Tomatenmark und Zucker verruehren, dann mit Salz und Pfeffer abschmecken. Alles ueber die Hackbaellchen geben. Den Mozzarella in Scheiben schneiden und darueber verteilen.  Im heissen Backofen bei 175  Grad C Umluft ca. 30 - 40 min. garen. Aufpassen, dass der Kaese nicht zu dunkel wird.  Dazu passt Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(28)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 180 Grad C vorheizen.  Paprikaschoten halbieren, putzen, waschen und in Stuecke schneiden. Zwiebeln abziehen und in feine Ringe schneiden. Sauerkraut abtropfen lassen und gut ausdruecken.  Hackfleisch in erhitztem oel von allen Seiten anbraten. Paprika, Zwiebeln und Kartoffelnudeln hinzugeben, anduensten und mit Sauerkraut in eine Auflaufform geben. Schmand mit Milch verruehren, mit Salz und Pfeffer abschmecken, ueber die Zutaten giessen, mit Kaese bestreuen und im vorgeheizten Backofen ca. 20-30 Min. backen (Gas: Stufe 3, Umluft: 160 Grad C).  Pro Portion:  kj/kcal: 3232/774  EW: 39,3 g  F: 47,0 g  KH: 45,0 g  BE: 3,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(29)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis nach Packungsanleitung kochen.  Das Fleisch haeuten, waschen und in spielwuerfelgrosse Stueckchen schneiden. Mit etwas oel in der Pfanne anbraten. Wenn es leicht Farbe bekommt, den Honig dazu geben. Fruehlingszwiebeln und Knoblauch dazu, kurz mit anschwitzen. Die Ananas abtropfen lassen und den Saft auffangen, dann die Ananasstuecke mit in die Pfanne geben und auch kurz mit anschwitzen. Den Curry dazu geben und kurz alles durchroesten.  Mit Sahne abloeschen. Den Schmelzkaese in Stueckchen dazu geben und schmelzen lassen. Alles aufkochen lassen, mit Salz, Pfeffer, Curry, Instantbruehe, etwas gemahlenem Chili und dem Ananassaft abschmecken und dann auf dem Reis servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(30)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Haehnchenbrust in Stuecke schneiden. Aus 1 TL Paprikapulver, 1 EL Limonen- bzw. Zitronensaft, 1 TL Salz, 1 Becher Joghurt, 1 TL Cayennepfeffer, 1 EL Garam Masala Pulver, 1 Stueck Ingwer und 1 Knoblauchzehe eine Marinade herstellen. Das Fleisch mit der Marinade mischen.  Mindestens eine Stunde einziehen lassen. Besser ist es, das Fleisch bereits am Vortag zu marinieren und ueber Nacht in den Kuehlschrank zu stellen.  Den Ofen auf 200  Grad C Ober-/Unterhitze vorheizen dann das Fleisch in einer Auflaufform fuer 25 Minuten garen.  Die Zwiebel klein hacken und in 2 EL Butter glasig anschwitzen. Die passierten Tomaten, den Zimt, 1 TL Salz, 2 TL Cayennepfeffer, 1 Stueck Ingwer und 1 Knoblauchzehe hinzugeben. Alles 20 Minuten mit Deckel und bei niedriger Temperatur koecheln lassen. Gelegentlich umruehren. Nun die restlichen 2 EL Butter, den Honig und die Sahne hinzufuegen, weitere 3 Minuten koecheln. Das Fleisch aus der Marinade nehmen, in die Sosse geben, kurz umruehren und 2 Minuten mitkoecheln lassen.  Dazu passt Reis oder Naan.  Wer gerne Koriandergruen mag, der kann ganz am Ende noch ein paar frisch gehackte Blaetter hinzufuegen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(31)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Huehnerfleisch in mundgerechte Wuerfel schneiden, die Zwiebel klein hacken, die Knoblauchzehen fein hacken, die Kardamomkapseln zerdruecken und mit den Nelken im Moerser klein mahlen.  Das oel in einem mittelgrossen Topf erhitzen, Zwiebeln und das Nelken-Kardamom-Gemisch darin anduensten und glasig werden lassen. Jetzt Huehnerfleisch, Knoblauch und das Ingwerpueree dazugeben und weitere 4 Minuten unter Ruehren durchbraten. Die restlichen Gewuerze dazugeben, einige Minuten weiterruehren und dabei das Ganze sehr gut durchmischen und durchkochen lassen. Tomatenpueree, Mandelmehl, Bruehe und Sahne nacheinander einruehren, aufkochen und bei kleiner Flamme dann 15 - 20 Minuten koecheln lassen, bis eine dick-cremige Konsistenz erreicht ist.  Dazu passen Reis oder Naan-Brot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(32)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln al dente kochen und erkalten lassen. Cocktailtomaten, getrocknete Tomaten und Oliven zerkleinern und mit den gekochten und erkalteten Nudeln mischen.  Aus den Sossenzutaten eine Vinaigrette nach eigenem Geschmack herstellen und mit dem Salat vermengen. Dabei auf die Intensitaet des oels aus dem Glas getrocknete Tomaten achten. Den Parmesan (am besten vom Stueck grob gehobelt) ebenfalls unter den Salat mengen.  Am besten 2 - 3 Stunden im Kuehlschrank ziehen lassen. Nun evtl. nochmals nachwuerzen und wenn noetig, das Verhaeltnis aus oel und Balsamico weiter verfeinern.  Den Rucola waschen, grob zerkleinern und erst vor dem Servieren mit dem Salat mischen. Zuletzt die Pinienkerne in der Pfanne kurz anroesten und auf den bereits auf Tellern angerichteten Salat geben. Am besten mit frischem Ciabatta und einem leckeren Rotwein servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(33)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Im lauwarmen Wasser und dem Olivenoel die Hefe mit dem Salz und Zucker aufloesen. Dann das Mehl hinzufuegen und einen glatten Teig kneten. Eine halbe Stunde an einem warmen Ort gehen lassen, zusammenkneten und abgedeckt im Kuehlschrank 2 Tage ruhen lassen.  Nun kann man vom Teig eine herrlich frische Pizza herstellen.  Der Teig reicht fuer 6 runde Pizzen.  Anmerkungen: Belegen kann man diese nach Belieben, natuerlich sollten die Tomatensosse und der Kaese nicht fehlen. Ich habe sie schon auf einem Blech sowie auf verschiedenen runden Pizzaformen gebacken. Sie wird immer supertoll und schmeckt original wie von meinem Lieblingsitaliener. Wenn man die Menge entsprechend reduzieren moechte, ist das auch kein Problem. Die Menge der Hefe habe ich jedoch immer bei 40 g gelassen.  Am besten gelingt die Pizza, wenn man den Ofen sehr gut auf der hoechstmoeglichen Temperatur vorheizt!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(34)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eier, Zucker, oel und Zimt mit dem Mixer verruehren. Die Karotten und Mandeln hinzugeben. Mehl und Backpulver mischen, ebenfalls unterruehren. Den Teig in eine gefettete 26er Springform fuellen, bei 180  Grad C Ober-/Unterhitze 40 - 50 Minuten backen. Man sollte eine Staebchenprobe machen und die Erfahrungswerte mit dem eigenen Backofen beruecksichtigen.  Fuer das Frosting Frischkaese und Zitronensaft mit dem Mixer auf niedriger Stufe glatt ruehren. Puderzucker und Vanillezucker einrieseln lassen.  Nach dem Backen den Kuchen abkuehlen lassen. Das Frosting mit der Streichpalette rundherum auftragen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(35)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln ungepellt und gewaschen ca. 15 min kochen. Sie sollen gar werden, aber nicht zu weich.  In der Zwischenzeit die Fruehlingszwiebeln und den Schnittlauch waschen und in kleine Stuecke schneiden. Die Fruehlingszwiebeln zusammen mit dem Speck im Sonnenblumenoel ca. 5 min braten und mit Pfeffer wuerzen.  Den Backofen auf ca. 200  Grad C Ober/Unterhitze vorheizen. Das Speck-Fruehlingszwiebel-Gemisch in einen tiefen Teller geben und die Crème fraîche und die Haelfte des Goudas hinzugeben. Mit etwas Salz und den Kraeutern der Provence wuerzen und gut mischen.  Die fertigen Kartoffeln abgiessen, in der Mitte laengs teilen und etwas abkuehlen lassen. Mit einem Teeloeffel mittelgrosse Mulden aushoehlen und die Fuellung auf die Haelften verteilen. (Die Fuellung darf gerne ueber die Mulden drueber gehen.)  Die Kartoffelhaelften auf ein Backblech auf Backfolie legen, sodass sie nicht umfallen. Den restlichen Gouda darauf verteilen. Auf der mittleren Schiene in 10 bis 15 min goldbraun ueberbacken.  Die Kartoffeln aus dem Ofen nehmen und mit Schnittlauch bestreut servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(36)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Hackfleisch mit Salz, Pfeffer, Tomatenmark, Ketchup, Oregano und einer halben klein gehackten Zwiebel vermengen. Die Hackfleischmasse dann in einer grossen Pfanne mit etwas Olivenoel kruemelig braten und abkuehlen lassen.  Die Kritharaki (gibt es in jedem gut sortierten Supermarkt dort, wo auch Couscous und Bulgur zu finden sind) in Salzwasser ca. 14 Minuten garen und abgiessen.  Die Paprikaschoten sehr klein wuerfeln (Reiskorngroesse), die restliche halbe Zwiebel ebenfalls und in drei Beuteln Salatfix Gartenkraeuter mit etwas oel ziehen lassen.  Es muessen keine Fertigprodukte sein. Ein selbst gemachtes Kraeuterdressing auf Essigbasis tut es auch.  Die abgegossenen Nudeln mit den Hackfleischbroeseln vermengen. Dann die marinierten Paprikawuerfel dazugeben. Alles vermengen und gut durchziehen lassen.  Der Salat schmeckt superlecker, frisch und ist schnell zuzubereiten. Auch rein optisch ein Hingucker, aufgrund der Reisnudeln. Wir essen den Salat - trotz des Fleischanteils - auch gern als Beilage zum Grillen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(37)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 175  Grad C Ober-/Unterhitze vorheizen.  Die Baguettes in den vorgeheizten Ofen legen und ca. 10 Minuten backen.  Derweil oel in einen grossen Topf geben. Das Hackfleisch darin von allen Seiten gut anbraten und mit Salz und Pfeffer wuerzen. Den Lauch putzen, in kleine Ringe schneiden und zum Hackfleisch geben. Ca. 5 Minuten mit anbraten. Das Wasser zugiessen, Bruehwuerfel hineingeben und alles ca. 10 Minuten auf kleiner Flamme koecheln lassen. Den Schmelzkaese einruehren und schmelzen lassen. Crème fraîche untermengen und noch einmal kurz aufkochen lassen. Die Suppe mit Salz, Pfeffer, Muskat, Knoblauch- und Zwiebelpulver kraeftig abschmecken.  Die Baguettes in Scheiben schneiden und zu der Suppe reichen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(38)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Kuerbis, Moehren, Ingwer und Zwiebel schaelen und wuerfeln, in der Butter anduensten. Mit der Bruehe aufgiessen und in etwa 15 - 20 Minuten weich kochen. Dann sehr fein puerieren, eventuell durch ein Sieb streichen. Die Kokosmilch unterruehren, mit Salz, Pfeffer, Sojasauce und Zitronensaft abschmecken und noch mal erwaermen. Mit Korianderblaettchen garniert servieren.  Eine schnelle, leicht exotische Suppe, schoen im Menue. Ich benutze fuer diese Suppe immer einen Hokkaido, den muss man nicht schaelen. In Thailand isst man Kuerbissuppe mit kleinen Garnelen als Einlage.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(39)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Ragú Bolognese:  In einem Topf das Olivenoel erhitzen, das Hackfleisch darin rundherum anbraten und die gehackten Zwiebeln und die gehackte Petersilie dazugeben. Knoblauch in feinen Scheiben und Tomatenmark dazu ruehren und mitbraten. Mit den Dosentomaten aufgiessen, salzen und pfeffern. Rotwein nach Belieben beifuegen. Das Ragú mindestens eine halbe Stunde lang bei geoeffnetem Topf einkochen lassen.  Béchamelsauce:  Butter in einem kleinen Topf schmelzen und das Mehl mit dem Schneebesen unterruehren und hellgelb anschwitzen. Die Milch dazugiessen und die Sauce glatt ruehren. Wer zu langsam geruehrt hat und Kluempchen in der Sauce findet, kann die Sauce durch ein feines Haarsieb passieren und dann weiterkochen lassen. Die Sauce sollte fast eine halbe Stunde lang auf kleiner Flamme koecheln, damit sie den Mehlgeschmack verliert. Mit Salz, Pfeffer und Zitronensaft sowie etwas Muskatnuss abschmecken.  Zubereitung der Lasagne:  In einer gebutterten, feuerfesten Form etwas Ragú Bolognese verteilen, eine Schicht Lasagneplatten darauf legen, die Nudelschicht wieder mit Ragú und dann mit einer Schicht Béchamel bedecken.  Anschliessend wieder eine Schicht Nudeln, Ragú und Béchamel. So Schicht fuer Schicht die Form fuellen.  Die letzte Schicht sollte die Béchamelsauce bilden. Dick mit geriebenem Kaese bestreuen und Butterfloeckchen darauf setzen.  Die Lasagne im heissen Backofen bei 180  Grad C Umluft ca. 30 - 40 Minuten backen, bis die Kruste goldbraun ist.  Tipp:  Die Lasagne kann man auch gut einen Tag vorher vorbereiten und im Kuehlschrank ziehen lassen.  Als Vorspeise empfehle ich Honigmelone mit Parmaschinken und als Nachspeise einen Beerenmix an Quark-Joghurt-Sahne-Creme mit brauner Zuckerkruste.  Pro Portion 1122 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(40)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Hackfleisch in einem grossen Topf anbraten. Zwiebel und Knoblauch klein hacken und dazugeben. Karotten schaelen, in kleine Scheiben schneiden und zum Hackfleisch geben. Alles 5 Minuten unter gelegentlichem Ruehren weiter braten. Tomatenmark hinzugeben und gut vermischen. Dann mit der Bruehe abloeschen, aufkochen und bei geringer Hitze 40 Minuten zugedeckt koecheln lassen.  Die Paprika in kleine Sticks schneiden und ca. 10 Minuten vor Ende der Kochzeit hinzufuegen. Zum Schluss noch mit Salz und Pfeffer abschmecken.  Anrichten und auf jeden Teller einen Klecks Crème fraîche geben.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(41)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Gefluegelfleisch, Champignons und Tomaten klein schneiden.  Das Fleisch in etwas oel anbraten und mit ein wenig Chiliflocken sowie Salz und Pfeffer wuerzen. Danach die Zwiebeln und Champignons dazugeben und 3 - 4 Minuten braten. Zum Schluss die restlichen Zutaten zugeben und umruehren. Weitere 5 Minuten leicht koecheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(42)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170  Grad C Ober-/Unterhitze vorheizen.  Fuer den Boden Quark, Eier und 120 g Kaese in einer Schuessel miteinander verruehren und wuerzen. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im heissen Ofen backen.  Das Backblech herausnehmen und den Boden beliebig belegen mit z. B. Tomatensauce, Salami, Schinken, Zucchini, Champignons oder Mais. Mit 60 g Kaese bestreuen und erneut in den Ofen schieben, bis der Kaese eine schoene Farbe hat.  Abkuehlen lassen, mit Rucola bestreuen und vorsichtig einrollen.  Eingerollt in Alufolie mehrere Tage im Kuehlschrank haltbar.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(43)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 170  Grad C Ober-/Unterhitze vorheizen.  Fuer den Boden Quark, Eier und 80 g vom Kaese in einer Schuessel miteinander verruehren. Die Masse auf das mit Backpapier ausgelegte Backblech kippen und glatt streichen. 15 Minuten im Ofen backen.  Das Backblech herausnehmen, den Kuchenboden mit Crème fraîche bestreichen und mit Speckwuerfeln, Lauchzwiebeln und dem restlichen Kaese bestreuen. Weitere 15 - 20 Minuten backen, bis der Kaese eine schoene Farbe hat.  Kann als Flammkuchen oder als Rolle gegessen werden.  Der Flammkuchen hat ca. 6 g Kohlenhydrate.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(44)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Magerquark, Reibekaese und Eier zu einer dickfluessigen Masse verruehren und auf einem mit Backpapier ausgelegten Backblech verteilen. Bei 180  Grad C Ober-/Unterhitze im heissen Backofen ca. 20 Minuten backen. Den Teig auskuehlen lassen.  Die Zutaten fuer die Sauce verruehren.  Das Hackfleisch in einer Pfanne mit Salz und Pfeffer kruemelig anbraten. Die Gurken in Scheiben schneiden und zum Hackfleisch geben. 2/3 der Sauce auf dem gebackenen Teig verteilen. Das noch warme Hackfleisch darueber verteilen und den Toastkaese ueber dem Hackfleisch schmelzen lassen.  Anschliessend Salat und evtl. Tomaten darauf legen und die restliche Sauce darauf verteilen. Den Teig mithilfe des Backpapiers einrollen, so dass die Big Mac Rolle aussieht wie eine Biskuitrolle.  Wichtig ist, nicht zu viel auf dem Teig zu verteilen, da die Rolle sonst zu dick wird und die Fuellung an beiden Enden hervorquillt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(45)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Haehnchenbrust saeubern und in mundgerechte Stuecke schneiden. In einer Pfanne mit etwas Pflanzenfett anbraten, bis das Fleisch schoen knusprig ist. Mit etwas Salz, Pfeffer und Curry wuerzen.  In der Zwischenzeit Zucchini, Gurke und Tomaten klein schneiden. Haehnchen beiseitelegen und warm halten.  In der gleichen Pfanne Zwiebeln und Knoblauch anbraten. Zucchini dazugeben und duensten, bis diese weich aber noch bissfest sind. Gurke und Tomaten dazugeben und ca. 4 Minuten duensten. Evtl. einen Schuss Wasser dazugeben.  Frischkaese und Milch einruehren. Haehnchenfleisch in die Pfanne geben und mit geschlossenem Deckel bei schwacher Hitze ca. 5 - 10 Minuten koecheln lassen, bis die Sauce cremig wird. Mit Paprika abschmecken.  Tipp: Man kann auch eine rote Paprikaschote zusammen mit der Zucchini dazugeben.  Dazu passt sehr gut mein Erdbeer-Avocado-Salat: http://www.chefkoch.de/rezepte/2762181428080627/Erdbeer-Avocado-Salat.html")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(46)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Lachsfilet, falls TK, etwas antauen lassen. Waschen und trocken tupfen. Mit Salz und Pfeffer, nach Wunsch auch mit Kraeutern, wuerzen.  Schafskaese in Wuerfel schneiden. Die Zucchini und Pilze in duenne Scheiben, die Paprika in Streifen schneiden. Tomaten halbieren oder vierteln. Knoblauch fein hacken. Das Gemuese mit Knoblauch, Salz und Pfeffer sowie ein paar Spritzern Chilioel in einer Schuessel vermengen.  Auf einem Backblech aus Alufolie* eine Schuessel formen, d.h. die Raender an 4 Seiten hochschlagen. Ich empfehle 2 Schichten Alufolie zu nehmen, dann kann nichts auslaufen. Anschliessend das Gemuese darauf verteilen. Dann den Lachs darauf legen, mit ein bisschen Chili-oel betraeufeln und den Schafskaese grosszuegig darueber kruemeln.  Bei 180  Grad C Ober-/Unterhitze ca. 30 - 35 Minuten im heissen Ofen garen.  *Anmerkung der Chefkoch.de Rezeptbearbeitung:  Wie auf vielen Bildern zu sehen ist, kann man auch eine Auflaufform verwenden. Das Gericht gelingt darin genau so gut.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(47)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Cashewkerne mit dem Currypulver in einer Pfanne bei schwacher Hitze 3 Minuten trocken roesten. Den Ingwer schaelen und reiben, den Knoblauch in kleine Stuecke schneiden.  Die Cashewkerne zusammen mit Ingwer, Knoblauch, Essig, Tomatenmark und Joghurt in einer Kuechenmaschine oder im Mixer puerieren. Die so entstandene Paste mit dem Fleisch in einer Schuessel vermischen und alles 24 Stunden im Kuehlschrank durchziehen lassen.  In einer grossen Pfanne oder einem grossen Topf die Butter zerlassen. Zwiebel, Zimt, Salz und Kardamom bei mittlerer Hitze ca. 5 Minuten anduensten, bis die Zwiebel weich ist. Das Fleisch mit der Marinade dazugeben und 10 Minuten kochen lassen. Die Chiliflocken, gehackte Tomaten aus der Dose und die Gemuesebruehe dazugeben und aufkochen lassen. Die Hitze reduzieren und ohne Deckel 40 - 45 Minuten koecheln lassen. Kurz vor dem Servieren die Sahne unterruehren und das Gericht mit dem gehackten Koriander bestreuen.  Dazu passt wunderbar Basmatireis oder Naanbrot.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(48)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Teigzutaten verkneten und einen geschmeidigen, nicht mehr klebenden Teig herstellen. Zwei Muffinbackformen mit je 12 Muffinmulden fetten und den Teig in den Mulden verteilen, dabei jeweils auch einen kleinen Rand andruecken.  Paprika und Lauch putzen und waschen, Zwiebel schaelen, alles fein hacken und in einer Pfanne mit etwas oel ca. 5 Minuten anduensten. Die Haelfte des Gemueses in eine Schuessel fuellen und abkuehlen lassen.  Getrocknete Tomaten abtropfen lassen, in kleine Stuecke schneiden. Schinken wuerfeln. Die Tomaten zur einen, den Schinken zur anderen Gemuesehaelfte geben. So erhaelt man nachher 12 Miniquiches fuer Schinkenliebhaber und 12 fuer Vegetarier.  Die Gusszutaten miteinander verquirlen und jeweils wieder halb und halb mit dem Gemuese mischen.  Dieses dann auf den Teig in den Muffinmulden geben.  Im vorgeheizten Backofen bei 180  Grad C Ober-/Unterhitze ca. 20 - 25 Minuten backen.  Diese Mini-Quiches passen super zu einem kalten Bufett oder als Fingerfood auf einer Party.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(49)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fleisch waschen und trocken tupfen. Mit Salz und Pfeffer wuerzen. oel in einer Pfanne erhitzen. Filets darin von allen Seiten ca. 5 Min. kraeftig anbraten.  Tomaten waschen und halbieren. Basilikumblaetter abzupfen, waschen und fein hacken.  Sahne in einem Topf aufkochen lassen. Schmelzkaese hineinruehren und schmelzen lassen. Mit Salz und Pfeffer wuerzen. 2/3 vom Basilikum unterruehren.  Fleisch und Tomaten in eine gefettete Auflaufform geben. Sauce darueber giessen. Mozzarella in kleine Stueckchen schneiden und auf dem Fleisch verteilen. Wer mag, kann noch geriebenen Parmesan und 1 EL Kraeuterbutter in kleine Floeckchen darauf verteilen.  Im vorgeheizten Ofen bei 200  Grad C Ober-/Unterhitze bzw. 175  Grad C Umluft ca. 30 Min. backen. Herausnehmen und mit restlichem Basilikum bestreuen.  Dazu schmecken Kroketten oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(50)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Eine flache Platte (oder einen grossen Teller) in den Backofen stellen und diesen mit 80  Grad C ca. eine halbe Stunde vorheizen. Temperatur wenn moeglich mit Backofenthermometer kontrollieren.  Schweinefilet 1 Stunde vor dem Anbraten aus dem Kuehlschrank nehmen, damit das Fleisch auch im Kern Zimmertemperatur annimmt. Falls der Metzger es nicht schon vorher getan hat, das Fleisch parieren (d.h. von Sehnen, Haeutchen, Fett etc. befreien). Hat man ein ganzes Schweinefilet, dann schlaegt man die Spitze soweit um, dass in etwa ein gleichmaessig dickes Fleischstueck entsteht.  Filet salzen (nur wenig wegen des Speckmantels!) und pfeffern.  Baconscheiben ueberlappt auslegen, in einer Breite, die der Laenge des Filetstuecks entspricht. Beide Enden des Filets je nach Dicke mit ein bis zwei (evtl. halbierten) Baconscheiben abdecken, das Filet auf die ausgelegten Scheiben legen und einrollen. Die Speckhuelle entweder mit Kuechengarn oder (von mir aus Handhabungsgruenden bevorzugt) mit Rouladennadeln fixieren.  In einem grossen Schmortopf oel bzw. Butterschmalz erhitzen und das Filet in ca. 6 Minuten von allen Seiten braun/kross anbraten. Auch die beiden Kopfseiten sollten dabei angebraten werden, dabei das Filet mit Hilfe von einer Kuechenzange oder gefaltetem Kuechenpapier senkrecht halten. Anschliessend das Fleisch mit einem Bratenthermometer versehen fuer ca. 2 Stunden in den vorgeheizten Backofen auf die Platte/den Teller legen und auf die gewuenschte Kerntemperatur bringen (ca. 60  Grad C fuer einen rosa Kern).  Den Bratensatz im Schmortopf entfetten und mit etwas Weisswein oder Bruehe loesen, dann fuer den spaeteren Gebrauch beiseitestellen.  Eine halbe Stunde vor Garende des Fleisches die Zwiebeln schaelen und wuerfeln, Knoblauchzehen schaelen und in kleine Scheiben/Wuerfel schneiden sowie die Pilze saeubern und je nach Groesse in 2, 4 oder 6 Teile schneiden.  In einer grossen Pfanne die Butter zerlassen, den Schinkenspeck/Bacon anbraten, Zwiebeln und Knoblauch anschwitzen. Die Champignons und das Tomatenmark hinzufuegen, etwas pfeffern und salzen und so lange braten, bis kaum noch Fluessigkeit uebrig geblieben ist. Waehrenddessen Sahne, Crème fraîche, Bruehe und Wein im Schmortopf mit dem geloesten Bratensatz zusammen erhitzen. Gleichzeitig kann man auch schon das Wasser fuer die Spaetzle aufsetzen.  Die gebratenen Champignons in den Schmortopf geben und ca. 5 Minuten leicht koecheln lassen, dabei nach Belieben klein gehackte Kraeuter hinzufuegen. Anschliessend mit Worcestersosse, Salz und Pfeffer abschmecken. Wem das Champignongemuese zu fluessig ist, kann gegebenenfalls noch mit Mehl/Mondamin andicken.  Die Spaetzle nach Anweisung im Salzwasser mit 2 EL oel bissfest kochen, abgiessen und - wenn sie nicht direkt auf die vorgewaermten Teller verteilt werden - kurz in etwas zerlassener Butter schwenken.  Das Fleisch aufschneiden (scharfes oder Elektromesser laesst den krossen Schinkenspeck heil an den Fleischscheiben) und mit Champignongemuese und Spaetzle servieren.  Fuer Interessierte noch einige Tipps:  Es empfiehlt sich, die Essteller von vornherein mit der Fleischplatte mit vorzuwaermen. Sie sind dann zwar relativ heiss (80  Grad C), das ist aber auch guenstig, da beim NT-Garen das Fleisch naturgemaess nicht sehr heiss auf den Teller kommt und dann noch schneller auskuehlen wuerde. Zwischendurch sollte man sie nicht in den Ofen zum Fleisch stellen, da das den NT-Garvorgang zu stark unterbricht.  Beim Anbraten der Filet-Enden hat sich bei mir das Halten des Filets mit Kuechenpapier in der Hand durchgesetzt. Dazu faltet man ein Blatt Kuechenpapier zweimal und achtet nur darauf, dass man sich nicht am heissen Fett verbrennt bzw. das Papier das heisse Fett aufsaugt. Man kann dann das Filet bequem ca. 30 sec. senkrecht halten, fuers Anbraten des Endes. Das Problem bei der Kuechenzange ist, dass man damit die Baconhuelle doch viel leichter verschiebt oder sogar zerstoert.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(51)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln kochen und mit kaltem Wasser abschrecken. Die Pinienkerne in einer Pfanne bei mittlerer Hitze ohne Fett leicht anbraeunen. Rucola gut waschen, trocken schleudern und etwas kleiner schneiden. Die getrockneten Tomaten gut abtropfen lassen und wie den Mozzarella und den Parmaschinken klein schneiden. Alles in eine grosse Schuessel geben, salzen und pfeffern.  oel, Essig, klein gehackte oder gepresste Knoblauchzehe, Pesto, Senf und Honig miteinander vermischen und kurz vor dem Essen ueber den Salat geben. Alles noch einmal gut durchmischen und mit dem geriebenen Parmesan garnieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(52)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln im Salzwasser al dente kochen, abkuehlen lassen. In der Pfanne die gehackte Zwiebel mit dem Knoblauch anschwitzen, das Fleisch hinzu fuegen und gut anbraten. Die klein gewuerfelten Tomaten zufuegen und mit Tomatenmark, den Gewuerzen, schoen pikant abschmecken.  Nacheinander Nudeln, Joghurt sowie die Hackfleischmischung in die Schuessel fuellen und alles gut vermengen. Zum Schluss mit der klein gehackten Petersilie bestreuen, aber erst kurz vor dem Anrichten untermengen.  Den Salat im Kuehlschrank gut durchkuehlen lassen. 1 Stunde vor dem Verzehr heraus nehmen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(53)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Nudeln nach Packungsanweisung bissfest kochen.  In der Zwischenzeit die Tomaten klein schneiden und den Schafskaese wuerfeln. Den Knoblauch abziehen, durchpressen oder winzig klein schneiden. Die Pinienkerne vorsichtig in einer Pfanne ohne Fett anroesten (Vorsicht - sie werden schnell schwarz!). Die Basilikumblaetter klein reissen oder schneiden.  Die gekochten Nudeln abgiessen und nun alles zusammen in eine Schuessel geben. Nun das Olivenoel (die Menge ist geschaetzt) darueber geben und mit Salz und Pfeffer abschmecken.  Tipp: Bei uns wird die erste Portion immer noch warm gegessen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(54)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Broetchen in Wasser einweichen.  Die Zwiebel schaelen und in feine Wuerfel schneiden. Wer moechte, kann die Zwiebel auch kurz in Butter glasig duensten (ich bevorzuge die rohen Zwiebeln).  Das Ei, die Zwiebeln und die Gewuerze zur Hackmasse geben und sehr gut vermengen, entweder mit einem grossen Loeffel oder mit den Haenden. Nicht mit dem Mixer arbeiten, dabei werden die Frikadellen oft zaeh!  Die Broetchenmasse sehr gut ausdruecken, entweder mit den Haenden, oder auch zwischen zwei Brettchen, zur Hackmasse geben und wieder gut vermengen. Bis hierhin sollten diese Arbeitsschritte wenigstens 10 - 15 Minuten dauern, denn je ordentlicher vermengt und geknetet wird, umso besser und lockerer das Ergebnis!  Wer die rohe Masse abschmecken kann, sollte das jetzt tun, oder eine Probe braten. Jetzt gleichmaessige, nicht zu kleine Baellchen/Kloesse/Klopse formen und auf einer bemehlten Arbeitsflaeche flachdruecken und glaetten. Wer moechte, kann sie in Mehl oder Semmelbroesel wenden. Oma und ich braten sie ohne alles.  Eine schwere Pfanne mit guter Margarine stark erhitzen und die Frikadellen einlegen, kurz auf beiden Seiten scharf anbraten und dann ca. 15 - 20 Minuten (1 - 2-mal vorsichtig wenden) auf mittlerer/schwacher Hitze fertig braten. Nicht zu viele Frikadellen auf einmal in einer Pfanne braten, eher eine zweite benutzen oder nacheinander braten.  Dazu passt z. B. Kartoffelsalat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(55)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln wuerfeln und mit dem Hackfleisch in Olivenoel anbraten. Die Paprikaschoten ebenfalls wuerfeln und mit den Champignons sowie dem Mais zum Hackfleisch geben. Alles kurz anbraten, anschliessend mit der Gemuesebruehe abloeschen. Die Sahne, die Tomatensauce und den Sahneschmelzkaese hinzugeben und ca. 10 Minuten koecheln lassen. Zum Schluss mit Salz, Pfeffer und Oregano abschmecken.  Beim Servieren nach Belieben etwas geriebenen Parmesan auf die Suppe streuen.  Dazu passt am besten Baguette.  Tipp: Schmeckt auch als Nudelsauce gut, dann weniger Gemuesebruehe verwenden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(56)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Reis in der Gemuesebruehe garen (eine Tasse mit ca. 200 - 250 ml Inhalt als Mass nehmen).  Die Chilischote laengs halbieren, von den Kernen befreien und hacken. Die Paprikaschoten putzen und wuerfeln. Die Zwiebeln fein wuerfeln und in einer Pfanne in etwas oel glasig duensten. Den gepressten Knoblauch, die Chilischote und das Tomatenmark hinzugeben und kurz mit anschwitzen. Die Paprikawuerfel in die Pfanne geben und ein paar Minuten lang anbraten, dabei ab und zu die Pfanne schwenken. Mit Paprikapulver, Salz und Pfeffer wuerzen. Den Reis hinzugeben, untermengen und heiss werden lassen. Die Kraeuter hacken und zuletzt untermischen. Nochmals abschmecken.  Joghurt und gepressten Knoblauch verruehren, mit Salz und Pfeffer abschmecken. Den Reis mit einem Klecks von der Joghurtsauce servieren.  Von der Menge werden ca. 3 - 4 Personen satt. Der Reis kann auch als Beilage gegessen werden.  Die Kraeutermenge kann nach Belieben erhoeht werden.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(57)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Haehnchenfilets waschen und mit Kuechenkrepp trocken tupfen. Mit Salz und Paprikapulver wuerzen und in einer Auflaufform dicht aneinanderlegen. Die Paprikaschoten waschen, entkernen, in schmale Streifen schneiden und auf den Filets verteilen.  Die Zwiebel in halbe Ringe schneiden und in einer Pfanne in etwas oel anduensten. Die Chilischote hineinzupfen, den Knoblauch pressen und hinzugeben. Paprikapulver und Tomatenmark hinzufuegen, mit der Bruehe abloeschen und kurz aufkochen lassen. Anschliessend Sahne und Schmand unter die Sosse ruehren und mit Salz abschmecken. Die Sosse in die Auflaufform giessen, Fleisch und Paprikastreifen sollten ganz bedeckt sein. Den geriebenen Kaese gleichmaessig darauf verteilen.  Im vorgeheizten Backofen bei 180  Grad C Ober-/Unterhitze ca. 1/2 Std. garen.  Beilagen: Bandnudeln oder Reis und Eisbergsalat mit Mandarinen und suess-saurer Vinaigrette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(58)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln in Spalten schneiden und in einer Schuessel mit Parmesan und Olivenoel vermischen. Die Gewuerze in einer separaten Schuessel vermengen und dann zu den Kartoffeln geben. Noch einmal kraeftig durchmischen, die Kartoffelecken dann auf einem mit Backpapier ausgelegten Backblech verteilen und bei 200  Grad C Ober-/Unterhitze fuer ca. 40 Minuten backen.  Hinweis: Heisshunger auf eine deftige Beilage oder einfach nur Appetit auf einen leckeren Snack? Diese Kartoffelecken sind genau das richtige fuer alle, die es gerne deftig moegen und etwas Neues ausprobieren wollen. Dazu schmeckt Sour Cream mit ein paar frischen Kraeutern wirklich koestlich, alternativ koennt ihr die Wedges natuerlich auch als Beilage zu einem leckeren Steak oder gebratenem Fisch servieren. Eurer Kreativitaet sind keine Grenzen gesetzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(59)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vorbereitende Schritte:  Die Butter wuerfeln und bei Raumtemperatur weich werden lassen.  Gruenes und rotes Pesto separat durch ein Sieb streichen und so etwas oel entfernen.  Mozzarella in Stuecke reissen.  Sonnengetrocknete Tomaten abtropfen lassen und fein hacken.  Die Oliven abtropfen lassen und grob hacken.  Erste Arbeitsschritte:  Zwei grosse Backbleche mit Backpapier auslegen.  Die groessere Ruehrschuessel einsetzen.  Den Spiral-Knethaken anbringen.  Schritt 1:  Die erste Zutat der Zutatenliste 1 (Milch) in einem kleinen Topf bei mittlerer Hitze erwaermen.  Vom Herd nehmen und in eine Karaffe giessen.  Die naechsten vier Zutaten der Zutatenliste 1 (Mehl, Hefe, Zucker, Salz) in die Ruehrschuessel geben. Den Spritzschutz anbringen.  20 Sekunden bei Geschwindigkeitsstufe 1 gut verruehren.  Waehrend die Kuechenmaschine langsam ruehrt, bei Geschwindigkeitsstufe 1 die warme Milch langsam dazugiessen.  Die naechsten zwei Zutaten der Zutatenliste 1 (Ei, Eigelb) hineingeben.  2 Minuten bei Geschwindigkeitsstufe 1 ruehren.  Nach und nach bei Geschwindigkeitsstufe 1 die letzte Zutat der Zutatenliste 1 (Butter) in die Ruehrschuessel geben.  6 bis 8 Minuten bei Geschwindigkeitsstufe 1 zu einem glatten und homogenen Teig ruehren.  Die Ruehrschuessel aus der Kuechenmaschine herausnehmen, mit Klarsichtfolie abdecken und an einem warmen Ort 1 Stunde gehen lassen.  Schritt 2:  Den Teig auf eine leicht bemehlte Arbeitsflaeche legen und flach druecken. Den Teig in 12 Portionen (je ca. 76 Gramm) teilen. Jedes Teigstueck zu einem festen Teigball formen.  Fuer die Pesto-Babki:  Sechs Teigbaelle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.  Die Zutaten der Zutatenliste 2 (Pesto, Mozzarella, schwarzer Pfeffer) ueber die Teigstuecke geben. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigstuecke vom langen Ende her zu einer Schlange fest aufrollen. Alle Naehte und Enden zusammendruecken. Mit einem scharfen Messer die Teigschlangen der Laenge nach halbieren. Die beiden halbierten Teigschlangen mit der gefuellten Seite nach oben zu einem Zopf flechten.  Den Hefezopf langziehen (25 cm). Beide Enden zusammenfuehren, sodass sie sich ueberlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendruecken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.  Schritt 3:  Die kleinere Ruehrschuessel einsetzen und den K-Haken anbringen.  Die Zutaten der Zutatenliste 3 (Pesto, Peperoni, sonnengetrocknete Tomaten, Oliven, Mozzarella, Oregano, schwarzen Pfeffer) in die Ruehrschuessel geben. Geschwindigkeitsstufe 1 einstellen, 20 Sekunden ruehren und in dieser Zeit auf Geschwindigkeitsstufe 3 erhoehen, um die Zutaten zu einer Paste zu ruehren.  Fuer die Pizza-Babki:  Die letzten sechs Teigbaelle zu einem Rechteck (ca. 12 x 7 cm) ausrollen.  Die Paste gleichmaessig ueber die Teigstuecke verteilen. Dabei rundum einen Rand von ca. 0,5 cm lassen. Die Teigstuecke vom langen Ende her zu einer Schlange fest aufrollen. Alle Naehte und Enden zusammendruecken. Mit einem scharfen Messer die Teigschlangen der Laenge nach halbieren. Die beiden halbierten Teigschlangen mit der gefuellten Seite nach oben zu einem Zopf flechten.  Den Hefezopf langziehen (25 cm). Beide Enden zusammenfuehren, sodass sie sich ueberlappen und in der Mitte ein Loch entsteht. Ein Teigende in das Loch geben und mit dem anderen Ende zusammendruecken. Auf ein Backblech legen. Mit Klarsichtfolie locker abdecken und 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.  Schritt 4:  Den Backofen auf 190  Grad C Ober-/Unterhitze vorheizen.  Die Klarsichtfolie entfernen. Babki mit verquirltem Ei (Eistreiche) bestreichen.  Im Backofen 12 bis 15 Minuten goldbraun backen.  Warm servieren.  Die herzhaften Babki schmecken nicht nur koestlich, sondern sind auch ein echter Hingucker auf dem Esstisch.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(60)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Ofen auf 170  Grad C Ober-/Unterhitze vorheizen.  Die TULIP Bacon-Scheiben auf ein mit Backpapier ausgelegtes Backblech legen.  Die Barbecuesauce mit braunem Zucker und Paprikapulver mischen. Die TULIP Bacon-Scheiben mit der Mischung gleichmaessig glasieren und im Ofen etwa 25 Min. auf der mittleren Einschubleiste kross backen. Anschliessend auf Kuechenpapier geben und 3 Min. ruhen lassen.  Mehl, Milch, Zucker, Eier, Butter und Salz zu einem glatten und dicken Pfannkuchenteig verruehren.  Die Pfannkuchen in einer heissen beschichteten Pfanne (Groesse nach Belieben) bei mittlerer Hitze von beiden Seiten goldbraun backen.  Serviervorschlag: Pfannkuchen mit Frischkaese, Ahornsirup und den knusprigen, glasierten Baconstreifen servieren. Nach Belieben mit frischen Johannisbeeren dekorieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(61)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Huehnerfleisch in kleine Stuecke schneiden und im Topf kurz anbraten. Die Fruehlingszwiebeln in Ringe schneiden und den Ingwer in kleine Stuecke. Beides zufuegen und kurz mitbraten.  Mit der Huehnerbruehe abloeschen. Kokosmilch, Sojasauce und Currypaste hinzufuegen. Das Zitronengras laengs kreuzweise einschneiden, sodass es noch am Stueck bleibt, dann kann man es spaeter einfacher wieder entnehmen, und in die Suppe geben.  5 Minuten kochen, das restliche Gemuese und die Gewuerze hinzufuegen. Die Nudeln nach Packungsangabe kochen und hinzufuegen.  Wer mag, kann noch ein wenig frischen Koriander aufheben und am Schluss ueber die Suppe streuen. Ich habe ab und zu noch getrocknete Chilifaeden zum Garnieren verwendet.  Anmerkung der Redaktion:  Viki roestet die Currypaste bereits zusammen mit Ingwer, Chili und etwas Speiseoel an, dadurch wird der Geschmack intensiver. Anstatt Fruehlingszwiebeln koennt ihr auch Schalotten oder Zwiebeln verwenden. Sie gibt die Paprikastreifen etwas frueher, als die Pilze und die Nudeln in die Suppe, damit sie schoen gar werden und so besser zu verdauen sind. Viki gibt zum Verfeinern noch zwei Prisen Zucker in die Suppe. Zum Anrichten drapiert Viki zunaechst ein paar Nudeln und etwas Gemuese in einen tiefen Teller, bevor sie ihn mit Suppe aufgiesst. Zum Schluss garniert sie die Suppe mit frischem Koriander und etwas Minze.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(62)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Mehl, Quark, Backpulver, Milch, oel, Salz und Zucker gut verkneten. Die uebrigen Zutaten zum Teig geben. Noch mal durchkneten und kleine Baellchen formen. Auf ein Backblech mit Backpapier legen.  Fuer 30 - 40 Min. bei 180  Grad C Ober-/Unterhitze in den heissen Ofen geben.  Tipp: Fuer Feiern mache ich mindestens die doppelte Menge, kamen dort immer sehr gut an. Die Geschmackszutaten (Roestzwiebeln, Schinken, Kaese) sind variabel, auf den Kaese wuerde ich aber nicht verzichten!  Beim Backen muss man hin und wieder gucken, sie werden je nach Herd von unten auch sehr schnell dunkel, aber zu hell sollten sie auch nicht sein. Vorsicht, wenn sie noch warm sind, werden sie gerne stibitzt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(63)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Der Teig reicht fuer 3 oder 4 runde Pizzen oder ein Blech.  Alle Zutaten in eine Schuessel geben und mindestens 5 Min. gut durchkneten. Den Teig ca. 30 Min. gehen lassen. Anschliessend in 3 - 4 Portionen teilen, die jeweils zu Kugeln geformt werden.  Nun kann es losgehen mit dem Auswellen und Belegen.  Der Teig ist fuer jegliche Weiterverarbeitung geeignet - ob im Backofen (220 Grad C, ca. 15 - 20 Min.), auf einem Pizzastein (250 Grad C, ca. 10 - 15 Min.) oder in einer Elektropfanne (Stufe 3, erste Seite 3 Min., dann wenden, belegen und noch einmal 3 Min. von der anderen Seite). Sofort servieren.  Ich habe das Rezept von einer italienischen Freundin.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(64)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fuer die Sauce das Olivenoel in einem Topf erhitzen. Das Hackfleisch hineingeben und unter Ruehren so lange braten, bis es braun und kruemelig ist. 1 EL Tomatenmark unterruehren und kurz anroesten. Mit der Gemuesebruehe abloeschen, die Sahne hinzufuegen und aufkochen lassen. Das restliche Tomatenmark unterruehren und die Sauce mindestens 30 Minuten koecheln lassen. Danach die Butter darin zerlassen und die Sauce mit Salz, Cayennepfeffer und Parmesan abschmecken.  Die Rigatoni nach Packungsanweisung in reichlich Salzwasser sehr bissfest kochen, dabei gelegentlich umruehren. In ein Sieb abgiessen und abtropfen lassen, dann wieder in den Topf geben.  Den Schinken in 1/2 bis 1 cm breite Streifen schneiden. Die Sauce zu den Rigatoni geben und alles erhitzen. Die Schinkenstreifen unterruehren und nur kurz darin erwaermen.  Den Backofen auf 180  Grad C vorheizen. Die Nudelmischung in eine grosse Auflaufform geben oder auf vier kleine ofenfeste Formen gleichmaessig verteilen. Den geriebenen Edamer darueber streuen. Auf der mittleren Schiene ueberbacken, bis der Kaese goldgelb ist.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(65)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Rinderrouladen aufrollen, waschen und mit Kuechenkrepp trockentupfen. Zwiebeln in Halbmonde, Gurken in Laengsstreifen schneiden. Schere und Kuechengarn bereitstellen.  Die ausgebreiteten Rouladen duenn mit Senf bestreichen, salzen und pfeffern. Auf jede Roulade mittig in der Laenge ca. 1/2 Zwiebel und 1 1/2 Scheiben Fruehstuecksspeck sowie 1/2 (evtl. mehr) Gurke verteilen. Nun von beiden Laengsseiten etwas einschlagen, dann aufrollen und mit dem Kuechengarn wie ein Postpaket verschnueren.  In einer Pfanne das Butterschmalz heiss werden lassen und die Rouladen dann rundherum darin anbraten. Herausnehmen und in einen Schmortopf umfuellen.  Den Sellerie, die restliche Zwiebel, Lauch und die Moehren kleinschneiden und in der Pfanne anbraten. Sobald sie halbwegs blond sind, kurz ruehren. Eine sehr duenne Schicht vom Rotwein angiessen, nicht mehr ruehren und die Fluessigkeit verdampfen lassen. Sobald das Gemuese dann wieder trockenbraet, wieder eine Schicht Wein angiessen, kurz ruehren und weiter verdampfen lassen. Dies wiederholen, bis die 1/2 Flasche Wein aufgebraucht ist. Auf diese Art wird das Roestgemuese sehr braun (gut fuer den Geschmack und die Farbe der Sosse), aber nicht trocken. Am Schluss mit dem Rinderfond, etwas Salz und Pfeffer und einem guten Schuss Gurkensud auffuellen und dann in den Schmortopf zu den Rouladen geben. Den Topf entweder auf kleiner Flamme oder bei ca. 160  Grad C Ober-/Unterhitze im heissen Backofen fuer 1 1/2 Stunden schmoren lassen. Ab und zu evtl. etwas Fluessigkeit zugiessen.  Nach 1 1/2 Stunden testen, ob die Rouladen weich sind (einfach mal mit den Kochloeffel ein bisschen draufdruecken, sie sollten sich willig eindruecken lassen - wenn nicht, nochmal eine halbe Stunde weiterschmoren). Dann vorsichtig aus dem Topf heben, warmstellen.  Die Sosse durch ein Sieb geben, aufkochen. Ca. 1 EL Senf mit etwas Wasser und der Speisestaerke gut verruehren, in die kochende Sosse nach und nach unter Ruehren eingiessen, bis die gewuenschte Konsistenz erreicht ist. Die Sosse evtl. nochmal mit Salz, Pfeffer, Rotwein, Gurkensud abschmecken.  Pro Portion 830 Kcal")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(66)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zwiebeln schaelen und in feine Wuerfel schneiden. Im Sonnenblumenoel glasig anschwitzen. Rote Linsen, Tomaten mit Saft und Kokosmilch hinzufuegen und gut umruehren. Mit der Gemuesebruehe aufgiessen und die Suppe ca. 20 Minuten koecheln.  Zum Schluss mit Salz, Chili- und Kurkumapulver abschmecken.  Die Suppe schmeckt am naechsten Tag doppelt so gut. Dazu passen Garnelenspiesse und Baguette.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(67)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Mehl mit Kakao und Backpulver in einer Ruehrschuessel mischen. Die uebrigen Zutaten fuer den Teig hinzufuegen und alles mit einem Mixer zu einem Teig verarbeiten. Anschliessend zu einer Kugel formen und den Teig in Frischhaltefolie gewickelt mindestens 30 Minuten kaltstellen.  Inzwischen fuer die Fuellung die Butter in einem Topf zerlassen und abkuehlen lassen. Den Boden der Springform fetten. Die Haelfte des Teiges mit einem Nudelholz ausrollen (wer lieber einen etwas dickeren Boden mag, kann auch 2/3 des Teiges verwenden) und eine 26er Springform damit auskleiden. Dabei sollte ein ca. 2 cm hoher Rand entstehen.  Den Quark mit Zucker, Vanillezucker, dem Mark einer Vanilleschote, den Eiern, dem Puddingpulver und der zerlassenen Butter mit einem Schneebesen zu einer gebundenen Masse verruehren, in die Form geben und glatt streichen. Den restlichen Teig in kleine Stuecke zupfen und auf der Fuellung verteilen.  Die Form auf dem Rost im unteren Drittel in den vorgeheizten Backofen schieben und bei 180 Grad C Ober-/Unterhitze ca. 60 Minuten backen. Nach dem Backen den Kuchen in der Form auf einem Kuchenrost erkalten lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(68)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die gehackte Zwiebel in einer Pfanne mit etwas oel anschwitzen. Das Hackfleisch zugeben und kruemelig braten. Mit Salz, Pfeffer, Currypulver, Chilipulver und Knoblauch wuerzig abschmecken. Das Tomatenmark zugeben und kurz mitroesten. Die Gemuesebruehe angiessen und den wuerfelig geschnittenen Kuerbis ebenfalls zugeben. Zugedeckt ca. 5 Minuten duensten.  Danach Crème fraîche, Basilikum und die Gnocchi zugeben und alles gut miteinander vermischen. In eine Auflaufform fuellen. Den Mozzarella in Scheiben schneiden und darueber verteilen.  Im vorgeheiztem Backrohr bei 200  Grad C Ober-/Unterhitze ca. 15 Minuten ueberbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(69)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Backofen auf 250  Grad C Ober-/Unterhitze vorheizen.  Knetteig bereiten, ganz duenn ausrollen. Schmand und Crème double mischen, wuerzen und auf dem Teig verstreichen.  Zwiebeln mit ganz wenig Wasser 1 Minute bei 600 Watt in der Mikrowelle duensten (durch die hohen Temperaturen beim Backen kann es leicht passieren, dass die Zwiebeln verbrennen - das wird durch diesen Trick vermieden). Zusammen mit dem Speck auf dem Belag verteilen.  Nun 20 Minuten im heissen Ofen auf der unteren Einschubleiste backen. Mit Schnittlauchroellchen bestreut servieren.  Tipp: Wer Kalorien sparen moechte, ersetzt Crème double durch 20%igen Quark.  Reicht fuer 2 - 3 Personen, je nach Hunger.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(70)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Fleisch mit je 1 EL oel, Sojasauce und Ingwer gut vermischen und ca. 30 Minuten marinieren. In der Zwischenzeit das Gemuese putzen und schneiden. Das Fleisch in einer beschichteten Pfanne rasch braten und dann zur Seite stellen.  Im Wok oder einer grossen Pfanne mit hohem Rand die Currypaste in 1 EL oel anroesten. Die Erdnussbutter unterruehren und schmelzen lassen. Mit Kokosmilch abloeschen, das Gemuese zugeben und alles ca. 15 Minuten koecheln lassen.  In der Zwischenzeit den Reis zubereiten und ausdaempfen lassen.  Kurz vor Ende der Garzeit (das Gemuese soll noch Biss haben) das Fleisch dazugeben und kurz wieder erhitzen. Das Curry mit Palmzucker, Fischsauce (notfalls etwas Salz nehmen) und Zitronengraspaste (soll nicht mitkochen) abschmecken. Nach Belieben Thai-Basilikum darueberstreuen und mit dem Reis servieren.  Die Zusammenstellung des Gemueses kann man ganz nach Geschmack und Verfuegbarkeit variieren/ergaenzen, z. B. fein geschnittene Wasserkastanien fuer noch mehr Biss, ein paar kleine Brokkoliroeschen oder einige Zuckerschoten (diagonal geteilt, kurz blanchiert oder angebraten) als zusaetzlichen Farbtupfer. Es sollten (geputzt und geschnitten gemessen) insgesamt ca. 4 - 5 Handvoll Gemuese sein.  Zitronengraspaste ist geriebenes, in etwas Pflanzenoel eingelegtes Zitronengras. Das angebrochene Glas am besten im Tiefkuehlfach aufbewahren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(71)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zubereitung:  Backofen auf 180 Grad C vorheizen. Zwiebel abziehen und in Wuerfel schneiden. Lauch putzen, waschen und in halbe Ringe schneiden. Zucchini und Tomaten waschen, halbieren und Zucchini zusaetzlich in Scheiben schneiden.  oel in einer Pfanne erhitzen und Zwiebelwuerfel darin anbraten. Hackfleisch dazugeben und kraeftig anbraten. Lauch und Zucchini hinzufuegen und mitduensten. Passierte Tomaten angiessen, Kirschtomaten unterheben, mit Salz und Cayennepfeffer abschmecken.  Kartoffelnudeln in Portionsauflaufformen geben und mit der Sauce uebergiessen.  Auflaeufe mit Kaese bestreuen und im vorgeheizten Backofen 15-20 Minuten backen (Gas: Stufe 3, Umluft 160 Grad C).  Zubereitungszeit: 30 Minuten  Backzeit: 15-20 Minuten  Pro Portion (bei 3 Portionen):  kJ/kcal: 3647/871  EW: 46,5 g  F: 47,0 g  KH: 66,0 g  BE: 5,0")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(72)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Wirsing putzen, waschen und in Streifen, Kasseler in Wuerfel schneiden. Zwiebeln abziehen und in Ringe schneiden. oel erhitzen, Zwiebeln dazugeben, goldbraun braten und herausnehmen. Wirsing in das verbliebene Bratfett geben und anduensten. Bruehe angiessen, Kasseler und gebratene Zwiebeln dazugeben und abgedeckt ca. 20 Min. garen.  2. Schupfnudeln und Schmand untermischen und alles mit Senf, Liebstoeckel, Salz, Pfeffer und Kuemmel abschmecken.  3. Mischung in eine Gratinform (20 x 30 cm) geben, Kaese ueberstreuen und im vorgeheizten Backofen bei 200  Grad C (Gas: Stufe 4, Umluft 180  Grad C) ca. 25-30 Min. goldbraun ueberbacken. Schnittlauch ueberstreuen und servieren.  Pro Portion (bei 6 Portionen):  kJ/kcal: 2.322/555  EW: 24,3 g  F: 24,5 g  KH: 59,2 g  BE: 4,5")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(73)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Vom Wirsing die groben aeusseren Blaetter loesen, den Wirsing vierteln und den Strunk herausschneiden. Den Wirsing abspuelen und abtropfen lassen, dann in Streifen schneiden.  Die Zwiebel abziehen, halbieren und in feine Streifen schneiden. Etwas oel in einem grossen Topf erhitzen und die Zwiebelstreifen darin unter gelegentlichem Ruehren anschwitzen. Die Wirsingstreifen zufuegen, salzen und mit geschlossenem Deckel duensten. Die Gemuesebruehe zugiessen und ca. 10 – 15 Minuten bissfest schmoren.  Waehrenddessen das Kasseler in kleine Wuerfel schneiden, zusammen mit den Schupfnudeln unter den Wirsing mischen. Die Hitze reduzieren, die saure Sahne unterheben, alles mit Senf, Salz, Pfeffer und Kuemmel abschmecken. Die Schupfnudel-Wirsing-Mischung in eine Auflaufform (ca. 20 x 30 cm) fuellen, mit dem geriebenen Kaese und den Schnittlauchroellchen bestreuen.  Im vorgeheizten Backofen bei 200  Grad C Ober-/Unterhitze ca. 25 Minuten goldbraun ueberbacken.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(74)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Sauerrahm und Crème fraîche mit der Bruehe verruehren und diese Mischung in eine grosse Auflaufform fuellen.  Die Kartoffeln gut waschen und mehrfach einschneiden, aber nicht ganz durchschneiden - sie sollen an der Unterseite noch zusammenhaengen. Die Abstaende zwischen den Schnitten sollten so aehnlich sein wie bei einem Eierschneider.  Die Kartoffeln mit der geschnittenen Seite nach oben in die Form setzen. Aber nur nebeneinander - nicht uebereinander - stapeln, sodass sie etwa zur Haelfte in der Sosse sitzen.  Im heissen Backofen bei 200  Grad C Ober-/Unterhitze ca. 45 - 60 Minuten backen, bis die Kartoffeln fast gar sind.  In der Zwischenzeit die Butter zerlassen. Katenschinken und Rosmarin hinzufuegen sowie die Toastbrotwuerfel dazumischen. Diese Mischung auf den Kartoffeln verteilen und noch einmal so lange backen, bis die Brotwuerfel schoen braun sind und die Kartoffeln gar.  Dazu Blattsalat servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(75)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Kartoffeln waschen, schaelen und in Wuerfel schneiden. Den Lauch waschen und in Ringe schneiden. Beides in zerlassener Butter leicht anbraten. Die Gemuesebruehe dazugeben und alles 15 Min. kochen. Evtl. mit dem Puerierstab ganz leicht puerieren (nur ein paar Impulse). Den Lachs in mundgerechte Wuerfel schneiden und zu der Suppe geben. Alles noch einmal 5 Min. ziehen lassen. Die Suppe mit Sahne verfeinern und mit Dill bestreuen. Heiss servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(76)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="De Tomaten, die Walnuesse, eine Knoblauchzehe und einen guten Schuss Olivenoel in einen Mixer geben und daraus ein Pesto herstellen. Mit Salz und Pfeffer wuerzen.  Zwiebel und Knoblauch wuerfeln, in etwas Olivenoel in einer Pfanne glasig duensten und mit ein wenig Gemuesebruehe abloeschen. Dann Spinat dazugeben und einige Minuten mitduensten, bis er zusammenfaellt. Mit Salz und Pfeffer wuerzen.  Den Blaetterteig auf einem Backblech ausbreiten und grosszuegig mit dem Tomatenpesto bestreichen. Danach den Spinat darauf verteilen und von der langen Seite her zu einem Strudel rollen. Wichtig: Mit dem Schluss nach unten auf das Backblech legen, damit er schoen zu bleibt.  Mit etwas Wasser bestreichen und bei 200  Grad C Ober-/Unterhitze backen, bis der Blaetterteig goldbraun ist. Das dauert ca. 20 Minuten.  Optional bietet sich natuerlich ein Knoblauchdip oder auch eine Tomatensosse dazu an; uns hat es aber auch ohne sehr gut geschmeckt.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(77)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Fuer den Reis 1 Teil Reis mit 2 Teilen kaltem Salzwasser in einem Topf mit Deckel aufkochen. Dann die Hitze reduzieren, sodass es gerade eben koechelt. Abgedeckt quellen lassen, bis alles Wasser verkocht ist. Das dauert ca. 15 - 20 Minuten.  1 EL Erdnussoel in eine heisse Pfanne geben. Die Huehnerbrust scharf darin anbraten und aus der Pfanne nehmen. Wieder 1 EL Erdnussoel in dieselbe heisse Pfanne geben, die Currypaste kurz darin anschwitzen und mit der Kokosmilch aufgiessen.  Tipp: Es gibt 3 verschiedene Currypasten. Gruene (am schaerfsten), rote (mittelscharf) und gelbe (am mildesten). Ich nehme auf jeden Fall einen sauberen Teeloeffel, um die Paste aus dem Glas zu nehmen und stelle das geoeffnete Glas in den Kuehlschrank. So haelt es sich mehrere Monate.  Die Erdnussbutter dazugeben, den Knoblauch dazupressen, die gekoernte Gemuesebruehe und die Zuckerschoten dazugeben. Wer keine Zuckerschoten bekommt, kann auch gruene Bohnen nehmen. Zuckerschoten schmecken aber besser.  Die Karotte schaelen, je nach Dicke laengs halbieren, in Scheiben schneiden und ebenfalls dazugeben. Alles mehrere Minuten koecheln lassen, sodass die Zuckerschoten und die Karotte noch bissfest sind.  Danach die Bambussprossen und das Fleisch wieder dazugeben und noch ein paar Minuten koecheln lassen. Die Speisestaerke in kaltem Wasser anruehren und in die koechelnde Sosse geben, um sie etwas anzudicken. Zum Schluss die Zitronengraspaste unterruehren und mit Salz wuerzen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(78)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Dieses Grundrezept kann je nach Lust und Laune durch Variieren des Fleisches (z. B. Huehnerbrust, Putenbrust, Rinderlende oder Schweinefilet) oder mit Fischfilet oder Garnelen und mit verschiedenem Gemuese (z. B. Bambussprossen in Streifen, Sojabohnenkeimlinge, Karotten, Babymais, Zuckerschoten, Thai-Auberginen, Pak Choi o. a.) zu immer neuem Genuss-Erlebnis fuehren. Lassen Sie Ihrer Kreativitaet freien Lauf! Es eignet sich auch fuer Vegetarier, da man es auch ausschliesslich mit vielem verschiedenem Gemuese zubereiten kann.  Das Gericht muss nicht im Wok zubereitet werden, es geht genauso gut in einem breiten Topf, da es Suppencharakter hat.  Die Currypaste im heissen oel sautieren, kurz mit etwas Wasser abloeschen, nach und nach die Kokosmilch dazugeben und immer erst gut verruehren, bevor man mehr dazugibt (bringt eine sehr schoene rote Farbe). Das vorgesehene Fleisch (Fisch oder Garnelen) in mundgerechte Stuecke schneiden, dazugeben und ca. 5 Minuten koecheln lassen, bis es gar ist. Garnelen brauchen nur sehr kurze Zeit!  Das in Streifen geschnittene Gemuese der Wahl (egal welches und wie viele Sorten) dazugeben und alles wieder zum Kochen bringen. Alles sollte bissfest bleiben und die Farbe behalten (Pak Choi oder Chinakohl erst kurz vor Ende dazugeben).  Mit der Fischsauce, der hellen Sojasauce und dem Palmzucker abschmecken. Thai-Basilikum-Blaetter und Peperoni dazufuegen, eine Minute weiterkochen. Nach Belieben und Schaerfe-Empfinden die kleingeschnittenen Chili-Roellchen einstreuen.  Das Gericht heiss mit Reis (Basmati, Jasminreis oder thailaendischer Duftreis) servieren, als Variation kann man auch roten Reis aus dem Asialaden probieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(79)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Tortellini nach Packungsanweisung kochen.  Den gekochten Schinken in einer tiefen Pfanne in Butter kurz anbraten, dann 400 ml von der Sahne hineingeben und auf kleiner Stufe koecheln lassen. Wenn die Tortellini gar sind, in die Pfanne zur Schinkensahne geben und weiter koecheln lassen.  In der Zwischenzeit in einer kleinen Schuessel das Eigelb mit Parmesan, Muskatnuss, Salz und den restlichen 200 ml Sahne verruehren. Dies dann in die Pfanne zu den Tortellini geben und so lange koecheln lassen, bis die Sosse dickfluessig wird. Sofort servieren.  Sehr gehaltvoll, aber der Geschmack ist fantastisch. Ab und zu kann man sich's mal goennen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(80)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die ersten sechs Zutaten fuer die Marinade mischen und die gewaschenen und getrockneten Haehnchenfilets hineinlegen. Mindestens 1 Std. darin marinieren (geht auch ueber Nacht).  Kartoffeln schaelen, groessere Knollen halbieren und in Olivenoel ca. 10 Min. von allen Seiten braun braten.  Die gebratenen Kartoffeln in eine mit Olivenoel ausgestrichene Auflaufform geben.  Knoblauch schaelen und klein hacken. Die Zwiebel schaelen, halbieren und die Haelften in Ringe schneiden. 1 Zweig Thymian und 1 Zweig Rosmarin waschen und hacken. Zwiebeln, Knoblauch und gehackte Kraeuter im Bratfett anduensten, dann ueber die Kartoffeln geben.  Das Fleisch mit der Marinade auf die Kartoffeln geben und alles im Backofen bei 200 Grad ca. 15 Min. braten. Dann heisse Huehnerbruehe angiessen, die Tomaten und zwei Rosmarinzweige im Auflauf verteilen und weitere 30 Min. im Ofen garen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(81)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Aus dem Mehl, Zucker, Butter, Ei und Backpulver einen Knetteig herstellen. Den Boden einer 26 cm Springform mit Backpapier auslegen, den Rand einfetten. Den Teig ausrollen und die Raender von Hand recht hoch druecken.  Den Backofen am besten jetzt auf 175 Grad C Ober-/Unterhitze vorheizen.  Den Quark kurz geschmeidig ruehren, dann nach und nach alle Zutaten zugeben und gut verruehren. Die sehr fluessige Masse in die Springform fuellen und den Kuchen 70 Minuten backen.  In der Zwischenzeit das Eiweiss mit dem Puderzucker steif schlagen. Nach 70 Minuten den Kuchen heraus holen und den Eischnee ca. 1 cm dick auf den Belag streichen. Es wird wohl nicht alles davon benoetigt! Nochmals 10 Minuten bei gleicher Hitze backen.  Dann den Kuchen etwas abkuehlen lassen und den Rand der Springform vorsichtig mit einem Messer loesen. Den Kuchen auf dem Boden der Springform mehrere Stunden abkuehlen lassen. Wenn alles funktioniert hat, dann sollten beim Abkuehlen auf dem Eiweissguss die Traenen entstehen. Schmecken tut der Kuchen aber auch ohne!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(82)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Schafskaesewuerfel in ein Sieb giessen und das oel dabei auffangen. Die Champignons in Scheiben schneiden. Die Paprikaschoten putzen und in Streifen schneiden. Den Knoblauch fein hacken.  In ca. 3 EL von dem aufgefangenen oel das Hackfleisch braun und kruemelig braten. Die Haelfte der Champignons dazugeben und mit anbraten. Nun auch die Paprikastreifen und den Knoblauch dazugeben und anbraten.  Nach ca. 5 Minuten die Crème fraîche und den Oregano einruehren und mit Salz und Pfeffer wuerzig abschmecken. Alles in eine feuerfeste Form geben und die restlichen Champignons darauf verteilen. Zuletzt die abgetropften Schafskaesewuerfel sowie den zerbroeckelten Schafskaese darauf streuen.  Den Auflauf ca. 20 - 30 Minuten im heissen Backofen bei 180  Grad C Umluft backen.  Dazu passt Tzatziki, Fladenbrot und/oder Reis.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(83)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 200  Grad C Ober-/Unterhitze vorheizen.  Fuer die Fuellung 1 EL Sesamoel in einer ausreichend grossen Pfanne erhitzen. Gemuese in mundgerechte Stuecke schneiden, Sprossen abtropfen lassen. Das vegane „Hack“ in der Pfanne kruemelig braten. Das Gemuese hinzugeben und alles vermengen. 3 Minuten bei hoher Hitze anduensten und mit Chili Flocken, Salz und Pfeffer wuerzen.  Die Strudelteigblaetter hochkant legen. Auf den unteren Teil mittig etwa 3 EL der Fuellung geben. Seiten einklappen und das gesamte Strudelteigblatt vorsichtig einrollen. Auf ein mit Backpapier ausgelegtes Backblech legen. Mit den uebrigen Blaettern gleich verfahren. Die fertigen Fruehlingsrollen mit dem restlichen Sesamoel einpinseln. Wer mag kann etwas Sesam drueberstreuen.  Die Fruehlingsrollen im vorgeheizten Backofen 25 - 30 Minuten auf der mittleren einschubleiste goldbraun backen.  Pro Stueck  Energie kJ/kcal 1059/253  Eiweiss 12,1 g  Fett 7,6 g  Kohlenhydrate 32 g")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(84)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Bruehe aufkochen lassen, den Reis hineingeben und 15 min kochen. Er sollte dann noch etwas al dente sein. Den Reis abgiessen und abkuehlen lassen.  Tipp: Man kann natuerlich auch einen Rest vom Vortag nehmen. Dann aber spaeter mit dem Salz nicht sparen. Der Reis sollte schon schoen wuerzig sein.  Den Kaese raspeln, die Moehren putzen und raspeln (ob man Kaese und Moehren fein oder grob raspelt, bleibt dem eigenen Gusto ueberlassen). Die Zwiebeln fein wuerfeln.  Reis, Kaese, Moehren, Zwiebeln und Eier miteinander verruehren. Pfeffer (ruhig reichlich), Salz und Kraeuter einruehren. Nun Semmelbroesel einruehren, bis die Masse etwas Konsistenz hat. Dann ca. 15 min quellen lassen. Pruefen, ob die Masse unter Druck in den Haenden zu einer Frikadelle geformt werden kann. Wenn ja, anschliessend noch leicht in Semmelbroeseln waelzen.  In reichlich Butterschmalz bei geringer Hitze vorsichtig von beiden Seiten goldbraun braten. Nach dem Braten auf Kuechenkrepp das Fett abtropfen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(85)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="1. Zwiebeln und Knoblauch schaelen und fein wuerfeln.  2. Kichererbsen abgiessen, abspuelen und abtropfen lassen, Rosinen abspuelen.  3. Wurzelgemuese schaelen und wuerfeln.  4. Koch-Ruehrelement und Ruehrhilfe einsetzen. Olivenoel in die Ruehrschuessel geben und Programm Eintopf waehlen.  5. Hackfleisch nach und nach dazu broeseln, Zwiebeln, Knoblauch und Zucker zugeben und Temperatur auf 160  Grad C erhoehen.  6. Wurzelgemuese (Suppengruen), Zimt, Kreuzkuemmel, Cayennepfeffer zugeben. Waehrend die KCC laeuft, mit Tomaten, Kichererbsen, Rosinen und Gemuesebruehe auffuellen.  7. Ende des Programms abwarten und gegebenenfalls mit Salz und Pfeffer abschmecken. Vor dem Servieren Zitronenabrieb zugeben.  Gefaellt Dir dieses Rezept? Dann freuen wir uns auf Deine Bewertungs-Sternchen!")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(86)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Den Backofen auf 175  Grad C - 195  Grad C vorheizen.  Zuerst die Schale von den 3 Zitronen abreiben, zwei Zitronen davon auspressen.  Dann Eier und Zucker schaumig ruehren. Das Mehl sieben und mit Vanillezucker, Backpulver, Zitronenschale und Margarine nach und nach dazugeben. Alles gut mixen. Den Teig auf ein mit Backpapier ausgelegtes Backblech streichen. In den vorgeheizten Backofen schieben und ca. 20 Min. auf der mittleren Schiene backen.  Nun aus dem Zitronensaft und dem Puderzucker nach und nach eine Glasur mischen - bitte sehr sparsam mit dem Zitronensaft umgehen, die Glasur muss schoen dickfluessig sein.  Solange der Kuchen noch warm ist, mit einer Gabel ueberall einstechen. Somit wird er schoen saftig, denn die Glasur kann so einsickern. Dann schnell die Glasur auf dem warmen Kuchen verstreichen und auskuehlen lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(87)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Das Haehnchenbrustfilet waschen, mit Kuechenpapier abtupfen und in mundgerechte Stuecke schneiden. Das Olivenoel mit der roten Currypaste in einer beschichteten Pfanne erhitzen und das Haehnchenfleisch darin von allen Seiten knusprig braten.  Waehrenddessen die Zucchini waschen und die Karotten schaelen. Nun mit einem Sparschaeler rundherum die „Bandnudeln“ abschaelen, bei den Zucchini moeglichst das innere Kerngehaeuse uebrig lassen, die Karotten koennen komplett verwendet werden. Sollten die Scheiben zu breit werden, kann man das Gemuese mit einem Messer vor dem Abschaelen laengs einschneiden.  Das fertig gebratene Haehnchenfleisch herausnehmen und dabei moeglichst den Bratsaft in der Pfanne lassen. Die Gemuesebandnudeln in Wasser und Bruehe mit dem Bratsaft aufkochen und einige Minuten garen lassen. Derweil die Tomaten wuerfeln und zusammen mit dem Tomatenmark zum Gemuese geben.  Zum Schluss den Ziegenfrischkaese und das Haehnchenfleisch zugeben und alles noch einmal unter Ruehren erhitzen. Mit Salz und Pfeffer abschmecken und servieren.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(88)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Zucchini waschen und laengs in fingerdicke Scheiben schneiden. In einer Pfanne in Olivenoel von beiden Seiten anbraten, danach auf Kuechenpapier abtropfen lassen. Oder alternativ die Scheiben mit Olivenoel bestreichen, ein wenig salzen und auf der obersten Schiene mit der Grillfunktion im Backofen braeunen. Das dauert allerdings laenger.  Die Zwiebel in Wuerfel schneiden und in der Pfanne in wenig Olivenoel glasig duensten. Die Knoblauchzehe dazu pressen und etwas mitduensten. Das Hackfleisch hinzugeben und kruemelig braten. Wenn das Fleisch Farbe bekommen hat, mit Salz, Pfeffer und Paprikapulver wuerzen, 1 EL Tomatenmark hinzugeben, unterruehren und eine Minute mit anschwitzen. Die Tomaten hinzugeben und mit Oregano, Thymian, Salz, Pfeffer und Paprika wuerzen. 10 min auf kleiner Flamme koecheln lassen, zum Schluss die gehackte Petersilie hinzugeben.  Den Frischkaese mit der Milch verruehren, wahlweise auch Sauerrahm unterruehren. Mit Salz, Pfeffer und etwas Muskat wuerzen, ca. 50 g Streukaese unterruehren.  Eine Lasagneform oder eine andere Auflaufform mit Zucchinischeiben auslegen. Darauf ein paar Loeffel Tomaten-Hack-Sosse verteilen, darauf eine Schicht Frischkaesesosse, und darauf wieder Zucchinischeiben. Weiter so schichten, bis alle Zutaten verbraucht sind. Die oberste Schicht soll Tomaten-Hack-Sosse sein. Diese mit dem restlichen Kaese bestreuen.  Die Zucchini-Lasagne im vorgeheizten Backofen bei 200  Grad C Ober-/Unterhitze in ca. 30 min goldbraun backen.  Dazu passt ein kleiner frischer Salat.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(89)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

handob = handlungsschritt(text="Die Zucchini schaelen und anschliessend mit einem Schaelmesser in Streifen schneiden - also wie Spaghetti bzw. Bandnudeln.  Die Zucchini in etwas Olivenoel anbraten. Inzwischen die Tomaten klein schneiden und dazugeben. Dann das Mineralwasser hinzufuegen (das sorgt dafuer, dass die Zucchini weicher werden und sich einfach besser um die Gabel wickeln lassen). Tomatenmark und eine beliebige Menge Frischkaese dazugeben (ich empfehle: 2 TL). Salzen, pfeffern und die Kraeuter hinzufuegen. Eventuell noch wuerzen (z. B. mit Paprikapulver oder Gyrosgewuerz). Noch ein wenig koecheln lassen.")
db.session.add(handob)
db.session.commit()
rezaus = rezept.query.get(90)
assoc = AssociationRHhat(position=1)
assoc.hatid = handob
with db.session.no_autoflush:
    rezaus.handlungsschritte.append(assoc)
db.session.commit()

