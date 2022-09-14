from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField, StringField, SelectField
from wtforms.validators import DataRequired
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
    eingabe = SelectMultipleField(
        'Zur Verfügung stehende Objekte', choices=zutatenListe)
    selected = SelectMultipleField('Ausgewählte Objekte', choices=[])
    submitAdd = SubmitField("-->")        # Hinzufuegen
    submitRm = SubmitField("<--")  # Entfernen
    submitLoesen = SubmitField("Auswahl lösen")
    submitSuchen = SubmitField("Suchen")

    # Altes Suchfeld
    suchtext = StringField('Zutat suchen')
    submitSuchtext = SubmitField('Starte Zutatensuche')

    # "Neues" Suchfeld, Script mit Dropdown Menü
    suchfeld = SelectField("Starte Zutatensuche", choices=[""] + zutatenListe)
    sumbitAddSuchbegriff = SubmitField("Hinzufügen")

    # Kategorien mit Buttons für Zutaten und Stringfields für Kategorienamen
    class homepage_kategorie():
        name = ""
        zutaten = []

        def __init__(self, _name, _zutaten):
            self.name = _name
            self.zutaten = _zutaten

    # Kategorien beinhaltet Objekte der Klasse oben, jeweils ein Stringfield für Name und Array von Submitfields
    kategorien = []

    for entry in kategorie.query.all():
        kategorieName = entry.name
        kat_zutatsubmits = []
        for zut in entry.bkat:
            # hänge Submitliste einen Button mit der Zutat an, der beim Drücken die Zutat in Auswahl Liste addet
            kat_zutatsubmits.append(zutat.query.get(zut.id))

        kategorien.append(homepage_kategorie(kategorieName, kat_zutatsubmits))


class rezeptanlegen(FlaskForm):
    """ Rezeptanlege Seite im Backend """
    rezeptname = StringField('Name des Rezepts', validators=[DataRequired()])
    bildupload = FileField('Bild des Rezepts')
    tags = SelectField('Tags')
    submit = SubmitField('Speichern')


class handlungschrittanlegen(FlaskForm):
    """ Handlungsschrittanzeige Seite im Backend """
    bildupload1 = FileField('Bild des Handlungsschrittes 1')
    bildupload2 = FileField('Bild des Handlungsschrittes 2')
    beschreibung = StringField(
        'Handlungschrittbeschreibung', validators=[DataRequired()])
    submit = SubmitField('Speichern')


class rzanlegen(FlaskForm):
    rezeptpicker = SelectField('Rezept Picker', validators=[DataRequired()])
    submit = SubmitField('Rezept auswählen')


class verknupfungsanleger(FlaskForm):  # rzzutaten
    zutaten = SelectMultipleField()
    submit = SubmitField('Einstellungen speichern')


class zutatanlegen(FlaskForm):
    name = StringField('Name der Zutat', validators=[DataRequired()])
    einheit = StringField('Einheit der Zutat', validators=[DataRequired()])
    bildupload = FileField('Bild der Zutat hochladen')
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
    optionaliat = SelectField("Optionalität", choices=["Nein", "Ja"])
    menge = StringField("Menge der Zutaten", validators=[DataRequired()])
    submit = SubmitField("Speichern")


class rezeptanzeige(FlaskForm):
    submitTest = SubmitField("Suchen")
    # Nicht löschen
    # Das heißt nur dämlich mit Test


class nutzerein(FlaskForm):
    rname = StringField('Name')
    bildupload = FileField('Bild')
    handlung = StringField('Handlungschritt')
    tags = SelectField('Tags')
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

    rezeptnamen = SelectField("Rezeptsuche", choices=[""]+alleRezeptNamen)
    rezeptkategorien = SelectField("Rezeptkategorien", choices=[""]+["Vegan", "Vegetarisch", "Leicht", "Viele Zutaten", "Tag1", "Tag2", "Tag3"])
    maxZutaten = StringField(render_kw={"placeholder": "Maximale Zutaten"})
