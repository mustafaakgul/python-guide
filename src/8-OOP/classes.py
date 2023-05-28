class Employee:
    emp_count = 0
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        Employee.emp_count += 1

    def display_count(self):
        print(f"Total Employee {Employee.emp_count}")

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Age: {self.age}")

emp1 = Employee("Mustafa", "asda@gmail.com", "25")
print(Employee.emp_count)
emp1.age = 26
print(emp1.age)

# Changing class attributes
print(getattr(emp1, "age"))
print(hasattr(emp1, "age"))
print(setattr(emp1, "age"))

# Built-in class attributes
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)