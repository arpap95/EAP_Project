import tkinter as tk
from gui.app import App


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Διαχείριση Ραντεβού")
    root.geometry("1000x800")

    app = App(root)

    root.mainloop()
