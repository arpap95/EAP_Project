import tkinter as tk
import ttkbootstrap as ttk

from gui.appointment_management.appointment_menu import appointment_menu
from gui.customer_management.customer_menu import customer_menu


def show_main_menu(content_frame):
    # Clear the frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_frame.configure(bootstyle="dark")

    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.pack(fill='x', pady=10, padx=50)  # Κεντρική στοίχιση

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', expand=True)

    right_section = ttk.Frame(lbl_container, bootstyle="dark")
    right_section.pack(side='right', expand=True)

    # Customer Management Section
    lbl_left = ttk.Label(left_section, text='Διαχείριση Πελατών', bootstyle="inverse-dark",
                         font=('Helvetica', 14, 'bold'))
    lbl_left.pack(pady=5)

    btn_left = ttk.Button(left_section, text="Διαχείριση Πελατών",
                          command=lambda: customer_menu(content_frame, lambda: show_main_menu(content_frame)),
                          bootstyle="secondary", width=20)
    btn_left.pack(pady=5)

    # Appointment Management Section
    lbl_right = ttk.Label(right_section, text='Διαχείριση Ραντεβού', bootstyle="inverse-dark",
                          font=('Helvetica', 14, 'bold'))
    lbl_right.pack(pady=5)

    btn_right = ttk.Button(right_section, text="Διαχείριση Ραντεβού",
                           command=lambda: appointment_menu(content_frame, lambda: show_main_menu(content_frame)),
                           bootstyle="secondary", width=20)
    btn_right.pack(pady=5)
