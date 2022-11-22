'''
    This is an example of a class that violates the Dependency Inversion Principle.
'''
class Store:
    bike_price = 200
    helmet_price = 100
    def __init__(self, username):
        self.stripe = Stripe(username)

    def purchase_bike(self, quantity):
        self.stripe.make_payment(self.bike_price * quantity)

    def purchase_helmet(self, quantity):
        self.stripe.make_payment(self.helmet_price * quantity)


class Stripe:
    def __init__(self, user):
        self.user = user

    def make_payment(self, amount):
        print("Payment made by " + self.user + " of amount $" + str(amount))

# Main code
if __name__ == "__main__":
    store = Store("John")
    store.purchase_bike(2)
    store.purchase_helmet(1)