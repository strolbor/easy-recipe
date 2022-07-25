from app import app, db, forms
from app.rezept import handlungsschritt, rezept,AssociationRHhat
from app.backend_helper import getNewID, savepic,createArrayHelper
from app.routesbackend import remover
from app.routesbackend import remover, MODE_HANDver,MODE_HANDadd,MODE_HANDver,MODE_HAND

import os
from flask import redirect, render_template,request
from flask.helpers import flash, url_for
from sqlalchemy import desc

##############
#  Handlung  #
##############

# Handlungschritte anzeigen lassen
@app.route('/admin/hand/showhandlungsschritt')
def showhandlungsschritt():
    page = request.args.get('page', 0, type=int)
    liste = rezept.query.order_by(handlungschritt.name).paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for('showhandlungsschritt', page=liste.next_num)  if liste.has_next else None
    prev_url = url_for('showhandlungsschritt', page=liste.prev_num)  if liste.has_prev else None
    return render_template('admin_show.html',liste=liste.items,titlet="Zutaten",next_url=next_url, \ 
        prev_url=prev_url,showCase=True,page=page)
    
    #liste = handlungsschritt.query.all()
    
    #return render_template('admin_show.html',liste=liste,titlet="Handlungsschritte")

# Handlungschritte Editor, bei der Anzeige
@app.route('/admin/hand/modifyHandlung/<path:ids>',methods=['GET','POST'])
def modifyHandlung(ids):
    """Hiermit wird eine Zutat modifiziert."""
    # ids => Rezeptid
    rezept1 = rezept.query.get(ids)
    # Formular initalisieren
    form = forms.handlungschrittanlegen()
    # Handlungschritt Objekt holen
    modifyHand = handlungsschritt.query.get(ids)

    # Wenn Formular abgeschickt ist
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


# Handlungschritte anlegen
@app.route('/admin/hand/addhandlung/',methods=['GET','POST'])
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

# Handlungschritt verknüpfer
# Part 1
# Rezept auswählen
@app.route("/admin/hand/handver1/")
def handver1():
    return remover(MODE_HANDadd,rezept,'handver1')  

@app.route("/admin/hand/handver2/<path:rid>",methods=['GET','POST'])
def handver2(rid):
    rezeptw = rezept.query.get(rid)
    form = forms.handlungverknüpfer()
    form.handlungschritt.choices=createArrayHelper(handlungsschritt.query.all())
    rezeptw = rezept.query.get(rid)
    if request.method == "POST":
        if form.validate_on_submit:
            assoc1 = AssociationRHhat(position=int(form.position.data)) # Extra Daten hinzufügen
            hand = handlungsschritt.query.get(form.handlungschritt.data)
            assoc1.hatid =  hand# Verknüpfung
            with db.session.no_autoflush:
                rezeptw.handlungsschritte.append(assoc1)
            db.session.commit()
            flash("Gespeichert")
            return redirect(url_for('handver2',rid=rid))
    return render_template('admin_handlungver.html',form=form,rezept1=rezeptw)

@app.route("/admin/hand/handdeleter1")
def handdeleter1():
    # Erst müssen wir die Rezepte auswählen
    return remover(MODE_HANDver,rezept,'handdeleter2')  

@app.route("/admin/hand/handdeleter2/<path:rid>")
def handdeleter2(rid):
    # Dann die aussocication suchen
    assoc1 =  AssociationRHhat.query.filter_by(rid=rid).all()
    r1 = rezept.query.get(rid)
    return render_template('admin_remove.html',inhalt=assoc1,titlet="Verknüpfungsentferner Handlungsschritte (keine Löschung der Handlungsschritte)",rid=rid,handdeleter2=True)
    # Dann entsorechend der Auswahl die Handlungsschritte löschen

# Handlungschritt entfernen
@app.route('/admin/hand/removehandlungsschritt/')
def removehandlungsschritt():
    """Hiermit wird ein Handlungsschritt entfernt"""
    return remover(MODE_HAND,handlungsschritt,"Handlungsschritt Entferner")
