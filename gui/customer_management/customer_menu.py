import ttkbootstrap as ttk

def customer_menu(content_frame, go_back_callback):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    # Main container
    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    from gui.customer_management.add_customer import addNewClient
    from gui.customer_management.delete_customer import deleteCustomer
    from gui.customer_management.search_modify_customer import search_modify_customer

    lbl_left = ttk.Label(left_section, text='Διαχείριση Πελατών', bootstyle="inverse-dark",
                         font=('Helvetica', 14, 'bold'))
    lbl_left.pack(pady=5)

    btn_add = ttk.Button(left_section, text="Προσθήκη Πελάτη",
                         command=lambda: addNewClient(content_frame),
                         bootstyle="secondary", padding=(10, 20), width=30)
    btn_add.pack(pady=5)

    btn_delete = ttk.Button(left_section, text="Διαγραφή Πελάτη",
                            command=lambda: deleteCustomer(content_frame),
                            bootstyle="secondary", padding=(10, 20), width=30)
    btn_delete.pack(pady=5)

    btn_search = ttk.Button(left_section, text="Αναζήτηση/Τροποποίηση Πελάτη",
                            command=lambda: search_modify_customer(content_frame),
                            bootstyle="secondary", padding=(10, 20), width=30)
    btn_search.pack(pady=5)

    # Bottom frame for "Back" button
    bottom_frame = ttk.Frame(content_frame, bootstyle="dark")
    bottom_frame.pack(fill='x', side='bottom', pady=10, padx=50)

    btn_back = ttk.Button(bottom_frame, text="↩️ Επιστροφή",
                          command=go_back_callback,
                          bootstyle="danger", width=15)
    btn_back.pack(side='right', padx=10)

