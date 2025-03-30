import ttkbootstrap as ttk
import tkinter as tk
from menu import show_main_menu

root = tk.Tk()
root.title("Διαχείριση Ραντεβού")
root.geometry("800x500")

content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

show_main_menu(content_frame)

root.mainloop()