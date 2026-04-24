# TASK 1 : Write a generator called even_numbers that yields even numbers from 0 to n

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
# Example usage:
for num in even_numbers(10):
    print(num)  # Output: 0, 2, 4, 6, 8, 10

# TASK 2 : Write a generator called running_total that takes a list of numbers and yields the running sum at each step:

def running_total(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
# Example usage:
for total in running_total([1, 2, 3, 4]):
    print(total)  # Output: 1, 3, 6, 10
