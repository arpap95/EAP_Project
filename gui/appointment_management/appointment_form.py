import tkinter as tk
import ttkbootstrap as ttk
from gui.main_menu import show_main_menu

def appointment_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

        customer_name = name_entry.get()
        appointment_date = date_entry.get()
        appointment_time = time_entry.get()
        appointment_duration = duration_entry.get()

        if not customer_name or not appointment_date or not appointment_time:
            messagebox.showerror("Error", "All fields except duration are required!")
            return

        # Display confirmation message
        messagebox.showinfo(
            "Appointment Saved",
            f"Appointment for {customer_name} on {appointment_date} at {appointment_time} "
            f"for {appointment_duration} minutes has been saved."
        )

    # Create the main window
    root = tk.Tk()
    root.title("Create Appointment")

    # Customer Name
    tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Appointment Date
    tk.Label(root, text="Appointment Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    date_entry = tk.Entry(root, width=30)
    date_entry.grid(row=1, column=1, padx=10, pady=5)

    # Appointment Time
    tk.Label(root, text="Appointment Time (HH:MM):").grid(row=2, column=0, padx=10, pady=5)
    time_entry = tk.Entry(root, width=30)
    time_entry.grid(row=2, column=1, padx=10, pady=5)

    # Appointment Duration
    tk.Label(root, text="Duration (minutes, default 30):").grid(row=3, column=0, padx=10, pady=5)
    duration_entry = tk.Entry(root, width=30)
    duration_entry.insert(0, "30")  # Default value
    duration_entry.grid(row=3, column=1, padx=10, pady=5)

    # Save Button
    save_button = tk.Button(root, text="Save Appointment", command=save_appointment)
    save_button.grid(row=4, column=0, columnspan=2, pady=20)

    # Run the application
    root.mainloop()

    # Buttons
    button_container = ttk.Frame(form_frame)
    button_container.pack(fill='x', expand=True, pady=(15, 10))

    def on_submit():
        print("Όνομα:", name.get())
        print("Επώνυμο:", lastname.get())
        print("Τηλέφωνο:", phone.get())
        print("Email:", email.get())
        show_main_menu(content_frame)

    cancel_btn = ttk.Button(
        master=button_container,
        text="Ακύρωση",
        command=lambda: show_main_menu(content_frame)
    )
    cancel_btn.pack(side='right', padx=5)

    submit_btn = ttk.Button(
        master=button_container,
        text="Προσθήκη",
        command=on_submit
    )
    submit_btn.pack(side='right', padx=5)
    submit_btn.focus_set()