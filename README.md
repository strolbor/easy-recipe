# Easy Recipe

Auf der Homepage gibt der Nutzer Zutaten ein, die er gerade im Kühlschrank oder Gewürzregal zur Verfügung hat. 
Aus diesen Zutaten wird in der Datenbank nach passenden Rezepten gesucht.
Diese Rezepte werden geordnet auf der Folgeseite angezeigt.
Der Nutzer kann auch Rezepte durchstöbern, ohne vorher Zutaten einzugeben. 
Außerdem kann nach Eigenschaften von Rezepten gefiltert werden, wie zum Beispiel vegan, vegetarisch, mit Fleisch oder einfache Rezepte.



## Datenbank
Zurzeit wird die SQLite Datenbank genutzt, welche sich im Verzeichnis app/ befindet.
Die Bilder werden im "Instance" Ordner gespeichert.

## benutzte Liberies
siehe requirements.txt
Wichtige Erweiterungen.
* Flask
  * Webserver
* Flask-SQLalchemy
  * Datenbank Verbindung
* opencv 2
  * zum bearbeiten der hochgeladen Bilder
  * 

## Programm starten
Installation der benötigten Packages: 
- venv/Scripts/pip.exe install -r requirements.txt

Starten der Anwendung: 
- venv/Scripts/python.exe -m flask run
- python easy-recipe.py

Production-WSGI Server:
gunicorn easy-recipe:app/

## Umwanldungsskripte
### Kategorie-ersteller.py
Hiermit werden die Kategorien der in der Datenbank befinden Zutaten, kategoriseirt.
#### benötigt:
* Zutaten

### rezept-handlungschrit-relationship.py
Mit diesne Hilffskript wird zwischen den Datenbestand aus dem Webscraper und unseren Daten die Verknüpfung erstellt.
Dabei müssen die Rezepte und die Handlungsschritt Objekte schon existieren
#### benötigt:
* Rezepte
* Handlungsschritte
#### erstellt:
* Assoicttion RHhat



## rezept-adder-skript.py
Mit diesen Hilfsskript werden die Rezepte erstellt. und in der "data-rezept-add.py" gespeichert.
#### benötigt:
* Webscraper Daten
#### erstellt:
* Rezepte
  * data-rezept-add.py


## rezept-zutaten-relationship.py
Mithilfe diesen Skripts werden Zutaten und Rezepte mit einander verbunden.
#### benötigt:
* Rezepte
* Zutaten 
#### erstellt:
* Association


### tags-adder-for-rezept.py
Mithilfe diesen Hilfskript werden den Rezepten ihre Tags gegeben.
#### benötigt:
* Webscraper-Daten 
* Rezept-Objekte
#### erstellt:
* Zutaten
  * data-addtags.py, womit die Daten abgespeichert werden können.

### zutatenadder.py
Mit dieses Hilfskript werden die Zutaten normalisiert und in die Datenbank eingespeichert
#### benötigt:
* Webscraper-Daten 
#### erstellt:
* Zutaten

# Binärdaten
* https://drive.google.com/drive/folders/1ElHNEzfGqB4-3EV3GZyg-ngCRvpf5NC2?usp=share_link
