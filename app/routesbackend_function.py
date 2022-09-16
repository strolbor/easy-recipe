from app import app, db, forms
from flask import redirect, render_template,request
from app.rezept import Association,AssociationRHhat, handlungsschritt, rezept, zutat, tags
from flask.helpers import url_for

#####################
# Objekte entfernen #
#####################

    



@app.route('/adminctl/delete/tags/<path:ids>')
def deleteTags(ids):
    """Tags Objekt entfernen"""
    page = request.args.get('page', 0, type=int)
    tagdel = tags.query.get(ids)

    # Tag Zugehörigkeiten löschen
    tagdel.belongs = []
    
    # Tag löschen
    db.session.delete(tagdel)

    db.session.commit()
    return redirect(url_for('removeTags',page=page))

@app.route('/adminctl/delete/handlung/<path:ids>')
def deleteHandlung(ids):
    """Handlungsschritt Objekt entfernen"""
    page = request.args.get('page', 0, type=int)
    handdel = handlungsschritt.query.get(ids)
    # Verknüpfung löschen
    for entry in handdel.rezepte:
        db.session.delete(entry)
        # Es gibt ja nur ein Assoc zu jeden Handlungschritt und dewegen einfach löschbar
    
    #Handlungsschritt löschen
    db.session.delete(handdel)
    db.session.commit()
    return redirect(url_for('removehandlungsschritt',page=page))


#############################
# M:n Beziehungen entfernen #
#############################

@app.route('/adminctl/delete/rzhat/<path:rid>-<path:zid>/<path:redirect_url>')
def deleterzhat(rid,zid,redirect_url):
    """Enternen von m:n-Beziehungen zwischen Rezept und Zutat"""
    page = request.args.get('page', 0, type=int)
    rezeptw = rezept.query.get(rid)
    assoc = Association.query.get((rid,zid))
    rezeptw.zutaten.remove(assoc)
    db.session.commit()
    return redirect(url_for(redirect_url, rid=rid, page=page))


@app.route('/adminctl/delete/rthat/<path:rid>-<path:tid>')
def deleterthat(rid, tid):
    """Enternen von m:n-Beziehungen zwischen Rezept und Tags"""
    page = request.args.get('page', 0, type=int)
    rezeptw = rezept.query.get(rid)
    tagw = tags.query.get(tid)
    rezeptw.tags.remove(tagw)
    db.session.commit()
    return redirect(url_for('removeTagshat2',rid=rid,page=page))

@app.route('/adminctl/delete/rhhat/<path:rid>-<path:aid>/<path:redirect_url>')
def deleterhhat(rid,aid,redirect_url):
    """Enternen von m:n-Beziehungen zwischen Rezept und Handlungsschritten"""
    page = request.args.get('page', 0, type=int)
    rezeptw = rezept.query.get(rid)
    assoc = AssociationRHhat.query.get(aid)
    rezeptw.handlungsschritte.remove(assoc)
    db.session.commit()
    return redirect(url_for(redirect_url, rid=rid, page=page))


##########
# Backup #
##########
@app.route("/backupctl/showdata/html")
def showData():
    """Alle Daten sicherin in Python Syntax"""
    return render_template('backup.html',rezept=rezept.query.all(),zutaten=zutat.query.all(),handlungsschritte=handlungsschritt.query.all(), tags=tags.query.all(),html=True)

