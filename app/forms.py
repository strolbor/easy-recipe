import os
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField

# gibt nur parent directory, also app zurück und sucht in app nach ZUTATEN.txt
zutatenPath = os.path.dirname(os.path.abspath(__file__)) + "\\ZUTATEN.txt"
zutatenListe = open(zutatenPath, 'r').readlines()

class d_felder(FlaskForm):
    """ Swip Swap Formular"""
    ein = SelectMultipleField('Zur Verfuegung stehende Objekte', choices=zutatenListe)
    submit2 = SubmitField("-->")        # Hinzufuegen
    selected = SelectMultipleField('Ausgewaehlte Objekte', choices=[])
    submit3 = SubmitField("<--")        #Entfernen
    submit = SubmitField("Speichern")   #Speichern
    submit4 = SubmitField("Auswahl loesen")