# Topic 7.1: Generators and the `yield` Keyword

# 1. Understanding iterators vs generators
# - An iterator is an object with __iter__() and __next__() methods.
# - A generator is a special kind of iterator created by a function using yield.
# - Generators produce values lazily, one at a time, and keep their state between yields.

# Iterator example:
class CountTo:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Generator equivalent:
def count_to(n):
    current = 0
    while current <= n:
        yield current
        current += 1


# 2. The `yield` keyword (vs `return`)
# - `return` exits the function and sends a final value back.
# - `yield` pauses the function and sends a value back, preserving local state.
# - When the generator resumes, it continues right after the yield statement.

def simple_generator():
    print("Start generator")
    yield 1
    print("Resume generator")
    yield 2
    print("Generator end")


# 3. Generator expressions (lazy version of list comprehensions)
# - Similar syntax to list comprehensions, but values are produced one at a time.
# - Generator expressions use parentheses instead of square brackets.

squares = (x * x for x in range(6))


# 4. `next()` function and StopIteration
# - `next(generator)` retrieves the next item from a generator.
# - When no more values remain, Python raises StopIteration.

def one_two_three():
    yield 1
    yield 2
    yield 3


# 5. Using generators in loops and with functions
# - Generators can be used directly in for loops.
# - Functions can accept generators as input and consume values lazily.

def even_numbers(n):
    """Yield even numbers from 0 to n inclusive."""
    for i in range(0, n + 1, 2):
        yield i


def running_total(numbers):
    """Yield the running total of the provided iterable."""
    total = 0
    for num in numbers:
        total += num
        yield total


def filter_even(numbers):
    """Yield only even numbers from the input iterable."""
    for num in numbers:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    print("--- iterator vs generator ---")
    print("Iterator count to 3:")
    for value in CountTo(3):
        print(value)

    print("Generator count to 3:")
    for value in count_to(3):
        print(value)

    print("\n--- yield vs return ---")
    gen = simple_generator()
    print(next(gen))
    print(next(gen))
    try:
        print(next(gen))
    except StopIteration:
        print("StopIteration raised after generator is exhausted")

    print("\n--- generator expression ---")
    for value in squares:
        print(value)

    print("\n--- next() and StopIteration ---")
    generator = one_two_three()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    try:
        print(next(generator))
    except StopIteration:
        print("No more values")

    print("\n--- using generators in loops and functions ---")
    print("Even numbers up to 10:")
    for num in even_numbers(10):
        print(num)

    print("Running totals for [1,2,3,4]:")
    for total in running_total([1, 2, 3, 4]):
        print(total)

    print("Filtered even numbers from generator:")
    for value in filter_even(range(10)):
        print(value)
