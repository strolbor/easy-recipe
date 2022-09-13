from app import app, db, forms
from app.rezept import handlungsschritt, rezept,AssociationRHhat
from app.backend_helper import getNewID, savepic,createArrayHelper
from app.routesbackend import remover
from app.routesbackend import remover, MODE_HANDver,MODE_HANDadd,MODE_HANDver,showclass

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
    return showclass(handlungsschritt,handlungsschritt.id,"Handlungsschritte","showhandlungsschritt")

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
    page = request.args.get('page', 0, type=int)


    # Wenn Formular abgeschickt ist
    if form.validate_on_submit():
        modifyHand.text = form.beschreibung.data
        if request.method == 'POST': 
            picure_url = savepic('bildupload1', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild = picure_url
            picure_url = savepic('bildupload2', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild2 = picure_url

        db.session.commit()
        flash(f"{modifyHand.text} wurde gespeichert")
        return redirect(url_for('modifyHandlung',ids=ids))
    array_pic =[]
    if modifyHand.bild is not None:
        array_pic.append(modifyHand.bild)
    if modifyHand.bild2 is not None:
        array_pic.append(modifyHand.bild2)
    form.beschreibung.data = modifyHand.text
    if len(array_pic) == 0:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,titlet="Handlungsschritt ändern")
    else:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,array_pic=array_pic,showbilds=True,titlet="Handlungsschritt ändern")

# Handlungschritt verknüpfer
# Part 1
# Rezept auswählen
@app.route("/admin/hand/handver1/")
def handver1():
    return remover(MODE_HANDadd,rezept,'handver1')  

@app.route("/admin/hand/handver2/<path:rid>",methods=['GET','POST'])
def handver2(rid):
    rezeptw : rezept = rezept.query.get(rid)
    form = forms.handlungverknüpfer()
    form.handlungschritt.choices=createArrayHelper(handlungsschritt.query.all())
    rezeptw = rezept.query.get(rid)
    if request.method == "POST":
        if form.validate_on_submit:
            # Position des Handlungsschritt erhalten
            pos = -1
            try:
                pos = int(form.position.data)
            except ValueError:
                pass
            # Gucken, ob es schon vorhanden ist.
            test : bool = False
            for entry in rezeptw.handlungsschritte:
                if entry.position == pos:
                    test = True
            
            # Wenn die Position erkannt haben und überprüft haben, dass es leer ist
            # So können wir das Element hinzufügen.
            if pos >= 0 and test == False:
                assoc1 = AssociationRHhat(position=int(form.position.data)) # Extra Daten hinzufügen
                hand = handlungsschritt.query.get(form.handlungschritt.data)
                assoc1.hatid =  hand# Verknüpfung
                with db.session.no_autoflush:
                    rezeptw.handlungsschritte.append(assoc1)
                db.session.commit()
                flash("Gespeichert")
            else:
                flash("Konnte nicht gespeichert werden.")
            return redirect(url_for('handver2',rid=rid))
    return render_template('admin_handlungver.html',form=form,rezept1=rezeptw)

