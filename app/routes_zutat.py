from operator import methodcaller
from app import app, db, forms
from app.rezept import kategorie, zutat, rezept
from app.backend_helper import getNewID, savepic
from app.routesbackend import remover, MODE_ZUTATEN, showclass, createArrayHelper

import os
from flask import redirect, render_template, request
from flask.helpers import flash, url_for
from sqlalchemy import desc


##############
#    Zutat   #
##############
@app.route('/admin/add/Zutat/', methods=['GET', 'POST'])
def addzutat():
    """Hiermit wird eine neue Zutat angelegt."""
    form = forms.zutatanlegen()
    if request.method == "POST" and form.submit.data:
        tmp = zutat.query.filter_by(name=form.name.data).first()
        print(tmp)
        if tmp is None:
            # Daten des Uploads holen
            bild_url = ""
            idneu = getNewID(zutat)
            picure_url = savepic('bildupload', request.files, f'zutat{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url = picure_url
            newzutat = zutat(name=form.name.data,
                            einheit=form.einheit.data, bild=bild_url)
            db.session.add(newzutat)
            db.session.commit()
            flash(f'{form.name.data} wurde erfolgreich angelegt!')
        else:
            flash("Zutat existiert schon.")
    return render_template('admin_zutat.html', form=form, zutat=None)


@app.route('/admin/show/zutat/')
def showZutaten():
    return showclass(zutat, zutat.name, "Zutaten", "showZutaten")


@app.route('/admin/remove/zutat')
def removeZutat():
    """Hiermit wird eine Zutat entfernt"""
    return remover(MODE_ZUTATEN, zutat, 'removeZutat')


@app.route('/admin/modify/zutat/<path:ids>', methods=['GET', 'POST'])
def modifyZutat(ids):
    """Hiermit wird eine Zutat modifiziert."""
    form = forms.zutatanlegen()
    modifyZutat = zutat.query.get(ids)
    form.kategorie.choices = createArrayHelper(kategorie.query.all())

    if request.method == "POST" and form.submit.data:
        # Daten speichern
        modifyZutat.name = form.name.data
        modifyZutat.einheit = form.einheit.data

        picure_url = savepic('bildupload', request.files,
                                f'zutat{modifyZutat.id}')
        if not (picure_url == "A" or picure_url == "B"):
            """Bild wurde gefunden und benutzt.
            Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
            modifyZutat.bild = picure_url

        # Kategorien reintun
        modifyZutat.kategorie = []
        for entrykategorie in form.kategorie.data:
            toaddKat = kategorie.query.get(entrykategorie)
            modifyZutat.kategorie.append(toaddKat)
        db.session.commit()

        flash(f"{modifyZutat.name}  wurde gespeichert")
        return redirect(url_for('modifyZutat', ids=ids))


    form.name.data = modifyZutat.name
    form.einheit.data = modifyZutat.einheit
    return render_template('admin_zutat.html', form=form, titlet="Zutat Eigenschaften ändern", zutat=modifyZutat)
