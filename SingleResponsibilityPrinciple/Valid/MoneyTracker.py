from Logger import Logger

class MoneyTracker:
    def __init__(self, max_amount):
        self.amount = 0
        self.max_amount = max_amount
        self.logger = Logger()
    

    def deposit_money(self, deposit):
        if (deposit < 0):
            self.logger.log_message("Invalid deposit amount")
        elif (deposit > self.max_amount):
            self.logger.log_message("Deposit amount exceeds max amount")
        else:
            self.amount += deposit
            self.logger.log_message("Amount Deposited")
            


myTracker = MoneyTracker(10000)
myTracker.deposit_money(1000)
myTracker.deposit_money(-1000)
myTracker.deposit_money(100000)