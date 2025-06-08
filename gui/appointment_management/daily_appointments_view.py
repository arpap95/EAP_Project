import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog
from datetime import datetime
import utils.database_appointment as db_appoint
import utils.helper as hp
import tkinter.messagebox as mbox
from collections import defaultdict

# ΚΑΝΤΕ ΤΑ ΟΠΩΣ ΘΕΛΕΤΕ ΓΙΑ ΝΑ ΕΜΦΑΝΙΖΟΝΤΑΙ ΟΙ ΕΓΓΡΑΦΕΣ ΑΠΟ ΤΗΝ ΒΑΣΗ
def show_appointments_for_date(selected_date, container):
    """Εμφάνιση ραντεβού για την επιλεγμένη ημερομηνία"""
    # Εδώ θα προσθέσεις τη λογική για εμφάνιση των ραντεβού ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
    # Προς το παρόν, απλώς εμφανίζουμε ένα μήνυμα

    # Αφαίρεση προηγούμενων αποτελεσμάτων
    for widget in container.winfo_children():
        if isinstance(widget, ttk.LabelFrame):
            widget.destroy()

    # Frame για αποτελέσματα
    results_frame = ttk.LabelFrame(container, text="Ραντεβού", bootstyle="info")
    results_frame.pack(fill='both', expand=True, pady=20)

    # Εδώ θα συνδέσεις ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ με τη βάση δεδομένων για να πάρεις τα ραντεβού
    # Προσωρινό μήνυμα
    no_appointments = ttk.Label(results_frame,
                                text=f"Δεν βρέθηκαν ραντεβού για την {selected_date.strftime('%d/%m/%Y')}",
                                bootstyle="secondary", font=('Helvetica', 10))
    no_appointments.pack(pady=20)


def daily_appointments_view(content_frame, go_back_callback):
    # Καθαρισμός του frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Κύριο container
    main_container = ttk.Frame(content_frame, bootstyle="dark")
    main_container.pack(fill="both", expand=True, pady=20, padx=50)

    # Τίτλος
    title_label = ttk.Label(
        main_container,
        text="Εμφάνιση Ραντεβού Ημέρας",
        bootstyle="inverse-dark",
        font=("Helvetica", 16, "bold")
    )
    title_label.pack(pady=10)

    # Frame για επιλογή ημερομηνίας
    date_frame = ttk.Frame(main_container, bootstyle="dark")
    date_frame.pack(pady=20)

    # Label για την επιλεγμένη ημερομηνία
    selected_date_var = ttk.StringVar(value="Δεν έχει επιλεγεί ημερομηνία")
    date_label = ttk.Label(
        date_frame,
        textvariable=selected_date_var,
        bootstyle="inverse-dark",
        font=("Helvetica", 14, "bold")
    )
    date_label.pack(pady=10)

    # Frame για τα κουμπιά (ημερομηνία και email)
    buttons_frame = ttk.Frame(date_frame, bootstyle="dark")
    buttons_frame.pack(pady=10)

    # Κουμπί που ανοίγει το date picker
    pick_btn = ttk.Button(
        buttons_frame,
        text="Επίλεξε Ημερομηνία",
        bootstyle="warning",
        command=lambda: open_date_picker()
    )
    pick_btn.pack(side="left", padx=(0, 10))

    # Κουμπί για αποστολή email υπενθυμίσεων
    email_btn = ttk.Button(
        buttons_frame,
        text="📧 Αποστολή Email Υπενθυμίσεων",
        bootstyle="info",
        state="disabled",  # Αρχικά απενεργοποιημένο
        command=lambda: send_email_reminders()
    )
    email_btn.pack(side="left")

    # Container όπου θα εμφανιστούν τα ραντεβού
    appointments_container = ttk.Frame(main_container, bootstyle="dark")
    appointments_container.pack(fill="both", expand=True, pady=(10, 0))

    # Μεταβλητή για να κρατάμε την επιλεγμένη ημερομηνία
    current_selected_date = None

    def open_date_picker():
        nonlocal current_selected_date

        # Άνοιγμα DatePickerDialog (επιστρέφει datetime.date)
        date_dialog = DatePickerDialog(bootstyle="warning")
        selected_date = date_dialog.date_selected

        if not selected_date:
            return

        # Αποθήκευση της επιλεγμένης ημερομηνίας
        current_selected_date = selected_date

        # 1) Εμφάνιση σε ελληνική μορφή
        formatted_date = selected_date.strftime("%d/%m/%Y")
        selected_date_var.set(f"Επιλεγμένη ημερομηνία: {formatted_date}")

        # Ενεργοποίηση του κουμπιού email
        email_btn.configure(state="normal")

        # 2) Καθαρίζουμε προηγούμενα ραντεβού
        for w in appointments_container.winfo_children():
            w.destroy()

        # 3) Μετατροπή σε "YYYY-MM-DD"
        db_date_str = selected_date.strftime("%Y-%m-%d")

        # 4) Καλούμε ΜΟΝΟ μία φορά
        rows = db_appoint.display_appointment_date(db_date_str)

        if rows is None:
            no_label = ttk.Label(
                appointments_container,
                text="Δεν υπάρχουν ραντεβού για αυτή την ημερομηνία.",
                bootstyle="inverse-dark",
                font=("Helvetica", 12)
            )
            no_label.pack(pady=10)
            return

        # 5) Φτιάχνουμε το Treeview και γεμίζουμε κάθε γραμμή
        cols = ("first_name", "last_name", "appointment_date", "start_time", "end_time", "email")
        tree = ttk.Treeview(
            appointments_container,
            columns=cols,
            show="headings",
            bootstyle="dark"
        )
        tree.heading("first_name", text="Όνομα")
        tree.heading("last_name", text="Επώνυμο")
        tree.heading("appointment_date", text="Ημερομηνία")
        tree.heading("start_time", text="Ώρα Έναρξης")
        tree.heading("end_time", text="Ώρα Λήξης")
        tree.heading("email", text="Email")

        tree.column("first_name", width=100, anchor="center")
        tree.column("last_name", width=100, anchor="center")
        tree.column("appointment_date", width=100, anchor="center")
        tree.column("start_time", width=80, anchor="center")
        tree.column("end_time", width=80, anchor="center")
        tree.heading("email", text="Email")

        for row in rows:
            db_date = row[2]
            if isinstance(db_date, datetime):
                displayed_date = db_date.strftime("%d/%m/%Y")
            else:
                displayed_date = row[2]

            tree.insert(
                "",
                "end",
                values=(row[0], row[1], displayed_date, row[3], row[4], row[5])
            )

        tree.pack(fill="both", expand=True, pady=5, padx=5)

    def send_email_reminders():
        """Στέλνει email υπενθυμίσεων σε όλους τους πελάτες της επιλεγμένης ημερομηνίας."""
        if current_selected_date is None:
            return

        # 1) Μετατροπή σε SQL format
        db_date_str = current_selected_date.strftime("%Y-%m-%d")

        # 2) Φέρνουμε τα ραντεβού from DB
        rows = db_appoint.display_appointment_date(db_date_str)
        if not rows:
            mbox.showinfo("Πληροφορία", "Δεν υπάρχουν ραντεβού για αυτή την ημερομηνία.")
            return

        # 3) Απενεργοποίησε το κουμπί για να μην το πατήσει ξανά
        email_btn.configure(state="disabled")
        email_btn.update()

        appointments_by_email = defaultdict(list)
        for first, last, apt_date, start, end, to_email in rows:
            appointments_by_email[to_email].append((first, last, apt_date, start, end))

        errors = []

        # 2) sent email for unique addresses
        for to_email, appts in appointments_by_email.items():
            # Use the first name/last name from the first appointment
            first, last, _, _, _ = appts[0]

            # Build a little bulleted list of this person's times
            date_display = (appts[0][2].strftime("%d/%m/%Y")
                            if hasattr(appts[0][2], "strftime")
                            else appts[0][2])
            lines = [f"- {date_display}, {start}–{end}" for *_, start, end in appts]

            subject = f"Υπενθύμιση Ραντεβού — {date_display}"
            body = (
                    f"Γεια σου {first} {last},\n\n"
                    "Σου υπενθυμίζουμε τα ραντεβού σου για την ημέρα:\n"
                    + "\n".join(lines)
                    + "\n\nΣε περιμένουμε!\n"
            )

            try:
                hp.sent_email(
                    email_subject=subject,
                    send_to=to_email,
                    content_plain=body
                )
            except Exception as e:
                errors.append(f"{to_email}: {e}")

        # 3) Export files
        hp.export_appointments_date(appointment_date=db_date_str)

        # 4) Επανενεργοποίηση του κουμπιού
        email_btn.configure(state="normal")
        if errors:
            mbox.showwarning("Σφάλματα", "Κάποια email ΔΕΝ στάλθηκαν:\n" + "\n".join(errors))
        else:
            mbox.showinfo("Επιτυχία", "Όλα τα email στάλθηκαν με επιτυχία.")

    # Bottom frame για τα κουμπιά
    bottom_frame = ttk.Frame(content_frame, bootstyle="dark")
    bottom_frame.pack(fill='x', side='bottom', pady=10, padx=50)

    btn_back = ttk.Button(bottom_frame, text="↩️ Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)