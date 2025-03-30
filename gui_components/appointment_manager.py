import ttkbootstrap as ttk
import tkinter as tk


def appointment_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    hdr = ttk.Label(master=content_frame, text="Προσθήκη Νέου Ραντεβού", width=50)
    hdr.pack(fill='x', pady=10)

    # Form variables
    name = tk.StringVar(value="")
    lastname = tk.StringVar(value="")
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")

    # Form frame
    form_frame = ttk.Frame(content_frame, padding=(20, 10))
    form_frame.pack(fill='both', expand=True)

    # Form fields
    for label_text, var in [("Όνομα", name), ("Επώνυμο", lastname), ("Τηλέφωνο", phone), ("Email", email)]:
        container = ttk.Frame(form_frame)
        container.pack(fill='x', expand=True, pady=5)
        label = ttk.Label(master=container, text=label_text, width=10)
        label.pack(side='left', padx=5)
        entry = ttk.Entry(master=container, textvariable=var)
        entry.pack(side='left', padx=5, fill='x', expand=True)

    # Buttons
    button_container = ttk.Frame(form_frame)
    button_container.pack(fill='x', expand=True, pady=(15, 10))

    def on_submit():
        print("Όνομα:", name.get())
        print("Επώνυμο:", lastname.get())
        print("Τηλέφωνο:", phone.get())
        print("Email:", email.get())
        show_main_menu(content_frame)

    cancel_btn = ttk.Button(button_container, text="Ακύρωση", command=lambda: show_main_menu(content_frame))
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(button_container, text="Προσθήκη", command=on_submit)
    submit_btn.pack(side='right', padx=5)
    submit_btn.focus_set()