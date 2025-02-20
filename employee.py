class Employee:
    employee = {}
    def __init__(self, employee_id, name, age, gender, department, salary, role):
        self.id = int(employee_id)
        self.name = name.strip().title()
        self.age = int(age)
        self.gender = gender.strip().lower()
        self.department = department.strip().title()
        self.salary = int(salary)
        self.role = role.strip().title()

    def add_employee(self):
        Employee.employee[self.id] = {
            "name":self.name,
            "age": self.age,
            "gender": self.gender,
            "department": self.department,
            "salary": self.salary,
            "role": self.role
        }

        print(f"{self.name} of ID: {self.id} added succesfully")
    @classmethod
    def view_employee(cls, employee_id = None):
        if employee_id:
            if employee_id in Employee.employee:
                employee = Employee.employee[cls.id]
                print(f"---------Employee Information---------\nID: {employee_id}\n Name: {employee["name"]}\nAge: {employee["age"]}\nGender: {employee["gender"]}\nDepartment: {employee["department"]}\nSalary: {employee["salary"]}\nRole: {employee["role"]}")
            else:
                print("Student ID not found")


        else:
            for id, employee in cls.employee.items():
                print( f"ID: {id}\nName: {employee["name"]}\nAge: {employee["age"]}\nGender: {employee["gender"]}\nDepartment: {employee["department"]}\nSalary: {employee["salary"]}\nRole: {employee["role"]}")

    @classmethod
    def update_employees(cls, employee_id,  name = None, age = None, gender = None, department = None, salary = None, role = None ):
        if employee_id in cls.employee:
            if name:
                cls.employee[employee_id]["name"] = name
            if age:
                 cls.employee[employee_id]["age"] = age
            if gender:
                 cls.employee[employee_id]["gender"] = gender
            if department:
                 cls.employee[employee_id]["department"] = department
            if salary:
                 cls.employee[employee_id]["salary"] = salary
            if role:
                 cls.employee[employee_id]["role"] = role
        else:
            print("Failed! Student ID not found")
    @classmethod
    def delete_employee(cls, employee_id):
        if employee_id in cls.employee:
            del cls.employee[employee_id]
            print(f"Employee {employee_id} has been deleted")
        else:
            print("Failed! Student ID not found")


while True:
    try:
        print("-------------WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM-------------")
        print("Please select an option to continue:\n1. Add Employee\n2. View all employees Details\n3. View an employee's info\n4. Update Employee's detail\n5. Delete an Employee\n6. Exit")
        option = int(input("Enter your option between 1 & 6: "))
        if option ==1:
            employee_id = int(input("Enter the employee's ID: "))
            name = input("Enter the employee's name: ").strip().capitalize()
            age = int(input("Enter the employee's age: "))
            gender = input("Enter the employee's gender: ").strip().lower()
            department = input("Enter the employee's department: ").strip().capitalize()
            salary = int(input("Enter employee's salary"))
            role = input("Enter the employee's role").strip().capitalize()

            x = Employee(employee_id,name,age,gender,department,salary,role)
            x.add_employee()
            
        elif option == 2:
            Employee.view_employee()

        elif option == 3:
            employee_id = int(input("Enter the employee's ID, to view their specific details"))
            Employee.view_employee(employee_id=employee_id)

        elif option == 4:
            employee_id = int(input("Enter the employee's details to update their details"))
            choice = int(input("Enter the field to change: 1. Name, 2.Age, 3. gender, 4. department 5. salary, 6. role"))
            if choice == 1:
                name = input("Enter the updated name")
                Employee.update_employees(employee_id, name=name)
            elif choice ==2:
                age = int(input("Enter the updated age"))
                Employee.update_employees(employee_id, age=age)

            elif choice == 3:
                gender = input("Enter the updated employee's gender").strip().title()
                Employee.update_employees(employee_id, gender = gender)
            elif choice == 4:
                department = input("Enter the updated empoyee's department").strip().title()
                Employee.update_employees(employee_id, department=department)
            elif choice == 5:
                salary = int(input("Enter the updated employee's salary"))
                Employee.update_employees(employee_id, salary=salary)
            elif choice ==6:
                role = input("Enter the updated employee's role")
                Employee.update_employees(employee_id, role=role)
            else:
                print("Invalid choice entered")

        elif option == 5:
            employee_id = int(input("Enter the employee's ID to be deleted"))
            Employee.delete_employee(employee_id=employee_id)

        elif option == 6:
            print("Exiting the system goodbye")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid choice entered")