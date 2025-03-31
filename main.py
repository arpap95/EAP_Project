import tkinter as tk
from gui.app import App

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Διαχείριση Ραντεβού")
    root.geometry("800x500")

    app = App(root)

    root.mainloop()