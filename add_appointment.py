from tkinter import *
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu


def add_appointment():
    # Retrieve data from entry fields
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    duration = duration_var.get()  # Get the selected duration from the dropdown

    # Validate inputs and display the appointment details
    if name and surname and phone and email and duration:
        appointments_text.insert("end",
                                 f"Appointment:\nName: {name} {surname}\nPhone: {phone}\nEmail: {email}\nDuration: {duration}\n\n")
        clear_fields()
    else:
        message_label.config(text="Please fill out all fields.", foreground="red")


def clear_fields():
    # Clear entry fields
    name_entry.delete(0, 'end')
    surname_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    duration_var.set("30 minutes")  # Reset duration to default


# Create main application window
root = ttk.Window(themename="darkly")
root.title("Appointment Scheduler")

# Add labels and entry widgets for customer details
ttk.Label(root, text="Name:").pack(pady=5)
name_entry = ttk.Entry(root, width=40)
name_entry.pack(pady=5)

ttk.Label(root, text="Surname:").pack(pady=5)
surname_entry = ttk.Entry(root, width=40)
surname_entry.pack(pady=5)

ttk.Label(root, text="Phone:").pack(pady=5)
phone_entry = ttk.Entry(root, width=40)
phone_entry.pack(pady=5)

ttk.Label(root, text="Email:").pack(pady=5)
email_entry = ttk.Entry(root, width=40)
email_entry.pack(pady=5)

# Dropdown menu for appointment duration
ttk.Label(root, text="Appointment Duration:").pack(pady=5)
duration_var = ttk.StringVar(value="30 minutes")  # Default value
duration_dropdown = ttk.Combobox(root, textvariable=duration_var,
                                 values=["30 minutes", "45 minutes", "1 hour", "1.5 hours"], width=37)
duration_dropdown.pack(pady=5)

# Add buttons to create and clear appointments
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Appointment", bootstyle="success", command=add_appointment)
add_button.pack(side=LEFT, padx=5)

clear_button = ttk.Button(button_frame, text="Clear Fields", bootstyle="danger", command=clear_fields)
clear_button.pack(side=LEFT, padx=5)

# Display appointments
ttk.Label(root, text="Appointments:").pack(pady=10)
appointments_text = ttk.Text(root, height=10, width=50, wrap="word")
appointments_text.pack(pady=5)

# Add a message label for feedback
message_label = ttk.Label(root, text="")
message_label.pack(pady=5)

cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=lambda: show_main_menu(content_frame),
        bootstyle="danger",
        width=12
    )
