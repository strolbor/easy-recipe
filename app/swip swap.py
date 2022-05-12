choices_array = []
LISTENFELDER = "Listenfelder.html"
@app.route('/change/swip_swap/<name>',methods=['GET','POST'])
def change_swip_swap(name):
    """ Gegenstands auswahl wie aus den 1980ziger Jahre"""
    global choices_array
    form = d_felder()

    # Settings
    filename = ""
    title = ""
    
    # Modus herausfinden
    integer = -1
    try:
        integer = int(name)
    except ValueError:
        flash(c.INPUT_ERROR)
        return redirect(url_for('dash'))        

    if integer == 0:
        # Sammel Modus
        filename = cof.SAMMLER_CONF
        title = "Sammel Modus"
    elif integer == 1:
        # Alarm Modus
        filename = cof.ALARM_CONF
        title = "Alarm Modus"
    else:
        # Unbekannter Modus
        flash(c.MODI_NOT_FOUND)
        return redirect(url_for('dash'))
    title = title +": Einstellungen"

    # Konfig Datei öffnen im Lese Modus
    # Zum zeigen, das es gepeichert wurden ist
    if form.submit.data == False and form.submit2.data == False and form.submit3.data == False:
        print("Erster Aufruf")
        try:
            choices_array = []
            datei = open(filename,'r')
            voreingestellt = datei.readline()
            datei.close()
            for entry in voreingestellt.split(","):
                choices_array.append([entry,entry])
        except FileNotFoundError:
            flash(c.FILE_NOT_FOUND_MSG2.format(filename))
    
    form.selected.choices = choices_array.copy()
    if form.validate_on_submit():
        ver = form.ein.data
        eing = form.selected.data
        print("Verfügbar:",ver)
        print("Eingestellt:",eing)
        if form.submit.data:
            # -> neue Datem speichern
            # Dateien löschen und öffnen
            delete_file(filename)
            datei = open(filename,"a")

            # Daten herausfinden
            save_str = ""
            for entry in form.selected.choices.copy():
                save_str = save_str + "," + entry[0]
            save_str = save_str[1:]
            print(save_str)

            # Datei schreiben
            datei.write(save_str)
            datei.flush()
            datei.close()
            
            # Fertig gesetzt
            flash(c.SUCESS_MSG)
            return redirect(url_for('change_swip_swap',name=name))

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
            form.ein.data = []
            form.selected.data = []
            return render_template(LISTENFELDER,form=form,label=title)
        else:
            flash("Don't hack this!")
            return redirect(url_for('change_swip_swap',name=name))

    return render_template(LISTENFELDER,form=form,label=title)