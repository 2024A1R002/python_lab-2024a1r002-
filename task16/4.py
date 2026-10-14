# create a bank account class that stores an account holder's name and balance . add instance methods to deposit money, withdraw money, and display the balance. do not allow a  withdraw greater than the available balance
class Bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: {self.balance}")

name = input("Enter account holder's name: ")
balance = float(input("Enter initial balance: "))
account = Bankaccount(name, balance)
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display()