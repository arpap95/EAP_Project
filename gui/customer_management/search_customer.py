import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu

def search_customer(content_frame):
    # Clear existing content in content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    query = search_entry.get()

#Main search frame
search_frame = ttk.Frame(bootstyle="dark")
search_frame.pack(fill="both", expand=True, padx=10, pady=10)

#Search label
search_label = ttk.Label(
    search_frame,
    text="Αναζήτηση Πελάτη",
    bootstyle="inverse-dark",
    font=("Helvetica", 12, "bold")
)
search_label.pack(pady=5)

# Search entry (search bar)
search_entry = ttk.Entry( width=30, font=("Helvetica", 11))
search_entry.pack(pady=5)

# Results display
tree = ttk.Treeview(
    columns=("ID", "Name", "Email", "Phone"),
    show="headings"
)
tree.heading("ID", text="ID")
tree.heading("Name", text="Όνομα")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Τηλέφωνο")
tree.pack(expand=True, fill="both", pady=5)


def search():
    # Clear previous search results
    for item in tree.get_children():
        tree.delete(item)

    # Get the search term
    # search_term = search_entry.get().strip()

# Search button
search_button = ttk.Button(
    text="Αναζήτηση",
    command=search,
    bootstyle="secondary",
    width=15
)
search_button.pack(pady=5)

# Back button to return to main menu
back_button = ttk.Button(
    search_frame,
    text="Πίσω",
    command=lambda: show_main_menu(),
    bootstyle="secondary",
    width=15
)
back_button.pack(pady=5)
