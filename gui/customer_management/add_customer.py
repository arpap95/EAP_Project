import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu
from utils.database import add_customer_to_db
from gui.customer_management.customer_menu import customer_menu

def addNewClient(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
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
    name_frame.pack(fill='x', pady=(0, 15))

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
            error_label.pack(fill='x', padx=5)
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
        show_main_menu(content_frame)

    # Buttons with styling
    cancel_btn = ttk.Button(
        master=button_container,
        text="Επιστροφή",
        command=lambda: customer_menu(content_frame, lambda: show_main_menu(content_frame)),
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