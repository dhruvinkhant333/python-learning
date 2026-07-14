"""
================================================================================
PYTHON LAMBDA FUNCTIONS MASTERCLASS
Anonymous Functions | map/filter/sorted/reduce | Pandas Use Cases
================================================================================
Run this file top to bottom, or copy sections into a REPL / Jupyter cell.
Every section prints its own output so you can SEE what's happening.
"""

from functools import reduce

print("=" * 80)
print("PART 1: WHAT IS LAMBDA?")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1a. Definition in simple words
# -----------------------------------------------------------------------------
# A lambda is a tiny, unnamed (anonymous) function, written on ONE line,
# that can hold exactly ONE expression. It exists so you can define a
# throwaway function right where you need it, without a formal `def` block.
#
# def double(x):
#     return x * 2
#
# is functionally the same as:
#
# double = lambda x: x * 2

def double_def(x):
    return x * 2

double_lambda = lambda x: x * 2

print("def version:   ", double_def(5))
print("lambda version:", double_lambda(5))

# -----------------------------------------------------------------------------
# 1b. When to use lambda vs a regular function
# -----------------------------------------------------------------------------
# USE LAMBDA when:
#   - The function is used ONCE, often as an argument to another function
#     (map, filter, sorted, key=, apply()).
#   - The logic fits in a single expression (no loops, no multiple statements).
#
# USE A REGULAR FUNCTION (def) when:
#   - You need to reuse the function in multiple places (give it a name).
#   - The logic needs more than one expression, error handling, comments,
#     or a docstring.
#   - Readability matters more than brevity (almost always, for anything
#     non-trivial).

# -----------------------------------------------------------------------------
# 1c. Limitations: single expression only
# -----------------------------------------------------------------------------
# A lambda CANNOT contain:
#   - Multiple statements (no semicolons-as-statements trick either)
#   - Assignments (x = 5)         <- SyntaxError inside a lambda
#   - if/for/while as STATEMENTS  <- only allowed as an inline expression
#     (conditional expressions like `a if cond else b` ARE allowed, since
#      that's an expression, not a statement)
#   - return statements (the expression's value IS the return value,
#     implicitly)

# Valid: conditional EXPRESSION
classify = lambda x: "even" if x % 2 == 0 else "odd"
print("\nClassify 4:", classify(4))
print("Classify 7:", classify(7))

# Invalid (commented out -- this would raise SyntaxError):
# bad_lambda = lambda x: y = x + 1

# -----------------------------------------------------------------------------
# 1d. Why lambda is useful in data science
# -----------------------------------------------------------------------------
# Data science code constantly needs small, one-off transformations applied
# across data: "multiply this column by 2", "keep only rows where age > 21",
# "sort these records by score". Lambda lets you write that transformation
# INLINE, right where you use it (map, filter, sorted, df.apply), instead
# of cluttering your script with a named function you'll only use once.


print("\n" + "=" * 80)
print("PART 2: SYNTAX & STRUCTURE")
print("=" * 80)

# Basic: one argument
basic = lambda x: x * 2
print("\nBasic  lambda x: x*2       ->", basic(5))

# Multiple arguments
multi = lambda x, y: x + y
print("Multi   lambda x, y: x+y    ->", multi(3, 4))

# With a conditional expression
cond = lambda x: x * 2 if x > 5 else x
print("Cond    lambda x: x*2 if x>5 else x ->", cond(10), "|", cond(2))

# No arguments at all
greet = lambda: "Hello"
print("No-arg  lambda: 'Hello'     ->", greet())

# Default argument value
with_default = lambda x, y=10: x + y
print("Default lambda x, y=10: x+y ->", with_default(5), "|", with_default(5, 20))

# Unpacking / *args style
sum_all = lambda *args: sum(args)
print("*args   lambda *args: sum(args) ->", sum_all(1, 2, 3, 4))


print("\n" + "=" * 80)
print("PART 3: REAL EXAMPLES -- SIMPLE TO COMPLEX")
print("=" * 80)

# a) Double a number
a_fn = lambda x: x * 2
print("\na) Double:", a_fn(7))

# b) Add two numbers
b_fn = lambda x, y: x + y
print("b) Add:", b_fn(3, 9))

# c) Square a number
c_fn = lambda x: x ** 2
print("c) Square:", c_fn(6))

# d) Check if even
d_fn = lambda x: x % 2 == 0
print("d) Is even?", d_fn(4), "/", d_fn(7))

# e) Conditional doubling
e_fn = lambda x: x * 2 if x > 5 else x
print("e) Conditional double (threshold 5):", e_fn(8), "/", e_fn(3))

# f) Default arguments -- e.g. apply a tax rate, defaulting to 18%
f_fn = lambda price, tax_rate=0.18: round(price * (1 + tax_rate), 2)
print("f) Price with default 18% tax:", f_fn(100), "| custom 5% tax:", f_fn(100, 0.05))

# g) Complex-ish transformation: normalize a value into a 0-1 range
#    (still ONE expression, just a longer one -- this is near the limit
#     of what should be a lambda before switching to def)
g_fn = lambda x, minimum, maximum: (x - minimum) / (maximum - minimum)
print("g) Normalize 75 in range[0,150]:", round(g_fn(75, 0, 150), 3))


print("\n" + "=" * 80)
print("PART 4: LAMBDA WITH HIGHER-ORDER FUNCTIONS")
print("=" * 80)

# -----------------------------------------------------------------------------
# 4a. map() -- apply a function to every element of an iterable
# -----------------------------------------------------------------------------
# map(function, iterable) returns a MAP OBJECT (lazy, like a generator) --
# wrap in list()/tuple() to see/use the values right away.

nums = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, nums)
print("\nmap doubled:", list(doubled))

# ML use case: scaling a feature (e.g. min-max scaling a list of raw scores)
raw_scores = [10, 25, 40, 55, 70]
scaled = list(map(lambda x: (x - min(raw_scores)) / (max(raw_scores) - min(raw_scores)), raw_scores))
print("map scaling (min-max):", [round(s, 2) for s in scaled])

# -----------------------------------------------------------------------------
# 4b. filter() -- keep only elements where the function returns True
# -----------------------------------------------------------------------------
nums2 = [1, 3, 5, 7, 9, 2, 4]
above_five = filter(lambda x: x > 5, nums2)
print("\nfilter > 5:", list(above_five))

# Data filtering use case: keep only valid (non-null-like) sensor readings
readings = [23.5, -1.0, 40.2, -5.0, 18.9]
valid = list(filter(lambda x: x >= 0, readings))
print("filter valid readings:", valid)

# -----------------------------------------------------------------------------
# 4c. sorted() -- sort using a custom key function
# -----------------------------------------------------------------------------
students = [
    {"name": "Aarav", "age": 22},
    {"name": "Diya", "age": 19},
    {"name": "Kabir", "age": 25},
]
by_age = sorted(students, key=lambda s: s["age"])
print("\nsorted by age:", [s["name"] for s in by_age])

by_age_desc = sorted(students, key=lambda s: s["age"], reverse=True)
print("sorted by age (desc):", [s["name"] for s in by_age_desc])

# -----------------------------------------------------------------------------
# 4d. reduce() -- combine all elements into a single accumulated value
# -----------------------------------------------------------------------------
# reduce is NOT a builtin -- it must be imported from functools.
# reduce(function, iterable) applies function(accumulator, next_item)
# repeatedly, carrying the running result forward.

total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("\nreduce sum:", total)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("reduce product (factorial-style):", product)

# Aggregate use case: find the student with the highest GPA using reduce
gpa_students = [
    {"name": "Aarav", "gpa": 3.8},
    {"name": "Diya", "gpa": 3.2},
    {"name": "Kabir", "gpa": 3.9},
]
top_student = reduce(lambda a, b: a if a["gpa"] > b["gpa"] else b, gpa_students)
print("reduce -> top student:", top_student["name"])
# NOTE: for "find the max by a key", Python's built-in max() with a key=
# is clearer than reduce -- shown for comparison:
top_student_max = max(gpa_students, key=lambda s: s["gpa"])
print("max() equivalent (preferred):", top_student_max["name"])


print("\n" + "=" * 80)
print("PART 5: PANDAS & DATA SCIENCE USE CASES")
print("=" * 80)

print("\n" + "=" * 80)
print("PART 4: LAMBDA WITH HIGHER-ORDER FUNCTIONS")
print("=" * 80)

# -----------------------------------------------------------------------------
# 4a. map() -- apply a function to every element of an iterable
# -----------------------------------------------------------------------------
# map(function, iterable) returns a MAP OBJECT (lazy, like a generator) --
# wrap in list()/tuple() to see/use the values right away.

nums = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, nums)
print("\nmap doubled:", list(doubled))

# ML use case: scaling a feature (e.g. min-max scaling a list of raw scores)
raw_scores = [10, 25, 40, 55, 70]
scaled = list(map(lambda x: (x - min(raw_scores)) / (max(raw_scores) - min(raw_scores)), raw_scores))
print("map scaling (min-max):", [round(s, 2) for s in scaled])

# -----------------------------------------------------------------------------
# 4b. filter() -- keep only elements where the function returns True
# -----------------------------------------------------------------------------
nums2 = [1, 3, 5, 7, 9, 2, 4]
above_five = filter(lambda x: x > 5, nums2)
print("\nfilter > 5:", list(above_five))

# Data filtering use case: keep only valid (non-null-like) sensor readings
readings = [23.5, -1.0, 40.2, -5.0, 18.9]
valid = list(filter(lambda x: x >= 0, readings))
print("filter valid readings:", valid)

# -----------------------------------------------------------------------------
# 4c. sorted() -- sort using a custom key function
# -----------------------------------------------------------------------------
students = [
    {"name": "Aarav", "age": 22},
    {"name": "Diya", "age": 19},
    {"name": "Kabir", "age": 25},
]
by_age = sorted(students, key=lambda s: s["age"])
print("\nsorted by age:", [s["name"] for s in by_age])

by_age_desc = sorted(students, key=lambda s: s["age"], reverse=True)
print("sorted by age (desc):", [s["name"] for s in by_age_desc])

# -----------------------------------------------------------------------------
# 4d. reduce() -- combine all elements into a single accumulated value
# -----------------------------------------------------------------------------
# reduce is NOT a builtin -- it must be imported from functools.
# reduce(function, iterable) applies function(accumulator, next_item)
# repeatedly, carrying the running result forward.

total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("\nreduce sum:", total)

product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("reduce product (factorial-style):", product)

# Aggregate use case: find the student with the highest GPA using reduce
gpa_students = [
    {"name": "Aarav", "gpa": 3.8},
    {"name": "Diya", "gpa": 3.2},
    {"name": "Kabir", "gpa": 3.9},
]
top_student = reduce(lambda a, b: a if a["gpa"] > b["gpa"] else b, gpa_students)
print("reduce -> top student:", top_student["name"])
# NOTE: for "find the max by a key", Python's built-in max() with a key=
# is clearer than reduce -- shown for comparison:
top_student_max = max(gpa_students, key=lambda s: s["gpa"])
print("max() equivalent (preferred):", top_student_max["name"])


print("\n" + "=" * 80)
print("PART 5: PANDAS & DATA SCIENCE USE CASES")
print("=" * 80)

try:
    import pandas as pd

    df = pd.DataFrame({
        "name": ["Aarav", "Diya", "Kabir", "Isha"],
        "age": [22, 19, 25, 20],
        "score": [88, 95, 76, 60],
    })

    print("\nOriginal DataFrame:")
    print(df)

    # df['column'].apply(lambda x: ...) -- transform a column element-wise
    df["score_doubled"] = df["score"].apply(lambda x: x * 2)
    print("\nAfter doubling score with .apply(lambda x: x*2):")
    print(df)

    # Filtering rows using a lambda-based boolean mask
    adults_only = df[df["age"].apply(lambda x: x > 21)]
    print("\nRows where age > 21 (via .apply(lambda)):")
    print(adults_only)

    # Equivalent (and more idiomatic) vectorized filter -- worth knowing:
    adults_only_vectorized = df[df["age"] > 21]
    print("\nSame filter, vectorized (preferred in real pandas code):")
    print(adults_only_vectorized)

    # Sorting a list of dict-like records with sorted() + lambda
    records = df.to_dict("records")
    ranked = sorted(records, key=lambda r: r["score"], reverse=True)
    print("\nRanked by score (desc) via sorted(key=lambda):")
    for r in ranked:
        print("  ", r["name"], r["score"])

except ImportError:
    print("\n(pandas not installed in this environment -- skipping live pandas demo)")
    print("The code above is still 100% correct and will run wherever pandas is installed.")
    print("""
Key patterns to remember:
    df['col'].apply(lambda x: x * 2)                # transform a column
    df[df['age'].apply(lambda x: x > 21)]            # filter rows
    sorted(data, key=lambda x: x['score'], reverse=True)  # rank records
""")


print("\n" + "=" * 80)
print("PART 6: LAMBDA VS REGULAR FUNCTIONS")
print("=" * 80)
try:
    import pandas as pd

    df = pd.DataFrame({
        "name": ["Aarav", "Diya", "Kabir", "Isha"],
        "age": [22, 19, 25, 20],
        "score": [88, 95, 76, 60],
    })

    print("\nOriginal DataFrame:")
    print(df)

    # df['column'].apply(lambda x: ...) -- transform a column element-wise
    df["score_doubled"] = df["score"].apply(lambda x: x * 2)
    print("\nAfter doubling score with .apply(lambda x: x*2):")
    print(df)

    # Filtering rows using a lambda-based boolean mask
    adults_only = df[df["age"].apply(lambda x: x > 21)]
    print("\nRows where age > 21 (via .apply(lambda)):")
    print(adults_only)

    # Equivalent (and more idiomatic) vectorized filter -- worth knowing:
    adults_only_vectorized = df[df["age"] > 21]
    print("\nSame filter, vectorized (preferred in real pandas code):")
    print(adults_only_vectorized)

    # Sorting a list of dict-like records with sorted() + lambda
    records = df.to_dict("records")
    ranked = sorted(records, key=lambda r: r["score"], reverse=True)
    print("\nRanked by score (desc) via sorted(key=lambda):")
    for r in ranked:
        print("  ", r["name"], r["score"])

except ImportError:
    print("\n(pandas not installed in this environment -- skipping live pandas demo)")
    print("The code above is still 100% correct and will run wherever pandas is installed.")
    print("""
Key patterns to remember:
    df['col'].apply(lambda x: x * 2)                # transform a column
    df[df['age'].apply(lambda x: x > 21)]            # filter rows
    sorted(data, key=lambda x: x['score'], reverse=True)  # rank records
""")


print("\n" + "=" * 80)
print("PART 6: LAMBDA VS REGULAR FUNCTIONS")
print("=" * 80)

# --- Example: compute a discounted price ---
print("\n--- Discounted price ---")

# def version
def discounted_price_def(price, discount_pct):
    """Return price after applying a percentage discount."""
    return round(price * (1 - discount_pct / 100), 2)

print("def version:", discounted_price_def(200, 15))

# lambda version
discounted_price_lambda = lambda price, discount_pct: round(price * (1 - discount_pct / 100), 2)
print("lambda version:", discounted_price_lambda(200, 15))

print("""
When to use which:
  - Both work identically here -- it's ONE expression either way.
  - Prefer `def` if this function will be:
        * reused in many places (a name makes it easy to find & reuse)
        * documented with a docstring
        * unit tested directly
        * potentially extended later with more logic
  - Prefer `lambda` if this function:
        * is used ONCE, inline, as an argument (e.g. inside sorted(), map())
        * is short enough that naming it would add more noise than clarity

Readability rule of thumb: if you have to squint or reread a lambda twice
to understand it, it should be a `def` function instead.
""")


print("\n" + "=" * 80)
print("PART 7: COMMON MISTAKES")
print("=" * 80)

print("""
1. TOO COMPLEX LOGIC -- if your lambda needs multiple conditions, nested
   ternaries, or several operations chained together, it's a sign to use
   `def` instead.

   BAD (hard to read):
     process = lambda x: x*2 if x > 10 else (x/2 if x < 0 else x+1 if x == 0 else x)

   BETTER:
     def process(x):
         if x > 10:
             return x * 2
         elif x < 0:
             return x / 2
         elif x == 0:
             return x + 1
         return x

2. FORGETTING LAMBDA CAN'T HAVE STATEMENTS -- no assignments, no `for`/`while`
   loops, no `print()` mixed with logic across multiple lines, no `return`.
   A lambda body must be exactly one expression whose VALUE is returned.

3. SCOPE / LATE-BINDING CLOSURE ISSUES -- a classic trap when creating
   lambdas inside a loop: they capture the VARIABLE, not its value at
   creation time. By the time you call them, the loop variable may have
   already changed to its final value.
""")

# Demonstrating the late-binding closure bug
print("--- Closure bug demo ---")
funcs_bad = []
for i in range(3):
    funcs_bad.append(lambda: i)  # BUG: all these lambdas share the same `i`

print("Bad (all lambdas return the LAST value of i):", [f() for f in funcs_bad])

# Fix: capture the current value as a default argument
funcs_fixed = []
for i in range(3):
    funcs_fixed.append(lambda i=i: i)  # i=i captures the value NOW

print("Fixed (each lambda captures its own i):", [f() for f in funcs_fixed])

print("""
4. PERFORMANCE WITH LARGE DATASETS -- lambda itself is not slower than a
   named function (they compile to the same bytecode kind of object).
   BUT calling any pure-Python function (lambda or def) inside map/filter/
   apply over millions of rows is much slower than a vectorized NumPy/pandas
   operation, because Python re-enters the interpreter for every single
   element. Prefer vectorized operations (df['col'] * 2) over
   df['col'].apply(lambda x: x * 2) once you're working at real ML-data
   scale.
""")


print("\n" + "=" * 80)
print("PART 8: PRACTICE EXERCISES (with solutions)")
print("=" * 80)

# Exercise 1: Double all numbers
ex1 = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print("\n1) Double all:", ex1)

# Exercise 2: Filter evens
ex2 = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print("2) Filter evens:", ex2)

# Exercise 3: Sort by second element of each tuple
ex3 = sorted([(1, 5), (2, 3), (3, 8)], key=lambda x: x[1])
print("3) Sort tuples by 2nd element:", ex3)

# Exercise 4: Find max by a specific criteria (e.g. longest word)
words = ["cat", "elephant", "dog", "hippopotamus", "ox"]
ex4 = max(words, key=lambda w: len(w))
print("4) Longest word:", ex4)

# Exercise 5: Transform list of strings (uppercase)
ex5 = list(map(lambda s: s.upper(), ["hello", "world", "python"]))
print("5) Uppercased:", ex5)

# Exercise 6: Create list of tuples from two lists using map
names = ["Aarav", "Diya", "Kabir"]
scores = [88, 95, 76]
ex6 = list(map(lambda n, s: (n, s), names, scores))
print("6) Zipped via map:", ex6)


print("\n" + "=" * 80)
print("PART 9: MINI-PROJECT -- Student GPA Pipeline")
print("=" * 80)

student_records = [
    {"name": "Leo", "gpa": 3.8},
    {"name": "Aarav", "gpa": 3.2},
    {"name": "Diya", "gpa": 3.9},
    {"name": "Kabir", "gpa": 2.8},
    {"name": "Isha", "gpa": 3.6},
]

print("\nOriginal records:", student_records)

# --- Step 1: map() to double GPAs (silly example, but demonstrates map) ---
doubled_gpas = list(map(lambda s: {"name": s["name"], "gpa": round(s["gpa"] * 2, 2)}, student_records))
print("\n1) GPAs doubled via map():")
for s in doubled_gpas:
    print("  ", s)

# --- Step 2: filter() to get students with GPA > 3.5 ---
high_performers = list(filter(lambda s: s["gpa"] > 3.5, student_records))
print("\n2) Students with GPA > 3.5 via filter():")
for s in high_performers:
    print("  ", s["name"], s["gpa"])

# --- Step 3: sorted() to rank by GPA, highest first ---
ranked = sorted(student_records, key=lambda s: s["gpa"], reverse=True)
print("\n3) Ranked by GPA (desc) via sorted():")
for rank, s in enumerate(ranked, start=1):
    print(f"   #{rank}: {s['name']} ({s['gpa']})")

# --- Step 4: Create new dict of name -> GPA ---
name_to_gpa = dict(map(lambda s: (s["name"], s["gpa"]), student_records))
print("\n4) name -> GPA dict via map():", name_to_gpa)

# Same result, comprehension style (worth comparing -- often preferred
# over map() + dict() for exactly this pattern):
name_to_gpa_comp = {s["name"]: s["gpa"] for s in student_records}
print("   Same result via dict comprehension:", name_to_gpa_comp)

print("""
--- Takeaway ---
map/filter/sorted + lambda are everywhere in real data pipelines, but for
building lists/dicts from scratch, a comprehension is often just as short
and more readable than map()/filter() wrapped in list()/dict(). Lambda
shines brightest as the `key=` argument to sorted()/max()/min(), and as
the throwaway function passed to df.apply().
""")

print("=" * 80)
print("END OF MASTERCLASS -- run sections individually to experiment!")
print("=" * 80) 