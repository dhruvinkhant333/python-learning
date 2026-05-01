# ============================================================================
# QUESTION 1: Fix the Late Binding Bug - SOLUTION
# ============================================================================
# This function should create multiplier functions (×2, ×3, ×4)
# But it has a late binding bug. Fix it!

# ❌ BROKEN VERSION - All functions will return x * 4
# ============================================================================
print("❌ BROKEN VERSION:")
print("-" * 60)

def create_multipliers_broken():
    multipliers = []
    for i in range(2, 5):
        def multiply(x):
            return x * i  # ← BUG: late binding issue
        multipliers.append(multiply)
    return multipliers

times_2_broken, times_3_broken, times_4_broken = create_multipliers_broken()
print(f"times_2(5) should be 10, got: {times_2_broken(5)} ❌")
print(f"times_3(5) should be 15, got: {times_3_broken(5)} ❌")
print(f"times_4(5) should be 20, got: {times_4_broken(5)} ✅")
print("\nWhy? All functions reference the same 'i' variable.")
print("After the loop ends, i = 4, so all functions use i=4\n")


# ✅ SOLUTION: Use default parameter to capture current value
# ============================================================================
print("\n✅ SOLUTION: Default Parameter Approach")
print("-" * 60)

def create_multipliers_fixed():
    multipliers = []
    for i in range(2, 5):
        def multiply(x, i=i):  # ← FIX: i=i captures i's current value
            return x * i
        multipliers.append(multiply)
    return multipliers

times_2, times_3, times_4 = create_multipliers_fixed()
print(f"times_2(5) should be 10, got: {times_2(5)} ✅")
print(f"times_3(5) should be 15, got: {times_3(5)} ✅")
print(f"times_4(5) should be 20, got: {times_4(5)} ✅")
print("\nHow it works:")
print("- i=i in the parameter list captures i's VALUE at function definition")
print("- Default parameters are evaluated ONCE when the function is defined")
print("- Each function gets its own copy of i's current value\n")


# 🎓 ALTERNATIVE SOLUTION: Factory Function Approach
# ============================================================================
print("\n🎓 ALTERNATIVE: Factory Function Approach")
print("-" * 60)

def create_multipliers_factory():
    """
    Creates a new scope for each multiplier using a factory function
    This is more explicit about creating separate closures
    """
    def make_multiplier(factor):
        def multiply(x):
            return x * factor
        return multiply
    
    multipliers = []
    for i in range(2, 5):
        multipliers.append(make_multiplier(i))
    return multipliers

times_2_v2, times_3_v2, times_4_v2 = create_multipliers_factory()
print(f"times_2(5) should be 10, got: {times_2_v2(5)} ✅")
print(f"times_3(5) should be 15, got: {times_3_v2(5)} ✅")
print(f"times_4(5) should be 20, got: {times_4_v2(5)} ✅")
print("\nHow it works:")
print("- make_multiplier(i) creates a NEW scope with its own 'factor'")
print("- Each call creates a fresh closure with isolated variables\n")


# 🎓 ALTERNATIVE SOLUTION: Lambda with Default Parameter
# ============================================================================
print("\n🎓 ALTERNATIVE: List Comprehension with Lambda")
print("-" * 60)

def create_multipliers_lambda():
    return [lambda x, i=i: x * i for i in range(2, 5)]

times_2_v3, times_3_v3, times_4_v3 = create_multipliers_lambda()
print(f"times_2(5) should be 10, got: {times_2_v3(5)} ✅")
print(f"times_3(5) should be 15, got: {times_3_v3(5)} ✅")
print(f"times_4(5) should be 20, got: {times_4_v3(5)} ✅")
print("\nHow it works:")
print("- List comprehension creates multiple lambda functions")
print("- i=i in lambda parameters captures each value\n")


# ============================================================================
# TEST MULTIPLE VALUES
# ============================================================================
print("\n" + "=" * 60)
print("COMPREHENSIVE TEST")
print("=" * 60)

test_values = [1, 5, 10, 100]
print(f"\nTesting with values: {test_values}\n")

for x in test_values:
    expected_2 = x * 2
    expected_3 = x * 3
    expected_4 = x * 4
    
    actual_2 = times_2(x)
    actual_3 = times_3(x)
    actual_4 = times_4(x)
    
    status_2 = "✅" if actual_2 == expected_2 else "❌"
    status_3 = "✅" if actual_3 == expected_3 else "❌"
    status_4 = "✅" if actual_4 == expected_4 else "❌"
    
    print(f"x={x:3d}: times_2={actual_2:4d} (expected {expected_2:4d}) {status_2} | " + 
          f"times_3={actual_3:4d} (expected {expected_3:4d}) {status_3} | " +
          f"times_4={actual_4:4d} (expected {expected_4:4d}) {status_4}")


# ============================================================================
# KEY TAKEAWAY
# ============================================================================
print("\n" + "=" * 60)
print("KEY LESSONS")
print("=" * 60)
print("""
1. LATE BINDING PROBLEM:
   - Closures capture variables by REFERENCE, not by VALUE
   - When the loop ends, all functions reference the final value of i
   - This is a common gotcha in Python!

2. THREE SOLUTIONS:
   ✅ Default Parameter: i=i captures current value (RECOMMENDED for loops)
   ✅ Factory Function: make_multiplier() creates new scope
   ✅ Lambda with default: lambda x, i=i works like default parameter

3. WHEN TO USE EACH:
   - Use default parameter for simple cases (most common)
   - Use factory function for clarity and complex logic
   - Use lambda when you need a quick, inline solution

4. REMEMBER:
   - Default parameters are evaluated at DEFINITION time
   - Loop variables are evaluated at CALL time
   - This timing difference is the root of late binding issues!
""")
