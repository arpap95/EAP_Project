import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu

def appointment_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    hdr_txt = "Προσθήκη Νέου Ραντεβού"
    hdr = ttk.Label(master=content_frame, text=hdr_txt, width=50)
    hdr.pack(fill='x', pady=10)

    # Form variables
    name = tk.StringVar(value="")
    lastname = tk.StringVar(value="")
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")

    # Create form entries
    form_frame = ttk.Frame(content_frame, padding=(20, 10))
    form_frame.pack(fill='both', expand=True)

    # Name entry
    name_container = ttk.Frame(form_frame)
    name_container.pack(fill='x', expand=True, pady=5)
    name_label = ttk.Label(master=name_container, text="Όνομα", width=10)
    name_label.pack(side='left', padx=5)
    name_entry = ttk.Entry(master=name_container, textvariable=name)
    name_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Lastname entry
    lastname_container = ttk.Frame(form_frame)
    lastname_container.pack(fill='x', expand=True, pady=5)
    lastname_label = ttk.Label(master=lastname_container, text="Επώνυμο", width=10)
    lastname_label.pack(side='left', padx=5)
    lastname_entry = ttk.Entry(master=lastname_container, textvariable=lastname)
    lastname_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Phone entry
    phone_container = ttk.Frame(form_frame)
    phone_container.pack(fill='x', expand=True, pady=5)
    phone_label = ttk.Label(master=phone_container, text="Τηλέφωνο", width=10)
    phone_label.pack(side='left', padx=5)
    phone_entry = ttk.Entry(master=phone_container, textvariable=phone)
    phone_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Email entry
    email_container = ttk.Frame(form_frame)
    email_container.pack(fill='x', expand=True, pady=5)
    email_label = ttk.Label(master=email_container, text="Email", width=10)
    email_label.pack(side='left', padx=5)
    email_entry = ttk.Entry(master=email_container, textvariable=email)
    email_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Buttons
    button_container = ttk.Frame(form_frame)
    button_container.pack(fill='x', expand=True, pady=(15, 10))

    def on_submit():
        print("Όνομα:", name.get())
        print("Επώνυμο:", lastname.get())
        print("Τηλέφωνο:", phone.get())
        print("Email:", email.get())
        show_main_menu(content_frame)

    cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=lambda: show_main_menu(content_frame)
    )
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(
        master=button_container,
        text="Προσθήκη",
        command=on_submit
    )
    submit_btn.pack(side='right', padx=5)
    submit_btn.focus_set()