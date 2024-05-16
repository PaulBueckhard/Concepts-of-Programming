class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Public method to get the name
    def get_name(self):
        return self.__name

    # Public method to set the name
    def set_name(self, name):
        self.__name = name

    # Public method to get the salary
    def get_salary(self):
        return self.__salary

    # Public method to set the salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")

if __name__ == "__main__":
    emp = Employee("John Doe", 50000)
    
    # Accessing private attributes via public methods
    print("Employee Name:", emp.get_name())
    print("Employee Salary:", emp.get_salary())

    # Modifying private attributes via public methods
    emp.set_name("Jane Doe")
    emp.set_salary(55000)
    
    print("Updated Employee Name:", emp.get_name())
    print("Updated Employee Salary:", emp.get_salary())
    
    # Attempt to directly access private attribute (will raise an AttributeError)
    # print(emp.__name)
