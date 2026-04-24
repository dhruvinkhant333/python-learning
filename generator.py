# TASK 1 : Write a generator called even_numbers that yields even numbers from 0 to n

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
# Example usage:
for num in even_numbers(10):
    print(num)  # Output: 0, 2, 4, 6, 8, 10


