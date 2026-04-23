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