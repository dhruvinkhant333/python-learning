# ============================================================================
# PYTHON CLOSURE: LATE BINDING ISSUE
# ============================================================================
# This demonstrates a common mistake with closures and loops in Python

# ❌ BROKEN VERSION - All functions return x ** 3
# ============================================================================
print("❌ BROKEN VERSION:")
print("-" * 50)

def make_power_functions_broken():
    powers = []
    for exp in range(1, 4):
        def power(x):
            return x ** exp     # ← Problem: captures 'exp' by reference
        powers.append(power)
    return powers

square, cube, fourth = make_power_functions_broken()
print(f"square(2) = {square(2)}   # expects 2   — gets {square(2)} ❌")
print(f"cube(2) = {cube(2)}       # expects 8   — gets {cube(2)} ✅")
print(f"fourth(2) = {fourth(2)}   # expects 16  — gets {fourth(2)} ❌")

# Why does this happen?
# When the loop finishes, exp = 3
# All functions reference the SAME 'exp' variable
# When we call square(2), it looks up exp (which is now 3), so: 2 ** 3 = 8
# When we call cube(2), it's 2 ** 3 = 8 (not 2 ** 2)
# When we call fourth(2), it's 2 ** 3 = 8 (not 2 ** 4)


# ✅ FIX #1: Default Parameter (Recommended for loops)
# ============================================================================
print("\n✅ FIX #1: Default Parameter (RECOMMENDED)")
print("-" * 50)

def make_power_functions_fix1():
    powers = []
    for exp in range(1, 4):
        def power(x, exp=exp):    # ← Capture exp's CURRENT value as default
            return x ** exp
        powers.append(power)
    return powers

square, cube, fourth = make_power_functions_fix1()
print(f"square(2) = {square(2)}   # expects 2   — gets {square(2)} ✅")
print(f"cube(2) = {cube(2)}       # expects 8   — gets {cube(2)} ✅")
print(f"fourth(2) = {fourth(2)}   # expects 16  — gets {fourth(2)} ✅")

# How it works:
# exp=exp creates a new local variable for each function
# Default parameters are evaluated at function definition time (when the loop runs)
# So each function gets its own copy of exp's current value


# ✅ FIX #2: Factory Function (Explicit scope creation)
# ============================================================================
print("\n✅ FIX #2: Factory Function")
print("-" * 50)

def make_power_functions_fix2():
    powers = []
    for exp in range(1, 4):
        # Create a NEW scope by calling a function
        def make_one_power(e):
            def power(x):
                return x ** e    # e is now from the make_one_power scope
            return power
        powers.append(make_one_power(exp))
    return powers

square, cube, fourth = make_power_functions_fix2()
print(f"square(2) = {square(2)}   # expects 2   — gets {square(2)} ✅")
print(f"cube(2) = {cube(2)}       # expects 8   — gets {cube(2)} ✅")
print(f"fourth(2) = {fourth(2)}   # expects 16  — gets {fourth(2)} ✅")

# How it works:
# Each call to make_one_power() creates a NEW scope with its own 'e'
# This isolates each closure from the loop variable


# ✅ FIX #3: Lambda with Default (Compact version)
# ============================================================================
print("\n✅ FIX #3: Lambda with Default")
print("-" * 50)

def make_power_functions_fix3():
    return [lambda x, exp=exp: x ** exp for exp in range(1, 4)]

square, cube, fourth = make_power_functions_fix3()
print(f"square(2) = {square(2)}   # expects 2   — gets {square(2)} ✅")
print(f"cube(2) = {cube(2)}       # expects 8   — gets {cube(2)} ✅")
print(f"fourth(2) = {fourth(2)}   # expects 16  — gets {fourth(2)} ✅")


# ============================================================================
# WHAT THIS TEACHES US
# ============================================================================
print("\n" + "=" * 70)
print("KEY LESSONS:")
print("=" * 70)
print("""
1. LATE BINDING IN PYTHON
   - Closures capture variables by REFERENCE, not VALUE
   - The variable is looked up when the function is CALLED, not when defined
   - This can cause surprises in loops!

2. LOOP VARIABLES ARE MUTABLE
   - The loop variable (exp) doesn't get "frozen" at definition time
   - All closures created in the loop reference the SAME variable
   - By the time you call the functions, the loop variable has its final value

3. THREE SOLUTIONS
   ✓ Default parameters: Simplest for simple closures
   ✓ Factory functions: Most explicit and clear
   ✓ Lambda with defaults: Most concise

4. WHY THIS MATTERS
   - This is a frequent bug in event handlers and callbacks
   - Understanding this prevents mysterious bugs in async code
   - It's a key concept for intermediate Python developers
""")
