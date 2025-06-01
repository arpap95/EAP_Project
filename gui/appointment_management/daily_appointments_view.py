import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog
from datetime import datetime
import utils.database_appointment as db_appoint
import utils.helper as hp



#ΚΑΝΤΕ ΤΑ ΟΠΩΣ ΘΕΛΕΤΕ ΓΙΑ ΝΑ ΕΜΦΑΝΙΖΟΝΤΑΙ ΟΙ ΕΓΓΡΑΦΕΣ ΑΠΟ ΤΗΝ ΒΑΣΗ
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

    # Κουμπί που ανοίγει το date picker
    pick_btn = ttk.Button(
        date_frame,
        text="Επίλεξε Ημερομηνία",
        bootstyle="warning",
        command=lambda: open_date_picker()
    )
    pick_btn.pack()

    # Container όπου θα εμφανιστούν τα ραντεβού
    appointments_container = ttk.Frame(main_container, bootstyle="dark")
    appointments_container.pack(fill="both", expand=True, pady=(10, 0))

    def open_date_picker():
        # Άνοιγμα DatePickerDialog (επιστρέφει datetime.date)
        date_dialog = DatePickerDialog(bootstyle="warning")
        selected_date = date_dialog.date_selected

        if not selected_date:
            return

        # 1) Εμφάνιση σε ελληνική μορφή
        formatted_date = selected_date.strftime("%d/%m/%Y")
        selected_date_var.set(f"Επιλεγμένη ημερομηνία: {formatted_date}")

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
        # de-duplication of email - addresses
        seen = set()
        emails = []

        for i in rows: # rows = results from DB
            email = i[-1] # last column from DB
            if email not in seen :
                seen.add(email)
                emails.append(email)

        for user in emails:
            hp.sent_email(email_subject=f"Υπενθύμιση Ραντεβου για ημερα : {db_date_str}", send_to=user, cc=None, bcc=None,
                          content_plain="Υπενθύμιση Ραντεβου",
                          content_html=None,
                          attach_dir=None,
                          attach_files=None
                          )



