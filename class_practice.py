class Circle_practice:
    def __init__(self, radius):
        self.radius = radius
    
    def area():
        return self.radius
    
    @circumference

    def circumference():

        return self.radius
    

class Circle:
    ## attribute as parameter
    def __init__(self, radius):
        ## assgin the value of radius to radius
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


class BankAccount:
    def __init__(self, account_number, balance=0):
        ## if we have any attribute, do this
        self.account_number = account_number
        self.balance = balance

    ## if we need to use attribute, do this
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        # how to use atrributes
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

