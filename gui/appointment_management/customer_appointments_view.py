import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog
from datetime import datetime


def customer_appointments_view(content_frame, go_back_callback):
    # Καθαρισμός του frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title in the header
    title = ttk.Label(header_frame, text="Εμφάνιση Ραντεβού Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=(5, 0))

    subtitle = ttk.Label(header_frame, text="Εισάγετε τηλέφωνο ή email για αναζήτηση", font=('Helvetica', 11),
                         bootstyle="inverse-dark")
    subtitle.pack(fill='x', padx=20, pady=(0, 5))

    # Form variables for search
    search_phone = tk.StringVar(value="")
    search_email = tk.StringVar(value="")

    # Error/Success message variable
    error_var = tk.StringVar(value="")

    # Search form frame
    search_form_frame = ttk.Frame(content_frame, bootstyle="dark")
    search_form_frame.pack(fill='x', padx=20, pady=0)

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

    # Error message label
    error_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(5, 10))

    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse", font=('Helvetica', 11))
    error_label.pack(fill='x', padx=5)
    error_label.pack_forget()

    # Bottom frame για τα κουμπιά
    bottom_frame = ttk.Frame(content_frame, bootstyle="dark")
    bottom_frame.pack(fill='x', side='bottom', pady=10, padx=50)

    # Results frame για τα ραντεβού
    results_container = ttk.Frame(content_frame, bootstyle="dark")
    results_container.pack(fill='both', expand=True, padx=20, pady=10)

    def search_customer():
        # Καθαρισμός προηγούμενων αποτελεσμάτων
        for widget in results_container.winfo_children():
            widget.destroy()
        error_label.pack_forget()

        phone = search_phone.get().strip()
        email = search_email.get().strip()

        # Έλεγχος αν έχει εισαχθεί τουλάχιστον ένα κριτήριο
        if not phone and not email:
            error_var.set("Παρακαλώ εισάγετε τηλέφωνο ή email")
            error_label.pack(fill='x', padx=5)
            return

        # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΣΑΣ ΓΙΑ ΑΝΑΖΗΤΗΣΗ ΣΤΗΝ ΒΑΣΗ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        # Προσωρινή λογική για δοκιμή
        customer_found = search_customer_in_database(phone, email)

        if not customer_found:
            error_var.set("Δεν βρέθηκε πελάτης με αυτά τα στοιχεία")
            error_label.pack(fill='x', padx=5)
        else:
            # Εμφάνιση ραντεβού πελάτη
            show_customer_appointments(customer_found, results_container)

    def clear_search():
        """Νέα συνάρτηση για καθαρισμό αναζήτησης"""
        search_phone.set("")
        search_email.set("")
        error_label.pack_forget()
        for widget in results_container.winfo_children():
            widget.destroy()

    def search_customer_in_database(phone, email):
        # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΣΥΝΔΕΣΗ ΜΕ ΤΗ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        # Προσωρινά επιστρέφω δοκιμαστικά δεδομένα

        if phone == "1234567890" or email == "test@test.com":
            return {
                'name': 'Γιάννης',
                'lastname': 'Παπαδόπουλος',
                'phone': '1234567890',
                'email': 'test@test.com'
            }
        return None

    def show_customer_appointments(customer, container):
        # Εμφάνιση στοιχείων πελάτη
        customer_frame = ttk.LabelFrame(container, text="Στοιχεία Πελάτη", bootstyle="info")
        customer_frame.pack(fill='x', pady=(0, 15))

        customer_info = ttk.Label(customer_frame,
                                  text=f"Όνομα: {customer['name']} {customer['lastname']}\n"
                                       f"Τηλέφωνο: {customer['phone']}\n"
                                       f"Email: {customer['email']}",
                                  bootstyle="dark", font=('Helvetica', 10))
        customer_info.pack(pady=10, padx=10)

        # Εμφάνιση ραντεβού
        appointments_frame = ttk.LabelFrame(container, text="Ραντεβού Πελάτη", bootstyle="success")
        appointments_frame.pack(fill='both', expand=True)

        # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΓΙΑ ΑΝΑΚΤΗΣΗ ΡΑΝΤΕΒΟΥ ΑΠΟ ΤΗ ΒΑΣΗ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        appointments = get_customer_appointments(customer['phone'])

        if not appointments:
            no_appointments = ttk.Label(appointments_frame,
                                        text="Δεν βρέθηκαν ραντεβού για αυτόν τον πελάτη",
                                        bootstyle="secondary", font=('Helvetica', 10))
            no_appointments.pack(pady=20)
        else:
            # Δημιουργία Treeview για εμφάνιση ραντεβού
            tree_frame = ttk.Frame(appointments_frame, bootstyle="dark")
            tree_frame.pack(fill='both', expand=True, padx=10, pady=10)

            # Columns για το Treeview
            columns = ("date", "time", "service", "status")
            tree = ttk.Treeview(tree_frame, columns=columns, show="headings", bootstyle="info")

            # Ορισμός headers με κεντρική στοίχιση
            tree.heading("date", text="Ημερομηνία", anchor="center")
            tree.heading("time", text="Ώρα", anchor="center")
            tree.heading("service", text="Υπηρεσία", anchor="center")
            tree.heading("status", text="Κατάσταση", anchor="center")

            # Ρύθμιση πλάτους στηλών
            tree.column("date", width=120, minwidth=120, anchor="center")
            tree.column("time", width=100, minwidth=100, anchor="center")
            tree.column("service", width=200, minwidth=200, anchor="center")
            tree.column("status", width=150, minwidth=150, anchor="center")

            # Προσθήκη scrollbar
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            # Εισαγωγή δεδομένων
            for appointment in appointments:
                tree.insert("", "end", values=(
                    appointment['date'],
                    appointment['time'],
                    appointment['service'],
                    appointment['status']
                ))

            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

    def get_customer_appointments(phone):
        # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΓΙΑ ΑΝΑΚΤΗΣΗ ΡΑΝΤΕΒΟΥ ΑΠΟ ΤΗ ΒΑΣΗ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        # Προσωρινά επιστρέφω δοκιμαστικά δεδομένα
        if phone == "1234567890":
            return [
                {'date': '15/12/2024', 'time': '10:00', 'service': 'Κούρεμα', 'status': 'Ολοκληρώθηκε'},
                {'date': '20/12/2024', 'time': '14:30', 'service': 'Χτένισμα', 'status': 'Επικείμενο'},
                {'date': '25/12/2024', 'time': '16:00', 'service': 'Βαφή', 'status': 'Επικείμενο'}
            ]
        return []

    # Κουμπιά στο bottom_frame
    # Κουμπί αναζήτησης
    btn_search = ttk.Button(bottom_frame, text="Αναζήτηση",
                            command=search_customer,
                            bootstyle="primary", width=15)
    btn_search.pack(side='left', padx=10)

    # Κουμπί καθαρισμού
    btn_clear = ttk.Button(bottom_frame, text="Νέα Αναζήτηση",
                           command=clear_search,
                           bootstyle="secondary", width=15)
    btn_clear.pack(side='left', padx=10)

    # Κουμπί επιστροφής
    btn_back = ttk.Button(bottom_frame, text="Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)