import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu

def customer_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Button(content_frame, text="Αποθήκευση",
               command=lambda: show_main_menu(content_frame)).pack(pady=10)
    ttk.Button(content_frame, text="Επιστροφή",
               command=lambda: show_main_menu(content_frame)).pack(pady=10)