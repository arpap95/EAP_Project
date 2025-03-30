import ttkbootstrap as ttk
import tkinter as tk


def addNewClient(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    title = ttk.Label(header_frame, text="Προσθήκη Νέου Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=5)

    # Form variables
    name = tk.StringVar(value="")
    lastname = tk.StringVar(value="")
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")
    error_var = tk.StringVar(value="")

    # Form frame
    form_frame = ttk.Frame(content_frame, bootstyle="dark")
    form_frame.pack(fill='both', expand=True, padx=20, pady=0)

    # Error message label
    error_frame = ttk.Frame(form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(0, 10), side='top')
    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()

    # Form fields
    for label_text, var in [("Όνομα", name), ("Επώνυμο", lastname), ("Τηλέφωνο", phone), ("Email", email)]:
        frame = ttk.Frame(form_frame, bootstyle="dark")
        frame.pack(fill='x', pady=(0, 15))
        label = ttk.Label(frame, text=label_text, width=10, bootstyle="inverse-dark")
        label.pack(side='left', padx=5)
        entry = ttk.Entry(frame, textvariable=var, bootstyle="dark")
        entry.pack(side='left', padx=5, fill='x', expand=True)

    # Button container
    button_container = ttk.Frame(form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    def validate_fields():
        if not all(var.get().strip() for var in [name, lastname, phone, email]):
            return "Παρακαλώ εισάγετε όλα τα στοιχεία"
        return None

    def customer_exists(name_value, lastname_value, phone_value, email_value):
        existing_customers = [
            {"name": "Γιώργος", "lastname": "Παπαδόπουλος", "phone": "6912345678", "email": "george@gmail.com"}
        ]
        return any(c["phone"] == phone_value or c["email"] == email_value for c in existing_customers)

    def on_submit():
        error_label.pack_forget()
        validation_error = validate_fields()
        if validation_error:
            error_var.set(validation_error)
            error_label.pack(fill='x', padx=5)
            return

        name_value, lastname_value, phone_value, email_value = [var.get().strip() for var in [name, lastname, phone, email]]
        if customer_exists(name_value, lastname_value, phone_value, email_value):
            error_var.set("Ο πελάτης υπάρχει ήδη")
            error_label.pack(fill='x', padx=5)
            return

        add_customer_to_db(name_value, lastname_value, phone_value, email_value)
        go_back()

    def add_customer_to_db(name_value, lastname_value, phone_value, email_value):
        print(f"Adding customer: {name_value} {lastname_value}, {phone_value}, {email_value}")

    # Buttons
    cancel_btn = ttk.Button(button_container, text="Ακύρωση", command=lambda: go_back(),
                           bootstyle="danger", width=12)
    cancel_btn.pack(side='right', padx=5)


    submit_btn = ttk.Button(button_container, text="Προσθήκη", command=on_submit,
                           bootstyle="secondary", width=12)
    submit_btn.pack(side='right', padx=5)

    def go_back():
        import show_main_menu from menu


    # Set focus
    form_frame.winfo_children()[1].winfo_children()[1].focus_set()

