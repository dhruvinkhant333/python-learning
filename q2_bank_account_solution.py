# ============================================================================
# QUESTION 2: Create a Bank Account with Closure - SOLUTION
# ============================================================================
# Create a closure that tracks a bank account balance
# The function should return functions: deposit(), withdraw(), and balance()

# 📚 CONCEPT: Using Closures for Private State
# ============================================================================
print("=" * 70)
print("QUESTION 2: Bank Account with Closure")
print("=" * 70)
print("""
Closures are perfect for creating "private" variables that can only be
accessed through specific functions. This is like object-oriented programming,
but without needing a class!
""")


# ❌ NAIVE ATTEMPT - Without Closure (Problem)
# ============================================================================
print("\n❌ NAIVE: Global Variables (BAD Practice)")
print("-" * 70)

balance_global = 0  # ← This is exposed and can be changed anywhere!

def deposit_global(amount):
    global balance_global
    balance_global += amount

def withdraw_global(amount):
    global balance_global
    balance_global -= amount

print("Problem: balance_global is accessible from anywhere!")
print(f"balance_global = {balance_global}")
balance_global = 999  # ← Someone can cheat and change it directly!
print(f"Someone changed it to: {balance_global}")
print("This is not safe or encapsulated!\n")


# ✅ SOLUTION: Bank Account with Closure
# ============================================================================
print("\n✅ SOLUTION: Closure-Based Bank Account")
print("-" * 70)

def create_bank_account(initial_balance):
    """
    Creates a bank account using closure for private state management.
    
    Args:
        initial_balance: Starting account balance
    
    Returns:
        Dictionary with methods: 'deposit', 'withdraw', 'balance', 'get_history'
    """
    # Private variable - only accessible within this function's scope
    balance = initial_balance
    transaction_history = []
    
    def deposit(amount):
        """Add money to account"""
        nonlocal balance  # Modify the outer scope's balance variable
        if amount <= 0:
            print(f"❌ Cannot deposit ${amount}. Amount must be positive!")
            return False
        balance += amount
        transaction_history.append(f"Deposit: +${amount}")
        print(f"✅ Deposited ${amount}. New balance: ${balance}")
        return True
    
    def withdraw(amount):
        """Remove money from account"""
        nonlocal balance
        if amount <= 0:
            print(f"❌ Cannot withdraw ${amount}. Amount must be positive!")
            return False
        if amount > balance:
            print(f"❌ Insufficient funds! Balance: ${balance}, Requested: ${amount}")
            return False
        balance -= amount
        transaction_history.append(f"Withdraw: -${amount}")
        print(f"✅ Withdrew ${amount}. New balance: ${balance}")
        return True
    
    def get_balance():
        """Get current balance"""
        return balance
    
    def get_history():
        """Get transaction history"""
        return transaction_history.copy()
    
    # Return dictionary of methods
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance,
        'history': get_history
    }


# TEST 1: Basic Operations
# ============================================================================
print("\n📝 TEST 1: Basic Operations")
print("-" * 70)

account = create_bank_account(100)
print(f"Initial balance: ${account['balance']()}")

account['deposit'](50)
print(f"Current balance: ${account['balance']()}")

account['withdraw'](30)
print(f"Current balance: ${account['balance']()}")

print(f"\nTransaction history: {account['history']()}")


# TEST 2: Error Handling
# ============================================================================
print("\n\n📝 TEST 2: Error Handling")
print("-" * 70)

account2 = create_bank_account(100)
print(f"Initial balance: ${account2['balance']()}\n")

# Try to withdraw more than available
account2['withdraw'](200)

# Try negative deposit
account2['deposit'](-50)

# Try negative withdrawal
account2['withdraw'](-10)

print(f"\nFinal balance: ${account2['balance']()}")


# TEST 3: Multiple Accounts (Separate Closures)
# ============================================================================
print("\n\n📝 TEST 3: Multiple Accounts - Each has Own Closure")
print("-" * 70)

alice_account = create_bank_account(500)
bob_account = create_bank_account(1000)

print(f"Alice's balance: ${alice_account['balance']()}")
print(f"Bob's balance: ${bob_account['balance']()}\n")

alice_account['deposit'](200)
print(f"Alice's balance after deposit: ${alice_account['balance']()}")
print(f"Bob's balance (unchanged): ${bob_account['balance']()}\n")

bob_account['withdraw'](300)
print(f"Bob's balance after withdrawal: ${bob_account['balance']()}")
print(f"Alice's balance (unchanged): ${alice_account['balance']()}")


# TEST 4: Can't Access Private Balance Directly
# ============================================================================
print("\n\n📝 TEST 4: Encapsulation - Private State")
print("-" * 70)

account3 = create_bank_account(100)
print(f"Balance through method: ${account3['balance']()}")
print("\nTrying to access 'balance' variable directly:")
print(f"account3.balance exists? {hasattr(account3, 'balance')}")
print(f"account3['balance'] is callable? {callable(account3['balance'])}")
print("\n✅ The balance variable is truly private!")
print("   It can ONLY be accessed through the provided methods.")


# 🎓 ALTERNATIVE: Using a Class (Comparison)
# ============================================================================
print("\n\n🎓 ALTERNATIVE: Using a Class (Object-Oriented Approach)")
print("-" * 70)

class BankAccount:
    """Class-based approach for comparison"""
    
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            print(f"❌ Cannot deposit ${amount}. Amount must be positive!")
            return False
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        print(f"✅ Deposited ${amount}. New balance: ${self.balance}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print(f"❌ Cannot withdraw ${amount}. Amount must be positive!")
            return False
        if amount > self.balance:
            print(f"❌ Insufficient funds! Balance: ${self.balance}, Requested: ${amount}")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdraw: -${amount}")
        print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")
        return True

print("\nClass-based example:")
class_account = BankAccount(100)
print(f"Initial balance: ${class_account.balance}")
class_account.deposit(50)
print(f"Final balance: ${class_account.balance}")


# ============================================================================
# KEY LESSONS & COMPARISON
# ============================================================================
print("\n\n" + "=" * 70)
print("KEY LESSONS & COMPARISON")
print("=" * 70)
print("""
CLOSURE APPROACH:
✅ Private state - balance cannot be accessed directly
✅ Lightweight - no class overhead
✅ Functional style - uses functions, not objects
❌ Less familiar to OOP developers
❌ Can't easily add new methods later

CLASS APPROACH:
✅ More familiar OOP pattern
✅ Easy to extend with inheritance
✅ Better for complex behavior
❌ Balance is technically accessible (not truly private)
❌ More overhead for simple use cases

WHEN TO USE CLOSURES:
- Simple state management
- Factory functions
- Callbacks and event handlers
- Functional programming style
- When you want true encapsulation

WHEN TO USE CLASSES:
- Complex object behavior
- Inheritance hierarchies
- Multiple related methods
- Object-oriented design patterns
""")

print("\n" + "=" * 70)
print("WHAT IS 'nonlocal'?")
print("=" * 70)
print("""
In Python, you need 'nonlocal' to MODIFY variables from outer scopes.

WITHOUT nonlocal:
    balance += amount  # Creates a NEW local variable, doesn't modify outer

WITH nonlocal:
    nonlocal balance   # Says "use the balance from the outer scope"
    balance += amount  # Now modifies the OUTER balance

Note: You DON'T need nonlocal just to READ outer variables, only to MODIFY them!
""")
