import ttkbootstrap as ttk
from add_cust import addNewClient
from delete_cust import deleteCustomer
from appointment_manager import appointment_management
from customer_manager import customer_management

def show_main_menu(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    right_section = ttk.Frame(lbl_container, bootstyle="dark")
    right_section.pack(side='right', expand=True)

    #Left
    lbl_left = ttk.Label(left_section, text='Διαχείριση Πελατών', bootstyle="inverse-dark",
                         font=('Helvetica', 14, 'bold'))
    lbl_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Προσθήκη Πελάτη", command=lambda: addNewClient(content_frame),
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Τροποποίηση Πελάτη", command=lambda: customer_management(content_frame),
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Διαγραφή Πελάτη", command=lambda: deleteCustomer(content_frame),
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Αναζήτηση Πελάτη", command=lambda: customer_management(content_frame),
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    #Right
    lbl_right = ttk.Label(right_section, text='Διαχείριση Ραντεβού', bootstyle="inverse-dark",
                          font=('Helvetica', 14, 'bold'))
    lbl_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Προσθήκη Ραντεβού", command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Τροποποίηση Ραντεβού", command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Διαγραφή Ραντεβού", command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Αναζήτηση Ραντεβού", command=lambda: appointment_management(content_frame),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)