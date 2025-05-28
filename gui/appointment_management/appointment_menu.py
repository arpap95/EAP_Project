import ttkbootstrap as ttk

def appointment_menu(content_frame, go_back_callback):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Main container
    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    from gui.appointment_management.daily_appointments_view import daily_appointments_view
    from gui.appointment_management.customer_appointments_view import customer_appointments_view
    from gui.customer_management.search_modify_customer import search_modify_customer

    lbl_left = ttk.Label(left_section, text='Διαχείριση Ραντεβού', bootstyle="inverse-dark",
                         font=('Helvetica', 14, 'bold'))
    lbl_left.pack(pady=5)

    btn_print_day = ttk.Button(left_section, text="Εμφάνιση Ραντεβού Ημέρας",
                               command=lambda: daily_appointments_view(content_frame,
                                                                       lambda: appointment_menu(content_frame,
                                                                                                go_back_callback)),
                         bootstyle="secondary", width=23)
    btn_print_day.pack(pady=5)

    btn_print_cust = ttk.Button(left_section, text="Εμφάνιση Ραντεβού Πελάτη",
                            command=lambda: customer_appointments_view(content_frame,
                                                                       lambda: appointment_menu(content_frame,
                                                                                                go_back_callback)),
                         bootstyle="secondary", width=23)
    btn_print_cust.pack(pady=5)
#Seperator between prints and options
    separator_frame = ttk.Frame(left_section, bootstyle="dark", height=15)
    separator_frame.pack(pady=10)

    btn_add = ttk.Button(left_section, text="Προσθήκη Ραντεβού",
                            command=lambda: search_modify_customer(content_frame),
                            bootstyle="secondary", width=23)
    btn_add.pack(pady=5)

    btn_delete = ttk.Button(left_section, text="Διαγραφή ραντεβού",
                            command=lambda: search_modify_customer(content_frame),
                            bootstyle="secondary", width=23)
    btn_delete.pack(pady=5)

    btn_edit = ttk.Button(left_section, text="Τροποποίηση ραντεβού",
                            command=lambda: search_modify_customer(content_frame),
                            bootstyle="secondary", width=23)
    btn_edit.pack(pady=5)

    # Bottom frame for "Back" button
    bottom_frame = ttk.Frame(content_frame, bootstyle="dark")
    bottom_frame.pack(fill='x', side='bottom', pady=10, padx=50)

    btn_back = ttk.Button(bottom_frame, text="Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)
