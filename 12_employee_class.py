
class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


e1 = Employee("Rahul", 25000)
e2 = Employee("Priya", 30000)
e3 = Employee("Amit", 28000)

e1.display()
e2.display()
e3.display()

print("Total Employee Objects:", Employee.count)
