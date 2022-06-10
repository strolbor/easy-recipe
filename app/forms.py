import os
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField,StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from app import db
from app.rezept import zutat


zutatenListe = []

try:
    for entry in zutat.query.all():
        #zutatenListe.append([entry.zid,entry.name])
        zutatenListe.append(entry.name)
except Exception as e:
    print(e)


class d_felder(FlaskForm):
    """ Swip Swap Formular"""
    global zutatenListe
    eingabe = SelectMultipleField('Zur Verfuegung stehende Objekte', choices=zutatenListe)
    selected = SelectMultipleField('Ausgewaehlte Objekte',choices=[])
    submit2 = SubmitField("-->")        # Hinzufuegen
    submit3 = SubmitField("<--")        #Entfernen
    submit4 = SubmitField("Auswahl loesen")
    submitSuchen = SubmitField("Suchen")

class rezeptanlegen(FlaskForm):
    rezeptname = StringField('Name des Rezepts',validators=[DataRequired()])
    bildupload = FileField('Bild des Rezepts',validators=[])
    tags = StringField('Tags')
    submit = SubmitField('Speichern')

class handlungschrittanlegen(FlaskForm):
    bildupload1 = FileField('Bild des Handlungsschrittes 1',validators=[])
    bildupload2 = FileField('Bild des Handlungsschrittes 2',validators=[])
    beschreibung = StringField('Handlungschrittbeschreibung',validators=[DataRequired()])
    submit = SubmitField('Speichern')

class rzanlegen(FlaskForm):
    submit = SubmitField('Speichern')

class zutatanlegen(FlaskForm):
    name = StringField('Name der Zutat',validators=[DataRequired()])
    einheit = StringField('Einheit der Zutat',validators=[DataRequired()])
    bildupload = FileField('Bild der Zutat hochladen',validators=[])
    submit = SubmitField('Speichern')