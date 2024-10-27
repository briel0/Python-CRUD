import json
import tkinter as tk
from GUI import CrudGuiApp 

def clear():
    app.entry_id.delete(0, tk.END)
    app.entry_name.delete(0, tk.END)
    app.entry_phone.delete(0, tk.END)
    app.entry_note.delete(0, tk.END)

def build():
    id = app.entry_id.get()
    info = {
        "name":app.entry_name.get(),
        "phone":app.entry_phone.get(),
        "date":app.entry_date.get(),
        "obs":app.entry_note.get()
    }
    with open("data.json", "r") as data:
        getdata = json.load(data)
        for current in getdata:
            current_data = list(getdata[current].values())
            current_data.insert(0, current)
            app.viewer.insert("", "end", values=current_data)

def add():
    id = app.entry_id.get()
    info = {
        "name":app.entry_name.get(),
        "phone":app.entry_phone.get(),
        "date":app.entry_date.get(),
        "obs":app.entry_note.get()
    }
    with open("data.json", "r") as data:
        getdata = json.load(data)
        getdata[id] = info

        with open("data.json", "w") as save:
            json.dump(getdata, save, indent=4)
    
    current_data = list(info.values())
    current_data.insert(0, id)

    app.viewer.insert("", "end", values=current_data)

    clear()

def delete():
    try:
        selected = app.viewer.focus()
        del_id = str(app.viewer.item(selected)["values"][0])
        with open("data.json", "r") as data:
            getdata = json.load(data)

            with open("data.json", "w") as save:
                del getdata[del_id]
                json.dump(getdata, save, indent=4)
        app.viewer.delete(selected)
    except:
        pass

def update():
    selected = app.viewer.focus()
    values = app.viewer.item(selected)["values"]

    print(values)

    app.entry_id.insert(0, values[0])
    app.entry_name.insert(0, values[1])
    app.entry_phone.insert(0, values[2])
    app.entry_date.delete(0, tk.END)
    app.entry_date.insert(0, values[3])
    app.entry_note.insert(0, values[4])

    delete()


app = CrudGuiApp()
build()

app.button_insert.configure(command=add)
app.button_delete.configure(command=delete)
app.button_update.configure(command=update)

if __name__ == "__main__":
    app.run()
