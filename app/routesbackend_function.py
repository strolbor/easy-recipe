from app import app, db, forms
from flask import redirect, render_template
from app.rezept import Association, handlungsschritt, rezept, zutat, tags
from flask.helpers import url_for

#
# Objekte entfernen
#
@app.route('/adminctl/delete/zutat/<path:ids>')
def deleteZutat(ids):
    """Zutaten Objekt entfernen"""
    db.session.delete(zutat.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeZutat'))
    

@app.route('/adminctl/delete/rezept/<path:ids>')
def deleteRezept(ids):
    """Rezept Objekt entfernen"""
    db.session.delete(rezept.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeRezept'))

@app.route('/adminctl/delete/tags/<path:ids>')
def deleteTags(ids):
    """Tags Objekt entfernen"""
    db.session.delete(tags.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeTags'))

#
# M:n Beziehungen entfernen
#

@app.route('/adminctl/delete/rzhat/<path:rid>/<path:zid>')
def deleterzhat(rid,zid):
    """Enternen von m:n-Beziehungen zwischen Rezept und Zutat"""
    rezeptw = rezept.query.get(rid)
    assoc = Association.query.get((rid,zid))
    print(assoc)
    rezeptw.zutaten.remove(assoc)
    db.session.commit()
    return redirect(url_for('removeRZhat2',rid=rid))

@app.route('/adminctl/delete/rthat/<path:rid>/<path:tid>')
def deleterthat(rid,tid):
    """Enternen von m:n-Beziehungen zwischen Rezept und Tags"""
    rezeptw = rezept.query.get(rid)
    tagw = tags.query.get(tid)
    rezeptw.tags.remove(tagw)
    db.session.commit()
    return redirect(url_for('home',rid=rid))

@app.route('/adminctl/delete/rhhat/<path:rid>/<path:hid>')
def deleterhhat(rid,hid):
    """Enternen von m:n-Beziehungen zwischen Rezept und Handlungsschritten"""
    rezeptw = rezept.query.get(rid)
    handh = handlungsschritt.query.get(hid)
    rezeptw.handlungsschritte.remove(handh)
    db.session.commit()
    return redirect(url_for('home',rid=rid))


#
# Backup
#
@app.route("/backupctl/showdata/html")
def showData():
    """Alle Daten sicherin in Python Syntax"""
    return render_template('backup.html',rezept=rezept.query.all(),zutaten=zutat.query.all(),handlungsschritte=handlungsschritt.query.all(), tags=tags.query.all(),html=True)

