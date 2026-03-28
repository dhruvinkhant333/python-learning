#Task 1 (Easy)
#Write a closure called make_greeter that remembers a greeting word:

def make_greeter(greeting):
    def greeter (name):
        return f"{greeting} ,{name}"
    return greeter


hello = make_greeter("Hello")
hi = make_greeter("Hi")

print(hello("Arjun"))   # Hello, Arjun!



#Task 2 (Medium)
#Write a closure called make_calculator that remembers a starting number and
#returns an add and subtract function:

def make_calculator(starting_number):
    number = starting_number

    def add(amount):
        nonlocal number 
        number += amount
        return number 
    
    def subtrack(amount):
        nonlocal number 
        number -= amount
        return number 
    return add , subtrack

add, subtract = make_calculator(100)

print (add(50))       # Result: 150
print(subtract(30))  # Result: 120
