import tkinter as tk
from tkinter import ttk


def show_add_form():
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Label(content_frame, text="Προσθήκη Νέου Ραντεβού").pack(pady=10)
    ttk.Entry(content_frame).pack(pady=5)
    ttk.Button(content_frame, text="Αποθήκευση", command=lambda: show_main_menu()).pack(pady=10)
    ttk.Button(content_frame, text="Επιστροφή", command=show_main_menu).pack(pady=10)

def customer_management():
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Button(content_frame, text="Αποθήκευση", command=lambda: show_main_menu()).pack(pady=10)
    ttk.Button(content_frame, text="Επιστροφή", command=show_main_menu).pack(pady=10)


def show_main_menu():
    for widget in content_frame.winfo_children():
        widget.destroy()

    ttk.Button(content_frame, text="Προσθήκη Ραντεβού", command=show_add_form).pack(pady=20)
    ttk.Button(content_frame, text="Διαχείριση Πελατών", command=customer_management).pack(pady=20)



root = tk.Tk()
root.title("Διαχείριση Ραντεβού")
root.geometry("600x400")

content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

show_main_menu()

root.mainloop()

# root = Tk()
# root.title("Appointments")
# root.geometry("1600x1020")
# root.configure(background = "black")
# root.resizable(width= True, height=True)
# label1 = Label(root, text="Προσθήκη πελάτη", bg="black", fg="white", font= "arial 12")
# label1.place(x=10, y=20)
#
#
# label2 = Label(root, text="Name", bg="black", fg="white", font= "arial 12")
# label2.place(x=10, y=50)
# text1 =Entry(root, width=20, bg="black", font="aria 12")
# text1.place(x=100, y=50)
#
# label3 = Label(root, text="Surname", bg="black", fg="white", font= "arial 12")
# label3.place(x=10, y=100)
# text2 =Entry(root, width=20, bg="black", font="aria 12")
# text2.place(x=100, y=100)
#
# label4 = Label(root, text="Email", bg="black", fg="white", font= "arial 12")
# label4.place(x=10, y=150)
# text3 =Entry(root, width=20, bg="black", font="aria 12")
# text3.place(x=100, y=150)
#
# label5 = Label(root, text="Phone", bg="black", fg="white", font= "arial 12")
# label5.place(x=10, y=200)
# text4 =Entry(root, width=20, bg="black", font="aria 12")
# text4.place(x=100, y=200)
#
# b1=Button(root, text="Cancel", width=10, height=1, bg="red", font="arial 12")
# b1.place(x=10, y=300)
# b1=Button(root, text="Submit", width=10, height=1, font="arial 12")
# b1.place(x=160, y=300)

# root.mainloop()

