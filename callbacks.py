def write_Button(app, acc):
    combo = app.combo.get()
    print(combo)
    value = int(app.entry.get())
    if combo == 'Доход':
        acc.set_income(value)
    else:
        acc.set_outcome(value)
    app.entry.delete(0, 'end')

def summary_button(app, acc):
    value = acc.get_summary()
    if value > 0:
        app.summary_label.config(background='green')
    elif value < 0:
        app.summary_label.config(background='red')
    app.summary_label.config(text=str(value)+' Р.')
    app.entry.delete(0, 'end')