from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID,createArrayHelper, savepic
from app.routesbackend import remover

import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc

##############
#  Handlung  #
##############

@app.route('/admin/add/handlungsschritt/',methods=['GET','POST'])
def addhandlung():
    """Dies ist der Admin Hauptindex"""
    form = forms.handlungschrittanlegen()
    if form.validate_on_submit():
        if request.method == 'POST':
            bild_url = ""
            bild_url2 = ""
            idneu = getNewID(handlungsschritt)
            picure_url = savepic('bildupload1', request.files, f'hand{idneu}')
            print(picure_url)
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url = picure_url
            # Zweites Handlungsbild
            picure_url = savepic('bildupload2', request.files, f'hand{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url2 = picure_url
            newhand = handlungsschritt(bild=bild_url,bild2=bild_url2,text=form.beschreibung.data)
            print(newhand)
            db.session.add(newhand)
            db.session.commit()
            flash(f'Handlungsschritt wurde erfolgreich angelegt!')
    return render_template('admin_hand.html',form=form,titlet="Neuen Handlungsschritt anlegen")

@app.route('/admin/modify/handlungsschritt/<path:ids>',methods=['GET','POST'])
def modifyHandlung(ids):
    """Hiermit wird eine Zutat modifiziert."""
    form = forms.handlungschrittanlegen()
    modifyHand = handlungsschritt.query.get(ids)

    if form.validate_on_submit():
        modifyHand.text = form.beschreibung.data
        if request.method == 'POST': 
            picure_url = savepic('bildupload1', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild = picure_url
                print("Bild neu gesetzt")
            picure_url = savepic('bildupload2', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild2 = picure_url
                print("Bild neu gesetzt")

        db.session.commit()
        flash(f"{modifyHand.text} wurde gespeichert")
        return redirect(url_for('modifyHandlung',ids=ids))
    array_pic =[]
    print(modifyHand.bild,modifyHand.bild2,modifyHand.id)
    if modifyHand.bild != "":
        array_pic.append(modifyHand.bild)
    if modifyHand.bild2 != "":
        array_pic.append(modifyHand.bild2)
    print(array_pic)
    form.beschreibung.data = modifyHand.text
    if len(array_pic) == 0:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,titlet="Handlungsschritt ändern")
    else:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,array_pic=array_pic,showbilds=True,titlet="Handlungsschritt ändern")

@app.route('/admin/remove/removehandlungsschritt')
def removehandlungsschritt():
    """Hiermit wird ein Handlungsschritt entfernt"""
    return remover(MODE_HAND,handlungsschritt,"Handlungsschritt Entferner")


@app.route('/admin/show/handlungsschritt/')
def showhandlungsschritt():
    liste = handlungsschritt.query.all()
    return render_template('admin_show.html',liste=liste,titlet="Handlungsschritte")