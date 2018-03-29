#An ATM is able to store cash
#The users will be able to use the ATM to do the following:
    #Withdraw none
    #Transfer money
    #Check balance
    #Add balance
#Problem
    #Farhan has 3.500.000 of initial balance
    #His mother transferred 3.200.000 to his account
    #Farhan purchased a compact camera for 2.750.000
    #Farhan bought lunch at SENCI for 75.000
    #Then he withdraw 300.000
    #How much money Farhan left from all those transaction

class ATM:


    def __init__(self, balance=3500000):
        self.balance = balance


    def add(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount > self.balance:
            return 'There is not enough money in your account'
        else:
            self.balance -= amount


    def check_balance(self):
        return self.balance

money = ATM()
money.add(3200000)
money.withdraw(2750000)
money.withdraw(75000)
money.withdraw(300000)
print("Money left: ", money.check_balance())
