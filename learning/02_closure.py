"""
================================================================================
PYTHON CLOSURES MASTERCLASS
Nested Functions | Scope | State Preservation | Function Factories
================================================================================
Run this file top to bottom, or copy sections into a REPL / Jupyter cell.
Every section prints its own output so you can SEE what's happening.
"""

print("=" * 80)
print("PART 1: FOUNDATIONAL CONCEPTS")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1a. What is a closure? (simple words)
# -----------------------------------------------------------------------------
# A closure is a function that "remembers" the variables from the place it
# was CREATED, even after that outer place has finished running.
#
# It happens when:
#   1. You have a nested function (a function defined inside another function)
#   2. The inner function uses a variable from the outer function
#   3. The outer function RETURNS the inner function
#
# The returned inner function carries a little backpack of the variables
# it needs, even though the outer function has already finished executing.

# -----------------------------------------------------------------------------
# 1b. Nested functions -- function inside function
# -----------------------------------------------------------------------------
def outer():
    print("  Inside outer()")

    def inner():
        print("  Inside inner()")

    inner()  # calling the nested function from within outer

print("\n--- Nested function demo ---")
outer()

# -----------------------------------------------------------------------------
# 1c. Variable scope review: Local, Enclosing, Global, Built-in (LEGB)
# -----------------------------------------------------------------------------
# Python looks up a variable name in this order:
#   L - Local:      inside the current function
#   E - Enclosing:  inside any enclosing (outer) function
#   G - Global:     at the top level of the module/script
#   B - Built-in:   Python's built-in names (len, print, etc.)

x_global = "I'm global"

def scope_demo():
    x_enclosing = "I'm enclosing"

    def inner_scope():
        x_local = "I'm local"
        print("  Local:    ", x_local)
        print("  Enclosing:", x_enclosing)  # found in the enclosing function
        print("  Global:   ", x_global)     # found at module level
        print("  Built-in: ", len("abc"))   # found in Python's builtins

    inner_scope()

print("\n--- LEGB scope demo ---")
scope_demo()

# -----------------------------------------------------------------------------
# 1d. How the inner function "remembers" outer variables
# -----------------------------------------------------------------------------
# When Python creates the inner function, it attaches a reference to the
# specific outer variables it uses. This bundle of remembered variables is
# called the function's __closure__. You can literally inspect it.

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello_greeter = make_greeter("Hello")
print("\n--- Inspecting a closure ---")
print("Calling hello_greeter('Leo'):", hello_greeter("Leo"))
print("Closure cell contents:", [cell.cell_contents for cell in hello_greeter.__closure__])
print("Free variable names:", hello_greeter.__code__.co_freevars)

# -----------------------------------------------------------------------------
# 1e. Why closures matter
# -----------------------------------------------------------------------------
# Closures let you:
#   - Create functions that carry their own private state, without needing
#     a class (lightweight "object-like" behavior).
#   - Build function FACTORIES: functions that generate other, customized
#     functions (e.g. make_greeter above).
#   - Form the foundation for decorators (Python's @decorator syntax is
#     built entirely on closures).


print("\n" + "=" * 80)
print("PART 2: STEP-BY-STEP EXAMPLES")
print("=" * 80)

# --- a) Simple nested function ---
def a_outer():
    def a_inner():
        return "hello from a_inner"
    return a_inner()  # called immediately, result returned

print("\n(a) Simple nested function:", a_outer())

# --- b) Nested function using an outer variable ---
def b_outer():
    message = "captured from b_outer"
    def b_inner():
        return message  # uses the outer variable
    return b_inner()

print("(b) Nested function using outer variable:", b_outer())

# --- c) Function returns another function (not calling it yet) ---
def c_outer():
    def c_inner():
        return "I was returned, not called, by c_outer"
    return c_inner  # NOTE: no parentheses -- returning the function ITSELF

returned_fn = c_outer()
print("(c) c_outer() returns a function object:", returned_fn)
print("    Calling it separately:", returned_fn())

# --- d) Closure in action: the returned function remembers outer state ---
def d_make_adder(n):
    def add(x):
        return x + n  # `n` is remembered even after d_make_adder() has returned
    return add

add_five = d_make_adder(5)
add_100 = d_make_adder(100)
print("\n(d) add_five(3):", add_five(3))     # 5 was remembered
print("    add_100(3):", add_100(3))          # 100 was remembered (separately!)

# --- e) Multiple levels of nesting ---
def e_level1(a):
    def e_level2(b):
        def e_level3(c):
            return a + b + c  # remembers BOTH a and b from outer scopes
        return e_level3
    return e_level2

print("\n(e) Triple-nested closure:", e_level1(1)(2)(3))

# --- f) Using the `nonlocal` keyword to MODIFY an enclosing variable ---
def f_counter():
    count = 0
    def increment():
        nonlocal count  # without this, `count += 1` would raise an error
        count += 1
        return count
    return increment

counter = f_counter()
print("\n(f) nonlocal counter:", counter(), counter(), counter())

# --- g) Closure with a MUTABLE object (no `nonlocal` needed) ---
# Mutating a list/dict in place doesn't require `nonlocal` -- you're not
# reassigning the outer variable, just changing what it points to.
def g_make_logger():
    log = []
    def log_message(msg):
        log.append(msg)  # mutating the list in place -- no nonlocal needed
        return log
    return log_message

logger = g_make_logger()
logger("first event")
logger("second event")
print("(g) Mutable closure (list):", logger("third event"))


print("\n" + "=" * 80)
print("PART 3: CORE CONCEPTS WITH CODE")
print("=" * 80)

# -----------------------------------------------------------------------------
# 3a. How variables are captured (by reference to the variable, not the value)
# -----------------------------------------------------------------------------
def capture_demo():
    value = "original"
    def show():
        return value  # looks up `value` each time it's CALLED, not when created
    value = "changed before first call"
    return show

show_fn = capture_demo()
print("\nCaptured variable reflects the LATEST value at call time:", show_fn())

# -----------------------------------------------------------------------------
# 3b. Returning functions
# -----------------------------------------------------------------------------
def power_of(exponent):
    def raise_to_power(base):
        return base ** exponent
    return raise_to_power

square = power_of(2)
cube = power_of(3)
print("\nsquare(4):", square(4))
print("cube(4):", cube(4))

# -----------------------------------------------------------------------------
# 3c. State preservation across calls
# -----------------------------------------------------------------------------
def running_total():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add

acc = running_total()
print("\nRunning total after 10:", acc(10))
print("Running total after +5:", acc(5))
print("Running total after +20:", acc(20))

# -----------------------------------------------------------------------------
# 3d. Multiple independent closures from the SAME factory function
# -----------------------------------------------------------------------------
# Each call to the factory creates a BRAND NEW, independent set of
# remembered variables -- they do not share state with each other.
acc_a = running_total()
acc_b = running_total()
acc_a(100)
acc_a(50)
acc_b(1)
print("\nacc_a total:", acc_a(0), "| acc_b total:", acc_b(0), "-- completely independent")


print("\n" + "=" * 80)
print("PART 4: PRACTICAL USE CASES")
print("=" * 80)

# --- Function factories ---
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print("\ndouble(7):", double(7), "| triple(7):", triple(7))

# --- Data transformers: custom scaler / normalizer ---
def make_min_max_scaler(data_min, data_max):
    def scale(x):
        return (x - data_min) / (data_max - data_min)
    return scale

exam_scaler = make_min_max_scaler(0, 100)
print("\nScaled exam score 75:", exam_scaler(75))
print("Scaled exam score 40:", exam_scaler(40))

# --- Callbacks and decorators foundation ---
# A decorator is just a closure that wraps another function and returns
# a new function with extra behavior added around it.
def with_logging(func):
    def wrapper(*args, **kwargs):
        print(f"  [LOG] Calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@with_logging
def add_numbers(a, b):
    return a + b

print("\n--- Decorator built from a closure ---")
add_numbers(3, 4)

# --- Currying / partial application ---
def curried_add(a):
    def add_b(b):
        def add_c(c):
            return a + b + c
        return add_c
    return add_b

print("\nCurried add: curried_add(1)(2)(3) =", curried_add(1)(2)(3))

# --- Encapsulation without a class ---
def make_bank_account(starting_balance):
    balance = starting_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    def get_balance():
        return balance

    # Return a dict of functions -- this is "encapsulation" via closures:
    # `balance` is private -- there's no way to touch it except through
    # these three functions.
    return {"deposit": deposit, "withdraw": withdraw, "balance": get_balance}

account = make_bank_account(100)
print("\n--- Bank account via closures (no class) ---")
print("Starting balance:", account["balance"]())
print("After deposit(50):", account["deposit"](50))
print("After withdraw(30):", account["withdraw"](30))


print("\n" + "=" * 80)
print("PART 5: CLOSURE VS CLASS")
print("=" * 80)

# The SAME bank account, implemented as a class, for direct comparison:
class BankAccount:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

acc_class = BankAccount(100)
print("\nClass-based account -- deposit(50):", acc_class.deposit(50))
print("Class-based account -- withdraw(30):", acc_class.withdraw(30))

print("""
When to use CLOSURE:
  - You only need ONE or TWO related pieces of behavior (e.g. one function
    with private state), not a whole family of related methods.
  - You want a lightweight, functional style (common in data pipelines).
  - You're building a decorator or a simple callback.

When to use CLASS:
  - You need MULTIPLE pieces of state AND multiple methods operating on
    that state together.
  - You need inheritance, multiple instances with rich behavior, or
    interfaces other code will subclass/extend.
  - The "object" concept genuinely models a real-world thing with several
    related behaviors (e.g. a Model class with .fit(), .predict(), .save()).

Equivalence: a closure is essentially a lightweight object with exactly
ONE method and some private data -- the enclosing variables ARE the
instance attributes, and the inner function IS the single method.
""")


print("\n" + "=" * 80)
print("PART 6: COMMON MISTAKES")
print("=" * 80)

print("""
1. LOOP VARIABLE CLOSURE -- capturing the VARIABLE, not the value at the
   time the closure was created. By the time the closures are called, the
   loop variable holds its FINAL value for every single one of them.

2. USING `global` VS `nonlocal` -- `global` reaches all the way to module
   level; `nonlocal` reaches the nearest ENCLOSING function scope. Using
   `global` inside a nested function when you meant the enclosing
   function's variable is a common mix-up.

3. MEMORY -- closures that capture large objects (e.g. a huge DataFrame)
   keep that object alive in memory for as long as the closure exists,
   even if nothing else references it anymore. Be mindful of what you
   capture in long-lived closures.

4. SCOPE CONFUSION -- forgetting that reading an enclosing variable works
   with no special keyword, but REASSIGNING one requires `nonlocal`
   (or `global` at module level).
""")

# --- THE loop closure bug, demonstrated and fixed ---
print("--- THE loop closure bug ---")

# BUGGY version
funcs_buggy = []
for i in range(3):
    def make_func():
        return i  # captures the VARIABLE `i`, looked up at CALL time
    funcs_buggy.append(make_func)

print("Buggy: all closures return the FINAL value of i:", [f() for f in funcs_buggy])
# Expected by beginners: [0, 1, 2] -- Actual: [2, 2, 2]

# FIX 1: default argument captures the value at DEFINITION time
funcs_fixed_default = []
for i in range(3):
    def make_func_fixed(i=i):  # `i=i` binds the CURRENT value as a default
        return i
    funcs_fixed_default.append(make_func_fixed)

print("Fixed (default arg):", [f() for f in funcs_fixed_default])

# FIX 2: use a factory function that creates a fresh scope per iteration
def make_func_factory(i):
    def inner():
        return i  # this `i` is now a parameter of make_func_factory,
                  # a NEW one is created on every call
    return inner

funcs_fixed_factory = [make_func_factory(i) for i in range(3)]
print("Fixed (factory function):", [f() for f in funcs_fixed_factory])

# --- global vs nonlocal mix-up ---
print("\n--- global vs nonlocal ---")
counter_value = 0  # module-level (global) variable

def uses_global():
    global counter_value
    counter_value += 1  # modifies the MODULE-level variable
    return counter_value

def outer_with_nonlocal():
    local_value = 0
    def uses_nonlocal():
        nonlocal local_value
        local_value += 1  # modifies the ENCLOSING function's variable
        return local_value
    return uses_nonlocal

print("global example:", uses_global(), uses_global())
nl_fn = outer_with_nonlocal()
print("nonlocal example:", nl_fn(), nl_fn())


print("\n" + "=" * 80)
print("PART 7: PRACTICE EXERCISES (with solutions)")
print("=" * 80)

# Exercise 1: Create a counter function (closure)
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

ex1_counter = make_counter()
print("\n1) Counter calls:", ex1_counter(), ex1_counter(), ex1_counter())

# Exercise 2: Create a multiplier factory
def make_multiplier_ex(factor):
    return lambda x: x * factor

ex2_times7 = make_multiplier_ex(7)
print("2) Multiplier factory (x7):", ex2_times7(6))

# Exercise 3: Create a custom filter function factory
def make_threshold_filter(threshold):
    def is_above(x):
        return x > threshold
    return is_above

ex3_above_10 = make_threshold_filter(10)
ex3_result = list(filter(ex3_above_10, [5, 15, 8, 20, 3]))
print("3) Custom filter factory (> 10):", ex3_result)

# Exercise 4: Create data transformer (scale by min/max)
def make_scaler(data_min, data_max):
    def scale(x):
        return (x - data_min) / (data_max - data_min)
    return scale

ex4_scaler = make_scaler(0, 200)
print("4) Scaled value 150 in [0,200]:", round(ex4_scaler(150), 3))

# Exercise 5: Create an accumulator
def make_accumulator():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add

ex5_acc = make_accumulator()
ex5_acc(10)
ex5_acc(20)
print("5) Accumulator after 10, 20:", ex5_acc(5))

# Exercise 6: Fix a loop closure bug
print("\n6) Loop closure bug -- before and after fix:")
buggy = [lambda: i for i in range(4)]
print("   Buggy:", [f() for f in buggy])
fixed = [lambda i=i: i for i in range(4)]
print("   Fixed:", [f() for f in fixed])


print("\n" + "=" * 80)
print("PART 8: REAL DATA SCIENCE EXAMPLES")
print("=" * 80)

# --- Custom scaling function ---
def make_standard_scaler(mean, std):
    """Returns a function that applies (x - mean) / std -- z-score scaling."""
    def scale(x):
        return (x - mean) / std
    return scale

heights = [150, 160, 170, 180, 190]
mean_height = sum(heights) / len(heights)
std_height = (sum((h - mean_height) ** 2 for h in heights) / len(heights)) ** 0.5
z_scaler = make_standard_scaler(mean_height, std_height)
print("\nZ-score scaled heights:", [round(z_scaler(h), 2) for h in heights])

# --- Function wrapper for preprocessing (a decorator using closures) ---
def with_preprocessing(preprocess_fn):
    """A decorator factory -- returns a decorator that preprocesses input
    before calling the wrapped function."""
    def decorator(func):
        def wrapper(x):
            cleaned = preprocess_fn(x)
            return func(cleaned)
        return wrapper
    return decorator

@with_preprocessing(lambda x: max(0, min(x, 100)))  # clip to [0, 100]
def report_score(score):
    return f"Final reported score: {score}"

print("\nPreprocessing wrapper (clip to 0-100):")
print(" ", report_score(150))   # gets clipped to 100
print(" ", report_score(-20))   # gets clipped to 0
print(" ", report_score(75))    # passes through unchanged

# --- Memoization (caching results) using a closure ---
def make_memoized(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
            print(f"  (computed and cached result for {n})")
        else:
            print(f"  (cache hit for {n})")
        return cache[n]
    return wrapper

def slow_square(n):
    return n * n

memoized_square = make_memoized(slow_square)
print("\nMemoization demo:")
print("  Result:", memoized_square(5))
print("  Result:", memoized_square(5))  # cache hit this time
print("  Result:", memoized_square(9))

# --- ML preprocessing pipeline built from chained closures ---
def make_pipeline(*steps):
    """Chains multiple single-argument functions into ONE function that
    applies them in order -- a mini preprocessing pipeline."""
    def run(x):
        for step in steps:
            x = step(x)
        return x
    return run

clip_step = lambda x: max(0, min(x, 100))
scale_step = lambda x: x / 100
round_step = lambda x: round(x, 2)

preprocessing_pipeline = make_pipeline(clip_step, scale_step, round_step)
print("\nPipeline on raw value 150:", preprocessing_pipeline(150))
print("Pipeline on raw value 42:", preprocessing_pipeline(42))


print("\n" + "=" * 80)
print("PART 9: MINI-PROJECT -- DataTransformer via Closures")
print("=" * 80)

# --- Closure-based scaler factory ---
def make_min_max_normalizer(data_min, data_max):
    def normalize(x):
        return (x - data_min) / (data_max - data_min)
    return normalize

# --- Closure-based offset adder factory ---
def make_offset_adder(offset):
    def add_offset(x):
        return x + offset
    return add_offset

# --- Chaining transformations together ---
def chain_transforms(*transforms):
    def apply_all(x):
        for t in transforms:
            x = t(x)
        return x
    return apply_all

raw_scores = [45, 88, 62, 100, 15]

normalizer = make_min_max_normalizer(0, 100)
offset_adder = make_offset_adder(0.1)  # small boost after normalizing

full_pipeline = chain_transforms(normalizer, offset_adder)

print("\nClosure-based DataTransformer:")
for score in raw_scores:
    print(f"   raw={score:>3} -> transformed={round(full_pipeline(score), 3)}")

# --- Same thing, class-based, for direct comparison ---
class DataTransformer:
    def __init__(self, data_min, data_max, offset=0.0):
        self.data_min = data_min
        self.data_max = data_max
        self.offset = offset

    def normalize(self, x):
        return (x - self.data_min) / (self.data_max - self.data_min)

    def transform(self, x):
        return self.normalize(x) + self.offset

class_transformer = DataTransformer(0, 100, offset=0.1)
print("\nClass-based DataTransformer (same logic):")
for score in raw_scores:
    print(f"   raw={score:>3} -> transformed={round(class_transformer.transform(score), 3)}")

print("""
--- Comparison ---
Both produce identical results. The closure version is shorter and reads
as a straight-line pipeline of small functions -- great for quick,
throwaway transformations in a data-cleaning script. The class version
is more explicit, easier to extend with new methods later (e.g. an
inverse_transform(), a fit() that learns min/max from data, saving state
to disk), and is what you'll see in real ML libraries (scikit-learn's
scalers are all classes for exactly these reasons).
""")


print("\n" + "=" * 80)
print("PART 10: CLOSURE DEBUGGING")
print("=" * 80)

def make_debug_example(a, b):
    def inner(c):
        return a + b + c
    return inner

debug_fn = make_debug_example(1, 2)

print("\n--- Inspecting closure variables ---")
print("Free variable names:      ", debug_fn.__code__.co_freevars)
print("Captured cell values:     ", [cell.cell_contents for cell in debug_fn.__closure__])
print("Function's own local vars:", debug_fn.__code__.co_varnames)

print("""
--- Common debugging issues ---
1. "NameError: free variable referenced before assignment" -- happens when
   you try to REASSIGN an enclosing variable inside the inner function
   without declaring `nonlocal` first. Python assumes you meant to create
   a NEW local variable, then gets confused when you read it before
   assigning.

2. __closure__ is None -- means the function has NO enclosing variables
   captured (it's not actually a closure, just a plain nested function,
   or the variables it uses are all global/builtin, not enclosing).

3. All closures in a loop showing the same value -- the classic loop bug
   from Part 6. Check __closure__/cell_contents to confirm they all point
   to the same cell if you're debugging this.

--- Testing closures ---
Test closures like any other function: call them with known inputs and
assert on the outputs. Since each closure instance is independent, create
a FRESH one in each test (or in a fixture) to avoid state leaking between
test cases.
""")

def test_counter_closure():
    counter = make_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3
    print("test_counter_closure passed!")

def test_independent_counters():
    counter_a = make_counter()
    counter_b = make_counter()
    counter_a()
    counter_a()
    counter_b()
    assert counter_a() == 3   # 3rd call on counter_a
    assert counter_b() == 2   # 2nd call on counter_b -- independent state
    print("test_independent_counters passed!")

print("--- Running simple closure tests ---")
test_counter_closure()
test_independent_counters()

print("\n" + "=" * 80)
print("END OF MASTERCLASS -- run sections individually to experiment!")
print("=" * 80)