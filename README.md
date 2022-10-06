# Easy Recipe

## Was EasyRecipe tut
Auf der Homepage gibt der Nutzer Zutaten ein, die er gerade im Kühlschrank oder Gewürzregal zur Verfügung hat. 
Aus diesen Zutaten wird in der Datenbank nach passenden Rezepten gesucht.
Diese Rezepte werden geordnet auf der Folgeseite angezeigt.
Der Nutzer kann auch Rezepte durchstöbern, ohne vorher Zutaten einzugeben. 
Außerdem kann nach Eigenschaften von Rezepten gefiltert werden, wie zum Beispiel vegan, vegetarisch, mit Fleisch oder einfache Rezepte.

## Wichtigste Libraries
### Flask
Web-Framework zum Erstellen von Web-Anwendungen. 
Alle Dateien in app/ nutzen Flask u.a. zur Routenerstellung (URLs). 
### Jinja2
Tool zum Erstellen von Templates für Seiten (siehe app/templates/)
Beinhaltet auch for-loops und if-Abfragen.
Aus dem Backend können Daten mitgegeben werden, die auf der Website dynamisch angezeigt werden.
### SQLAlchemy


## Tipps zum Starten
Python 3.8

Installation der benötigten Packages: 
- venv/Scripts/pip.exe install -r requirements.txt

Starten der Anwendung: 
- venv/Scripts/python.exe -m flask run


