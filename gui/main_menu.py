import tkinter as tk
import ttkbootstrap as ttk

from gui.appointment_management.appointment_menu import appointment_menu
from gui.customer_management.customer_menu import customer_menu


def show_main_menu(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Ρύθμιση σκούρου φόντου
    content_frame.configure(bootstyle="dark")

    ttk.Frame(content_frame, height=40, bootstyle="dark").pack()

    # Title
    title = ttk.Label(
        content_frame,
        text="ΤΑ ΡΑΝΤΕΒΟΥ ΜΟΥ",
        font=("Helvetica", 26, "bold"),
        bootstyle="inverse-dark"
    )
    title.pack(pady=(20, 40))

    # Line
    separator = ttk.Separator(content_frame)
    separator.pack(fill='x', padx=100, pady=10)

    # Space
    ttk.Frame(content_frame, height=30, bootstyle="dark").pack()

    # Center
    lbl_container = ttk.Frame(content_frame, bootstyle="dark")
    lbl_container.place(relx=0.5, rely=0.5, anchor='center')

    left_section = ttk.Frame(lbl_container, bootstyle="dark")
    left_section.pack(side='left', padx=35)

    right_section = ttk.Frame(lbl_container, bootstyle="dark")
    right_section.pack(side='right', padx=35)

    #Button
    btn_left = ttk.Button(
        left_section,
        text="Διαχείριση Πελατών",
        command=lambda: customer_menu(content_frame, lambda: show_main_menu(content_frame)),
        bootstyle="success",
        padding = (10, 20),
        width = 30
    )
    btn_left.pack(pady=5)

    #Button
    btn_right = ttk.Button(
        right_section,
        text="Διαχείριση Ραντεβού",
        command=lambda: appointment_menu(content_frame, lambda: show_main_menu(content_frame)),
        bootstyle="info",
        padding=(10, 20),
        width=30
    )
    btn_right.pack(pady=5)
