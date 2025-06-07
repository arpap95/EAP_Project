import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog, Messagebox
from datetime import datetime
from gui.appointment_management.appointment_edit import edit_appointment_window
import utils.database_appointment as db_appoint
import utils.database as db


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

    # Global variables για τον πίνακα και τα δεδομένα
    current_tree = None
    current_customer = None
    current_appointments = []

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
        nonlocal current_customer, current_appointments

        # 1) Clear previous results
        for widget in results_container.winfo_children():
            widget.destroy()
        error_label.pack_forget()

        phone = search_phone.get().strip()
        email = search_email.get().strip()

        if not phone and not email:
            error_var.set("Παρακαλώ εισάγετε τηλέφωνο ή email")
            error_label.pack(fill='x', padx=5)
            return

        # 2) First get the customer_id (int)
        cid = db.search_customer(phone, email)
        if not cid:
            error_var.set("Δεν βρέθηκε πελάτης με αυτά τα στοιχεία")
            error_label.pack(fill='x', padx=5)
            current_customer = None
            current_appointments = []
            return

        # 3) Then fetch the full row: (first, last, phone, email)
        rows = db.get_customer(mobile_number=phone, email=email)
        if not rows:
            error_var.set("Σφάλμα στη φόρτωση στοιχείων πελάτη")
            error_label.pack(fill='x', padx=5)
            return

        first_name, last_name, phone_val, email_val = rows[0]

        # 4) Build a dict so show_customer_appointments can index by keys
        customer_found = {
            'name':     first_name,
            'lastname': last_name,
            'phone':    phone_val,
            'email':    email_val
        }

        current_customer = customer_found
        show_customer_appointments(current_customer, results_container)

    def clear_search():
        """Νέα συνάρτηση για καθαρισμό αναζήτησης"""
        nonlocal current_customer, current_appointments, current_tree

        search_phone.set("")
        search_email.set("")
        error_label.pack_forget()
        current_customer = None
        current_appointments = []
        current_tree = None
        for widget in results_container.winfo_children():
            widget.destroy()



    def delete_appointment(appointment_id, appointment_data):
        """Διαγραφή συγκεκριμένου ραντεβού"""
        try:
            # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΓΙΑ ΔΙΑΓΡΑΦΗ ΑΠΟ ΤΗ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ
            # π.χ. db.delete_appointment(appointment_id)

            # Προσωρινή λογική - αφαίρεση από τη λίστα
            nonlocal current_appointments
            current_appointments = [apt for apt in current_appointments if not (
                    apt['date'] == appointment_data['date'] and
                    apt['start_time'] == appointment_data['start_time'] and
                    apt['end_time'] == appointment_data['end_time']
            )]

            # Ανανέωση του πίνακα
            refresh_appointments_display()

            # Εμφάνιση μηνύματος επιτυχίας
            error_var.set(
                f"Το ραντεβού της {appointment_data['date']} στις {appointment_data['start_time']}-{appointment_data['end_time']} διαγράφηκε επιτυχώς")
            error_label.configure(bootstyle="success-inverse")
            error_label.pack(fill='x', padx=5)

            return True

        except Exception as e:
            # Εμφάνιση μηνύματος σφάλματος
            error_var.set(f"Σφάλμα κατά τη διαγραφή: {str(e)}")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return False

    def edit_appointment(appointment_data):
        """Τροποποίηση συγκεκριμένου ραντεβού"""
        try:
            # Κλήση του παραθύρου τροποποίησης
            result = edit_appointment_window(content_frame, appointment_data, current_customer)

            if result:
                # Ανανέωση της εμφάνισης αν επιστράφηκε True (επιτυχής ενημέρωση)
                refresh_full_display()

                # Εμφάνιση μηνύματος επιτυχίας
                error_var.set("Το ραντεβού ενημερώθηκε επιτυχώς")
                error_label.configure(bootstyle="success-inverse")
                error_label.pack(fill='x', padx=5)

        except Exception as e:
            # Εμφάνιση μηνύματος σφάλματος
            error_var.set(f"Σφάλμα κατά την τροποποίηση: {str(e)}")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)



    def delete_selected_appointment():
        """Διαγραφή επιλεγμένου ραντεβού με κουμπί"""
        if not current_tree:
            error_var.set("Δεν υπάρχει πίνακας ραντεβού")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        selection = current_tree.selection()
        if not selection:
            error_var.set("Παρακαλώ επιλέξτε ένα ραντεβού για διαγραφή")
            error_label.configure(bootstyle="warning-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Παίρνουμε τα δεδομένα του επιλεγμένου ραντεβού
        item = selection[0]
        values = current_tree.item(item, 'values')

        if values:
            appointment_data = {
                'date': values[0],
                'start_time': values[1],
                'end_time': values[2]
            }

            # Επιβεβαίωση διαγραφής
            result = Messagebox.yesno(
                title="Επιβεβαίωση Διαγραφής",
                message=f"Θέλετε να διαγράψετε το ραντεβού:\n\n"
                        f"Ημερομηνία: {appointment_data['date']}\n"
                        f"Ώρα έναρξης: {appointment_data['start_time']}\n"
                        f"Ώρα λήξης: {appointment_data['end_time']}",
                parent=content_frame
            )

            if result == "Yes":
                delete_appointment(item, appointment_data)

    def edit_selected_appointment():
        """Τροποποίηση επιλεγμένου ραντεβού με κουμπί"""
        if not current_tree:
            error_var.set("Δεν υπάρχει πίνακας ραντεβού")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        selection = current_tree.selection()
        if not selection:
            error_var.set("Παρακαλώ επιλέξτε ένα ραντεβού για τροποποίηση")
            error_label.configure(bootstyle="warning-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Παίρνουμε τα δεδομένα του επιλεγμένου ραντεβού
        item = selection[0]
        values = current_tree.item(item, 'values')

        if values:
            appointment_data = {
                'date': values[0],
                'start_time': values[1],
                'end_time': values[2]
            }

            edit_appointment(appointment_data)

    def refresh_appointments_display():
        """Ανανέωση της εμφάνισης ραντεβού"""
        if not current_tree or not current_customer:
            return

        # Καθαρισμός του πίνακα
        for item in current_tree.get_children():
            current_tree.delete(item)

        # Επαναφόρτωση δεδομένων από τη βάση
        fresh_appointments = get_customer_appointments(current_customer['phone'])
        nonlocal current_appointments
        current_appointments = fresh_appointments

        # Εισαγωγή νέων δεδομένων στον πίνακα
        if current_appointments:
            for appointment in current_appointments:
                current_tree.insert("", "end", values=(
                    appointment['date'],
                    appointment['start_time'],
                    appointment['end_time']
                ))

    def refresh_full_display():
        """Πλήρης ανανέωση της εμφάνισης (για το κουμπί ανανέωσης)"""
        if not current_customer:
            return

        # Καθαρισμός του results_container
        for widget in results_container.winfo_children():
            widget.destroy()

        # Επαναφόρτωση όλων των δεδομένων
        show_customer_appointments(current_customer, results_container)

    def show_customer_appointments(customer, container):
        nonlocal current_tree, current_appointments

        # ΣΗΜΑΝΤΙΚΟ: Καθαρισμός του container πριν τη δημιουργία νέων widgets
        for widget in container.winfo_children():
            widget.destroy()

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
        current_appointments = get_customer_appointments(customer['phone'])

        if not current_appointments:
            no_appointments = ttk.Label(appointments_frame,
                                        text="Δεν βρέθηκαν ραντεβού για αυτόν τον πελάτη",
                                        bootstyle="secondary", font=('Helvetica', 10))
            no_appointments.pack(pady=20)
            current_tree = None
        else:
            # Δημιουργία Treeview για εμφάνιση ραντεβού
            tree_frame = ttk.Frame(appointments_frame, bootstyle="dark")
            tree_frame.pack(fill='both', expand=True, padx=10, pady=10)

            # Columns για το Treeview - ΜΟΝΟ τα 3 απαιτούμενα πεδία
            columns = ("date", "start_time", "end_time")
            current_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", bootstyle="info")

            # Ορισμός headers με κεντρική στοίχιση
            current_tree.heading("date", text="Ημερομηνία", anchor="center")
            current_tree.heading("start_time", text="Ώρα Έναρξης", anchor="center")
            current_tree.heading("end_time", text="Ώρα Λήξης", anchor="center")

            # Ρύθμιση πλάτους στηλών
            current_tree.column("date", width=150, minwidth=150, anchor="center")
            current_tree.column("start_time", width=150, minwidth=150, anchor="center")
            current_tree.column("end_time", width=150, minwidth=150, anchor="center")

            # Προσθήκη scrollbar
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=current_tree.yview)
            current_tree.configure(yscrollcommand=scrollbar.set)

            # Bind διπλού κλικ για διαγραφή
            current_tree.bind("<Double-1>", on_appointment_double_click)

            # Εισαγωγή δεδομένων
            for appointment in current_appointments:
                current_tree.insert("", "end", values=(
                    appointment['date'],
                    appointment['start_time'],
                    appointment['end_time']
                ))

            current_tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Κουμπιά διαχείρισης ραντεβού
            appointments_buttons_frame = ttk.Frame(appointments_frame)
            appointments_buttons_frame.pack(fill='x', padx=10, pady=(0, 10))

            # Οδηγίες χρήσης
            instructions_label = ttk.Label(appointments_buttons_frame,
                                           text="💡 Διπλό κλικ σε ραντεβού για διαγραφή ή χρησιμοποιήστε τα κουμπιά παρακάτω",
                                           bootstyle="info-inverse", font=('Helvetica', 9))
            instructions_label.pack(fill='x', pady=(5, 10))

            # Κουμπί τροποποίησης επιλεγμένου
            edit_btn = ttk.Button(appointments_buttons_frame, text="✏️ Τροποποίηση Επιλεγμένου",
                                  command=edit_selected_appointment,
                                  bootstyle="warning", width=25)
            edit_btn.pack(side='left', padx=5)

            # Κουμπί διαγραφής επιλεγμένου
            delete_btn = ttk.Button(appointments_buttons_frame, text="🗑️ Διαγραφή Επιλεγμένου",
                                    command=delete_selected_appointment,
                                    bootstyle="danger", width=25)
            delete_btn.pack(side='left', padx=5)

            # Κουμπί ανανέωσης
            refresh_btn = ttk.Button(appointments_buttons_frame, text="🔄 Ανανέωση",
                                     command=refresh_full_display,
                                     bootstyle="secondary", width=15)
            refresh_btn.pack(side='left', padx=5)

    def get_customer_appointments(phone):
        # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΓΙΑ ΑΝΑΚΤΗΣΗ ΡΑΝΤΕΒΟΥ ΑΠΟ ΤΗ ΒΑΣΗ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        # Προσωρινά επιστρέφω δοκιμαστικά δεδομένα με μόνο τα 3 απαιτούμενα πεδία
        if phone == "1234567890":
            return [
                {'date': '15/12/2024', 'start_time': '10:00', 'end_time': '11:00'},
                {'date': '20/12/2024', 'start_time': '14:30', 'end_time': '15:30'},
                {'date': '25/12/2024', 'start_time': '16:00', 'end_time': '17:00'}
            ]
        return []

    # Κουμπιά στο bottom_frame
    # Κουμπί αναζήτησης
    btn_search = ttk.Button(bottom_frame, text="🔍 Αναζήτηση",
                            command=search_customer,
                            bootstyle="primary", width=15)
    btn_search.pack(side='left', padx=10)

    # Κουμπί καθαρισμού
    btn_clear = ttk.Button(bottom_frame, text="🧹 Καθαρισμός",
                           command=clear_search,
                           bootstyle="secondary", width=15)
    btn_clear.pack(side='left', padx=10)

    # Κουμπί επιστροφής
    btn_back = ttk.Button(bottom_frame, text="↩️ Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)