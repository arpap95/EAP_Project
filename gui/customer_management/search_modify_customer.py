import tkinter as tk
import ttkbootstrap as ttk
import utils.database as db
from gui.main_menu import show_main_menu
from gui.customer_management.customer_menu import customer_menu


def search_modify_customer(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title in the header
    title = ttk.Label(header_frame, text="Αναζήτηση / Τροποποίηση Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=(5, 0))

    subtitle = ttk.Label(header_frame, text="Εισάγετε τηλέφωνο ή email για αναζήτηση", font=('Helvetica', 11),
                         bootstyle="inverse-dark")
    subtitle.pack(fill='x', padx=20, pady=(0, 5))

    # Form variables for search
    search_phone = tk.StringVar(value="")
    search_email = tk.StringVar(value="")

    # Form variables for modification
    name = tk.StringVar(value="")
    lastname = tk.StringVar(value="")
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")

    # Error/Success message variable
    error_var = tk.StringVar(value="")

    # Customer found flag
    customer_found = tk.BooleanVar(value=False)

    # Search form frame
    search_form_frame = ttk.Frame(content_frame, bootstyle="dark")
    search_form_frame.pack(fill='both', expand=True, padx=20, pady=0)

    # Phone input row for search
    search_phone_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    search_phone_frame.pack(fill='x', pady=(0, 15))

    search_phone_label = ttk.Label(search_phone_frame, text="Τηλέφωνο", width=10, bootstyle="inverse-dark")
    search_phone_label.pack(side='left', padx=5)

    search_phone_entry = ttk.Entry(search_phone_frame, textvariable=search_phone, bootstyle="dark")
    search_phone_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Email input row for search
    search_email_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    search_email_frame.pack(fill='x', pady=(0, 15))

    search_email_label = ttk.Label(search_email_frame, text="Email", width=10, bootstyle="inverse-dark")
    search_email_label.pack(side='left', padx=5)

    search_email_entry = ttk.Entry(search_email_frame, textvariable=search_email, bootstyle="dark")
    search_email_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Search button frame
    search_button_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    search_button_frame.pack(fill='x', pady=(10, 15))

    # Error message label (hidden)
    error_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(5, 10))

    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()

    # Customer details frame (hidden)
    details_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    details_frame.pack(fill='x', pady=(10, 0))
    details_frame.pack_forget()

    # Name input row
    name_frame = ttk.Frame(details_frame, bootstyle="dark")
    name_frame.pack(fill='x', pady=(0, 15))

    name_label = ttk.Label(name_frame, text="Όνομα", width=10, bootstyle="inverse-dark")
    name_label.pack(side='left', padx=5)

    name_entry = ttk.Entry(name_frame, textvariable=name, bootstyle="dark")
    name_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Last name input row
    lastname_frame = ttk.Frame(details_frame, bootstyle="dark")
    lastname_frame.pack(fill='x', pady=(0, 15))

    lastname_label = ttk.Label(lastname_frame, text="Επώνυμο", width=10, bootstyle="inverse-dark")
    lastname_label.pack(side='left', padx=5)

    lastname_entry = ttk.Entry(lastname_frame, textvariable=lastname, bootstyle="dark")
    lastname_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Phone input row
    phone_frame = ttk.Frame(details_frame, bootstyle="dark")
    phone_frame.pack(fill='x', pady=(0, 15))

    phone_label = ttk.Label(phone_frame, text="Τηλέφωνο", width=10, bootstyle="inverse-dark")
    phone_label.pack(side='left', padx=5)

    phone_entry = ttk.Entry(phone_frame, textvariable=phone, bootstyle="dark")
    phone_entry.pack(side='left', padx=5, fill='x', expand=True)

    # Email input row
    email_frame = ttk.Frame(details_frame, bootstyle="dark")
    email_frame.pack(fill='x', pady=(0, 15))

    email_label = ttk.Label(email_frame, text="Email", width=10, bootstyle="inverse-dark")
    email_label.pack(side='left', padx=5)

    email_entry = ttk.Entry(email_frame, textvariable=email, bootstyle="dark")
    email_entry.pack(side='left', padx=5, fill='x', expand=True)


    def search_customer():
        # need these values in order to retrieve it on the update statement
        global phone_value
        global email_value
        # Hide previous messages and details
        error_label.pack_forget()
        details_frame.pack_forget()

        # Get search values
        phone_value = search_phone.get().strip()
        email_value = search_email.get().strip()

        # Check if at least one field is filled
        if not phone_value and not email_value:
            error_var.set("Συμπληρώστε τουλάχιστον ένα πεδίο")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Search for customer
        customer = db.customer_exists_check(mobile_number=phone_value, email=email_value)

        if customer:
            # Customer found - show details
            customer_found.set(True)
            #customer_data.clear()
            #customer_data.append(customer)

            # get details from DB
            customer_lst = db.get_customer(mobile_number=phone_value, email=email_value)

            # Fill the form with customer data from extracted details
            name.set(customer_lst[0][0]) # First Name
            lastname.set(customer_lst[0][1]) # Last Name
            phone.set(customer_lst[0][2]) # Mobile
            email.set(customer_lst[0][3]) # Email

            error_var.set(f"Πελάτης βρέθηκε: {customer_lst[0][0]} {customer_lst[0][1]}")
            error_label.configure(bootstyle="success-inverse")
            error_label.pack(fill='x', padx=5)
            details_frame.pack(fill='x', pady=(10, 0))
        else:
            # Customer not found
            customer_found.set(False)
            error_var.set("Ο πελάτης δεν βρέθηκε")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)

    def validate_modification_fields():
        # Check if any field is empty
        if (not name.get().strip() or
                not lastname.get().strip() or
                not phone.get().strip() or
                not email.get().strip()):
            return "Παρακαλώ εισάγετε όλα τα στοιχεία"
        return None

    def on_modify():
        # Hide previous error message
        error_label.pack_forget()

        # Validate all fields are filled
        validation_error = validate_modification_fields()
        if validation_error:
            error_var.set(validation_error)
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Get values from form
        name_value = name.get().strip()
        lastname_value = lastname.get().strip()
        new_phone_value = phone.get().strip()
        new_email_value = email.get().strip()
        old_mobile_number = phone_value # global var
        old_email = email_value # global var

        # Update Customer Details
        db.update_customer(
            update_first_name=name_value,
            update_last_name=lastname_value,
            update_mobile_number=new_phone_value,
            update_email=new_email_value,
            old_mobile_number=old_mobile_number,
            old_email=old_email
        )
        error_var.set("Τα στοιχεία του πελάτη ενημερώθηκαν επιτυχώς!")
        error_label.configure(bootstyle="success-inverse")
        error_label.pack(fill='x', padx=5)


    # Search button
    search_btn = ttk.Button(
        master=search_button_frame,
        text="Αναζήτηση",
        command=search_customer,
        bootstyle="primary",
        width=12
    )
    search_btn.pack(pady=5)

    # Modify button
    modify_button_frame = ttk.Frame(details_frame, bootstyle="dark")
    modify_button_frame.pack(fill='x', pady=(10, 0))

    modify_btn = ttk.Button(
        master=modify_button_frame,
        text="Ενημέρωση",
        command=on_modify,
        bootstyle="secondary",
        width=12
    )
    modify_btn.pack(side='right', padx=5)

    # Bottom button container
    button_container = ttk.Frame(search_form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    # Buttons with styling
    cancel_btn = ttk.Button(
        master=button_container,
        text="Επιστροφή",
        command=lambda: customer_menu(content_frame, lambda: show_main_menu(content_frame)),
        bootstyle="danger",
        width=12
    )
    cancel_btn.pack(side='right', padx=5)

    # Set focus on the first field
    search_phone_entry.focus_set()