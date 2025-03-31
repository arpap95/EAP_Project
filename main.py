import tkinter as tk
from gui.app import App

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Διαχείριση Ραντεβού")
    root.geometry("800x500")

    app = App(root)

    root.mainloop()

import ttkbootstrap as ttk
import tkinter as tk
from gui_components.menu import show_main_menu


root = tk.Tk()
root.title("Διαχείριση Ραντεβού")
root.geometry("800x500")

content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

show_main_menu(content_frame)

root.mainloop()

