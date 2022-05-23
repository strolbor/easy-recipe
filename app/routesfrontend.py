from flask import render_template, flash
from app import app, forms


@app.route('/base')
def index():
    return render_template('base.html', title="base")

@app.route('/rezeptanzeige')
def rezeptanzeige():
    return render_template('rezeptanzeige.html', title="Rezeptanzeige")


choices_array = []
home_html = "home.html"
@app.route('/', methods=['GET', 'POST'])
def home():
    global choices_array
    form = forms.d_felder()
    form.selected.choices = choices_array.copy()
    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            print(error_field,error_message)
    if form.validate_on_submit():
        print("validate")
        ver = form.eingabe.data
        eingabe = form.selected.data
        if form.submit2.data:
            print("submit2")
            # Item soll hinzugefügt werden
            # Neue ausgewählte Elemente werden kopiert
            # und hinzugefügt
            for entry in ver.copy():
                choices_array.append([entry,entry])
            
            # Neue List wird kopiert in die Liste
            form.selected.choices = choices_array.copy()
            
            if len(form.eingabe.data) == 0:
                flash("Input error")
            else:
                flash("Success")
            # neues Template an Client senden
            form.eingabe.data = []
            form.selected.data = []
            
            return render_template(home_html,form=form)
        
        if form.submit3.data:
            print("submit3")
            # Item soll aus choices entfernt werden

            # Aktuelle Auswahl kopieren
            form.selected.choices = choices_array.copy()
            array = choices_array.copy()
            print(array)
            # Was wir entfernen wollen, kopieren
            to_delete = form.selected.data.copy()
            print(to_delete)
            try:
                for entry in to_delete:
                    array.remove([entry,entry])
            except ValueError:
                pass
            print(array)
            form.selected.choices = array.copy()
            choices_array = array.copy()

            if len(form.eingabe.data) == 0:
                flash("Input error")
            else:
                flash("Success")

            
            form.eingabe.data = []
            form.selected.data = []
            return render_template(home_html,form=form)
        if form.submit4.data:
            form.eingabe.data = []
            form.selected.data = []
            form.selected.choices = choices_array
            return render_template(home_html,form=form)
        else:
            flash("Don't hack this!")

    if form.submit2.data == False and form.submit3.data == False:
        #erster Aufruf
        print("first")
        choices_array = []
        form.selected.choices = choices_array.copy()

    print("last return")
    form.selected.choices = choices_array
    return render_template(home_html, form=form)
