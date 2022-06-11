from app import app, db, forms
from flask import redirect, render_template
from app.rezept import rezept, zutat
from flask.helpers import flash, url_for

@app.route('/admin/remove/rezept')
def removeRezept():
    """ Löschen eines Rezeptes"""
    liste = rezept.query.all()
    return render_template('admin_remove.html',inhalt=liste,title="Rezept Entferner",targetrezept=True)

@app.route('/admin/remove/zutat')
def removeZutat():
    liste = zutat.query.all()
    return render_template('admin_remove.html',inhalt=liste,title="Zutaten Entferner",targetzutat=True)

"""Controll Section"""
@app.route('/admin/delete/zutat/<path:ids>')
def deleteZutat(ids):
    db.session.delete(zutat.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeZutat'))
    

@app.route('/admin/delete/rezept/<path:ids>')
def deleteRezept(ids):
    db.session.delete(rezept.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeRezept'))