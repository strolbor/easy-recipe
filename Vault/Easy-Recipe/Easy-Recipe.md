# Easy Recipe Expose
Teilnehmer:  
• Tom Herzberg  
• Urs-Benedict Braun  
Betreuer (mögliche):  
• Manuela Kanneberg  
• Prof. Dr. David Hausheer (?)  

## Kontext  
Es gibt bereits einige Internetdienste wie Pinterest, Chefkoch, Instagram, die Rezepte für  
Getränke und Mahlzeiten enthalten. Wenige bis keine bieten davon eine Funktion, um die  
Zutaten einzutragen, die man als Nutzer zur Verfügung hat, um geeignete Rezepte  
vorgeschlagen zu bekommen. Noch dazu bietet kein Dienst bisher die Möglichkeit, ein Foto  
von den bereits vorhandenen Zutaten zu machen, dieses Foto auf einer Website hochzuladen  
und anhand der auf diesem Foto automatisch erkannten Zutaten Rezepte vorzuschlagen.  
Fragestellung  
Ist es möglich, einen bequemen Dienst bereitzustellen, der dem Nutzer anhand von  
ausgewählten Zutaten, später anhand eines Fotos, Cocktail-, Kuchen- und andere Rezepte  
vorschlägt? Würde dieser Dienst zuverlässig Zutaten erkennen und vom Nutzer akzeptiert  
werden?  
## Lösungsansatz  
Um einen Dienst bereitzustellen, der anhand von Fotos Rezepte vorschlägt, muss die  
Grundstruktur für eine Website, die Rezepte anhand von eingegebenen Zutaten vorschlägt,  
gegeben sein.  
### Vorhaben  
Unsere Idee ist, dass wir eine Website entwickeln, auf der man Rezepte, wie zum Beispiel  
Cocktail-, Kuchen- und andere Rezepte anhand der bereits vorhandenen Zutaten, die man  
momentan zur Verfügung hat, heraussucht.  
### [[Meilenstein 1 - Frontend]] 
Die Zutaten, die man bereits hat, kann man im Frontend auswählen. Daraufhin wird das  
“Suchfeld” aktiv, welches dem Nutzer die Rezepte anhand der zuvor ausgewählten Zutaten  
vorschlägt.  
Aufgrund der Vorauswahl der Zutaten wird ein Ranking erstellt. Dies bedeutet, wir zählen die  
Anzahl der benutzten vorausgewählten Zutaten, die für das Gericht benötigt werden. Je mehr  
Zutaten für ein Gericht fehlen, desto niedriger ist das Ranking für das Gericht. Fehlen mehr  
als eine notwendige Zutat, wird das Gericht nicht vorgeschlagen. Sind alle notwendigen  
Zutaten verfügbar, bezieht sich das Ranking auf die Verfügbarkeit der optionalen Zutaten.  

### [[Meilenstein 2 - Datenbank]] 
Wir implementieren eine rationale Datenbank, die die Rezepte zu den Gerichten bereithält.  
Jedes Rezept enthält Arbeitsschritte, notwendige Zutaten und optionale Zutaten. Zu Beginn  
soll die Datenbank einige Rezepte enthalten. Optional kann zu jedem Rezept zusätzlich ein  
Bild vom fertigen Gericht beigefügt werden. Zusätzlich können zu jedem Arbeitsschritt  
ebenfalls Bilder gespeichert werden, die den Nutzer bei der Zubereitung unterstützen.
 
### [[Meilenstein 3 - Backend]]  
Hier geschieht die Administration der Datenbank. Hier können Rezepte geändert, gelöscht  
und/oder erstellt werden. Diese Daten werden in die Datenbank gespeichert. Der Nutzer kann  
neue Zutaten und neue Rezepte in die Datenbank eintragen (technische Umsetzung erfolgt in  
Meilenstein 4).  

### [[Meilenstein 4 - Datensatz erweitern]]
Der Nutzer soll die Möglichkeit haben, neue Zutaten und neue Rezepte zu einer bestehenden  
Datenbank hinzuzufügen. Dazu öffnet sich auf der Website eine Maske, auf der die  
hinzuzufügende Zutat eine Beschreibung und ein Bild erhalten und schließlich in die  
Datenbank geschrieben werden soll. Legt der Nutzer ein neues Rezept an, öffnet sich  
ebenfalls eine Maske, in der die notwendigen und optionalen Zutaten sowie dazu gehörige  
Arbeitsschritte und Bilder eingetragen werden sollen. Diese Zutaten müssen bereits in der  
Datenbank existieren.  
### [[Meilenstein 5 - Rezepte nach Schwierigkeit zusätzlich sortieren]]  
Mit diesem Meilenstein wird eine weitere Rankingeigenschaft hinzugefügt, welche dem  
Nutzer mitteilt, wie schwer oder leicht das von ihm ausgesuchte Rezept ist. Die Schwierigkeit  
wird vom Rezeptersteller bestimmt.  
Anhand dieser Eigenschaft kann man die Rezepte zusätzlich zum bestehenden Ranking besser  
einordnen, damit ein Kochprofi, sowie auch ein Laie, schmackhafte Rezepte zubereiten kann.  
## Ausblicke  
### [[Ausblick 1 - Google Lens Integration ]]  
Google Lens bietet die Möglichkeit, Objekte in einer Bilddatei mit bekannten Bildern aus der  
Google-Bildersuche zu vergleichen. Wenn wir die Google Lens API in unsere Website  
einbinden, könnte der Nutzer Fotos von seinem Kühlschrankinhalt machen und auf der  
Website hochladen. Diese Fotos werden an die Google Lens API weitergeleitet, um  
herauszufinden, welche Zutaten der Nutzer zur Verfügung hat.  
Um diese Funktion zu implementieren müssten wir eine Mobile-Version unserer Website  
anbieten. Auf der Website sollte ein Button sein, der die Handy-Kamera-App öffnet. Der  
Nutzer macht das Foto von seinen Zutaten und bekommt angezeigt, welche Zutaten von  
Google Lens auf dem Foto erkannt wurden. Diese Zutatenliste kann aufgrund der  
Fehleranfälligkeit von Google Lens vom Nutzer korrigiert werden.  
### [[Ausblick 2 Datenverarbeitung]] 
• Wie könnte man automatische Rezepte aus dem Internet einfangen? Wie kann man  
sich dabei vor “Trolle” (“Witzbolde”/“Saboteure”) schützen, damit nur sinnvolle  
Rezepte in der Datenbank stehen?  
• Frage: Inwieweit müssen sich die Service Apps auf den gleichen/verschiedenen  
Servern befinden (verteilte Systemdienste)

## Zeitplanung
* Planung:  
  * Beide beteiligt  
  * Scrum-Modell (Artefakte, Meetings, Backlog, Sprintlog), inkl. Planung:  
  * 2x30h  
* Meilenstein 1 Frontend  
  * Übernimmt einer  
   Dauer: 1x60h  
* Meilenstein 2 Datenbank  
  * 2x20h  
* Meilenstein 3 Backend  
  * Übernimmt einer  
  * Dauer: 1*60h  
* Meilenstein 4 Datensatz erweitern mit Zutaten  
  * 2x20h  
* Meilenstein 5 Schwierigkeit  
  * 2x20h  
* Dokumentation  
  * 2x30h  
Ergibt: 360h/2 Personen => 180h/Person => 6CP/Person  
## Programme, die wir voraussichtlich benutzen  
Diese Frameworks werden wir mit höchster Wahrscheinlichkeit benutzen:  
• PHP  
• MySQL  
• Bootstrap (CSS-Framework)  
Diese überprüfen wir auf die Kompatibilität mit unserem Projekt.  
• Node.js  
• Ruby on Rails (speziell fürs Backend entwickeltes Framework)  
• Angular (front-end web development frameworks for developers)  
## Abgrenzung zu anderen Projekten  
Unser Projekt unterscheidet sich z.B. zu Chefkoch oder Lidl-kochen in dem Sinne, dass wir  
anhand der Zutaten Rezepte suchen, die man sofort zubereiten können - ohne, dass der Nutzer  
erst einkaufen muss, um nicht vorhandene Zutaten kaufen zu müssen.  
Chefkoch sucht anhand der Gerichtbezeichnung ein passendes Rezept. Man kann dort keine  
Zutaten eingeben, um das passende Rezept für diese Zutaten zu erhalten. Stattdessen wird  
anhand der Gerichtbezeichnung der in ihrer Datenbank eingetragene Rezept-Titel gesucht.  
Das Problem dabei ist, dass der Nutzer ein ihm unbekanntes Gericht und das Rezept dazu  
nicht finden kann.