#**
#***************************************************************************
#*   @file        : project.py
#*   @author      : Mohamed Montasser
#*   @brief       : Contains the functionality of my application
#*   @title       : Employee Data Management System
#***************************************************************************
#*/

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

# Create a list to store employee data
employees = []

# Function to add an employee to the list
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    employee = Employee(emp_id, name, salary)
    employees.append(employee)
    print(f"Employee {name} added successfully!")

# Function to display all employees
def display_employees():
    if not employees:
        print("No employees to display.")
    else:
        print("Employee List:")
        for employee in employees:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Salary: {employee.salary}")

# Function to save employee data to a file
def save_data():
    try:
        with open("employee_data.txt", "w") as file:
            for employee in employees:
                file.write(f"{employee.emp_id},{employee.name},{employee.salary}\n")
        print("Employee data saved to file successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Function to load employee data from a file
def load_data():
    try:
        with open("employee_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                emp_id, name, salary = line.strip().split(",")
                employee = Employee(emp_id, name, float(salary))
                employees.append(employee)
        print("Employee data loaded from file successfully!")
    except FileNotFoundError:
        print("File 'employee_data.txt' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Function to edit employee data
def edit_employee():
    emp_id = input("Enter the Employee ID to edit: ")
    for employee in employees:
        if employee.emp_id == emp_id:
            print(f"Editing Employee: {employee.emp_id}, Name: {employee.name}, Salary: {employee.salary}")

            # Update fields with user input or keep them unchanged
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_salary = input("Enter new salary (leave blank to keep current): ").strip()

            if new_name:
                employee.name = new_name
            if new_salary:
                try:
                    employee.salary = float(new_salary)
                except ValueError:
                    print("Invalid salary input. Keeping the current salary.")

            print(f"Employee {employee.emp_id} updated successfully!")
            return

    print("Employee not found.")

# Function to delete employee data
def delete_employee():
    emp_id = input("Enter the Employee ID to delete: ")
    for employee in employees:
        if employee.emp_id == emp_id:
            employees.remove(employee)
            print(f"Employee {employee.name} with ID {employee.emp_id} has been deleted.")
            return
    print("Employee not found.")

# Function to search employee data
def search_employee():
    emp_id = input("Enter the Employee ID to search: ")
    for employee in employees:
        if employee.emp_id == emp_id:
            print(f"Employee Found: ID: {employee.emp_id}, Name: {employee.name}, Salary: {employee.salary}")
            return
    print("Employee not found.")


# Main program loop
while True:
    print("\nEmployee Data Management System")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Save Data to File")
    print("7. Load Data from File")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        display_employees()
        edit_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        display_employees()
        delete_employee()
    elif choice == "6":
        save_data()
    elif choice == "7":
        load_data()
    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")


# Copyright 2024 by Mohamed Montasser.
# All rights reserved.
