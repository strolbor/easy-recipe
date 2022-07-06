from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
from app.backend_helper import createArrayHelper
from app.routesbackend import remover,MODE_TAGS,MODE_TAGver

import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc

##############
#    tags   #
##############

# Um die Tags anzuzeigen
@app.route('/admin/tags/showTags/')
def showTags():
    liste = tags.query.order_by(tags.name).all()
    return render_template('admin_show.html',liste=liste,titlet="Tags")

# Tags hiunzufügen
@app.route("/admin/tags/addTags",methods=['GET','POST'])
def addTags():
    form = forms.taganlegen()
    if form.validate_on_submit():
        newtag = tags(name=form.name.data)
        db.session.add(newtag)
        db.session.commit()
        flash(f'Tag <{form.name.data}> wurde erfolgreich angelegt.')
        return redirect(url_for('addTags'))

    return render_template('admin_tag.html',form=form)

# Verknüpfunganlegen
# Part 1
# Auswählen der Rezepte
@app.route("/admin/tags/modifyTags/<path:ids>",methods=['GET','POST'])
def modifyTags(ids):
    form = forms.taganlegen()
    zuTag = tags.query.get(ids)
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
@app.route('/admin/tags/CHGrthat',methods=['GET','POST'])
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
@app.route('/admin/tags/CHGrthat2/<path:ids>',methods=['GET','POST'])
def CHGrthat2(ids):
    """Wir wählen, die Zutaten aus, die wir zum rezept speichern wollen."""
    form = forms.verknupfungsanleger()
    # Alle Zutaten, die schon verknüpft sind, müssen gelöscht werden
    form.zutaten.choices = createArrayHelper(tags.query.order_by(tags.name).all())
    auswahl = rezept.query.get(ids)
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

# Tagsverknüpfer entfernen
# Part 1
@app.route('/admin/tags/removeTagshat/',methods=['GET','POST'])
def removeTagshat():
    return remover(MODE_TAGver,rezept,'removeTagshat')    


# Tagsverknüpfer entfernen
# Part 2
# Übersicht der Tags zu eine nRezept erstellen
@app.route("/admin/tags/removeTagshat2/<path:rid>")
def removeTagshat2(rid):
    ausrezept = rezept.query.get(rid)
    liste = ausrezept.tags
    return render_template('admin_remove.html',inhalt=liste,titlet="Verknüpfungsentferner Tags (keine Löschung der Tags)",rid=rid,removeTagshat2=True)


# Tag löschen lassen
@app.route('/admin/tags/removeTags')
def removeTags():
    return remover(MODE_TAGS,tags,'removeTags')
