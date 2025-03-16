import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def show_add_form():
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
        show_main_menu()

    cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=show_main_menu
    )
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(
        master=button_container,
        text="Προσθήκη",
        command=on_submit
    )
    submit_btn.pack(side='right', padx=5)
    submit_btn.focus_set()

def customer_management():
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Button(content_frame, text="Αποθήκευση", command=lambda: show_main_menu()).pack(pady=10)
    ttk.Button(content_frame, text="Επιστροφή", command=show_main_menu).pack(pady=10)

def show_main_menu():
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Button(content_frame, text="Διαχείριση Ραντεβού", command=show_add_form).pack(pady=20)
    ttk.Button(content_frame, text="Διαχείριση Πελατών", command=customer_management).pack(pady=20)



root = tk.Tk()
root.title("Διαχείριση Ραντεβού")
root.geometry("600x400")

content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

show_main_menu()

root.mainloop()

# root = Tk()
# root.title("Appointments")
# root.geometry("1600x1020")
# root.configure(background = "black")
# root.resizable(width= True, height=True)
# label1 = Label(root, text="Προσθήκη πελάτη", bg="black", fg="white", font= "arial 12")
# label1.place(x=10, y=20)
#
#
# label2 = Label(root, text="Name", bg="black", fg="white", font= "arial 12")
# label2.place(x=10, y=50)
# text1 =Entry(root, width=20, bg="black", font="aria 12")
# text1.place(x=100, y=50)
#
# label3 = Label(root, text="Surname", bg="black", fg="white", font= "arial 12")
# label3.place(x=10, y=100)
# text2 =Entry(root, width=20, bg="black", font="aria 12")
# text2.place(x=100, y=100)
#
# label4 = Label(root, text="Email", bg="black", fg="white", font= "arial 12")
# label4.place(x=10, y=150)
# text3 =Entry(root, width=20, bg="black", font="aria 12")
# text3.place(x=100, y=150)
#
# label5 = Label(root, text="Phone", bg="black", fg="white", font= "arial 12")
# label5.place(x=10, y=200)
# text4 =Entry(root, width=20, bg="black", font="aria 12")
# text4.place(x=100, y=200)
#
# b1=Button(root, text="Cancel", width=10, height=1, bg="red", font="arial 12")
# b1.place(x=10, y=300)
# b1=Button(root, text="Submit", width=10, height=1, font="arial 12")
# b1.place(x=160, y=300)

# root.mainloop()

