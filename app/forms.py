from wtforms import SubmitField, SelectMultipleField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from app import db
from app.rezept import zutat, kategorie, rezept


class d_felder(FlaskForm):
    """ Swip Swap Formular auf der Startseite """
    zutatenListe = []
    try:
        for entry in zutat.query.all():
            # zutatenListe.append([entry.zid,entry.name])
            zutatenListe.append(entry.name)
        pass
    except Exception as e:
        print(e)

    submitSuchen = SubmitField("Suchen")
    # "Neues" Suchfeld, Script mit Dropdown Menü
    suchfeld = SelectField("Direktsuche", choices=[""] + zutatenListe)
    sumbitAddSuchbegriff = SubmitField("Hinzufügen")

    # Kategorien mit Buttons für Zutaten und Stringfields für Kategorienamen
    class homepage_kategorie():
        """Name der Kategorie und dazugehörige Zutaten"""
        name = ""
        zutaten = []
        def __init__(self, _name, _zutaten):
            self.name = _name
            self.zutaten = _zutaten

    # Kategorien beinhaltet Objekte der Klasse oben, jeweils ein Stringfield für Name und Array von Submitfields
    kategorien = []
    alleZutaten = []

    for entry in kategorie.query.all():
        kategorieName = entry.name
        kat_zutatsubmits = []

        for zutats in entry.bkat:
            # hänge Submitliste einen Button mit der Zutat an, der beim Drücken die Zutat in Auswahl Liste addet
            kat_zutatsubmits.append(zutat.query.get(zutats.id))
            alleZutaten.append(zutats)

        kategorien.append(homepage_kategorie(kategorieName, kat_zutatsubmits))


class rezeptaendern(FlaskForm):
    """ Rezeptanlege Seite in der Verwaltung """
    rezeptname = StringField(
        'Name', validators=[DataRequired()])  # des Rezepts
    bildupload = FileField('Bild')
    tags = SelectMultipleField('Tag')
    handlung = TextAreaField("Anleitung")
    submit = SubmitField('Speichern')


class handlungschrittanlegen(FlaskForm):
    """ Handlungsschrittanzeige Seite in der Verwaltung """
    bildupload1 = FileField('Bild 1')
    bildupload2 = FileField('Bild 2')
    beschreibung = TextAreaField(
        'Beschreibung', validators=[DataRequired()])
    submit = SubmitField('Speichern')


class rzanlegen(FlaskForm):
    """Erstes Formular zum Rezept auswählen"""
    rezeptpicker = SelectField('Rezept Picker', validators=[DataRequired()])
    submit = SubmitField('Rezept auswählen')


class verknupfungsanleger(FlaskForm):  # rzzutaten
    """Feld zum Verknüpfungen anlegen"""
    zutaten = SelectMultipleField()
    submit = SubmitField('Einstellungen speichern')


class zutatanlegen(FlaskForm):
    """Zutat anlegen"""
    name = StringField('Name', validators=[DataRequired()])
    einheit = StringField('Einheit', validators=[DataRequired()])
    bildupload = FileField('Bild')
    kategorie = SelectMultipleField("Kategorie")
    submit = SubmitField('Speichern')


class taganlegen(FlaskForm):
    name = StringField('Name des Tags')
    submit = SubmitField('Speichern')


class handlungverknüpfer(FlaskForm):
    position = StringField("Position", validators=[DataRequired()])
    handlungschritt = SelectField("Handlungschritt")
    submit = SubmitField('Speichern')


class rezeptzutatadder(FlaskForm):
    zutat = SelectField("Zutat auswählen")
    #optionaliat = SelectField("Optionalität", choices=["Nein", "Ja"])
    menge = StringField("Menge der Zutaten", validators=[DataRequired()])
    submit = SubmitField("Speichern")


class rezeptanzeige(FlaskForm):
    submitTest = SubmitField("Suchen")
    # Nicht löschen
    # Das heißt nur dämlich mit Test


class nutzerein(FlaskForm):
    rname = StringField('Name')#, validators=[DataRequired()])
    bildupload = FileField('Bild')
    handlung = TextAreaField('Handlungschritt')#, validators=[DataRequired()])
    submit = SubmitField("Speichern")

class rezeptranking(FlaskForm):
    btnSort0 = SubmitField(label="Bestes Verhältnis")
    btnSort1 = SubmitField(label="Wenigste fehlende Zutaten")
    btnSort2 = SubmitField(label="Meiste vorhandene Zutaten")

class rezeptsammlung(FlaskForm):
    btnSuchen = SubmitField("🔎")
    alleRezeptNamen = []
    for entry in rezept.query.all():
        alleRezeptNamen.append(entry.name)

    rezeptnamen = SelectField("Direktsuche", choices=[""]+alleRezeptNamen)
    rezeptkategorien = SelectField("Eigenschaft", choices=[""]+["Vegan", "Vegetarisch", "Einfach", "Fleisch"])
    maxZutaten = SelectField("Maximale Zutaten", choices=["",4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
