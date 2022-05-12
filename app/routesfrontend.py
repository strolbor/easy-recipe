from flask import render_template, flash
from app import app, forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Test")


choices_array = []
home_html = "home.html"
@app.route('/home', methods=['GET', 'POST'])
def home():
    global choices_array
    form = forms.d_felder()
    if form.submit.data == False and form.submit2.data == False and form.submit3.data == False:
        pass
    if form.validate_on_submit():
        if form.submit.data:
            # -> neue Datem speichern
            # Dateien löschen und öffnen
            pass
        elif form.submit2.data:
            # Item soll hinzugefügt werden

            # Choices werden hart kopiert
            old_choices = form.selected.choices.copy()

            # Neue ausgewählte Elemente werden kopiert
            # und hinzugefügt
            for entry in form.ein.data.copy():
                old_choices.append([entry,entry])
            
            # Neue List wird kopiert in die Liste
            form.selected.choices = old_choices.copy()
            choices_array = old_choices.copy()

            if len(ver) == 0:
                flash(c.INPUT_ERROR)
            else:
                flash(c.SUC_ADD)
            # neues Template an Client senden
            form.ein.data = []
            form.selected.data = []
            return render_template(LISTENFELDER,form=form,label=title)
        elif form.submit3.data:
            # Item soll aus choices entfernt werden

            # Aktuelle Auswahl kopieren
            array = form.selected.choices.copy()
            # Was wir entfernen wollen, kopieren
            to_delete = form.selected.data.copy()
            for entry in to_delete:
                array.remove([entry,entry])
            form.selected.choices = array.copy()
            choices_array = array.copy()

            if len(eing) == 0:
                flash(c.INPUT_ERROR)
            else:
                flash(c.SUC_DEL)
            form.ein.data = []
            form.selected.data = []
            return render_template(LISTENFELDER,form=form,label=title)
        elif form.submit4.data:
            pass
        else:
            flash("Don't hack this!")

    return render_template(home_html, title="Suche", form=form)
