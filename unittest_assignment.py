# unittest assigment

class BankAccount:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def _init_(self, account_number, balance, interest_rate):
        super()._init_(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return self.balance


# Write a unit test to check that the deposit() method correctly increases the balance of a bank account.




# Write a unit test to check that the withdraw() method correctly decreases the balance of a bank account and returns "Insufficient funds" when there is not enough money in the account.
# Write a unit test to check that the check_balance() method correctly returns the current balance of a bank account.
# Write a unit test to check that the add_interest() method correctly increases the balance of a savings account by the interest rate.
# Write a unit test to check that the withdraw() method of SavingsAccount correctly calls the parent method and also checks that it does not withdraw more than the min balance and returns "Insufficient funds" when there is not enough money in the account to maintain the minimum balance.
# Write a unit test to check that the withdraw() method raises an exception when the withdrawn amount is greater than the balance and the account is not a savings account.
