# ============================================================================
# QUESTION 5: Function Factory - SOLUTION
# ============================================================================
# Create a function that makes custom adder functions

def make_adder(x):
    """
    Takes a number x and returns a function that adds x to any number
    Example: add_5 = make_adder(5)
             add_5(3) returns 8
    """
    def adder(y):
        return x + y
    return adder


# Test it
add_10 = make_adder(10)
add_100 = make_adder(100)
print(f"add_10(5) should be 15: {add_10(5)}")
print(f"add_100(5) should be 105: {add_100(5)}")
