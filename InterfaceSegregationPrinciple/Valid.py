class UserInterface:
    def create_user(self, name: str, email: str, password: str):
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

    def update_user(self, name: str, email: str, password: str):
        print("Employee updated\n")

    def get_user_details(self):
        print("Name: " + self.name + "\nEmail: " +
              self.email + "\nPassword: " + self.password + "\n") 

    def delete_user(user):
        print("User deleted\n")

class Customer(UserInterface):
    def create_user(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        print("Customer created\n")

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


employee.delete_user(customerA)

