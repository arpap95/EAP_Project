import ttkbootstrap as ttk
import tkinter as tk


def deleteCustomer(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))
    title = ttk.Label(header_frame, text="Διαγραφή Πελάτη", font=('Helvetica', 16, 'bold'), bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=(5, 0))
    subtitle = ttk.Label(header_frame, text="Εισάγετε τηλέφωνο ή email", font=('Helvetica', 11),
                         bootstyle="inverse-dark")
    subtitle.pack(fill='x', padx=20, pady=(0, 5))

    # Form variables
    phone = tk.StringVar(value="")
    email = tk.StringVar(value="")
    error_var = tk.StringVar(value="")

    # Form frame
    form_frame = ttk.Frame(content_frame, bootstyle="dark")
    form_frame.pack(fill='both', expand=True, padx=20, pady=0)

    # Error message
    error_frame = ttk.Frame(form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(5, 10), side='top')
    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()

    # Form fields
    for label_text, var in [("Τηλέφωνο", phone), ("Email", email)]:
        frame = ttk.Frame(form_frame, bootstyle="dark")
        frame.pack(fill='x', pady=(0, 15))
        label = ttk.Label(frame, text=label_text, width=10, bootstyle="inverse-dark")
        label.pack(side='left', padx=5)
        entry = ttk.Entry(frame, textvariable=var, bootstyle="dark")
        entry.pack(side='left', padx=5, fill='x', expand=True)

    # Button container
    button_container = ttk.Frame(form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    def on_submit():
        phone_value, email_value = phone.get().strip(), email.get().strip()
        if not (phone_value or email_value):
            error_var.set("Συμπληρώστε τουλάχιστον ένα πεδίο")
            error_label.pack(fill='x', padx=5)
            return

        found = check_customer_exists(phone_value, email_value)
        if not found:
            error_var.set("Ο πελάτης δεν βρέθηκε")
            error_label.pack(fill='x', padx=5)
        else:
            delete_customer_from_db(phone_value, email_value)
            show_main_menu(content_frame)

    def check_customer_exists(phone, email):
        return False  # Placeholder

    def delete_customer_from_db(phone, email):
        pass  # Placeholder

    # Buttons
    cancel_btn = ttk.Button(button_container, text="Ακύρωση", command=lambda: show_main_menu(content_frame),
                           bootstyle="danger", width=12)
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(button_container, text="Διαγραφή", command=on_submit,
                           bootstyle="secondary", width=12)
    submit_btn.pack(side='right', padx=5)

    # Set focus
    form_frame.winfo_children()[1].winfo_children()[1].focus_set()