import time

#Task 1 (Easy)
#Write a decorator called uppercase that makes any function's 
# string return value uppercase@uppercase

def uppercase(func):
    def wrapper(*args , **kwargs):
        result = func(*args , **kwargs)

        if (result ,str):
            result = result.upper()
        return result 
    return wrapper 
    
@uppercase 
def greet(name):
    return f"hello {name}"

print(greet("arjun"))   # Should print: HELLO ARJUN


#Task 3 (Hard)
#Write a decorator called timer that prints how long the function took 
# to run in mi(lliseconds. Use the time module.

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()

        ms = ( end - start )* 1000
        print(f"executed in {ms:.2f}ms")
        return result
    return wrapper
    
@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

print (f"final result : {slow_function()}")
# Should print: "Executed in X ms"



def repeat(n):
    def decoder(func):

        def wrapper(*args, **kwargs):
         for i in range(n):
            func(*args, **kwargs)
        return wrapper
    return decoder

@repeat(5)
def say(msg):
    print(msg)

say("Python!")


def smart_timer(n):
    def decorator(func):
        def wrapper(*args , **kwargs):
            times = []
            for i in range(n):

                start = time.time()
                result = func(*args , **kwargs)
                end = time.time()

                final_time = (end - start)*1000
                times.append(final_time)
                print(f" Run {i +1} : {final_time: .2f} ms ")
                
        
            print(f"Average : {sum(times)/len(times)}")   
            return result 
        return wrapper 
    return decorator 

@smart_timer(3)
def calculate():
    total = 0
    for i in range(500000):
        total += i
    return total

calculate()