# Title: The Call Counting Wrapper
# Difficulty: Core
# Topics Used: Closures, Decorators
# Problem Statement: Build a decorator that can be applied to any function and tracks, for that specific function only, how many times it has been called — without using any global variables, and without modifying the function's own return value.
# Input: Decorate two different functions, call one 3 times and the other 2 times, then check each one's individual count.
# Output: The two functions report 3 and 2 respectively, independently of each other.
# Constraints: No global counters. Each decorated function must keep its own count.
# Logic Trigger: Ask yourself where a value could live so it survives between calls but isn't visible from outside.

