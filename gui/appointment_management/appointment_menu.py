import ttkbootstrap as ttk

def appointment_menu(content_frame, go_back_callback):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)  # Κεντρική στοίχιση

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    right_section = ttk.Frame(lbl_container, bootstyle="dark")
    right_section.pack(side='right', expand=True)

    from gui.appointment_management.appointment_form import appointment_management

    # Right Label & Button
    lbl_right = ttk.Label(right_section, text='Διαχείριση Ραντεβού', bootstyle="inverse-dark",
                          font=('Helvetica', 14, 'bold'))
    lbl_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Προσθήκη Ραντεβού",
                           command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Τροποποίηση Ραντεβού",
                           command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Διαγραφή Ραντεβού",
                           command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Αναζήτηση Ραντεβού",
                           command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    # Bottom frame for "Back" button
    bottom_frame = ttk.Frame(content_frame, bootstyle="dark")
    bottom_frame.pack(fill='x', side='bottom', pady=10, padx=50)

    btn_back = ttk.Button(bottom_frame, text="Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)
