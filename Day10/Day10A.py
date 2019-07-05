"""This module is for calculate Employee salary"""
class Employee:
    """This is class Employee
Hello world"""
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d"%Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name, "Salary:",self.salary)

if __name__ == '__main__':
    emp1=Employee("Nikhil",9999)
    emp1.displayEmployee()
    print("Is salary an attribute:",hasattr(emp1,'salary'))
    print(getattr(emp1,'salary'))
    setattr(emp1,'salary',7000)
    print("Modified salary",getattr(emp1,'salary'))
    print(hasattr(emp1,'desg'))
    setattr(emp1,'desg','manager')
    print(hasattr(emp1,'desg'))
    print("Added Attribute",getattr(emp1,'desg'))
    delattr(emp1,'salary')
    print("Is salary an attribute:",hasattr(emp1,'salary'))
