from app import app, forms
from werkzeug.utils import secure_filename
import os
from flask import redirect, render_template, url_for

@app.route('/admin')
def admin():
    """Dies ist der Admin Hauptindex"""
    return render_template('adminindex.html')


@app.route('/admin/addrezept',methods=['GET','POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        data = form.photo.data
        filename = secure_filename(data.filename)
        data.save(os.path.join(
            app.instance_path,'fotos',filename
        ))
        return redirect(url_for('admin'))
    return render_template('newrezept.html',form=form)

@app.route('/admin/addhandlungsschritt')
def addhandlung():
    """Dies ist der Admin Hauptindex"""
    return render_template('adminindex.html')

@app.route('/admin/modifyRZ')
def CHGverknupfung():
    """Dies ist der Admin Hauptindex"""
    return render_template('adminindex.html')

@app.route('/admin/addZutat')
def addZutat():
    """Dies ist der Admin Hauptindex"""
    return render_template('adminindex.html')