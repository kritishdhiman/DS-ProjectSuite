employee_data = {}

def main_menu():
    while True:
        print("\nEmployee Management Menu")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")

def add_employee():
    print("\nAdd New Employee")

    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employee_data:
                print("This Employee ID already exists. Please enter a different ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric Employee ID.")

    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        employee_data[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }

        print("Employee added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter correct data types.\n")

def view_employees():
    print("\nAll Employees")

    if not employee_data:
        print("No employees available.\n")
        return
    
    print("{:<10} {:<15} {:<5} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)

    for emp_id, details in employee_data.items():
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
            emp_id,
            details["name"],
            details["age"],
            details["department"],
            details["salary"]
        ))
    print()

def search_employee():
    print("\nSearch for an Employee")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employee_data:
            details = employee_data[emp_id]
            print("\nEmployee Details")
            print(f"ID        : {emp_id}")
            print(f"Name      : {details['name']}")
            print(f"Age       : {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary    : {details['salary']}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.\n")

main_menu()