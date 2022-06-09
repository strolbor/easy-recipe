from app import app, db, forms
from app.rezept import rezept, zutat
from werkzeug.utils import secure_filename
import os
from flask import redirect, render_template
from flask.helpers import flash, url_for

@app.route('/admin')
@app.route('/admin/')
def admin():
    """Dies ist der Admin Hauptindex"""
    return render_template('admin_index.html')


@app.route('/admin/add/rezept',methods=['GET','POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        data = form.bildupload.data
        bild_url=""
        if data is not None:
            filename = secure_filename(data.filename)
            data.save(os.path.join(
                app.instance_path,'fotos',filename
            ))
            bild_url="fotos/"+filename

        
        new = rezept(name=form.rezeptname.data,bild=bild_url,tags=form.tags.data)
        print(new)
        db.session.add(new)
        db.session.commit()
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_newrezept.html',form=form)

@app.route('/admin/add/handlungsschritt')
def addhandlung():
    """Dies ist der Admin Hauptindex"""
    form = forms.handlungschrittanlegen()
    return render_template('admin_newhand.html',form=form)

@app.route('/admin/modifyRZ')
def CHGverknupfung():
    """Dies ist der Admin Hauptindex"""
    return render_template('admin_index.html')

@app.route('/admin/add/Zutat',methods=['GET','POST'])
def addZutat():
    """Dies ist der Admin Hauptindex"""
    form = forms.zutatanlegen()
    return render_template('admin_newzutat.html',form=form)

@app.route('/admin/show/rezepte')
@app.route('/admin/show/rezepte/')
def showRezepte():
    list = rezept.query.all()
    return render_template('admin_show.html',inhalt=list)

@app.route('/admin/show/zutat')
@app.route('/admin/show/zutat/')
def showZutaten():
    list = zutat.query.all()
    return render_template('admin_show.html',inhalt=list)
