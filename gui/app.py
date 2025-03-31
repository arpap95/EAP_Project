import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu


class App:
    def __init__(self, root):
        self.root = root

        # Main content frame
        self.content_frame = ttk.Frame(root)
        self.content_frame.pack(fill="both", expand=True)

        # Show the main menu initially
        show_main_menu(self.content_frame)