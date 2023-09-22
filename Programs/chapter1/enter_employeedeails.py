#requesting for details 

class Staff:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.department = ""
        self.office_location = ""
        self.boss_name = ""
        self.year_experice = 0.0
        self.working_days = []

    def request_info(self):
        self.name = input("Enter name: ")
        self.salary = float(input("Enter salary: "))
        self.department = input("Enter department: ")
        self.office_location = input("Enter office location: ")
        self.boss_name = input("Enter boss name: ")
        self.year_experice = input("Enter the years of experience: ")
        working_days_input = input("Enter working days (comma-separated): ")
        self.working_days = [day.strip() for day in working_days_input.split(",")]

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print(f"Office Location: {self.office_location}")
        print(f"Boss Name: {self.boss_name}")


# Create a list to store employee objects
employees = []

# Input the number of employees you want to add
num_employees = int(input("Enter the number of employees: "))

# Request details for each employee
for _ in range(num_employees):
    employee = Staff()
    employee.request_info()
    employees.append(employee)

# Display information for all employees
for i, employee in enumerate(employees, start=1):
    print(f"\nEmployee {i} Details:")
    employee.display_info()
