import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu


# This could be the same as modify_customer for now,
# or could be expanded with search functionality
def search_customer(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Header
    header_frame = ttk.Frame(content_frame, bootstyle="dark")
    header_frame.pack(fill='x', pady=(10, 20))

    title = ttk.Label(header_frame, text="Αναζήτηση Πελάτη", font=('Helvetica', 16, 'bold'),
                      bootstyle="inverse-dark")
    title.pack(fill='x', padx=20, pady=5)

    # Search form goes here

    # Return button
    btn_return = ttk.Button(
        content_frame,
        text="Επιστροφή",
        command=lambda: show_main_menu(content_frame),
        bootstyle="secondary",
        width=12
    )
    btn_return.pack(side='bottom', pady=20)