class Employee:
    total_employees = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total_employees += 1
        self.employee_number = self.total_employees

    def print_info(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

class HourlyPaid(Employee):
    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay=hourly_pay
        #goi init cua cha, lay ho ten cua employee tu class Employee
        super().__init__(first_name, last_name)
    def print_info(self):
        #goi ham print ho ten cua Cha
        super().print_info()
        #sau do, in them cai gi minh muon (hourly pay)
        print(f"Hourly pay: {self.hourly_pay}")


class MonthlyPaid(Employee):
    def __init__(self,first_name, last_name, monthly_pay):
        self.monthly_pay=monthly_pay
        super().__init__(first_name, last_name)
    def print_info(self):
        super().print_info()
        print(f"Monthly pay: {self.monthly_pay}")

employees = []
employee1 = Employee ("Mia", "Le")
employee2 = HourlyPaid("John","Jo",2250)
employee3 = MonthlyPaid ("An","Minh", 4500)
employees.append(employee1)
employees.append(employee2)
employees.append(employee3)

for employee in employees:
    #call print method (action) in each object employee created from Employee class
    employee.print_info()

