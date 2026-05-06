# ============================================================================
# QUESTION 9: Fix Multiple Late Binding Bugs
# ============================================================================

def create_mixed_functions_fixed():
    """
    Create list of power functions: x^1, x^2, x^3
    Create list of multiply functions: x*2, x*3, x*4
    Fixed using default arguments to capture loop variables (Early Binding).
    """
    functions = []
    
    # Power functions
    for exp in range(1, 4):
        # We capture 'exp' as a local variable 'e' at creation time
        def power(x, e=exp):
            return x ** e
        functions.append(power)
    
    # Multiply functions
    for mult in range(2, 5):
        # We capture 'mult' as a local variable 'm' at creation time
        def multiply(x, m=mult):
            return x * m
        functions.append(multiply)
    
    return functions

# Test it
if __name__ == "__main__":
    funcs = create_mixed_functions_fixed()
    
    print(f"x^1 with x=2: {funcs[0](2)} (Expected 2)")
    print(f"x^2 with x=2: {funcs[1](2)} (Expected 4)")
    print(f"x^3 with x=2: {funcs[2](2)} (Expected 8)")
    print(f"x*2 with x=5: {funcs[3](5)} (Expected 10)")
    print(f"x*3 with x=5: {funcs[4](5)} (Expected 15)")
    print(f"x*4 with x=5: {funcs[5](5)} (Expected 20)")