# ============================================================================
# QUESTION 6: Nested Closures - SOLUTION
# ============================================================================
# Create a function that creates a function that creates a function!
# This is called "Currying" in functional programming

# 📚 CONCEPT: Function Composition with Multiple Levels of Closures
# ============================================================================
print("=" * 70)
print("QUESTION 6: Nested Closures (Currying)")
print("=" * 70)
print("""
Nested closures allow you to create functions that return functions that
return functions. This is powerful for:
- Partial application of arguments
- Function composition
- Creating specialized functions
- Advanced functional programming patterns

This technique is called "CURRYING" - breaking a function with multiple
arguments into a sequence of functions with single arguments.
""")


# ✅ BASIC SOLUTION: Simple Nested Closures
# ============================================================================
print("\n✅ SOLUTION 1: Simple Nested Closures")
print("-" * 70)

def outer(a):
    """
    Level 1: Takes parameter 'a'
    Returns a function that takes 'b'
    """
    def middle(b):
        """
        Level 2: Takes parameter 'b'
        Returns a function that takes 'c'
        """
        def inner(c):
            """
            Level 3: Takes parameter 'c'
            Returns the final result
            """
            return a + b + c
        return inner
    return middle

# Test basic solution
result = outer(1)(2)(3)
print(f"outer(1)(2)(3) = {result}")
print(f"Expected: 6 ✅\n")

# Store intermediate results to understand the flow
step1 = outer(1)
print(f"outer(1) returns a function: {step1}")
step2 = step1(2)
print(f"outer(1)(2) returns a function: {step2}")
step3 = step2(3)
print(f"outer(1)(2)(3) returns: {step3}")


# 🎓 ALTERNATIVE 1: Lambda Version (Compact)
# ============================================================================
print("\n\n🎓 ALTERNATIVE 1: Lambda-Based Currying")
print("-" * 70)

outer_lambda = lambda a: lambda b: lambda c: a + b + c

result_lambda = outer_lambda(1)(2)(3)
print(f"outer_lambda(1)(2)(3) = {result_lambda}")
print(f"Expected: 6 ✅")
print("Note: Much more compact, but less readable!")


# 🎓 ALTERNATIVE 2: Partial Application
# ============================================================================
print("\n\n🎓 ALTERNATIVE 2: Partial Application Pattern")
print("-" * 70)

def outer_partial(a, b=None, c=None):
    """
    This version allows flexible calling:
    - outer_partial(1, 2, 3) - all at once
    - outer_partial(1)(2)(3) - curried style
    - outer_partial(1, 2)(3) - mixed
    """
    if b is None:
        # Return a function waiting for b
        def wait_for_b(b_val):
            if c is None:
                # Return a function waiting for c
                def wait_for_c(c_val):
                    return a + b_val + c_val
                return wait_for_c
            return a + b_val + c
        return wait_for_b
    
    # All arguments provided
    return a + b + c

print("Different calling styles:")
print(f"outer_partial(1, 2, 3) = {outer_partial(1, 2, 3)}")
print(f"outer_partial(1)(2)(3) = {outer_partial(1)(2)(3)}")
print(f"outer_partial(1, 2)(3) = {outer_partial(1, 2)(3)}")


# 🎓 ALTERNATIVE 3: With Default Values
# ============================================================================
print("\n\n🎓 ALTERNATIVE 3: Nested Closures with Defaults")
print("-" * 70)

def outer_with_defaults(a, multiplier=1):
    """Shows how to include configuration in closures"""
    def middle(b, power=1):
        def inner(c):
            # Demonstrate closure capturing outer variables
            return (a + b + c) ** power * multiplier
        return inner
    return middle

result_defaults = outer_with_defaults(1, multiplier=2)(2, power=2)(3)
print(f"outer_with_defaults(1, multiplier=2)(2, power=2)(3)")
print(f"  = (1 + 2 + 3) ** 2 * 2")
print(f"  = 6 ** 2 * 2")
print(f"  = 36 * 2")
print(f"  = {result_defaults} ✅")


# 🎓 ALTERNATIVE 4: Multiplication Version
# ============================================================================
print("\n\n🎓 ALTERNATIVE 4: Multiplication Instead of Addition")
print("-" * 70)

def multiply_nested(a):
    def multiply_b(b):
        def multiply_c(c):
            return a * b * c
        return multiply_c
    return multiply_b

result_mult = multiply_nested(2)(3)(4)
print(f"multiply_nested(2)(3)(4) = {result_mult}")
print(f"Expected: 2 * 3 * 4 = 24 ✅")


# ============================================================================
# COMPREHENSIVE TESTS
# ============================================================================
print("\n\n" + "=" * 70)
print("COMPREHENSIVE TESTS")
print("=" * 70)

test_cases = [
    (1, 2, 3, 6),
    (5, 5, 5, 15),
    (10, 20, 30, 60),
    (-1, -2, -3, -6),
    (100, 50, 25, 175),
]

print("\nTest Case: outer(a)(b)(c)")
print("-" * 70)
print(f"{'a':>5} | {'b':>5} | {'c':>5} | Expected | Got | Status")
print("-" * 70)

for a, b, c, expected in test_cases:
    result = outer(a)(b)(c)
    status = "✅" if result == expected else "❌"
    print(f"{a:>5} | {b:>5} | {c:>5} | {expected:>8} | {result:>3} | {status}")


# ============================================================================
# REAL-WORLD EXAMPLE: API Request Builder
# ============================================================================
print("\n\n" + "=" * 70)
print("REAL-WORLD EXAMPLE: API Request Builder")
print("=" * 70)

def build_api_request(domain):
    """First level: domain"""
    def set_endpoint(endpoint):
        """Second level: endpoint"""
        def set_params(params):
            """Third level: query parameters"""
            url = f"https://{domain}/{endpoint}"
            if params:
                param_str = "&".join([f"{k}={v}" for k, v in params.items()])
                url += f"?{param_str}"
            return url
        return set_params
    return set_endpoint

# Build different API requests
get_users = build_api_request("api.example.com")("users")({})
get_users_filtered = build_api_request("api.example.com")("users")({"role": "admin", "status": "active"})

print(f"\nAPI URL 1: {get_users}")
print(f"API URL 2: {get_users_filtered}")


# ============================================================================
# REAL-WORLD EXAMPLE: Logger with Levels
# ============================================================================
print("\n\n" + "=" * 70)
print("REAL-WORLD EXAMPLE: Logger with Levels")
print("=" * 70)

def create_logger(app_name):
    """First level: application name"""
    def set_level(level):
        """Second level: log level (DEBUG, INFO, ERROR, etc.)"""
        def log_message(message):
            """Third level: the actual message"""
            timestamp = "2026-05-05 10:30:00"
            return f"[{timestamp}] {app_name}:{level} - {message}"
        return log_message
    return set_level

# Create loggers
error_logger = create_logger("MyApp")("ERROR")
info_logger = create_logger("MyApp")("INFO")
debug_logger = create_logger("MyApp")("DEBUG")

print(f"\n{error_logger('Database connection failed')}")
print(f"{info_logger('Server started on port 8000')}")
print(f"{debug_logger('Processing request #42')}")


# ============================================================================
# UNDERSTANDING THE FLOW
# ============================================================================
print("\n\n" + "=" * 70)
print("HOW NESTED CLOSURES WORK - STEP BY STEP")
print("=" * 70)

print("""
When you call outer(1)(2)(3), here's what happens:

1. outer(1) is called:
   - Parameter a = 1
   - Captures a in a closure
   - Returns the 'middle' function

2. middle(2) is called (on the returned function):
   - Parameter b = 2
   - Captures b and a (from outer closure)
   - Returns the 'inner' function

3. inner(3) is called (on the returned function):
   - Parameter c = 3
   - Has access to a, b, and c
   - Computes a + b + c = 1 + 2 + 3 = 6
   - Returns 6

EACH LEVEL CREATES A NEW CLOSURE that captures variables from outer scopes!

This is why it's powerful:
✅ Each function "remembers" previous arguments
✅ You can partially apply functions
✅ Enables powerful functional programming patterns
✅ Creates specialized functions from general ones
""")


# ============================================================================
# CURRYING VS PARTIAL APPLICATION
# ============================================================================
print("\n" + "=" * 70)
print("CURRYING VS PARTIAL APPLICATION")
print("=" * 70)

print("""
CURRYING:
- Breaking a function into multiple single-argument functions
- outer(a)(b)(c) - each function takes ONE argument
- Mathematical concept from lambda calculus
- outer(1)(2)(3) or outer(1) then later (2) then later (3)

PARTIAL APPLICATION:
- "Fixing" some arguments and leaving others open
- add = functools.partial(operator.add, 5)
- add(3) # returns 8
- Can provide multiple arguments at once or partially

BOTH are useful but different approaches!

In Python, nested closures enable currying naturally.
""")


# ============================================================================
# COMMON MISTAKES
# ============================================================================
print("\n" + "=" * 70)
print("COMMON MISTAKES & DEBUGGING")
print("=" * 70)

print("\n❌ MISTAKE 1: Forgetting to return functions")
print("-" * 70)

def outer_wrong(a):
    def middle(b):
        def inner(c):
            return a + b + c
        # ❌ Forgot to return inner!
    # ❌ Forgot to return middle!
    return None

try:
    result = outer_wrong(1)(2)(3)
except TypeError as e:
    print(f"Error: {e}")
    print("✅ Remember: Each level must return a function!\n")


print("✅ CORRECT VERSION:")
def outer_correct(a):
    def middle(b):
        def inner(c):
            return a + b + c
        return inner  # ✅ Return inner function
    return middle    # ✅ Return middle function

result = outer_correct(1)(2)(3)
print(f"outer_correct(1)(2)(3) = {result}\n")


print("❌ MISTAKE 2: Wrong number of arguments")
print("-" * 70)
try:
    result = outer(1, 2, 3)  # Wrong! Should be outer(1)(2)(3)
except TypeError as e:
    print(f"Error: {e}")
    print("✅ Remember: Each level takes ONE argument, use () for each!\n")


# ============================================================================
# PERFORMANCE NOTE
# ============================================================================
print("=" * 70)
print("PERFORMANCE CONSIDERATION")
print("=" * 70)

print("""
Nested closures create multiple function objects in memory.
For simple cases, calling outer(1)(2)(3) is slightly slower than
calling a single function add3(1, 2, 3).

However, the benefits for code organization and functional programming
often outweigh the small performance cost.

For performance-critical code, consider:
- Using a regular function for hot paths
- Using @lru_cache to memoize results
- Using functools.partial for better performance
""")
