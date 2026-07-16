# 4. Title: The Overdraft Guardian
# Difficulty: Core
# Topics Used: OOP, Exception Handling
# Problem Statement: Design a BankAccount class supporting deposit and withdraw operations. Withdrawals that exceed the balance should raise a custom exception rather than silently failing or returning an error code, and deposits of non-positive amounts should raise a different custom exception.
# Input: deposit(1000), withdraw(1500), withdraw(-50)
# Output: Deposit succeeds; withdraw raises an "insufficient funds" style exception; the negative withdraw raises a separate validation exception.
# Constraints: Balance must never go negative under any code path.
# Logic Trigger: Try separating "is this operation valid" from "perform this operation."

# ---------------------------------------------------------------------------- #
#                                   Sulution                                   #
# ---------------------------------------------------------------------------- #


class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"Deposited ₹{amount}")
        print(f"Balance = ₹{self.balance}")

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")

        self.balance -= amount

        print(f"Withdrawn ₹{amount}")
        print(f"Balance = ₹{self.balance}")

account = BankAccount()

try:

    account.deposit(1000)

    account.withdraw(1500)

    account.withdraw(-50)

except InvalidAmountError as e:
    print("Validation Error:", e)

except InsufficientFundsError as e:
    print("Bank Error:", e)