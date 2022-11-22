class MoneyTracker:
    def __init__(self, max_amount):
        self.amount = 0
        self.max_amount = max_amount
    

    def deposit_money(self, deposit):
        if (deposit < 0):
            self.logging_function("Invalid deposit amount")
        elif (deposit > self.max_amount):
            self.logging_function("Deposit amount exceeds max amount")
        else:
            self.amount += deposit
            self.logging_function("Amount Deposited")
    
    def logging_function(self, msg):
        print(msg)

myTracker = MoneyTracker(10000)
myTracker.deposit_money(1000)
myTracker.deposit_money(-1000)
myTracker.deposit_money(100000)