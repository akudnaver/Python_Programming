class Account:
    def __init__(self, acc_number, owner, balance=0.0):
        self.acc_number = acc_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print(f"Deposited {amount}. New Balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrawl {amount}. New balance is {self.balance}")
        elif amount > self.balance:
            print("Insufficient Funds")
        else:
            print("Withdrawl amount must be positive")



    def get_balance(self):
        return self.balance
    

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, owner):
        if acc_number not in self.accounts:
            self.accounts[acc_number] = Account(acc_number, owner)
            print(f"Account {acc_number} created for {owner}")

        else:
            print("Account number already exisit")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


def main():
    bank = Bank()
    bank.create_account('123', 'Alice')
    bank.create_account('456', 'Bob')

    account = bank.get_account('123')
    if account:
        account.deposit(100)
        account.withdraw(50)
        print(f"Balance for account 123: {account.get_balance()}")

    account = bank.get_account('456')
    if account:
        account.deposit(400)
        account.withdraw(150)
        print(f"Balance for account 456: {account.get_balance()}")


if __name__ == "__main__":
    main()