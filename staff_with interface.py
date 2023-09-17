import tkinter as tk
from tkinter import ttk
import json

class Staff:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.department = ""
        self.office_location = ""
        self.boss_name = ""
        self.working_days = []

def save_employee():
    employee = Staff()
    employee.name = name_entry.get()
    employee.salary = float(salary_entry.get())
    employee.department = department_entry.get()
    employee.office_location = office_location_entry.get()
    employee.boss_name = boss_name_entry.get()
    employee.working_days = [day.strip() for day in working_days_entry.get().split(",")]

    employee_dict = employee.__dict__
    employee_data.append(employee_dict)
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    office_location_entry.delete(0, tk.END)
    boss_name_entry.delete(0, tk.END)
    working_days_entry.delete(0, tk.END)

def save_to_json():
    with open("Employee.json", "w") as json_file:
        json.dump(employee_data, json_file, indent=4)
    print("Employee data saved to 'Employee.json'.")

# Create a list to store employee dictionaries
employee_data = []

# Create the main window
root = tk.Tk()
root.title("Employee Details")
root.geometry("400x400")

# Create a blue-themed style
style = ttk.Style()
style.configure("TButton", foreground="white", background="blue")
style.configure("TLabel", foreground="blue")

# Create a label for the welcome message
welcome_label = ttk.Label(root, text="Welcome to Employee Logger", font=("Helvetica", 12, "bold"))
welcome_label.pack()

# Create labels and entry fields for employee details
name_label = ttk.Label(root, text="Name:")
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()

salary_label = ttk.Label(root, text="Salary:")
salary_label.pack()
salary_entry = ttk.Entry(root)
salary_entry.pack()

department_label = ttk.Label(root, text="Department:")
department_label.pack()
department_entry = ttk.Entry(root)
department_entry.pack()

office_location_label = ttk.Label(root, text="Office Location:")
office_location_label.pack()
office_location_entry = ttk.Entry(root)
office_location_entry.pack()

boss_name_label = ttk.Label(root, text="Boss Name:")
boss_name_label.pack()
boss_name_entry = ttk.Entry(root)
boss_name_entry.pack()

working_days_label = ttk.Label(root, text="Working Days (comma-separated):")
working_days_label.pack()
working_days_entry = ttk.Entry(root)
working_days_entry.pack()

# Create a "Save Employee" button
save_button = ttk.Button(root, text="Save Employee", command=save_employee)
save_button.pack()

# Create a "Save to JSON" button
save_to_json_button = ttk.Button(root, text="Save to JSON", command=save_to_json)
save_to_json_button.pack()

#creator Copyright
creator_label = ttk.Label(root, text= "c Aron Ayub",  font=("Helvetica", 9, "bold"))
creator_label.pack()

# Start the Tkinter main loop
root.mainloop()
