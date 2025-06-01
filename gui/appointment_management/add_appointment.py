import tkinter as tk
import ttkbootstrap as ttk
import utils.database as db
from ttkbootstrap.dialogs import DatePickerDialog
from datetime import datetime, timedelta
import utils.database_appointment as db_appoint
from ttkbootstrap import Querybox

def add_appointment(content_frame, go_back_callback):
    # Καθαρισμός του frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    # Title in the header
    title = ttk.Label(header_frame, text="Προσθήκη Ραντεβού Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=(5, 0))

    subtitle = ttk.Label(header_frame, text="Εισάγετε τηλέφωνο ή email για αναζήτηση", font=('Helvetica', 11),
                         bootstyle="inverse-dark")
    subtitle.pack(fill='x', padx=20, pady=(0, 5))

    # Form variables for search
    search_phone = tk.StringVar(value="")
    search_email = tk.StringVar(value="")

    # Form variables for appointment
    selected_date = tk.StringVar(value="")
    start_time = tk.StringVar(value="09:00")
    end_time = tk.StringVar(value="09:30")
    appointment_notes = tk.StringVar(value="")

    # Error/Success message variable
    error_var = tk.StringVar(value="")

    # Customer found variables
    customer_found = tk.BooleanVar(value=False)
    customer_name = tk.StringVar(value="")
    customer_lastname = tk.StringVar(value="")

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

    # Appointment details frame (hidden initially)
    appointment_frame = ttk.Frame(search_form_frame, bootstyle="dark")
    appointment_frame.pack(fill='x', pady=(10, 0))
    appointment_frame.pack_forget()

    # Customer info display frame
    customer_info_frame = ttk.Frame(appointment_frame, bootstyle="dark")
    customer_info_frame.pack(fill='x', pady=(0, 15))

    customer_info_label = ttk.Label(customer_info_frame, text="", bootstyle="info-inverse",
                                    font=('Helvetica', 11, 'bold'))
    customer_info_label.pack(fill='x', padx=5)

    # Date selection row
    date_frame = ttk.Frame(appointment_frame, bootstyle="dark")
    date_frame.pack(fill='x', pady=(0, 15))

    date_label = ttk.Label(date_frame, text="Ημερομηνία", width=12, bootstyle="inverse-dark")
    date_label.pack(side='left', padx=5)

    # Date picker button
    date_button = ttk.Button(date_frame, text="📅 Επιλογή Ημερομηνίας", bootstyle="info")
    date_button.pack(side='left', padx=5)

    # Selected date display
    selected_date_label = ttk.Label(date_frame, textvariable=selected_date, bootstyle="inverse-dark",
                                    font=('Helvetica', 10))
    selected_date_label.pack(side='left', padx=10)

    # Time selection frame
    time_frame = ttk.Frame(appointment_frame, bootstyle="dark")
    time_frame.pack(fill='x', pady=(0, 15))

    # Start time
    start_time_label = ttk.Label(time_frame, text="Ώρα Έναρξης", width=12, bootstyle="inverse-dark")
    start_time_label.pack(side='left', padx=5)

    # Create time options (every 15 minutes from 08:00 to 20:00)
    time_options = []
    for hour in range(8, 21):  # 08:00 to 20:45
        for minute in [0, 15, 30, 45]:
            time_options.append(f"{hour:02d}:{minute:02d}")

    start_time_combo = ttk.Combobox(time_frame, textvariable=start_time, values=time_options,
                                    width=8, bootstyle="dark", state="readonly")
    start_time_combo.pack(side='left', padx=5)

    # End time
    end_time_label = ttk.Label(time_frame, text="Ώρα Λήξης", width=12, bootstyle="inverse-dark")
    end_time_label.pack(side='left', padx=(20, 5))

    end_time_combo = ttk.Combobox(time_frame, textvariable=end_time, values=time_options,
                                  width=8, bootstyle="dark", state="readonly")
    end_time_combo.pack(side='left', padx=5)

    # Notes/Description frame
    notes_frame = ttk.Frame(appointment_frame, bootstyle="dark")
    notes_frame.pack(fill='x', pady=(0, 15))

    notes_label = ttk.Label(notes_frame, text="Σημειώσεις", width=12, bootstyle="inverse-dark")
    notes_label.pack(side='left', padx=5, anchor='n')

    notes_entry = ttk.Entry(notes_frame, textvariable=appointment_notes, bootstyle="dark")
    notes_entry.pack(side='left', padx=5, fill='x', expand=True)

    def open_date_picker():
        """Άνοιγμα του date picker dialog και λήψη επιλεγμένης ημερομηνίας."""
        today = datetime.now()

        # Δημιουργούμε και εμφανίζουμε αμέσως το DatePickerDialog
        chosen_date = Querybox.get_date(
            parent=content_frame,
            title="Επιλογή Ημερομηνίας",
            firstweekday=0,    # 0 = Δευτέρα πρώτη μέρα της εβδομάδας
            startdate=today,
            bootstyle="primary"
        )

        if chosen_date:
            on_date_selected(chosen_date)

    def on_date_selected(date_obj):
        """Callback όταν επιλεγεί ημερομηνία (λαμβάνει datetime.date)."""
        formatted_date = date_obj.strftime("%d/%m/%Y")
        selected_date.set(formatted_date)

    def calculate_end_time(start_time_str):
        """Υπολογισμός ώρας λήξης (προσθήκη 30 λεπτών)"""
        try:
            start_hour, start_minute = map(int, start_time_str.split(':'))
            start_datetime = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            end_datetime = start_datetime + timedelta(minutes=30)
            return end_datetime.strftime("%H:%M")
        except:
            return "09:30"

    def on_start_time_change(event=None):
        """Αυτόματος υπολογισμός ώρας λήξης όταν αλλάζει η ώρα έναρξης"""
        start_time_str = start_time.get()
        if start_time_str:
            calculated_end_time = calculate_end_time(start_time_str)
            end_time.set(calculated_end_time)

    # Bind the start time change event
    start_time_combo.bind('<<ComboboxSelected>>', on_start_time_change)
    date_button.configure(command=open_date_picker)

    def search_customer():
        global phone_value
        global email_value
        """Αναζήτηση πελάτη στη βάση δεδομένων"""
        # Hide previous messages and appointment form
        error_label.pack_forget()
        appointment_frame.pack_forget()

        # Get search values
        phone_value = search_phone.get().strip()
        email_value = search_email.get().strip()

        # Check if at least one field is filled
        if not phone_value and not email_value:
            error_var.set("Συμπληρώστε τουλάχιστον ένα πεδίο")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Search for customer in database
        customer = db.customer_exists_check(mobile_number=phone_value, email=email_value)

        if customer:
            # Customer found - get full details
            customer_lst = db.get_customer(mobile_number=phone_value, email=email_value)

            # Store customer info
            customer_name.set(customer_lst[0][0])  # First Name
            customer_lastname.set(customer_lst[0][1])  # Last Name
            customer_found.set(True)

            # Display customer info
            customer_info_text = f"Πελάτης: {customer_lst[0][0]} {customer_lst[0][1]} | Τηλ: {customer_lst[0][2]} | Email: {customer_lst[0][3]}"
            customer_info_label.configure(text=customer_info_text)

            # Show success message
            error_var.set(f"Πελάτης βρέθηκε! Συμπληρώστε τα στοιχεία του ραντεβού.")
            error_label.configure(bootstyle="success-inverse")
            error_label.pack(fill='x', padx=5)

            # Show appointment form
            appointment_frame.pack(fill='x', pady=(10, 0))

            # Set default date to today
            today = datetime.now().strftime("%d/%m/%Y")
            selected_date.set(today)

        else:
            # Customer not found
            customer_found.set(False)
            error_var.set("Ο πελάτης δεν βρέθηκε στη βάση δεδομένων")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)

    def validate_appointment_fields():
        """Έλεγχος ότι όλα τα απαραίτητα πεδία είναι συμπληρωμένα"""
        if not selected_date.get().strip():
            return "Παρακαλώ επιλέξτε ημερομηνία"

        if not start_time.get().strip():
            return "Παρακαλώ επιλέξτε ώρα έναρξης"

        if not end_time.get().strip():
            return "Παρακαλώ επιλέξτε ώρα λήξης"

        # Check if end time is after start time
        try:
            start_hour, start_minute = map(int, start_time.get().split(':'))
            end_hour, end_minute = map(int, end_time.get().split(':'))

            start_total_minutes = start_hour * 60 + start_minute
            end_total_minutes = end_hour * 60 + end_minute

            if end_total_minutes <= start_total_minutes:
                return "Η ώρα λήξης πρέπει να είναι μετά την ώρα έναρξης"
        except:
            return "Μη έγκυρες ώρες"

        return None

    def save_appointment():
        """Αποθήκευση του ραντεβού στη βάση δεδομένων"""
        # Hide previous error message
        error_label.pack_forget()

        # Validate appointment fields
        validation_error = validate_appointment_fields()
        if validation_error:
            error_var.set(validation_error)
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
            return

        # Get appointment values
        appointment_date = selected_date.get()
        appointment_start_time = start_time.get()
        appointment_end_time = end_time.get()
        notes = appointment_notes.get().strip()

        # Get customer values
        phone_value = search_phone.get().strip()
        email_value = search_email.get().strip()

        try:
            # Save appointment to database
            # Εδώ θα πρέπει να καλέσεις τη συνάρτηση της βάσης δεδομένων για αποθήκευση ραντεβού ΝΙΚΟ ΚΑΙ ΔΗΜΗΤΡΗ
            db_appoint.add_appointment(appointment_date=appointment_date,start_time=appointment_start_time,end_time=appointment_end_time,mobile_number=phone_value, email=email_value )

            # Show success message
            error_var.set(
                f"Το ραντεβού αποθηκεύτηκε επιτυχώς για την {appointment_date} από {appointment_start_time} έως {appointment_end_time}")
            error_label.configure(bootstyle="success-inverse")
            error_label.pack(fill='x', padx=5)

            # Clear form after successful save
            clear_appointment_form()


        except ValueError as ve:
            # Χειριζόμαστε σφάλματα τύπου ValueError (π.χ. «Δεν βρέθηκε πελάτης…» που ρίχνει η helper)
            # Show error message
            error_var.set(str(ve))
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)

        except psycopg2.IntegrityError as ie:
            # Π.χ. διπλό insert με ίδιες συναρτήσεις/κλειδιά (αν υπάρχουν μοναδικοί περιορισμοί)
            error_var.set("Το ραντεβού υπάρχει ήδη ή παραβιάζει κανόνες μοναδικότητας.")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)

        except Exception as e:
            # Άλλα απρόβλεπτα σφάλματα
            error_var.set(f"Σφάλμα κατά την αποθήκευση: {e}")
            error_label.configure(bootstyle="danger-inverse")
            error_label.pack(fill='x', padx=5)
        finally:
            # Ενεργοποιούμε ξανά το κουμπί (είτε πετύχαμε είτε πέσαμε σε exception)
            save_btn.configure(state="normal")
            save_btn.update()

    def clear_appointment_form():
        """Καθαρισμός της φόρμας ραντεβού"""
        selected_date.set("")
        start_time.set("09:00")
        end_time.set("09:30")
        appointment_notes.set("")
        search_phone.set("")
        search_email.set("")
        customer_found.set(False)
        appointment_frame.pack_forget()

    # Search button
    search_btn = ttk.Button(
        master=search_button_frame,
        text="🔍 Αναζήτηση Πελάτη",
        command=search_customer,
        bootstyle="primary",
        width=25
    )
    search_btn.pack(pady=5)

    # Save appointment button frame
    save_button_frame = ttk.Frame(appointment_frame, bootstyle="dark")
    save_button_frame.pack(fill='x', pady=(10, 0))

    save_btn = ttk.Button(
        master=save_button_frame,
        text="💾 Αποθήκευση Ραντεβού",
        command=save_appointment,
        bootstyle="success",
        width=20
    )
    save_btn.pack(side='left', padx=5)

    clear_btn = ttk.Button(
        master=save_button_frame,
        text="🧹 Καθαρισμός",
        command=clear_appointment_form,
        bootstyle="warning",
        width=12
    )
    clear_btn.pack(side='left', padx=5)

    # Bottom button container
    button_container = ttk.Frame(search_form_frame, bootstyle="dark")
    button_container.pack(fill='x', pady=(20, 10), side='bottom')

    # Back button
    cancel_btn = ttk.Button(
        master=button_container,
        text="↩️ Επιστροφή",
        command=go_back_callback,
        bootstyle="danger",
        width=12
    )
    cancel_btn.pack(side='right', padx=5)

    # Set focus on the first field
    search_phone_entry.focus_set()