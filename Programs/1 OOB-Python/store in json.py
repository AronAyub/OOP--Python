import json

class Staff:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.department = ""
        self.office_location = ""
        self.boss_name = ""
        self.working_days = []

    def request_info(self):
        self.name = input("Enter name: ")
        self.salary = float(input("Enter salary: "))
        self.department = input("Enter department: ")
        self.office_location = input("Enter office location: ")
        self.boss_name = input("Enter boss name: ")
        
        working_days_input = input("Enter working days (comma-separated): ")
        self.working_days = [day.strip() for day in working_days_input.split(",")]

    def to_dict(self):
        # Convert employee data to a dictionary
        return {
            "Name": self.name,
            "Salary": self.salary,
            "Department": self.department,
            "Office Location": self.office_location,
            "Boss Name": self.boss_name,
            "Working Days": self.working_days
        }

# Create a list to store employee dictionaries
employee_data = []

# Input the number of employees you want to add
num_employees = int(input("Enter the number of employees: "))

# Request details for each employee
for _ in range(num_employees):
    employee = Staff()
    employee.request_info()
    employee_dict = employee.to_dict()
    employee_data.append(employee_dict)
    
    # Display information for the current employee
    print("\nEmployee Details:")
    for key, value in employee_dict.items():
        print(f"{key}: {value}")

# Save employee data to a JSON file named "Employee.json"
with open("Employee.json", "w") as json_file:
    json.dump(employee_data, json_file, indent=4)

print("Employee data displayed in the terminal and stored in 'Employee.json'.")
