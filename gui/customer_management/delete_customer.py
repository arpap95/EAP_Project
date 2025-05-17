import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu
from utils.database import delete_customer_from_db
from gui.customer_management.customer_menu import customer_menu

def deleteCustomer(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title
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

    # Form frame
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

    def check_customer_exists(phone, email):
        return False  # demonstration - always shows error

    def on_submit():
        phone_value = phone.get().strip()
        email_value = email.get().strip()

        # Check if at least one field is filled
        if not phone_value and not email_value:
            error_var.set("Συμπληρώστε τουλάχιστον ένα πεδίο")
            error_label.pack(fill='x', padx=5)  # Show error
            return

        # placeholder
        found = check_customer_exists(phone_value, email_value)

        if not found:
            error_var.set("Ο πελάτης δεν βρέθηκε")
            error_label.pack(fill='x', padx=5)  # Show error
        else:
            # Delete customer from database
            delete_customer_from_db(phone_value, email_value)
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
        text="Διαγραφή",
        command=on_submit,
        bootstyle="secondary",
        width=12
    )
    submit_btn.pack(side='right', padx=5)

    # Set focus on the first field
    phone_entry.focus_set()