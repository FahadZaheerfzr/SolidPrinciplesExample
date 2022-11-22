'''
    This is an example of class that follows the Dependency Inversion Principle.
'''
class Stripe:
    def __init__(self, user):
        self.user = user

    def make_payment(self, amount):
        print("Payment made by " + self.user + " of amount $" + str(amount))


class StripePaymentProcessor:
    def __init__(self, username):
        self.stripe = Stripe(username)

    def pay(self, amount):
        self.stripe.make_payment(amount)


class Store:
    bike_price = 200
    helmet_price = 100
    
    def __init__(self, payment_processor:StripePaymentProcessor):
        self.payment_processor = payment_processor

    def purchase_bike(self, quantity):
        self.payment_processor.pay(self.bike_price * quantity)

    def purchase_helmet(self, quantity):
        self.payment_processor.pay(self.helmet_price * quantity)


# Main code
if __name__ == "__main__":
    store = Store(StripePaymentProcessor("Ahmed"))
    store.purchase_bike(2)
    store.purchase_helmet(1)