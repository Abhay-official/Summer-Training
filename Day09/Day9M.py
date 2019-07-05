class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' %Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)

emp1 = Employee('Nikhil', 9999)
emp1.displayEmployee()
emp1.salary = 17000
emp1.experience = 3
emp1.displayEmployee()
emp1.name = 'Manoj'
emp1.displayEmployee()
print(print(emp1.experience))
emp1.displayEmployee()
   
