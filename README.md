# Easy Recipe

Easy Recipe ist eine Reverse-Rezeptsuchmaschine, bei der man die Rezepte anhand der Zutaten suchen kann.


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
Mithilfe von *python easy-recipe.py* für die Entwicklung bzw. mit einen Production-WSGI Server, wie gunicorn.

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