import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog, Messagebox
from datetime import datetime


def edit_appointment_window(parent, appointment_data, customer_data):
    """
    Δημιουργεί νέο παράθυρο για την τροποποίηση ραντεβού

    Args:
        parent: Γονικό παράθυρο
        appointment_data: Δεδομένα του ραντεβού προς τροποποίηση
        customer_data: Δεδομένα του πελάτη

    Returns:
        True αν το ραντεβού ενημερώθηκε επιτυχώς, False διαφορετικά
    """

    # Δημιουργία νέου παραθύρου
    edit_window = tk.Toplevel(parent)
    edit_window.title("Τροποποίηση Ραντεβού")
    edit_window.geometry("600x500")
    edit_window.configure(bg="#2C3E50")
    edit_window.resizable(False, False)

    # Κεντράρισμα παραθύρου
    edit_window.transient(parent)
    edit_window.grab_set()

    # Μεταβλητές για τα πεδία
    date_var = tk.StringVar(value=appointment_data['date'])
    start_time_var = tk.StringVar(value=appointment_data['start_time'])
    end_time_var = tk.StringVar(value=appointment_data['end_time'])
    error_var = tk.StringVar(value="")

    # Μεταβλητή για αποτέλεσμα
    result = [False]  # Χρησιμοποιούμε λίστα για να μπορούμε να την τροποποιήσουμε στις εσωτερικές συναρτήσεις

    # Main frame
    main_frame = ttk.Frame(edit_window, bootstyle="light")
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    # Header
    header_frame = ttk.Frame(main_frame, bootstyle="light")
    header_frame.pack(fill='x', pady=(0, 20))

    title_label = ttk.Label(header_frame, text="Τροποποίηση Ραντεβού",
                            font=('Helvetica', 16, 'bold'))
    title_label.pack(fill='x')

    # Στοιχεία πελάτη
    customer_frame = ttk.LabelFrame(main_frame, text="Στοιχεία Πελάτη", bootstyle="info")
    customer_frame.pack(fill='x', pady=(0, 20))

    customer_info = ttk.Label(customer_frame,
                              text=f"Όνομα: {customer_data['name']} {customer_data['lastname']}\n"
                                   f"Τηλέφωνο: {customer_data['phone']}\n"
                                   f"Email: {customer_data['email']}",
                              bootstyle="dark", font=('Helvetica', 10))
    customer_info.pack(pady=10, padx=10)

    # Form για τροποποίηση
    form_frame = ttk.LabelFrame(main_frame, text="Στοιχεία Ραντεβού", bootstyle="warning")
    form_frame.pack(fill='x', pady=(0, 20))

    # Ημερομηνία
    date_frame = ttk.Frame(form_frame)
    date_frame.pack(fill='x', padx=10, pady=10)

    date_label = ttk.Label(date_frame, text="Ημερομηνία:", width=15)
    date_label.pack(side='left', padx=(0, 10))

    date_entry = ttk.Entry(date_frame, textvariable=date_var, width=20)
    date_entry.pack(side='left', padx=(0, 10))

    def select_date():
        try:
            # Μετατροπή της τρέχουσας ημερομηνίας σε datetime object
            current_date_str = date_var.get()
            if current_date_str:
                # Υποθέτουμε format DD/MM/YYYY
                current_date = datetime.strptime(current_date_str, "%d/%m/%Y")
            else:
                current_date = datetime.now()

            # Άνοιγμα DatePicker
            date_dialog = DatePickerDialog(parent=edit_window, title="Επιλογή Ημερομηνίας",
                                           startdate=current_date)
            selected_date = date_dialog.date_selected

            if selected_date:
                # Μορφοποίηση της επιλεγμένης ημερομηνίας
                formatted_date = selected_date.strftime("%d/%m/%Y")
                date_var.set(formatted_date)
        except Exception:
            # Αν υπάρχει σφάλμα, ανοίγουμε με σημερινή ημερομηνία
            date_dialog = DatePickerDialog(parent=edit_window, title="Επιλογή Ημερομηνίας")
            selected_date = date_dialog.date_selected

            if selected_date:
                formatted_date = selected_date.strftime("%d/%m/%Y")
                date_var.set(formatted_date)

    date_btn = ttk.Button(date_frame, text="📅", command=select_date,
                         bootstyle="light", width=0)
    date_btn.pack(side='left')

    # Ώρα έναρξης
    start_time_frame = ttk.Frame(form_frame)
    start_time_frame.pack(fill='x', padx=10, pady=10)

    start_time_label = ttk.Label(start_time_frame, text="Ώρα Έναρξης:", width=15)
    start_time_label.pack(side='left', padx=(0, 10))

    start_time_entry = ttk.Entry(start_time_frame, textvariable=start_time_var, width=10)
    start_time_entry.pack(side='left', padx=(0, 10))

    # Ώρα λήξης
    end_time_frame = ttk.Frame(form_frame)
    end_time_frame.pack(fill='x', padx=10, pady=10)

    end_time_label = ttk.Label(end_time_frame, text="Ώρα Λήξης:", width=15)
    end_time_label.pack(side='left', padx=(0, 10))

    end_time_entry = ttk.Entry(end_time_frame, textvariable=end_time_var, width=10)
    end_time_entry.pack(side='left', padx=(0, 10))

    # Error message
    error_frame = ttk.Frame(main_frame, bootstyle="dark")
    error_frame.pack(fill='x', pady=(0, 20))

    error_label = ttk.Label(error_frame, textvariable=error_var, bootstyle="danger-inverse",
                            font=('Helvetica', 10), wraplength=550)
    error_label.pack(fill='x')
    error_label.pack_forget()

    def validate_time_format(time_str):
        """Ελέγχει αν η ώρα είναι σε σωστή μορφή HH:MM"""
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def validate_form():
        """Ελέγχει την εγκυρότητα των δεδομένων της φόρμας"""
        error_label.pack_forget()

        # Έλεγχος ημερομηνίας
        date_str = date_var.get().strip()
        if not date_str:
            error_var.set("Παρακαλώ εισάγετε ημερομηνία")
            error_label.pack(fill='x')
            return False

        try:
            appointment_date = datetime.strptime(date_str, "%d/%m/%Y")
            # Έλεγχος αν η ημερομηνία είναι στο παρελθόν
            if appointment_date.date() < datetime.now().date():
                error_var.set("Η ημερομηνία δεν μπορεί να είναι στο παρελθόν")
                error_label.pack(fill='x')
                return False
        except ValueError:
            error_var.set("Μη έγκυρη ημερομηνία. Χρησιμοποιήστε τη μορφή ΗΗ/ΜΜ/ΕΕΕΕ")
            error_label.pack(fill='x')
            return False

        # Έλεγχος ώρας έναρξης
        start_time_str = start_time_var.get().strip()
        if not start_time_str:
            error_var.set("Παρακαλώ εισάγετε ώρα έναρξης")
            error_label.pack(fill='x')
            return False

        if not validate_time_format(start_time_str):
            error_var.set("Μη έγκυρη ώρα έναρξης. Χρησιμοποιήστε τη μορφή ΩΩ:ΛΛ")
            error_label.pack(fill='x')
            return False

        # Έλεγχος ώρας λήξης
        end_time_str = end_time_var.get().strip()
        if not end_time_str:
            error_var.set("Παρακαλώ εισάγετε ώρα λήξης")
            error_label.pack(fill='x')
            return False

        if not validate_time_format(end_time_str):
            error_var.set("Μη έγκυρη ώρα λήξης. Χρησιμοποιήστε τη μορφή ΩΩ:ΛΛ")
            error_label.pack(fill='x')
            return False

        # Έλεγχος αν η ώρα λήξης είναι μετά την ώρα έναρξης
        try:
            start_time = datetime.strptime(start_time_str, "%H:%M")
            end_time = datetime.strptime(end_time_str, "%H:%M")

            if end_time <= start_time:
                error_var.set("Η ώρα λήξης πρέπει να είναι μετά την ώρα έναρξης")
                error_label.pack(fill='x')
                return False
        except ValueError:
            error_var.set("Σφάλμα στον έλεγχο των ωρών")
            error_label.pack(fill='x')
            return False

        return True

    def save_appointment():
        """Αποθήκευση των αλλαγών στο ραντεβού"""
        if not validate_form():
            return

        try:
            # ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΓΙΑ ΕΝΗΜΕΡΩΣΗ ΤΗΣ ΒΑΣΗΣ ΔΕΔΟΜΕΝΩΝ
            # π.χ. db.update_appointment(appointment_id, new_data)

            # Νέα δεδομένα ραντεβού
            new_appointment_data = {
                'date': date_var.get().strip(),
                'start_time': start_time_var.get().strip(),
                'end_time': end_time_var.get().strip(),
                'customer_phone': customer_data['phone']
            }

            # Προσωρινή λογική - εδώ θα καλέσετε τη συνάρτηση ενημέρωσης της βάσης
            success = update_appointment_in_database(appointment_data, new_appointment_data)

            if success:
                result[0] = True  # Επιτυχής ενημέρωση

                # Εμφάνιση μηνύματος επιτυχίας
                Messagebox.showinfo(
                    title="Επιτυχία",
                    message="Το ραντεβού ενημερώθηκε επιτυχώς!",
                    parent=edit_window
                )

                # Κλείσιμο παραθύρου
                edit_window.destroy()
            else:
                error_var.set("Σφάλμα κατά την ενημέρωση του ραντεβού")
                error_label.pack(fill='x')

        except Exception as e:
            error_var.set(f"Σφάλμα: {str(e)}")
            error_label.pack(fill='x')

    def cancel_edit():
        """Ακύρωση τροποποίησης"""
        edit_window.destroy()

    def update_appointment_in_database(old_data, new_data):
        """
        Ενημέρωση ραντεβού στη βάση δεδομένων
        ΕΔΩ ΘΑ ΒΑΛΕΤΕ ΤΗ ΛΟΓΙΚΗ ΣΑΣ ΓΙΑ ΕΝΗΜΕΡΩΣΗ ΣΤΗΝ ΒΑΣΗ ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
        """
        try:
            # Προσωρινή λογική για δοκιμή - επιστρέφει πάντα True
            # Εδώ θα συνδεθείτε με τη βάση δεδομένων και θα ενημερώσετε το ραντεβού

            print(f"Ενημέρωση ραντεβού:")
            print(f"Παλιά δεδομένα: {old_data}")
            print(f"Νέα δεδομένα: {new_data}")

            # Παράδειγμα:
            # cursor.execute("""
            #     UPDATE appointments
            #     SET date = ?, start_time = ?, end_time = ?
            #     WHERE customer_phone = ? AND date = ? AND start_time = ? AND end_time = ?
            # """, (new_data['date'], new_data['start_time'], new_data['end_time'],
            #       new_data['customer_phone'], old_data['date'], old_data['start_time'], old_data['end_time']))
            #
            # connection.commit()

            return True  # Προσωρινά επιστρέφουμε True

        except Exception as e:
            print(f"Σφάλμα κατά την ενημέρωση: {e}")
            return False

    # Buttons frame
    buttons_frame = ttk.Frame(main_frame)
    buttons_frame.pack(fill='x', pady=(10, 0))

    # Κουμπί αποθήκευσης
    save_btn = ttk.Button(buttons_frame, text="💾 Αποθήκευση",
                          command=save_appointment, bootstyle="success", width=20)
    save_btn.pack(side='left', padx=(0, 10))

    # Κουμπί ακύρωσης
    cancel_btn = ttk.Button(buttons_frame, text="❌ Ακύρωση",
                            command=cancel_edit, bootstyle="danger", width=20)
    cancel_btn.pack(side='left')

    # Κεντράρισμα παραθύρου στην οθόνη
    edit_window.update_idletasks()
    x = (edit_window.winfo_screenwidth() // 2) - (edit_window.winfo_width() // 2)
    y = (edit_window.winfo_screenheight() // 2) - (edit_window.winfo_height() // 2)
    edit_window.geometry(f"+{x}+{y}")

    # Περιμένουμε μέχρι να κλείσει το παράθυρο
    edit_window.wait_window()

    return result[0]