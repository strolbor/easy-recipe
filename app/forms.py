import os
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField, TextField, TextAriaField
from flask_wtf.file import FileField

# gibt nur parent directory, also app zurück und sucht in app nach ZUTATEN.txt
zutatenPath = os.path.dirname(os.path.abspath(__file__)) + "\\ZUTATEN.txt"
#zutatenListe = open(zutatenPath, 'r').readlines()
zutatenListe = ["Ei", "Apfel"]

class d_felder(FlaskForm):
    global zutatenListe
    """ Swip Swap Formular"""
    eingabe = SelectMultipleField('Zur Verfuegung stehende Objekte', choices=zutatenListe)
    selected = SelectMultipleField('Ausgewaehlte Objekte',choices=[])
    submit2 = SubmitField("-->")        # Hinzufuegen
    submit3 = SubmitField("<--")        #Entfernen
    submit4 = SubmitField("Auswahl loesen")

class rezeptanlegen(FlaskForm):
    rezeptname = TextField('Name des Rezepts')
    bildupload = FileField('Bild des Rezepts',validators=[])
    submit = SubmitField('Speichern')

class handlungschrittanlegen(FlaskForm):
    bildupload = FileField('Bild des Rezepts',validators=[])
    beschreibung = TextAriaField('Handlungschritt')
    submit = SubmitField('Speichern')

class rzanlegen(FlaskForm):
    submit = SubmitField('Speichern')

"""
CREATE TABLE `Zutat` (
  `ZID` bigint(20) NOT NULL,
  `Zutatname` text,
  `Einheit` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""
class zutatanlefen(FlaskForm):
    namen = TextField('Name der Zutat')
    einheit = TextField('sinnvolle Einheit der Zutat')
    submit = SubmitField('Speichern')