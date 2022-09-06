from app import app, db, forms
from app.rezept import kategorie, zutat
from app.backend_helper import getNewID, savepic
from app.routesbackend import remover,MODE_ZUTATEN,showclass,createArrayHelper

import os
from flask import redirect, render_template,request
from flask.helpers import flash, url_for
from sqlalchemy import desc



##############
#    Zutat   #
##############
@app.route('/admin/add/Zutat/',methods=['GET','POST'])
def addzutat():
    """Hiermit wird eine neue Zutat angelegt."""
    form = forms.zutatanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        bild_url=""
        if request.method == 'POST':
            idneu = getNewID(zutat)
            picure_url = savepic('bildupload', request.files, f'zutat{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url = picure_url
        newzutat = zutat(name=form.name.data,einheit=form.einheit.data,bild=bild_url)
        db.session.add(newzutat)
        db.session.commit()
        flash(f'{form.name.data} wurde erfolgreich angelegt!')
    return render_template('admin_zutat.html',form=form)

@app.route('/admin/show/zutat/')
def showZutaten():
    return showclass(zutat,zutat.name,"Zutaten","showZutaten")

@app.route('/admin/remove/zutat')
def removeZutat():
    """Hiermit wird eine Zutat entfernt"""
    return remover(MODE_ZUTATEN,zutat,'removeZutat')

@app.route('/admin/modify/zutat/<path:ids>',methods=['GET','POST'])
def modifyZutat(ids):
    """Hiermit wird eine Zutat modifiziert."""
    form = forms.zutatanlegen()
    modifyZutat = zutat.query.get(ids)
    form.kategorie.choices = createArrayHelper(kategorie.query.all())


    if form.validate_on_submit() or form.submit.data:
        print("vcalidate")
        modifyZutat.name = form.name.data
        modifyZutat.einheit = form.einheit.data

        if request.method == 'POST':
            picure_url = savepic('bildupload', request.files, f'zutat{modifyZutat.id}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyZutat.bild = picure_url
            getkategorie = kategorie.query.get(form.kategorie.data)
            modifyZutat.kategorie.append(getkategorie)
        db.session.commit()
        
        flash(f"{modifyZutat.name}  wurde gespeichert")
        return redirect(url_for('modifyZutat',ids=ids))

    form.name.data = modifyZutat.name
    form.einheit.data = modifyZutat.einheit
    
    
    if modifyZutat.bild == "":
        return render_template('admin_zutat.html',form=form,titlet="Zutat Eigenschaften ändern",zukate=modifyZutat.kategorie)
    else:
        return render_template('admin_zutat.html',form=form,titlet="Zutat Eigenschaften ändern",showbild=modifyZutat.bild,showbilds=True,zukate=modifyZutat.kategorie)
       