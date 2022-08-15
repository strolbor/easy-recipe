# Verknüpfer Rezepte Zutaten
nennt sich im Quellcode "scrapper-zutaten.py" und "scrapper-hat.py"
## 1. Aufgabe (scrapper-zutaten)
1. Er durchsucht den Ordner mit den Rezepten nach
	1. den Zutaten
	2. Rezeptnamen
2. Erstellt eine Liste von einzigartigen Zutatennamen
	1. Die wir gefiltert haben nach:
		1. gleiche Schreibweise
		2. Synonyme
		3. Schreibfehler elimierung
		4. Sonderzeichen eliminierung
3. Schreibt diese Einzigartigen Namen in die Datei: "zutaten_add.txt"

## 2. Aufgabe (scrapper-hat.py)
Verknüpft die zuvor elimierten doppelten Zutaten mit dem Rezepten.
Bei keinen unstimmigkeiten, das heißt, wir suchen nach dem Rezept und erhalten nur ein Ergebnis aus der Datenbank, so verknüpft er dieses eine Zutat mit dem Rezept. 
Falls wir nichts erhalten (0 == Abfrage-Array) so müssen wir manuell nach der Zutat suchen. 
Wenn wir mehr Ergebnisse erhalten können, werden die Einträge mit den Indexzahl angezigt und wir entscheiden (als Mensch) welche Verknüpfung er herstellen soll.
## Einpflege in die Datenbank
Wir erhalten eine zutaten-add.txt Datei, die wir einfach mit PYthon durchlaufen können. Python erkennt den Python Code und fügt die Zutaten hinzu.
Das selbe Prinzip ist bei der hat-add.py Datei. Die Scrapper und Verknüpfer generieren dabei ein Python-Code der ausführbar ist.