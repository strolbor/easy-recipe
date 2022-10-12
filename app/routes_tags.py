from app import app, db, forms
from app.rezept import rezept,tags
from app.backend_helper import createArrayHelper
from app.routesbackend import showclass

import os
from flask import redirect, render_template, request
from flask.helpers import flash, url_for

##############
#    tags   #
##############

# Um die Tags anzuzeigen
@app.route('/tags/show/')
def showTags():
    return showclass(tags,tags.name,"Tags","showTags")

# Tags hinzufügen
@app.route("/tags/add",methods=['GET','POST'])
def addTags():
    form = forms.taganlegen()
    if form.validate_on_submit():
        # prüfen, ob Tag schon vorhanden ist
        isnew = tags.query.filter_by(name=form.name.data).first()
        if isnew is None:
            newtag = tags(name=form.name.data)
            db.session.add(newtag)
            db.session.commit()
            flash(f'Tag <{form.name.data}> wurde erfolgreich angelegt.')
        else:
            flash(f"Fehler: Tag <{form.name.data}> existiert schon.")
        return redirect(url_for('addTags'))

    return render_template('admin_tag.html',form=form)

# Verknüpfunganlegen
# Part 1
# Auswählen der Rezepte
@app.route("/tags/modify/<path:ids>",methods=['GET','POST'])
def modifyTags(ids):
    form = forms.taganlegen()
    zuTag = tags.query.get(ids)
    page = int(request.args.get('page', 1))
    if zuTag is None:
        return redirect(url_for('showTags',ppage=page))
    if form.validate_on_submit():
        zuTag.name = form.name.data
        db.session.commit()
        flash(f"{zuTag.name} wurde gespeichert!")
        return redirect(url_for('modifyTags',ids=ids))
    form.name.data = zuTag.name
    return render_template('admin_tag.html',form=form,titlet="Tag ändern")

# Verknüpfunganlegen
# Part 2
# Tags mit dem vorgenannten Rezept verknüpfen.
@app.route('/tags/relationship1',methods=['GET','POST'])
def CHGrthat():
    """Wir wählen zuerst eine Rezept aus um es dann zu bearbeiten"""
    form = forms.rzanlegen()
    form.rezeptpicker.choices = createArrayHelper(rezept.query.order_by(rezept.name).all())
    if form.validate_on_submit():
        return redirect(url_for('CHGrthat2',ids=form.rezeptpicker.data))
    return render_template('admin_rzpicker.html',form=form,titlet="Verknüpfung anlegen")

# Verknüpfunganlegen
# Part 2a
# Tags mit dem vorgenannten Rezept verknüpfen.
@app.route('/tags/relationship1/<path:ids>', methods=['GET', 'POST'])
def CHGrthat2(ids):
    """Wir wählen, die Zutaten aus, die wir zum Rezept speichern wollen."""
    form = forms.verknupfungsanleger()
    # Alle Zutaten, die schon verknüpft sind, müssen gelöscht werden
    form.zutaten.choices = createArrayHelper(tags.query.order_by(tags.name).all())
    auswahl = rezept.query.get(ids)
    if auswahl is None:
        page = int(request.args.get('page', 1))
        return redirect(url_for('showTags',page=page))
    if form.validate_on_submit() or form.submit.data:
        """ Hier funktioniert validate on submit nicht"""
        
        ausgewählte = form.zutaten.data
        """Alle Zutaten, die man ausgewählt holen"""
        for entry in ausgewählte:
            gettingclass = tags.query.get(entry)
            """ Zielobjekt aus der entsprechen Klasse zum Adden hinzufügen holen"""
            auswahl.tags.append(gettingclass)
            db.session.commit()
        flash("Gespeichert!")
        return redirect(url_for('CHGrthat2',ids=ids))
    return render_template('admin_rzpickerzutat.html',form=form,modus="Tags",rezeptnamen=auswahl.name,inhalt=auswahl.tags)


@app.route('/tags/delete/<path:ids>/')
def deleteTags(ids):
    """Tags Objekt entfernen"""
    page = request.args.get('page', 0, type=int)
    tagdel = tags.query.get(ids)
    if tagdel is None:
        pass
    else:
        # Tag Zugehörigkeiten löschen
        try:
            tagdel.belongs = []
        except AttributeError:
            pass
        
        # Tag löschen
        db.session.delete(tagdel)

        db.session.commit()
    return redirect(url_for('showTags',page=page))