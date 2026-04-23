# These two do the EXACT same thing:

# Using Closure:
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Using Class:
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count
    

# Example usage:
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1
counterA = Counter()
counterB = Counter()
print(counterA.increment())  # Output: 1
print(counterA.increment())  # Output: 2
print(counterB.increment())  # Output: 1

