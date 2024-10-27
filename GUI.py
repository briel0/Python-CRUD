import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class CrudGuiApp:
    def __init__(self, master=None):
        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.window.configure(background="#636363")
        self.window.resizable(True, True)
        self.window.title("Student Registration")

        # Configurar o grid da janela principal para ser redimensionável
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        # Left frame (form)
        self.left = tk.Frame(self.window, background="#636363")
        self.left.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Title frame
        self.title = tk.Frame(self.left, background="#85C7F2", height=70, padx=10, pady=10)
        self.title.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        self.form_title = tk.Label(self.title, text="Student Management System", background="#85C7F2", font="{Ivy} 16 {bold}")
        self.form_title.pack(fill="x")

        # Form frame
        self.form = tk.Frame(self.left, background="#BABABA")
        self.form.grid(row=1, column=0, sticky="nsew")
        
        # Configurar o form para expandir com o redimensionamento
        self.form.grid_rowconfigure(9, weight=1)
        self.form.grid_columnconfigure(0, weight=1)

        # Student ID
        self.label_id = tk.Label(self.form, text="Student ID", background="#BABABA")
        self.label_id.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_id = tk.Entry(self.form, borderwidth=1, relief="ridge", width=40)
        self.entry_id.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Name
        self.label_name = tk.Label(self.form, text="Name", background="#BABABA")
        self.label_name.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_name = tk.Entry(self.form, borderwidth=1, relief="ridge", width=40)
        self.entry_name.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # Phone
        self.label_phone = tk.Label(self.form, text="Phone", background="#BABABA")
        self.label_phone.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.entry_phone = tk.Entry(self.form, borderwidth=1, relief="ridge", width=40)
        self.entry_phone.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        # Register Date
        self.label_registerdate = tk.Label(self.form, text="Register Date", background="#BABABA")
        self.label_registerdate.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.entry_date = DateEntry(self.form, width=12)
        self.entry_date.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        # Extra Information
        self.label_note = tk.Label(self.form, text="Extra Information", background="#BABABA")
        self.label_note.grid(row=8, column=0, sticky="w", padx=10, pady=5)
        self.entry_note = tk.Entry(self.form, relief="ridge", width=40)
        self.entry_note.grid(row=9, column=0, padx=10, pady=5, sticky="ew")

        # Buttons
        self.buttons_frame = tk.Frame(self.form, background="#BABABA")
        self.buttons_frame.grid(row=10, column=0, pady=10)

        self.button_insert = tk.Button(self.buttons_frame, text="Insert", background="green", font="{arial} 9 {bold}", width=10)
        self.button_insert.grid(row=0, column=0, padx=5)

        self.button_update = tk.Button(self.buttons_frame, text="Update", background="#85C7F2", font="{arial} 9 {bold}", width=10)
        self.button_update.grid(row=0, column=1, padx=5)

        self.button_delete = tk.Button(self.buttons_frame, text="Delete", background="red", font="{arial} 9 {bold}", width=10)
        self.button_delete.grid(row=0, column=2, padx=5)

        # Right frame (table)
        self.view = tk.Frame(self.window, background="#DBDBDB")
        self.view.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Configuring table to expand 
        self.view.grid_rowconfigure(0, weight=1)
        self.view.grid_columnconfigure(0, weight=1)

        list_headers = ['id', 'name', 'phone', 'date', 'obs']
        self.viewer = ttk.Treeview(self.view, columns=list_headers, show="headings", selectmode="browse")
        self.viewer.grid(row=0, column=0, sticky="nsew")

        self.scrolly = ttk.Scrollbar(self.view, orient="vertical", command=self.viewer.yview)
        self.scrolly.grid(row=0, column=1, sticky="ns")
        self.scrollx = ttk.Scrollbar(self.view, orient="horizontal", command=self.viewer.xview)
        self.scrollx.grid(row=1, column=0, sticky="ew")

        self.viewer.configure(xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)

        # Configuring columns
        self.viewer.column('id', minwidth=0, width=50, anchor="center")
        self.viewer.column('name', minwidth=0, width=150, anchor="center")
        self.viewer.column('phone', minwidth=0, width=100, anchor="center")
        self.viewer.column('date', minwidth=0, width=100, anchor="center")
        self.viewer.column('obs', minwidth=0, width=250, anchor="w")

        self.viewer.heading('id', text="ID", anchor="center")
        self.viewer.heading('name', text="Name", anchor="center")
        self.viewer.heading('phone', text="Phone", anchor="center")
        self.viewer.heading('date', text="Date", anchor="center")
        self.viewer.heading('obs', text="Extra Information", anchor="center")

        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = CrudGuiApp()
    app.run()

