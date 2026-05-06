# ============================================================================
# QUESTION 8: Memoization (Caching with Closure)
# ============================================================================

def create_fibonacci_memoized():
    """
    Returns a function that calculates fibonacci numbers
    and caches results to avoid recalculation
    """
    # The cache dictionary lives in the closure's scope
    cache = {0: 0, 1: 1}

    def fib(n):
        # Check if the value is already in the cache
        if n not in cache:
            # If not, calculate it recursively and store it
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib

# Test it
if __name__ == "__main__":
    fib = create_fibonacci_memoized()
    
    print(f"fib(5) = {fib(5)}")   # Expected: 5
    print(f"fib(10) = {fib(10)}") # Expected: 55
    print(f"fib(50) = {fib(50)}") # Should calculate instantly due to memoization