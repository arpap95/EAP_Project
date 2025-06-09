import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import DatePickerDialog, Messagebox
from datetime import datetime
from gui.appointment_management.appointment_edit import edit_appointment_window
import utils.database_appointment as db_appoint
import utils.database as db

def customer_appointments_view(content_frame, go_back_callback):
    # clear the frame
    for w in content_frame.winfo_children():
        w.destroy()
    content_frame.configure(bootstyle="dark")

    # Header
    header = ttk.Frame(content_frame, bootstyle="dark")
    header.pack(fill='x', pady=(10,20))
    ttk.Label(header, text="Εμφάνιση Ραντεβού Πελάτη",
              font=('Helvetica',16,'bold'), bootstyle="inverse-dark").pack(fill='x', padx=20)
    ttk.Label(header, text="Εισάγετε τηλέφωνο ή email για αναζήτηση",
              font=('Helvetica',11), bootstyle="inverse-dark").pack(fill='x', padx=20)

    # Search form
    search_phone, search_email = tk.StringVar(), tk.StringVar()
    error_var = tk.StringVar()
    form = ttk.Frame(content_frame, bootstyle="dark")
    form.pack(fill='x', padx=20)

    row = ttk.Frame(form, bootstyle="dark"); row.pack(fill='x', pady=5)
    ttk.Label(row, text="Τηλέφωνο", width=10, bootstyle="inverse-dark").pack(side='left')
    ttk.Entry(row, textvariable=search_phone, bootstyle="dark").pack(side='left', fill='x', expand=True)

    row = ttk.Frame(form, bootstyle="dark"); row.pack(fill='x', pady=5)
    ttk.Label(row, text="Email", width=10, bootstyle="inverse-dark").pack(side='left')
    ttk.Entry(row, textvariable=search_email, bootstyle="dark").pack(side='left', fill='x', expand=True)

    error_label = ttk.Label(form, textvariable=error_var, bootstyle="danger-inverse")
    error_label.pack(fill='x', pady=(5,0))
    error_label.pack_forget()

    # Results container
    results = ttk.Frame(content_frame, bootstyle="dark")
    results.pack(fill='both', expand=True, padx=20, pady=10)

    # Bottom buttons
    bottom = ttk.Frame(content_frame, bootstyle="dark")
    bottom.pack(fill='x', side='bottom', pady=10, padx=20)
    ttk.Button(bottom, text="🔍 Αναζήτηση", command=lambda: search_customer(), bootstyle="primary").pack(side='left')
    ttk.Button(bottom, text="🧹 Καθαρισμός", command=lambda: clear_search(), bootstyle="secondary").pack(side='left', padx=5)
    ttk.Button(bottom, text="↩️ Επιστροφή", command=go_back_callback, bootstyle="danger").pack(side='right')

    # state
    current_tree = None
    current_customer = None
    current_appointments = []

    def on_appointment_double_click(evt):
        delete_selected_appointment()

    def search_customer():
        nonlocal current_customer, current_appointments
        # clear
        for w in results.winfo_children(): w.destroy()
        error_label.pack_forget()

        phone = search_phone.get().strip()
        email = search_email.get().strip()
        if not (phone or email):
            error_var.set("Παρακαλώ εισάγετε τηλέφωνο ή email")
            error_label.pack(fill='x')
            return

        cid = db.search_customer(phone, email)
        if not cid:
            error_var.set("Δεν βρέθηκε πελάτης με αυτά τα στοιχεία")
            error_label.pack(fill='x')
            return

        # load customer details
        rows = db.get_customer(phone, email)
        fn, ln, ph, mail = rows[0]
        current_customer = {'name':fn, 'lastname':ln, 'phone':ph, 'email':mail}

        # load appointments
        tuples = db_appoint.display_appointment_user(ph, mail) or []
        current_appointments = []
        for (aid, _, _, _, _, date_, start, end) in tuples:
            disp = date_.strftime("%d/%m/%Y") if hasattr(date_, "strftime") else date_
            current_appointments.append({
                'appointment_id': aid,
                'date': disp,
                'start_time': start,
                'end_time': end
            })

        show_customer_appointments()

    def clear_search():
        nonlocal current_customer, current_appointments, current_tree
        search_phone.set(""); search_email.set("")
        error_label.pack_forget()
        current_customer = None
        current_appointments = []
        current_tree = None
        for w in results.winfo_children(): w.destroy()

    def delete_selected_appointment():
        nonlocal current_appointments
        if not current_tree:
            return
        sel = current_tree.selection()
        if not sel:
            return
        item = sel[0]
        vals = current_tree.item(item, 'values')
        apt = {'date':vals[0], 'start_time':vals[1], 'end_time':vals[2]}
        if Messagebox.yesno("Επιβεβαίωση","Θέλετε να διαγράψετε αυτό το ραντεβού;"):
            # call your DB delete by appointment_id stored in iid
            db_appoint.delete_appointment(int(item))
            current_appointments = [a for a in current_appointments if a['appointment_id'] != int(item)]
            show_customer_appointments()
            Messagebox.yesno("ΟΚ", "Διαγράφηκε.")

    def edit_selected_appointment():
        if not current_tree: return
        sel = current_tree.selection()
        if not sel: return
        item = sel[0]
        apt = next(a for a in current_appointments if str(a['appointment_id'])==item)
        if edit_appointment_window(content_frame, apt, current_customer):
            # refresh after edit
            search_customer()

    def show_customer_appointments():
        nonlocal current_tree
        # clear
        for w in results.winfo_children(): w.destroy()

        # customer info
        cf = ttk.LabelFrame(results, text="Στοιχεία Πελάτη", bootstyle="info")
        cf.pack(fill='x', pady=(0,10))
        ttk.Label(cf,
            text=(f"Όνομα: {current_customer['name']} {current_customer['lastname']}\n"
                  f"Τηλέφωνο: {current_customer['phone']}\n"
                  f"Email: {current_customer['email']}"),
            bootstyle="dark"
        ).pack(padx=10,pady=10)

        # appointments
        af = ttk.LabelFrame(results, text="Ραντεβού", bootstyle="success")
        af.pack(fill='both', expand=True)
        if not current_appointments:
            ttk.Label(af, text="Δεν βρέθηκαν ραντεβού", bootstyle="secondary").pack(pady=20)
            current_tree = None
            return

        tf = ttk.Frame(af, bootstyle="dark"); tf.pack(fill='both', expand=True, padx=10, pady=10)
        cols = ("date","start_time","end_time")
        current_tree = ttk.Treeview(tf, columns=cols, show="headings", bootstyle="info")
        for c,h in zip(cols,("Ημερομηνία","Ώρα Έναρξης","Ώρα Λήξης")):
            current_tree.heading(c,text=h,anchor="center")
            current_tree.column(c,anchor="center",width=150)
        sb = ttk.Scrollbar(tf, orient="vertical", command=current_tree.yview)
        current_tree.configure(yscrollcommand=sb.set)
        current_tree.bind("<Double-1>", on_appointment_double_click)

        for a in current_appointments:
            current_tree.insert("", "end",
                                iid=str(a['appointment_id']),
                                values=(a['date'], a['start_time'], a['end_time']))
        current_tree.pack(side='left',fill='both',expand=True)
        sb.pack(side='right',fill='y')

        btns = ttk.Frame(af); btns.pack(fill='x', pady=5)
        ttk.Button(btns, text="✏️ Τροποποίηση", command=edit_selected_appointment, bootstyle="warning").pack(side='left')
        ttk.Button(btns, text="🗑️ Διαγραφή",  command=delete_selected_appointment, bootstyle="danger").pack(side='left', padx=5)
        ttk.Button(btns, text="🔄 Ανανέωση", command=search_customer, bootstyle="secondary").pack(side='left', padx=5)
