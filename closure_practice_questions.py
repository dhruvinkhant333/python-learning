# ============================================================================
# CLOSURE & LATE BINDING - PRACTICE QUESTIONS
# ============================================================================
# Solve these problems to master closures!

# ============================================================================
# QUESTION 1: Fix the Late Binding Bug
# ============================================================================
# This function should create multiplier functions (×2, ×3, ×4)
# But it has a late binding bug. Fix it!

def create_multipliers_broken():
    multipliers = []
    for i in range(2, 5):
        def multiply(x):
            return x * i  # ← BUG: late binding issue
        multipliers.append(multiply)
    return multipliers

# TODO: Rewrite this function to fix the bug
def create_multipliers_fixed():
    # YOUR CODE HERE
    pass

# Test it
# times_2, times_3, times_4 = create_multipliers_fixed()
# print(f"times_2(5) should be 10: {times_2(5)}")
# print(f"times_3(5) should be 15: {times_3(5)}")
# print(f"times_4(5) should be 20: {times_4(5)}")


# ============================================================================
# QUESTION 2: Create a Bank Account with Closure
# ============================================================================
# Create a closure that tracks a bank account balance
# The function should return two functions: deposit() and withdraw()

def create_bank_account(initial_balance):
    """
    Returns a dictionary with 'deposit' and 'withdraw' functions
    that share the same balance variable (closure)
    """
    # YOUR CODE HERE
    pass

# Test it
# account = create_bank_account(100)
# print(f"Initial balance: {account['balance']()}")  # Should print 100
# account['deposit'](50)
# print(f"After deposit 50: {account['balance']()}")  # Should print 150
# account['withdraw'](30)
# print(f"After withdraw 30: {account['balance']()}")  # Should print 120


# ============================================================================
# QUESTION 3: Event Handler with Loop (Tricky!)
# ============================================================================
# This simulates a common web development problem

def setup_buttons_broken():
    """
    Creates 3 buttons. When clicked, each should print its button number
    But this code has a closure bug!
    """
    buttons = []
    for button_id in range(1, 4):
        def on_click():
            print(f"Button {button_id} clicked!")  # ← BUG HERE
        buttons.append(on_click)
    return buttons

# TODO: Create a fixed version
def setup_buttons_fixed():
    # YOUR CODE HERE
    pass

# Test it
# buttons = setup_buttons_fixed()
# buttons[0]()  # Should print "Button 1 clicked!"
# buttons[1]()  # Should print "Button 2 clicked!"
# buttons[2]()  # Should print "Button 3 clicked!"


# ============================================================================
# QUESTION 4: Create a Counter with Closure
# ============================================================================
# Create a function that returns a counter object with:
# - increment() - adds 1 to counter
# - decrement() - subtracts 1 from counter
# - get_count() - returns current count

def create_counter():
    """
    Returns a dictionary with methods to manage a counter
    """
    # YOUR CODE HERE
    pass

# Test it
# counter = create_counter()
# counter['increment']()
# counter['increment']()
# print(f"Count after 2 increments: {counter['get_count']()}")  # Should be 2
# counter['decrement']()
# print(f"Count after 1 decrement: {counter['get_count']()}")  # Should be 1


# ============================================================================
# QUESTION 5: Function Factory
# ============================================================================
# Create a function that makes custom adder functions

def make_adder(x):
    """
    Takes a number x and returns a function that adds x to any number
    Example: add_5 = make_adder(5)
             add_5(3) returns 8
    """
    # YOUR CODE HERE
    pass

# Test it
# add_10 = make_adder(10)
# add_100 = make_adder(100)
# print(f"add_10(5) should be 15: {add_10(5)}")
# print(f"add_100(5) should be 105: {add_100(5)}")


# ============================================================================
# QUESTION 6: Nested Closures
# ============================================================================
# Create a function that creates a function that creates a function!

def outer(a):
    """
    outer creates a middle function that takes b
    middle creates an inner function that takes c
    inner returns a + b + c
    """
    # YOUR CODE HERE
    pass

# Test it
# result = outer(1)(2)(3)  # Should be 1 + 2 + 3 = 6
# print(f"outer(1)(2)(3) should be 6: {result}")


# ============================================================================
# QUESTION 7: Configuration Manager
# ============================================================================
# Create a closure that manages application configuration

def create_config_manager():
    """
    Returns a dictionary with:
    - set_config(key, value) - sets a config value
    - get_config(key) - gets a config value
    - reset() - clears all config
    """
    # YOUR CODE HERE
    pass

# Test it
# config = create_config_manager()
# config['set_config']('theme', 'dark')
# config['set_config']('language', 'en')
# print(f"Theme: {config['get_config']('theme')}")  # Should be 'dark'
# print(f"Language: {config['get_config']('language')}")  # Should be 'en'


# ============================================================================
# QUESTION 8: Memoization (Caching with Closure)
# ============================================================================
# Create a function that caches results

def create_fibonacci_memoized():
    """
    Returns a function that calculates fibonacci numbers
    and caches results to avoid recalculation
    """
    # YOUR CODE HERE
    pass

# Test it
# fib = create_fibonacci_memoized()
# print(f"fib(5) = {fib(5)}")  # Should be 5
# print(f"fib(10) = {fib(10)}")  # Should be 55
# The second call should be faster if using cache


# ============================================================================
# QUESTION 9: Fix Multiple Late Binding Bugs
# ============================================================================
# This creates functions to calculate powers AND multiply

def create_mixed_functions_broken():
    """
    Create list of power functions: x^1, x^2, x^3
    Create list of multiply functions: x*2, x*3, x*4
    """
    functions = []
    
    # Power functions
    for exp in range(1, 4):
        def power(x):
            return x ** exp  # ← BUG
        functions.append(power)
    
    # Multiply functions
    for mult in range(2, 5):
        def multiply(x):
            return x * mult  # ← BUG
        functions.append(multiply)
    
    return functions

# TODO: Fix this function
def create_mixed_functions_fixed():
    # YOUR CODE HERE
    pass

# Test it
# funcs = create_mixed_functions_fixed()
# print(f"x^1 with x=2: {funcs[0](2)} should be 2")
# print(f"x^2 with x=2: {funcs[1](2)} should be 4")
# print(f"x^3 with x=2: {funcs[2](2)} should be 8")
# print(f"x*2 with x=5: {funcs[3](5)} should be 10")
# print(f"x*3 with x=5: {funcs[4](5)} should be 15")
# print(f"x*4 with x=5: {funcs[5](5)} should be 20")


# ============================================================================
# QUESTION 10: Logger with Closure
# ============================================================================
# Create a simple logging system with closures

def create_logger(log_prefix):
    """
    Returns a function that logs messages with a prefix
    Example: error_log = create_logger("[ERROR]")
             error_log("Something went wrong")
             prints: [ERROR] Something went wrong
    """
    # YOUR CODE HERE
    pass

# Test it
# info_log = create_logger("[INFO]")
# error_log = create_logger("[ERROR]")
# info_log("Application started")  # Should print: [INFO] Application started
# error_log("File not found")      # Should print: [ERROR] File not found
