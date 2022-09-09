import imp
import re
from app import app, db, forms
from app.rezept import rezept, zutat, handlungsschritt, tags, Association, AssociationRHhat
from app.backend_helper import getNewID, createArrayHelper, savepic, createArrayHelper2
from app.routesbackend import remover, MODE_REZEPT,  MODE_REZEPTadd, showclass

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
        tagid = request.form.get('tags')
        handlungsschritttext = request.form.get('handlung')
        
        # Rezept anlegen
        idn = newRezept(rezeptname, tagid,  request.method, request.files)
        rnew : rezept = rezept.query.get(idn)

        # Zutaten verknüpfen
        counter = 0
        for entry in zutaten:
            if int(entry) > 0:
                print(f"Erhalte Zutaten zum hinzufügen: {entry}")
                zuttmp = zutat.query.get(entry)
                assoc1 = Association(menge=menge[counter], optional=False)
                assoc1.hatzutat = zuttmp
                with db.session.no_autoflush:
                    rnew.zutaten.append(assoc1)
                db.session.commit()
            counter +=1

        # Handlungschritt anlegen
        handlung = handlungsschritt(
            bild="", bild2="", text=handlungsschritttext)
        db.session.add(handlung)
        db.session.commit()

        # Handlungsschritt verknüpfen
        nhand = handlungsschritt.query.filter_by(text=handlungsschritttext).first()
        assoc1 = AssociationRHhat(position=1)
        assoc1.hatid = nhand
        with db.session.no_autoflush:
            rnew.handlungsschritte.append(assoc1)
        db.session.commit()

        # Tag verknüpfen
        print(tagid)
        tag1 = tags.query.get(tagid)
        rnew.tags = []
        rnew.tags.append(tag1)

        # speichern
        db.session.commit()
        print("Rezept:", rezeptname)
        for value in zutaten:
            print(f"Erhalten in Zutaten: {value}")
        for value in menge:
            print(f"Erhalten in Menge: {value}")
        #flash('New record created successfully')
    return "ok"


@app.route('/admin/modify/rezept/<path:ids>', methods=['GET', 'POST'])
def modifyrezept(ids):
    form = forms.rezeptanlegen()
    form.tags.choices = createArrayHelper(tags.query.all())
    zuRezept : rezept = rezept.query.get(ids)
    form.handlung.data = zuRezept.handlungsschritte[0].hatid.text

    if form.validate_on_submit():
        # Name speichern
        zuRezept.name = form.rezeptname.data
        if request.method == 'POST':
            # Bild aktualisieren
            picure_url = savepic('bildupload', request.files, f'rezept{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                zuRezept.bild = picure_url
        # Handlungsschritt Text bearbeiten
        zuRezept.handlungsschritte[0].hatid.text = form.handlung.data
        # Speichern des Eintrages
        db.session.commit()
        flash(f"{zuRezept.name} wurde gespeichert!")
        return redirect(url_for('modifyrezept', ids=ids))

    form.rezeptname.data = zuRezept.name
    form.tags.data = createArrayHelper(zuRezept.tags)

    if zuRezept.bild != "":
        # Diese Aufruf wird gemacht, wenn ein Bild vorhanden ist
        return render_template('admin_rezept.html', form=form, titlet="Rezepts ändern", showbilds=True, showbild=zuRezept.bild, rid=ids)
    else:
        # Diese Aufruf wird gemacht, wenn kein Bild vorhanden ist
        return render_template('admin_rezept.html', form=form, titlet="Rezepts ändern", rid=ids)

# Rezept <-> Handlungschritt Verknüpfer


@app.route("/admin/rezept/rezeptver1")
def rezeptver1():
    return remover(MODE_REZEPTadd, rezept, 'rezeptver1')


@app.route("/admin/rezept/rezeptver2/<path:rid>", methods=['GET', 'POST'])
def rezeptver2(rid):
    rezept1 = rezept.query.get(rid)
    form = forms.rezeptzutatadder()
    # Zutaten auswählbar machen
    form.zutat.choices = createArrayHelper2(zutat.query.all())
    if form.validate_on_submit and request.method == "POST":
        # Wir speichern  das Formular
        assoc1 = Association(menge=int(form.menge.data), optional=False)
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
