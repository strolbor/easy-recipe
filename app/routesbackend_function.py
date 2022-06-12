from app import app, db, forms
from flask import redirect, render_template
from app.rezept import rezept, zutat
from flask.helpers import flash, url_for

"""Controll Section"""
@app.route('/adminctl/delete/zutat/<path:ids>')
def deleteZutat(ids):
    db.session.delete(zutat.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeZutat'))
    

@app.route('/adminctl/delete/rezept/<path:ids>')
def deleteRezept(ids):
    db.session.delete(rezept.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeRezept'))

@app.route('/adminctl/delete/rzhat/<path:rid>/<path:zid>')
def deleterzhat(rid,zid):
    rezeptw = rezept.query.get(rid)
    zutatw = zutat.query.get(zid)
    rezeptw.zutaten.remove(zutatw)
    db.session.commit()
    return redirect(url_for('removeRZhat2',rid=rid))
