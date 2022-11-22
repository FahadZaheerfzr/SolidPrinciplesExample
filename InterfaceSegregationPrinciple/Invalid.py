class UserInterface:
    def create_user(self, name: str, email: str, password: str):
        pass

    def delete_user(self, user):
        pass

    def update_user(self, name: str, email: str, password: str):
        pass

    def get_user_details(self):
        pass


class Employee(UserInterface):
    def create_user(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        print("Employee created\n")

    def delete_user(self, user):
        print("User deleted\n")

    def update_user(self, name: str, email: str, password: str):
        print("Employee updated\n")

    def get_user_details(self):
        print("Name: " + self.name + "\nEmail: " +
              self.email + "\nPassword: " + self.password + "\n") 


class Customer(UserInterface):
    def create_user(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        print("Customer created\n")

    def delete_user(self, user):
        raise NotImplementedError("Customers cannot delete\n")

    def update_user(self, name: str, email: str, password: str):
        print("Customer updated\n")

    def get_user_details(self):
        print("Name: " + self.name + "\nEmail: " +
              self.email + "\nPassword: " + self.password + "\n")


# Test code
employee = Employee()
employee.create_user("John", "john@example.com", "123456")
employee.get_user_details()


customerA = Customer()
customerA.create_user("Jane", "jane@example.com", "123456")
customerA.get_user_details()

customerB = Customer()

customerB.create_user("Jack", "jack@example.com", "123456")

try:
    customerB.delete_user(customerA)
except:
    print("Customer cannot delete\n")

employee.delete_user(customerA)

