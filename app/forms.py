import os
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField,StringField
from flask_wtf.file import FileField
from app import db
from app.rezept import zutat


zutatenListe = []

try:
    for entry in zutat.query.all():
        zutatenListe.append([entry.zid,entry.name])
except Exception as e:
    print(e)


class d_felder(FlaskForm):
    global zutatenListe
    """ Swip Swap Formular"""
    eingabe = SelectMultipleField('Zur Verfuegung stehende Objekte', choices=zutatenListe)
    selected = SelectMultipleField('Ausgewaehlte Objekte',choices=[])
    submit2 = SubmitField("-->")        # Hinzufuegen
    submit3 = SubmitField("<--")        #Entfernen
    submit4 = SubmitField("Auswahl loesen")
    submitSuchen = SubmitField("Suchen")

class rezeptanlegen(FlaskForm):
    rezeptname = StringField('Name des Rezepts')
    bildupload = FileField('Bild des Rezepts',validators=[])
    tags = StringField('Tags')
    submit = SubmitField('Speichern')

class handlungschrittanlegen(FlaskForm):
    bildupload1 = FileField('Bild des Rezepts',validators=[])
    bildupload2 = FileField('Bild des Rezepts',validators=[])
    beschreibung = StringField('Handlungschritt')
    submit = SubmitField('Speichern')

class rzanlegen(FlaskForm):
    submit = SubmitField('Speichern')

class zutatanlegen(FlaskForm):
    name = StringField('Name der Zutat')
    einheit = StringField('sinnvolle Einheit der Zutat')
    bildupload = FileField('Bild des Rezepts',validators=[])
    submit = SubmitField('Speichern')