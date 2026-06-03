# Parent class
class Employee:
    def work(self):
        print("Employee working")

# Child class inheriting from Employee
class Manager(Employee):
    def manage(self):
        print("Managing team")


# Example usage
emp = Employee()
emp.work()

mgr = Manager()
mgr.work()      # inherited method
mgr.manage()    # child class method
