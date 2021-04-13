class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def withdraw(self, money1):
        self.balance -= money1
        if money1 > self.balance:
            raise ValueError
        else:
            return f'{self.name} has {self.balance}.'
    
    def check(self, other, money2):
        if money2 > other.balance:
            raise ValueError
        elif other.checking_account != True:
            raise ValueError
        else:
            other.balance -= money2
            self.balance += money2
            return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'
    def add_cash(self, added_money):
        self.balance += added_money
        return f'{self.name} has {self.balance}.'