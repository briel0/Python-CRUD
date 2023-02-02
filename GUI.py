#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry 

class CrudGuiApp:
    def __init__(self, master=None):
        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)

        self.window.configure(background="#636363", width=200)

        self.window.geometry("1000x450")

        self.window.resizable(False, False)

        self.window.title("Student Registration")

        self.left = tk.Frame(self.window)

        self.left.configure(background="#636363", height=350, width=400)

        self.title = tk.Frame(self.left)

        self.title.configure(
            background="#85C7F2",
            height=70,
            padx=10,
            width=350)

        self.form_title = tk.Label(self.title)

        self.form_title.configure(
            anchor="center",
            background="#85C7F2",
            font="{Ivy} 16 {bold}",
            text='Student Management System')

        self.form_title.place(anchor="nw", height=70, width=400, x=-35)

        self.title.grid(column=0, padx=1, pady=1, row=0)

        self.form = tk.Frame(self.left)

        self.form.configure(background="#BABABA", height=376, width=350)

        self.label_id = tk.Label(self.form)

        self.label_id.configure(background="#BABABA", text='Student ID')

        self.label_id.place(anchor="nw", x=10, y=10)

        self.entry_id = tk.Entry(self.form)

        self.entry_id.configure(borderwidth=1, relief="ridge", width=54)

        self.entry_id.place(anchor="nw", x=10, y=35)

        self.label_name = tk.Label(self.form)

        self.label_name.configure(background="#BABABA", text='Name')

        self.label_name.place(anchor="nw", x=10, y=60)

        self.entry_name = tk.Entry(self.form)

        self.entry_name.configure(borderwidth=1, relief="ridge", width=54)

        self.entry_name.place(anchor="nw", x=10, y=85)

        self.label_phone = tk.Label(self.form)

        self.label_phone.configure(background="#BABABA", text='Phone')

        self.label_phone.place(anchor="nw", x=10, y=110)

        self.entry_phone = tk.Entry(self.form)

        self.entry_phone.configure(borderwidth=1, relief="ridge", width=54)

        self.entry_phone.place(anchor="nw", x=10, y=135)

        self.label_registerdate = tk.Label(self.form)

        self.label_registerdate.configure(
            background="#BABABA", text='Register Date')

        self.label_registerdate.place(anchor="nw", x=10, y=160)

        self.entry_date = DateEntry(self.form)

        self.entry_date.configure(width=12)

        self.entry_date.place(anchor="nw", x=10, y=185)

        self.label_note = tk.Label(self.form)

        self.label_note.configure(
            background="#BABABA",
            text='Extra Information')
        self.label_note.place(anchor="nw", x=10, y=210)

        self.entry_note = tk.Entry(self.form)

        self.entry_note.configure(relief="ridge", width=54)

        self.entry_note.place(anchor="nw", x=10, y=235)

        self.button_insert = tk.Button(self.form)

        self.button_insert.configure(
            background="green",
            font="{arial} 9 {bold}",
            text='Insert',
            width=10)

        self.button_insert.place(anchor="nw", x=33, y=275)

        self.button_update = tk.Button(self.form)

        self.button_update.configure(
            background="#85C7F2",
            font="{arial} 9 {bold}",
            text='Update',
            width=10)

        self.button_update.place(anchor="nw", x=133, y=275)

        self.button_delete = tk.Button(self.form)

        self.button_delete.configure(
            background="red",
            font="{arial} 9 {bold}",
            text='Delete',
            width=10)

        self.button_delete.place(anchor="nw", x=233, y=275)

        self.form.grid(column=0, padx=1, pady=1, row=1)

        self.left.pack(anchor="n", side="left")

        self.view = tk.Frame(self.window)

        self.view.configure(background="#DBDBDB", height=450, width=800)

        self.view.pack(padx=1, pady=1, side="top")

        list_headers = ['id', 'name', 'phone', 'date', 'obs']

        self.viewer = ttk.Treeview(
                self.view, 
                columns=list_headers,
                show='headings',
                selectmode="browse")

        self.scrolly = ttk.Scrollbar(self.view, orient="vertical", command=self.viewer.yview)

        self.scrollx = ttk.Scrollbar(self.view, orient="horizontal", command=self.viewer.xview)

        self.viewer.configure(xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)

        self.viewer.column('id', minwidth=0, width=15, anchor="center")
        self.viewer.column('name', minwidth=0, width=150, anchor="center")
        self.viewer.column('phone', minwidth=0, width=15, anchor="center")
        self.viewer.column('date', minwidth=0, width=15, anchor="center")
        self.viewer.column('obs', minwidth=0, width=150, anchor="nw")

        self.viewer.heading('id', text="ID", anchor="center")
        self.viewer.heading('name', text="Name", anchor="center")
        self.viewer.heading('phone', text="Phone", anchor="center")
        self.viewer.heading('date', text="Date", anchor="center")
        self.viewer.heading('obs', text="Extra Information", anchor="center")
        
        self.viewer.place(anchor='nw', width=646, height=450)
        self.scrolly.place(anchor="nw", x=628, y=1, height=445)
        self.scrollx.place(anchor="nw", x=1, y=429, width=627)

        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = CrudGuiApp()
    app.run()
