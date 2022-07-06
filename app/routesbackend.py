from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID,createArrayHelper, savepic


import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc


##############
# Startseite #
##############

@app.route('/admin/')
def admin():
    """Dies ist der Admin Hauptindex"""
    return render_template('admin_index.html')





MODE_ZUTATEN = 0
MODE_TAGS = 1
MODE_REZEPT = 2
MODE_HAND = 3
MODE_RZHAT = 4
MODE_TAGver = 5
MODE_HANDver = 6
MODE_HANDadd = 7

def remover(mode : int,classes, redirect_url: str):
    page = request.args.get('page', 0, type=int)
    liste = classes.query.paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for(redirect_url, page=liste.next_num)  if liste.has_next else None
    prev_url = url_for(redirect_url, page=liste.prev_num)  if liste.has_prev else None
    if mode == MODE_ZUTATEN:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Zutatentferner",targetzutat=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_REZEPT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Rezeptentferner",targetrezept=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_TAGS:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Tagsentferner",targettags=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_RZHAT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Zutat <-> Rezept",targerzhat=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HAND:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Handlungsschritten (old)",handlung=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_TAGver:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Tags <-> Rezept",Tagver=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HANDver:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Handlungschritten <-> Rezept",HANDver=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HANDadd:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungadder von Handlungschritten <-> Rezept",MODE_HANDadd=True,next_url=next_url,prev_url=prev_url,page=page)
   
    else:
        print("Kein Tamplate gefunden!")
        return "Kein Tamplate gefunden!"



##############
#    rzhat   #
##############


@app.route('/admin/remove/rzhat/picker/',methods=['GET','POST'])
def removeRZhat():
    return remover(MODE_RZHAT,rezept,'removeRZhat')    

@app.route('/admin/remove/rzhat/remover/<path:rid>',methods=['GET','POST'])
def removeRZhat2(rid):
    ausrezept = rezept.query.get(rid)
    zutatenliste = ausrezept.zutaten
    for assoc in zutatenliste:
        print(assoc.hatzutat.id)
    return render_template('admin_remove.html',inhalt=zutatenliste,titlet="Verknüpfungs Entferner",rid=rid,targerzhat2=True)


##############
#   generic  #
##############


def entfernerAnzeiger(classes,redirect_url : str,title):
    """Wir wählen zuerst eine Rezept aus um es dann zu bearbeiten"""
    form = forms.rzanlegen()
    form.rezeptpicker.choices = createArrayHelper(classes.query.order_by(classes.name).all())
    if form.validate_on_submit():
        return redirect(url_for(redirect_url,ids=form.rezeptpicker.data))
    return render_template('admin_rzpicker.html',form=form,titlet=title)

def entfernerfuction(ids,classes,ursprung_class,mode,redirect_url):
    """Wir wählen, die Zutaten aus, die wir zum rezept speichern wollen."""
    form = forms.verknupfungsanleger()
    # Alle Zutaten, die schon verknüpft sind, müssen gelöscht werden
    if classes == handlungsschritt:
        # Handlungsschritt hat keinen .name Attribut
        form.zutaten.choices = createArrayHelper(classes.query.all())
    else:
        form.zutaten.choices = createArrayHelper(classes.query.order_by(classes.name).all())
    auswahl = ursprung_class.query.get(ids)
    if auswahl is None:
        abort(404) 

    if form.validate_on_submit() or form.submit.data:
        """ Hier funktioniert validate on submit nicht"""
        
        ausgewählte = form.zutaten.data
        """Alle Zutaten, die man ausgewählt holen"""
        for entry in ausgewählte:
            gettingclass = classes.query.get(entry)
            """ Zielobjekt aus der entsprechen Klasse zum Adden hinzufügen holen"""
            if mode == MODE_ZUTATEN:
                """ Zielobjekt ist Zutat"""
                # auswahl = Klasse von rezept
                # gettingclass = Klasse von Zutat
                a = Association(menge=25,optional=True)
                a.hatzutat = gettingclass
                with db.session.no_autoflush:
                    auswahl.zutaten.append(a)
            if mode == MODE_TAGS:
                """ Zielobjekt ist Klasse Tags """
                auswahl.tags.append(gettingclass)
            if mode == MODE_HAND:
                """Wir fügen Handlungsschritte mit Positionen zu."""
                a = AssociationRHhat(position=1)
                a.hatid = gettingclass
                with db.session.no_autoflush:
                    auswahl.handlungsschritte.append(a)
            db.session.commit()
        flash("Gespeichert!")
        return redirect(url_for(redirect_url,ids=ids))
    if mode == MODE_ZUTATEN:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Zutaten",rezeptnamen=auswahl.name,inhalt=auswahl.zutaten)
    if mode == MODE_TAGS:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Tags",rezeptnamen=auswahl.name,inhalt=auswahl.tags)
    if mode == MODE_HAND:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Handlungsschritte",rezeptnamen=auswahl.name,inhalt=auswahl.handlungsschritte)
    else:
        return "Error! <br />Kein Template gefunden!"





