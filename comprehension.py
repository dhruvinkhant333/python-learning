"""
================================================================================
PYTHON COMPREHENSIONS MASTERCLASS
List Comprehensions | Generator Expressions | Dict/Set Comprehensions
================================================================================
"""

print("=" * 80)
print("PART 1: CONCEPTUAL FOUNDATION")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1a. What IS a list comprehension?
# -----------------------------------------------------------------------------
# A list comprehension is a single expression that BUILDS A LIST by looping
# over an iterable and (optionally) filtering/transforming each item.
#
# It is NOT a different language feature from a for-loop -- it's syntactic
# sugar. Under the hood, Python still loops. The difference is:
#   - A for-loop is a STATEMENT (does something, doesn't produce a value)
#   - A comprehension is an EXPRESSION (produces a value: the new list)
#
# General shape:
#   [ EXPRESSION for ITEM in ITERABLE if CONDITION ]
#     ^output        ^loop var  ^source    ^optional filter

numbers = [1, 2, 3, 4, 5]

# The loop way
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)

# The comprehension way
doubled_comp = [n * 2 for n in numbers]

print("Loop result:        ", doubled_loop)
print("Comprehension result:", doubled_comp)

# -----------------------------------------------------------------------------
# 1b. Why use comprehensions?
# -----------------------------------------------------------------------------
# READABILITY: one line expresses "build a list where each item is f(x)"
#              instead of 3 lines of scaffolding (init, loop, append).
# EFFICIENCY: comprehensions are implemented in C internally and avoid the
#             repeated attribute lookup of `.append()` on every iteration.
#             They are typically 20-30% faster than the equivalent loop.
# INTENT: comprehensions signal "I am transforming/filtering data into a
#         new collection" -- which is EXACTLY what most data science code does.

import timeit

loop_time = timeit.timeit(
    "result = []\nfor n in range(10000): result.append(n*2)", number=1000
)
comp_time = timeit.timeit("[n*2 for n in range(10000)]", number=1000)
print(f"\nLoop time:          {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s  (usually faster)")

# -----------------------------------------------------------------------------
# 1c. Generator expressions -- same syntax, LAZY evaluation
# -----------------------------------------------------------------------------
# A list comprehension builds the ENTIRE list in memory immediately.
# A generator expression builds NOTHING immediately -- it creates a
# "generator object" that produces items ONE AT A TIME, on demand, only
# when you iterate it (in a for-loop, or with next()).
#
# Syntax: replace [ ] with ( )

list_comp = [n * 2 for n in numbers]     # built NOW, fully in memory
gen_exp = (n * 2 for n in numbers)       # nothing built yet -- just a plan

print("\nList comprehension object:", list_comp)
print("Generator expression object:", gen_exp)  # shows <generator ...>, no values yet
print("Values pulled one at a time:", list(gen_exp))  # NOW it runs

# -----------------------------------------------------------------------------
# 1d. Dictionary comprehensions
# -----------------------------------------------------------------------------
# Shape: { KEY_EXPR: VALUE_EXPR for ITEM in ITERABLE if CONDITION }

squares_dict = {n: n * n for n in numbers}
print("\nDict comprehension:", squares_dict)

# -----------------------------------------------------------------------------
# 1e. Set comprehensions
# -----------------------------------------------------------------------------
# Shape: { EXPRESSION for ITEM in ITERABLE if CONDITION }
# Automatically removes duplicates, like any set.

nums_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_doubled = {n * 2 for n in nums_with_dupes} #{} set
print("Set comprehension (dupes removed):", unique_doubled)


print("\n" + "=" * 80)
print("PART 2: STEP-BY-STEP EXAMPLES")
print("=" * 80)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- a) Basic transformation ---
a_result = [x * 2 for x in data]
print("\n(a) Basic [x*2 for x in list]:", a_result)

# --- b) With a condition (filter) ---
b_result = [x for x in data if x > 5]
print("(b) Filter [x for x in list if x > 5]:", b_result)

# --- c) Nested comprehension (flattening / matrix work) ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c_result = [[y * 10 for y in row] for row in matrix]
print("(c) Nested comprehension on matrix:", c_result)

# --- d) Multiple conditions (both must be true -- like chained `and`) ---
d_result = [x for x in data if x > 3 if x % 2 == 0]
# Equivalent to: [x for x in data if x > 3 and x % 2 == 0]
print("(d) Multiple conditions (>3 AND even):", d_result)

# --- e) Dictionary comprehension ---
e_result = {x: x * 2 for x in data}
print("(e) Dict comprehension {x: x*2}:", e_result)

# --- f) Set comprehension ---
f_result = {x * 2 for x in data}
print("(f) Set comprehension {x*2}:", f_result)

# --- g) Generator expression ---
g_result = (x * 2 for x in data)
print("(g) Generator expression (lazy):", g_result)
print("    Consumed via sum():", sum(g_result))  # generators are consumed ONCE

# --- h) Complex transformation: multiple operations chained in one expr ---
words = ["hello", "WORLD", "Python", "AI", "ml"]
h_result = [w.capitalize() + f"({len(w)})" for w in words if len(w) > 2]
print("(h) Complex transform:", h_result)


print("\n" + "=" * 80)
print("PART 3: LOOP vs COMPREHENSION SIDE-BY-SIDE")
print("=" * 80)

# --- Example 1: squares of even numbers ---
print("\n--- Squares of even numbers ---")
# Long way
squares_loop = []
for x in range(1, 11):
    if x % 2 == 0:
        squares_loop.append(x ** 2)
print("Loop:", squares_loop)

# Short way
squares_comp = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Comprehension:", squares_comp)
# WHY preferred: 4 lines -> 1 line, same result, no risk of forgetting
# to initialize the list or mistyping .append()

# --- Example 2: build a lookup dict ---
print("\n--- Word -> length lookup ---")
words2 = ["cat", "elephant", "dog", "hippopotamus"]

lengths_loop = {}
for w in words2:
    lengths_loop[w] = len(w)
print("Loop:", lengths_loop)

lengths_comp = {w: len(w) for w in words2}
print("Comprehension:", lengths_comp)

# --- Example 3: flatten a nested list ---
print("\n--- Flatten nested list ---")
nested = [[1, 2], [3, 4], [5, 6]]

flat_loop = []
for sublist in nested:
    for item in sublist:
        flat_loop.append(item)
print("Loop:", flat_loop)

flat_comp = [item for sublist in nested for item in sublist]
print("Comprehension:", flat_comp)
# Reading order for nested comprehensions = reading order of the equivalent
# nested for-loops, left to right: "for sublist in nested" (outer, first)
# then "for item in sublist" (inner, second)


print("\n" + "=" * 80)
print("PART 4: REAL-WORLD DATA SCIENCE EXAMPLES")
print("=" * 80)

# --- Filtering: remove negative values / outliers ---
sensor_readings = [23.5, -5.2, 41.0, 999.9, 18.3, -1.0, 22.7, 500.0]

# Remove negatives (invalid sensor readings)
valid_readings = [r for r in sensor_readings if r >= 0]
print("\nValid (non-negative) readings:", valid_readings)

# Remove outliers (e.g. anything beyond a sane physical range, say 0-100)
clean_readings = [r for r in sensor_readings if 0 <= r <= 100]
print("Outliers removed (0-100 range):", clean_readings)

# --- Transforming: Celsius to Fahrenheit ---
celsius_temps = [0, 20, 37, 100, -10]
fahrenheit_temps = [c * 9 / 5 + 32 for c in celsius_temps]
print("\nCelsius:", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)

# --- Extracting from dictionaries: student records ---
students = [
    {"name": "Aarav", "gpa": 3.8, "major": "CS"},
    {"name": "Diya", "gpa": 3.2, "major": "EE"},
    {"name": "Kabir", "gpa": 3.9, "major": "CS"},
    {"name": "Isha", "gpa": 2.9, "major": "ME"},
]

names = [s["name"] for s in students]
print("\nAll student names:", names)

cs_students = [s["name"] for s in students if s["major"] == "CS"]
print("CS majors:", cs_students)

# --- Processing lists of lists (e.g. rows from a CSV) ---
csv_rows = [
    ["Aarav", "23", "3.8"],
    ["Diya", "21", "3.2"],
    ["Kabir", "22", "3.9"],
]
# Convert age and GPA columns to proper numeric types
parsed_rows = [[row[0], int(row[1]), float(row[2])] for row in csv_rows]
print("\nParsed CSV rows:", parsed_rows)

# --- Creating a feature matrix (common ML preprocessing step) ---
# e.g. turning raw student records into a numeric feature matrix for a model
feature_matrix = [[s["gpa"], len(s["name"])] for s in students]
print("\nFeature matrix [gpa, name_length]:", feature_matrix)


print("\n" + "=" * 80)
print("PART 5: WHEN TO USE WHAT")
print("=" * 80)

print("""
LIST COMPREHENSION -- use when:
  - You need ALL the results immediately (e.g. to index into it, loop over
    it multiple times, or pass it to something that needs a real list like
    len() or numpy.array()).
  - The dataset is small/medium enough to comfortably fit in memory.

GENERATOR EXPRESSION -- use when:
  - The dataset is huge (millions of rows) and you only need to process
    items ONE AT A TIME (e.g. streaming a large log file, summing a huge
    column) -- you never need all values in memory at once.
  - You're passing directly into a function that consumes an iterable once,
    like sum(), max(), any(), all() -- no need to materialize a list first.
  - Example: sum(x**2 for x in range(10_000_000))  -- never builds a
    10-million-element list, just streams and sums as it goes.

REGULAR FOR-LOOP -- use when:
  - The logic needs multiple statements per iteration (e.g. try/except,
    multiple side effects, logging, updating several variables).
  - You need early exit with break, or complex control flow.
  - The comprehension would become hard to read (see Part 6).
""")

# Demonstration: generator saves memory
import sys
list_version = [x for x in range(100000)]
gen_version = (x for x in range(100000))
print(f"List of 100,000 ints uses:      {sys.getsizeof(list_version):,} bytes")
print(f"Generator (same range) uses:    {sys.getsizeof(gen_version):,} bytes")


print("\n" + "=" * 80)
print("PART 6: COMMON MISTAKES")
print("=" * 80)

print("""
1. READABILITY -- comprehensions that try to do too much become worse than
   a loop. If you need 2+ nested loops AND multiple conditions AND a
   complex expression, switch to a regular loop.

   BAD (hard to read):
     result = [y for x in data for y in x if y > 0 if isinstance(y, int) for z in range(y)]

   BETTER: write it as a loop with clear variable names and comments.

2. MEMORY ISSUES -- using a list comprehension on huge/unbounded data loads
   everything into RAM at once. Prefer a generator expression when you don't
   need the full list simultaneously.

     BAD:  squares = [x**2 for x in range(100_000_000)]   # ~800MB+ in memory
     GOOD: squares = (x**2 for x in range(100_000_000))   # near-zero memory

3. PERFORMANCE -- comprehensions are usually faster than equivalent loops,
   but NOT faster than vectorized operations (e.g. NumPy). Once you reach
   Phase 12+ (NumPy/Pandas), prefer vectorized array ops over comprehensions
   for numeric work at scale -- comprehensions still loop in Python, NumPy
   loops in C.

4. SCOPE ISSUES -- in Python 3, the loop variable inside a comprehension
   does NOT leak into the enclosing scope (unlike a plain for-loop).
""")

# Demonstrating scope isolation
for leaked_var in range(3):
    pass
print("After a normal for-loop, leaked_var still exists:", leaked_var)

try:
    _ = [comp_var for comp_var in range(3)]
    print("comp_var value:", comp_var)
except NameError as e:
    print("After a comprehension, comp_var does NOT exist:", e)


print("\n" + "=" * 80)
print("PART 7: PRACTICE EXERCISES (with solutions)")
print("=" * 80)

# Exercise 1: Filter even numbers from 1-100
ex1 = [n for n in range(1, 101) if n % 2 == 0]
print("\n1) Even numbers 1-100 (first 10 shown):", ex1[:10], "...")

# Exercise 2: Square all numbers in a list
nums = [1, 2, 3, 4, 5]
ex2 = [n ** 2 for n in nums]
print("2) Squares of", nums, "->", ex2)

# Exercise 3: Convert list of temps F to Celsius
temps_f = [32, 68, 98.6, 212]
ex3 = [(f - 32) * 5 / 9 for f in temps_f]
print("3) Fahrenheit", temps_f, "-> Celsius", [round(c, 1) for c in ex3])

# Exercise 4: Extract all names from list of dicts
people = [{"name": "Ravi"}, {"name": "Meera"}, {"name": "Sam"}]
ex4 = [p["name"] for p in people]
print("4) Names extracted:", ex4)

# Exercise 5: Create multiplication table (nested)
ex5 = [[row * col for col in range(1, 6)] for row in range(1, 6)]
print("5) 5x5 multiplication table:")
for row in ex5:
    print("   ", row)

# Exercise 6: Filter and transform in one comprehension
raw = [-4, 15, -2, 33, 7, -9, 20]
ex6 = [n * 10 for n in raw if n > 0]
print("6) Positive numbers x10:", ex6)

# Exercise 7: Find all duplicates in a list
items = [1, 2, 3, 2, 4, 5, 3, 6, 1]
seen = set()
ex7 = list({x for x in items if x in seen or seen.add(x)})
print("7) Duplicates found:", ex7)
# NOTE: this uses the trick where seen.add(x) returns None (falsy), letting
# the `or` short-circuit -- it's clever but borderline unreadable. A regular
# loop with a Counter is clearer for real code; shown here for the exercise.

# Exercise 8: Create dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
ex8 = {k: v for k, v in zip(keys, values)}
print("8) Dict from two lists:", ex8)


print("\n" + "=" * 80)
print("PART 8: MINI-PROJECT -- Student Records Analysis")
print("=" * 80)

# Fake "CSV" data: list of dicts with student records
student_records = [
    {"name": "Aarav", "gpa": 3.8, "credits": 90},
    {"name": "Diya", "gpa": 3.2, "credits": 75},
    {"name": "Kabir", "gpa": 3.9, "credits": 100},
    {"name": "Isha", "gpa": 2.9, "credits": 60},
    {"name": "Rohan", "gpa": 3.6, "credits": 88},
    {"name": "Priya", "gpa": 3.7, "credits": 95},
]

# --- Task 1: Filter students with GPA > 3.5 ---
print("\n--- Task 1: Students with GPA > 3.5 ---")

# Loop way
honor_roll_loop = []
for s in student_records:
    if s["gpa"] > 3.5:
        honor_roll_loop.append(s)
print("Loop:", [s["name"] for s in honor_roll_loop])

# Comprehension way
honor_roll_comp = [s for s in student_records if s["gpa"] > 3.5]
print("Comprehension:", [s["name"] for s in honor_roll_comp])

# --- Task 2: Extract just names ---
print("\n--- Task 2: Extract all names ---")

names_loop = []
for s in student_records:
    names_loop.append(s["name"])
print("Loop:", names_loop)

names_comp = [s["name"] for s in student_records]
print("Comprehension:", names_comp)

# --- Task 3: Calculate a "new GPA" column (e.g. +0.1 grading curve, capped at 4.0) ---
print("\n--- Task 3: Curved GPA (add 0.1, cap at 4.0) ---")

curved_loop = []
for s in student_records:
    new_gpa = min(s["gpa"] + 0.1, 4.0)
    curved_loop.append({"name": s["name"], "curved_gpa": round(new_gpa, 2)})
print("Loop:", curved_loop)

curved_comp = [
    {"name": s["name"], "curved_gpa": round(min(s["gpa"] + 0.1, 4.0), 2)}
    for s in student_records
]
print("Comprehension:", curved_comp)

# --- Task 4: Create dict of name -> GPA ---
print("\n--- Task 4: name -> GPA lookup dict ---")

gpa_lookup_loop = {}
for s in student_records:
    gpa_lookup_loop[s["name"]] = s["gpa"]
print("Loop:", gpa_lookup_loop)

gpa_lookup_comp = {s["name"]: s["gpa"] for s in student_records}
print("Comprehension:", gpa_lookup_comp)

print("""
--- Comparison summary ---
Every "loop way" above takes 3-4 lines and needs a pre-initialized
container (list/dict) plus manual appends/assignments.
Every "comprehension way" is a single expression, reads left-to-right
like a sentence ("give me s['name'] for each s in student_records"),
and is what you'll see constantly in real pandas/numpy-adjacent code.
""")

print("=" * 80)
print("END OF MASTERCLASS -- run sections individually to experiment!")
print("=" * 80)