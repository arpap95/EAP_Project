import ttkbootstrap as ttk
import tkinter as tk
from tkinter import ttk


def show_main_menu():
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)  # Κεντρική στοίχιση

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    right_section = ttk.Frame(lbl_container, bootstyle="dark")
    right_section.pack(side='right', expand=True)

    # Left Label & Button
    lbl_left = ttk.Label(left_section, text='Διαχείριση Πελατών', bootstyle="inverse-dark",
                         font=('Helvetica', 14, 'bold'))
    lbl_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Προσθήκη Πελάτη", command=addNewClient,
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Τροποποίηση Πελάτη", command=customer_management,
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Διαγραφή Πελάτη", command=deleteCustomer,
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Αναζήτηση Πελάτη", command=customer_management,
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    # Right Label & Button
    lbl_right = ttk.Label(right_section, text='Διαχείριση Ραντεβού', bootstyle="inverse-dark",
                          font=('Helvetica', 14, 'bold'))
    lbl_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Προσθήκη Ραντεβού", command=appointment_management,
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Τροποποίηση Ραντεβού", command=appointment_management,
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Διαγραφή Ραντεβού", command=appointment_management,
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Αναζήτηση Ραντεβού", command=appointment_management,
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

def addNewClient():
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title in the header
    title = ttk.Label(header_frame, text="Προσθήκη Νέου Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=5)

    # Form variables
    name = tk.StringVar(value="")
    lastname = tk.StringVar(value="")
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")

    # Error message variable
    error_var = tk.StringVar(value="")

    # Form frame
    form_frame = ttk.Frame(content_frame, bootstyle="dark")
    form_frame.pack(fill='both', expand=True, padx=20, pady=0)

    # Error message label (hidden)
    error_frame = ttk.Frame(form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(0, 10), side='top')

    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()  # Initially hidden

    # Name input row
    name_frame = ttk.Frame(form_frame, bootstyle="dark")
    name_frame.pack(fill='x', pady=(0, 15))  # Space between fields

    name_label = ttk.Label(name_frame, text="Όνομα", width=10, bootstyle="inverse-dark")
    name_label.pack(side='left', padx=5)

    name_entry = ttk.Entry(name_frame, textvariable=name, bootstyle="dark")
    name_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Last name input row
    lastname_frame = ttk.Frame(form_frame, bootstyle="dark")
    lastname_frame.pack(fill='x', pady=(0, 15))

    lastname_label = ttk.Label(lastname_frame, text="Επώνυμο", width=10, bootstyle="inverse-dark")
    lastname_label.pack(side='left', padx=5)

    lastname_entry = ttk.Entry(lastname_frame, textvariable=lastname, bootstyle="dark")
    lastname_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Phone input row
    phone_frame = ttk.Frame(form_frame, bootstyle="dark")
    phone_frame.pack(fill='x', pady=(0, 15))

    phone_label = ttk.Label(phone_frame, text="Τηλέφωνο", width=10, bootstyle="inverse-dark")
    phone_label.pack(side='left', padx=5)

    phone_entry = ttk.Entry(phone_frame, textvariable=phone, bootstyle="dark")
    phone_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Email input row
    email_frame = ttk.Frame(form_frame, bootstyle="dark")
    email_frame.pack(fill='x', pady=(0, 15))

    email_label = ttk.Label(email_frame, text="Email", width=10, bootstyle="inverse-dark")
    email_label.pack(side='left', padx=5)

    email_entry = ttk.Entry(email_frame, textvariable=email, bootstyle="dark")
    email_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Button container
    button_container = ttk.Frame(form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    def validate_fields():
        # Check if any field is empty
        if (not name.get().strip() or
                not lastname.get().strip() or
                not phone.get().strip() or
                not email.get().strip()):
            return "Παρακαλώ εισάγετε όλα τα στοιχεία"
        return None

    def customer_exists(name_value, lastname_value, phone_value, email_value):
        # Return True if customer exists, False otherwise
        existing_customers = [
            {"name": "Γιώργος", "lastname": "Παπαδόπουλος", "phone": "6912345678", "email": "george@gmail.com"},
        ]
        for customer in existing_customers:
            if (customer["phone"] == phone_value or customer["email"] == email_value):
                return True
        return False

    def on_submit():
        # Hide any previous error message
        error_label.pack_forget()

        # Validate all fields are filled
        validation_error = validate_fields()
        if validation_error:
            error_var.set(validation_error)
            error_label.pack(fill='x', padx=5)  # Show error
            return

        # Get values from form
        name_value = name.get().strip()
        lastname_value = lastname.get().strip()
        phone_value = phone.get().strip()
        email_value = email.get().strip()

        # Check if customer exists
        if customer_exists(name_value, lastname_value, phone_value, email_value):
            error_var.set("Ο πελάτης υπάρχει ήδη")
            error_label.pack(fill='x', padx=5)  # Show error
            return

        # If all validations pass, add customer to database
        add_customer_to_db(name_value, lastname_value, phone_value, email_value)
        show_main_menu()

    def add_customer_to_db(name_value, lastname_value, phone_value, email_value):
        """
        cursor = connection.cursor()
        query = "INSERT INTO customers (name, lastname, phone, email) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (name_value, lastname_value, phone_value, email_value))
        connection.commit()
        """
        print(f"Adding customer: {name_value} {lastname_value}, {phone_value}, {email_value}")
        pass

    # Buttons with styling
    cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=show_main_menu,
        bootstyle="danger",
        width=12
    )
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(
        master=button_container,
        text="Προσθήκη",
        command=on_submit,
        bootstyle="secondary",
        width=12
    )
    submit_btn.pack(side='right', padx=5)

    # Set focus on the first field
    name_entry.focus_set()

def deleteCustomer():
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title and subtitle in the header
    title = ttk.Label(header_frame, text="Διαγραφή Πελάτη", font=('Helvetica', 16, 'bold'), bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=(5, 0))

    subtitle = ttk.Label(header_frame, text="Εισάγετε τηλέφωνο ή email", font=('Helvetica', 11),
                         bootstyle="inverse-dark")
    subtitle.pack(fill='x', padx=20, pady=(0, 5))

    # Form variables
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")

    # Error message variable
    error_var = tk.StringVar(value="")

    # Form frame without any separators or empty labels
    form_frame = ttk.Frame(content_frame, bootstyle="dark")
    form_frame.pack(fill='both', expand=True, padx=20, pady=0)

    # Phone input row
    phone_frame = ttk.Frame(form_frame, bootstyle="dark")
    phone_frame.pack(fill='x', pady=(0, 15))

    phone_label = ttk.Label(phone_frame, text="Τηλέφωνο", width=10, bootstyle="inverse-dark")
    phone_label.pack(side='left', padx=5)

    phone_entry = ttk.Entry(phone_frame, textvariable=phone, bootstyle="dark")
    phone_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Email input row
    email_frame = ttk.Frame(form_frame, bootstyle="dark")
    email_frame.pack(fill='x', pady=(0, 15))

    email_label = ttk.Label(email_frame, text="Email", width=10, bootstyle="inverse-dark")
    email_label.pack(side='left', padx=5)

    email_entry = ttk.Entry(email_frame, textvariable=email, bootstyle="dark")
    email_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Error message label (hidden)
    error_frame = ttk.Frame(form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(5, 10), side='top')

    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()

    # Button container
    button_container = ttk.Frame(form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    def on_submit():
        phone_value = phone.get().strip()
        email_value = email.get().strip()

        # Check if at least one field is filled
        if not phone_value and not email_value:
            error_var.set("Συμπληρώστε τουλάχιστον ένα πεδίο")
            error_label.pack(fill='x', padx=5)  # Show error
            return

        #placeholder
        found = check_customer_exists(phone_value, email_value)

        if not found:
            error_var.set("Ο πελάτης δεν βρέθηκε")
            error_label.pack(fill='x', padx=5)  # Show error
        else:
            # Delete customer from database
            delete_customer_from_db(phone_value, email_value)
            show_main_menu()

    def check_customer_exists(phone, email):
        return False  #demonstration - always shows error

    def delete_customer_from_db(phone, email):
        """
        cursor = connection.cursor()
        query = "DELETE FROM customers WHERE phone = ? OR email = ?"
        cursor.execute(query, (phone, email))
        connection.commit()
        """
        pass

    # Buttons with styling
    cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=show_main_menu,
        bootstyle="danger",
        width=12
    )
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(
        master=button_container,
        text="Διαγραφή",
        command=on_submit,
        bootstyle="secondary",
        width=12
    )
    submit_btn.pack(side='right', padx=5)

    # Set focus on the first field
    phone_entry.focus_set()

def appointment_management():
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




root = tk.Tk()
root.title("Διαχείριση Ραντεβού")
root.geometry("800x500")

content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

show_main_menu()

root.mainloop()

