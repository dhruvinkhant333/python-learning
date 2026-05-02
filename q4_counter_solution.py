"""
QUESTION 4: Create a Counter with Closure
Solution for maintaining state with closures
"""

# ============================================================================
# SOLUTION - Basic Counter with Closure
# ============================================================================
def create_counter():
    """
    Creates a counter object using closure to maintain state.
    
    How it works:
    - The 'count' variable is in the enclosing scope of inner functions
    - Each inner function (increment, decrement, get_count) forms a closure
    - They can all access and modify the same 'count' variable
    - This creates a private state that persists between calls
    
    Returns:
        dict: Dictionary with three functions: increment, decrement, get_count
    """
    count = 0  # ← This is captured by closure
    
    def increment():
        nonlocal count  # ← Allow modification of enclosing scope variable
        count += 1
    
    def decrement():
        nonlocal count
        count -= 1
    
    def get_count():
        return count
    
    return {
        'increment': increment,
        'decrement': decrement,
        'get_count': get_count
    }


# ============================================================================
# ALTERNATIVE SOLUTION - With Validation
# ============================================================================
def create_counter_v2():
    """
    Counter with additional features:
    - Validate operations
    - Prevent negative counts (optional)
    - Add reset functionality
    """
    count = 0
    
    def increment(amount=1):
        nonlocal count
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Increment amount must be a positive integer")
        count += amount
    
    def decrement(amount=1):
        nonlocal count
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Decrement amount must be a positive integer")
        if count - amount < 0:
            raise ValueError("Cannot go below 0")
        count -= amount
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = 0
    
    return {
        'increment': increment,
        'decrement': decrement,
        'get_count': get_count,
        'reset': reset
    }


# ============================================================================
# ALTERNATIVE SOLUTION - Class-based (for comparison)
# ============================================================================
class Counter:
    """
    Counter using a class (not a closure).
    Included for comparison - shows the closure alternative to classes.
    """
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
    
    def get_count(self):
        return self.count


# ============================================================================
# TEST & DEMONSTRATE
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("BASIC COUNTER (Closure-based):")
    print("=" * 60)
    counter = create_counter()
    
    print(f"Initial count: {counter['get_count']()}")  # Should be 0
    
    counter['increment']()
    counter['increment']()
    print(f"After 2 increments: {counter['get_count']()}")  # Should be 2
    
    counter['decrement']()
    print(f"After 1 decrement: {counter['get_count']()}")  # Should be 1
    
    counter['increment']()
    counter['increment']()
    counter['increment']()
    print(f"After 3 more increments: {counter['get_count']()}")  # Should be 4
    
    print("\n" + "=" * 60)
    print("ADVANCED COUNTER (With Validation):")
    print("=" * 60)
    counter2 = create_counter_v2()
    
    print(f"Initial count: {counter2['get_count']()}")  # Should be 0
    
    counter2['increment'](5)
    print(f"After increment(5): {counter2['get_count']()}")  # Should be 5
    
    counter2['decrement'](2)
    print(f"After decrement(2): {counter2['get_count']()}")  # Should be 3
    
    counter2['reset']()
    print(f"After reset: {counter2['get_count']()}")  # Should be 0
    
    print("\n" + "=" * 60)
    print("CLASS-BASED COUNTER (for comparison):")
    print("=" * 60)
    counter3 = Counter()
    
    print(f"Initial count: {counter3.get_count()}")  # Should be 0
    
    counter3.increment()
    counter3.increment()
    print(f"After 2 increments: {counter3.get_count()}")  # Should be 2
    
    counter3.decrement()
    print(f"After 1 decrement: {counter3.get_count()}")  # Should be 1
    
    print("\n" + "=" * 60)
    print("WHY CLOSURES ARE USEFUL HERE:")
    print("=" * 60)
    print("""
    Closure Benefits:
    1. Encapsulation: The 'count' variable is private - can't be accessed directly
    2. State Management: Each counter instance has its own 'count'
    3. Simplicity: No need to create a class
    4. Functional Style: Works with functional programming paradigms
    
    Closure vs Class:
    - Closure: Lightweight, simple state management, more functional
    - Class: More feature-rich, better for complex objects, more OOP
    
    Key Concept - nonlocal:
    - Without 'nonlocal count', we can only READ the count variable
    - With 'nonlocal count', we can WRITE/MODIFY it
    - This allows the closure to maintain and update state
    """)
    
    print("\n" + "=" * 60)
    print("MULTIPLE INDEPENDENT COUNTERS:")
    print("=" * 60)
    counter_a = create_counter()
    counter_b = create_counter()
    
    counter_a['increment']()
    counter_a['increment']()
    counter_a['increment']()
    
    counter_b['increment']()
    
    print(f"Counter A: {counter_a['get_count']()}")  # Should be 3
    print(f"Counter B: {counter_b['get_count']()}")  # Should be 1
    print("Each counter maintains its own independent state!")
