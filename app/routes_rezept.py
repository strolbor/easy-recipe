import imp
import re
from app import app, db, forms
from app.rezept import rezept, zutat, handlungsschritt, tags, Association, AssociationRHhat
from app.backend_helper import getNewID, createArrayHelper, savepic
from app.routesbackend import remover, MODE_REZEPT, MODE_RZHAT, MODE_REZEPTadd, showclass

import os
from flask import redirect, render_template, request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc
import sqlalchemy

##############
#   Rezept   #
##############


@app.route('/admin/show/rezepte/')
def showRezepte():
    return showclass(rezept, rezept.name, "Rezepte", "showRezepte")


def newRezept(rname: str, tname: str, reqmethod, reqfiles):
    """Kapselung von Rezepte"""
    # Daten des Uploads holen
    bild_url = ""
    if reqmethod == 'POST':
        """ Die Post Methode wird aufgerufen, wenn wir ein Bild hochladen möchten und verarbeiten wollen."""
        idneu = getNewID(rezept)

        """ Wir suchen die nächste ID"""
        picure_url = savepic('bildupload', reqfiles, f'rezept{idneu}')
        if not (picure_url == "A" or picure_url == "B"):
            """ Bild wurde gefunden und hochgeladen"""
            bild_url = picure_url

    new = rezept(name=rname, bild=bild_url)
    new.tags.append(tags.query.get(tname))
    """ Neues Rezept wurde erstellt."""
    db.session.add(new)
    db.session.commit()
    rnew: rezept  = rezept.query.filter_by(name=rname).first()
    return rnew.id


@app.route('/admin/add/rezept/', methods=['GET', 'POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    # Alle Tags holen
    form.tags.choices = createArrayHelper(tags.query.all())

    # Formular wird abgesendet
    if form.validate_on_submit():
        idn = newRezept(form.rezeptname.data, form.tags.data, request.method,request.files)
        print(idn)
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_rezept.html', form=form, titlet="Neues Rezept anlegen")


@app.route("/nutzer/rezept/eingabe")
def nutzerrezeptein():
    """Nutzereingabe Menü"""
    form = forms.nutzerein()
    # Alle Tags holen
    form.tags.choices = createArrayHelper(tags.query.all())
    # Das ist schon so fertig
    return render_template('nutzer_rezeptanlege.html', form=form, zutaten=zutat.query.all())


@app.route("/ctl/nutzer/rezept/post", methods=["POST", "GET"])
def postrezept():
    print("hirewhi")
    # GET /nutzer/rezept/eingabe?
    # csrf_token=ImQyYmE0ZjNiMTY0YTgyZDZiNzhjOWMxMjQwY2Y5N2Q2MWY0MTUyZWMi.YxnmQQ.PvCAKVJUzzIA8VIXTdAn4HRUTmI&
    # rname=we432&
    # bildupload=
    # &zutat%5B%5D=3& menge%5B%5D=1&
    # zutat%5B%5D=17& menge%5B%5D=2&
    # zutat%5B%5D=16& menge%5B%5D=3
    # handlung=ew&tags=1&
    # submit=Speichern
    if request.method == 'POST':
        # Informationen abrufen
        zutaten = request.form.getlist('zutat[]')
        menge = request.form.getlist('menge[]')
        rezeptname = request.form.get('rname')
        tagname = request.form.get('tags')
        
        # Rezept anlegen
        idn = newRezept(rezeptname, tagname,  request.method, request.files)
        rnew : rezept = rezept.query.get(idn)

        # Zutaten verknüpfen

        # Handlungsschritt verknüpfen

        # Tag verknüpfen
        rnew.tags.append(tagname)

        # speichern
        db.session.commit()
        print("Rezept:", rezeptname)
        for value in zutaten:
            print(f"Erhalten in Zutaten: {value}")
        for value in menge:
            print(f"Erhalten in Menge: {value}")
        flash('New record created successfully')
    return "ok"


@app.route('/admin/modify/rezept/<path:ids>', methods=['GET', 'POST'])
def modifyrezept(ids):
    form = forms.rezeptanlegen()
    form.tags.choices = createArrayHelper(tags.query.all())
    zuRezept = rezept.query.get(ids)

    if form.validate_on_submit():
        # Name speichern
        zuRezept.name = form.rezeptname.data
        if request.method == 'POST':
            # Bild aktualisieren
            picure_url = savepic('bildupload', request.files, f'rezept{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                zuRezept.bild = picure_url
        # Speichern des Eintrages
        db.session.commit()
        flash(f"{zuRezept.name} wurde gespeichert!")
        return redirect(url_for('modifyrezept', ids=ids))

    form.rezeptname.data = zuRezept.name
    form.tags.data = createArrayHelper(zuRezept.tags)

    if zuRezept.bild != "":
        # Diese Aufruf wird gemacht, wenn ein Bild vorhanden ist
        return render_template('admin_rezept.html', form=form, titlet="Rezepts ändern", showbilds=True, showbild=zuRezept.bild)
    else:
        # Diese Aufruf wird gemacht, wenn kein Bild vorhanden ist
        return render_template('admin_rezept.html', form=form, titlet="Rezepts ändern")

# Rezept <-> Handlungschritt Verknüpfer


@app.route("/admin/rezept/rezeptver1")
def rezeptver1():
    return remover(MODE_REZEPTadd, rezept, 'rezeptver1')


@app.route("/admin/rezept/rezeptver2/<path:rid>", methods=['GET', 'POST'])
def rezeptver2(rid):
    rezept1 = rezept.query.get(rid)
    form = forms.rezeptzutatadder()
    # Zutaten auswählbar machen
    form.zutat.choices = createArrayHelper(zutat.query.all())
    if form.validate_on_submit and request.method == "POST":
        # Wir speichern  das Formular
        optionalbool = False
        if form.optionaliat.data == "Ja":
            optionalbool = True
        assoc1 = Association(menge=int(form.menge.data), optional=optionalbool)
        zutat1 = zutat.query.get(int(form.zutat.data))
        assoc1.hatzutat = zutat1
        try:
            with db.session.no_autoflush:
                rezept1.zutaten.append(assoc1)
            db.session.commit()
            flash("Gespeichert!")
            return redirect(url_for('rezeptver2', rid=rid))
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            flash("Fehler: Zutat wurde bereits verknüpft!")

    return render_template('admin_addrzver.html', form=form, rezept1=rezept1)


@app.route('/admin/rezept/removeRezept')
def removeRezept():
    """ Löschen eines Rezeptes"""
    return remover(MODE_REZEPT, rezept, 'removeRezept')
