"""
================================================================================
NUMPY BASICS MASTERCLASS
Arrays | Creation | Properties | Indexing | Slicing | Boolean & Fancy Indexing
================================================================================
Run this file top to bottom, or copy sections into a REPL / Jupyter cell.
Every section prints its own output so you can SEE what's happening.
"""

import numpy as np

print("=" * 80)
print("PART 1: WHY NUMPY?")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1a. Python lists vs NumPy arrays -- speed and memory
# -----------------------------------------------------------------------------
# A Python list stores a collection of POINTERS to separate Python objects
# scattered around memory. A NumPy array stores raw numbers CONTIGUOUSLY in
# one memory block, all of the SAME data type. This is why NumPy is fast:
#   - No per-element Python object overhead
#   - Operations run in compiled C loops (vectorized), not Python bytecode
#   - CPU cache-friendly (contiguous memory = fewer cache misses)

import time
import sys

size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
list_result = [x * 2 for x in python_list]
list_time = time.time() - start

start = time.time()
array_result = numpy_array * 2
array_time = time.time() - start

print(f"\nPython list comprehension time: {list_time:.5f}s")
print(f"NumPy vectorized operation time: {array_time:.5f}s")
print(f"NumPy is roughly {list_time / array_time:.0f}x faster on this operation")

print(f"\nMemory per element -- Python int object: {sys.getsizeof(1)} bytes")
print(f"Memory per element -- NumPy int64:        {numpy_array.itemsize} bytes")

# -----------------------------------------------------------------------------
# 1b. When to use NumPy
# -----------------------------------------------------------------------------
# Use NumPy whenever you're doing NUMERIC computation on collections of
# numbers: math operations across many values at once, linear algebra,
# statistics, image data (pixels are just number grids), or any data
# that's naturally a matrix/tensor of numbers.
#
# Don't reach for NumPy for: mixed-type collections, text processing,
# small one-off calculations where plain Python is simpler.

# -----------------------------------------------------------------------------
# 1c. How NumPy relates to Pandas and Scikit-learn
# -----------------------------------------------------------------------------
# - Pandas DataFrames are built ON TOP of NumPy arrays -- each column is
#   internally backed by a NumPy array. df.values / df.to_numpy() gives
#   you the raw NumPy array underneath.
# - Scikit-learn models expect input as NumPy arrays (or DataFrames that
#   get converted to NumPy arrays internally). X (features) is typically
#   a 2D NumPy array of shape (n_samples, n_features), and y (target) is
#   a 1D NumPy array of shape (n_samples,).
#
# In short: NumPy is the FOUNDATION that the entire Python data science
# stack (Pandas, Scikit-learn, and even PyTorch/TensorFlow tensors) is
# conceptually built around.

# -----------------------------------------------------------------------------
# 1d. Installation and import
# -----------------------------------------------------------------------------
# Install:  pip install numpy --break-system-packages   (on this system)
# Import (universal convention, always use this alias):
#   import numpy as np
print("\nNumPy version installed:", np.__version__)


print("\n" + "=" * 80)
print("PART 2: ARRAY CREATION -- ALL METHODS")
print("=" * 80)

# --- a) np.array() -- from a Python list ---
a = np.array([1, 2, 3, 4, 5])
print("\n(a) np.array([1,2,3,4,5]):")
print("    Output:", a)
print("    Use case: convert existing Python data (list, tuple) into a fast array")

# 2D version -- from a list of lists
a2d = np.array([[1, 2, 3], [4, 5, 6]])
print("    2D version np.array([[1,2,3],[4,5,6]]):\n", a2d)

# --- b) np.zeros() -- array of zeros ---
b = np.zeros(5)
b2d = np.zeros((3, 4))
print("\n(b) np.zeros(5):", b)
print("    np.zeros((3,4)):\n", b2d)
print("    Use case: pre-allocate an array before filling it in (e.g. results buffer)")

# --- c) np.ones() -- array of ones ---
c = np.ones(5)
c2d = np.ones((2, 3))
print("\n(c) np.ones(5):", c)
print("    np.ones((2,3)):\n", c2d)
print("    Use case: initialize weights/biases, or a mask of 'all included' flags")

# --- d) np.arange() -- like Python's range(), but returns an array ---
d = np.arange(0, 10, 2)  # start, stop (exclusive), step
print("\n(d) np.arange(0, 10, 2):", d)
print("    Use case: generate evenly-STEPPED sequences (e.g. time indices)")

# --- e) np.linspace() -- evenly spaced numbers over an interval ---
e = np.linspace(0, 1, 5)  # start, stop (INCLUSIVE), number of points
print("\n(e) np.linspace(0, 1, 5):", e)
print("    Use case: generate N evenly spaced points for plotting a function")

# --- f) np.logspace() -- evenly spaced numbers on a LOG scale ---
f = np.logspace(0, 3, 4)  # 10^0 to 10^3, 4 points
print("\n(f) np.logspace(0, 3, 4):", f)
print("    Use case: generate hyperparameter search ranges (e.g. learning rates)")

# --- g) np.full() -- array filled with a specific value ---
g = np.full((2, 3), 7)
print("\n(g) np.full((2,3), 7):\n", g)
print("    Use case: initialize an array with a constant default value")

# --- h) np.eye() -- identity matrix ---
h = np.eye(4)
print("\n(h) np.eye(4):\n", h)
print("    Use case: linear algebra (identity transformations, solving systems)")

# --- i) np.random.rand() -- random floats, uniform [0, 1) ---
np.random.seed(42)  # for reproducible output in this demo
i = np.random.rand(3, 3)
print("\n(i) np.random.rand(3,3):\n", i)
print("    Use case: random initialization, simulations, quick synthetic data")

# --- j) np.random.randn() -- random floats, standard normal distribution ---
j = np.random.randn(3, 3)
print("\n(j) np.random.randn(3,3):\n", j)
print("    Use case: initializing neural network weights (normal distribution)")


print("\n" + "=" * 80)
print("PART 3: ARRAY PROPERTIES")
print("=" * 80)

demo_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nDemo 2D array:\n", demo_matrix)

print("\n.shape:", demo_matrix.shape, " -- (rows, columns) = (2, 3)")
print(".size: ", demo_matrix.size, " -- total number of elements (2*3=6)")
print(".dtype:", demo_matrix.dtype, "-- data type of every element")
print(".ndim: ", demo_matrix.ndim, " -- number of dimensions (2D here)")
print(".T (transpose):\n", demo_matrix.T, "\n   -- rows and columns swapped, now shape", demo_matrix.T.shape)


print("\n" + "=" * 80)
print("PART 4: INDEXING (1D ARRAYS)")
print("=" * 80)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print("\nBase array:", arr)

print("arr[0]     (first element):     ", arr[0])
print("arr[-1]    (last element):      ", arr[-1])
print("arr[2:5]   (slice, idx 2 to 4): ", arr[2:5])
print("arr[:3]    (from start):        ", arr[:3])
print("arr[3:]    (to end):            ", arr[3:])
print("arr[::2]   (every 2nd):         ", arr[::2])
print("arr[-3:]   (last 3 elements):   ", arr[-3:])
print("arr[::-1]  (reversed):          ", arr[::-1])


print("\n" + "=" * 80)
print("PART 5: SLICING (2D & 3D ARRAYS)")
print("=" * 80)

# The 2D array we'll reuse throughout this section

matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16],
])
print("\nBase 2D matrix:\n", matrix)

print("\nmatrix[0, :]      (first row):        ", matrix[0, :])
print("matrix[:, 0]      (first column):     ", matrix[:, 0])
print("matrix[0:2, 1:3]  (sub-matrix):\n", matrix[0:2, 1:3])
print("matrix[::2, ::2]  (every 2nd row/col):\n", matrix[::2, ::2])
print("matrix[-1, :]     (last row):         ", matrix[-1, :])

# --- 3D array example ---
cube = np.arange(24).reshape(2, 3, 4)  # 2 "layers", each 3 rows x 4 cols
print("\n3D array (shape 2,3,4):\n", cube)
print("\ncube[0]        (first layer, a 2D matrix):\n", cube[0])
print("cube[0, 1]     (2nd row of the 1st layer):  ", cube[0, 1])
print("cube[0, 1, 2]  (single element):             ", cube[0, 1, 2])
print("cube[:, 0, :]  (1st row from EVERY layer):\n", cube[:, 0, :])


print("\n" + "=" * 80)
print("PART 6: BOOLEAN INDEXING (critical for data filtering!)")
print("=" * 80)
import numpy as np
bool_arr = np.array([3, 8, 1, 12, 5, 20, 7, 15])
print("\nBase array:", bool_arr)

print("\nbool_arr > 5             (the boolean mask itself):", bool_arr > 5)
print("bool_arr[bool_arr > 5]   (elements > 5):            ", bool_arr[bool_arr > 5])

# Combining conditions: MUST use & (not `and`), | (not `or`), and parentheses
# around each condition -- this is one of the most common NumPy gotchas.
print("\nbool_arr[(bool_arr > 5) & (bool_arr < 15)]  (between 5 and 15):",
      bool_arr[(bool_arr > 5) & (bool_arr < 15)])

print("bool_arr[bool_arr % 2 == 0]  (even numbers):", bool_arr[bool_arr % 2 == 0])

# Using a condition to filter, then further process
above_threshold = bool_arr[bool_arr > 10]
doubled_above = above_threshold * 2
print("\nFilter (>10) then transform (x2):", doubled_above)


print("\n" + "=" * 80)
print("PART 7: FANCY INDEXING")
print("=" * 80)

fancy_arr = np.array([100, 200, 300, 400, 500])
print("\nBase array:", fancy_arr)

print("fancy_arr[[0, 2, 4]]  (select specific indices):", fancy_arr[[0, 2, 4]])

# Using an actual array/list of indices (same idea, explicit index array)
indices = np.array([1, 3])
print("fancy_arr[indices] where indices = [1, 3]:", fancy_arr[indices])

# Fancy indexing on a 2D matrix: select specific ROWS by index
print("\nSelecting rows [0, 2] from matrix:\n", matrix[[0, 2]])

# Selecting specific (row, col) PAIRS -- note this is different from a
# sub-matrix: it picks out matrix[0,1], matrix[2,3] as individual elements
print("\nmatrix[[0, 2], [1, 3]]  (element-wise pairs -- picks (0,1) and (2,3)):",
      matrix[[0, 2], [1, 3]])


print("\n" + "=" * 80)
print("PART 8: PRACTICAL EXAMPLES")
print("=" * 80)

np.random.seed(1)  # reproducible synthetic data for this demo

# --- Create a data matrix for ML: 100 samples, 5 features ---
data_matrix = np.random.randn(100, 5) * 10 + 50  # random-ish feature values
print("\nData matrix shape (100 samples, 5 features):", data_matrix.shape)
print("First 3 rows:\n", data_matrix[:3])

# --- Extract specific features (columns) ---
feature_0 = data_matrix[:, 0]
features_1_to_3 = data_matrix[:, 1:3]
print("\nFeature 0 (first 5 values):", feature_0[:5])
print("Features 1-2 (first 3 rows):\n", features_1_to_3[:3])

# --- Filter outliers: values > mean + 2*std, on feature 0 ---
mean_f0 = feature_0.mean()
std_f0 = feature_0.std()
outlier_mask = feature_0 > (mean_f0 + 2 * std_f0)
outliers = feature_0[outlier_mask]
print(f"\nFeature 0 mean={mean_f0:.2f}, std={std_f0:.2f}")
print("Outliers (> mean + 2*std):", outliers)

# --- Select training vs test data (simple index-based split) ---
n_samples = data_matrix.shape[0]
split_point = int(n_samples * 0.8)  # 80% train, 20% test
train_data = data_matrix[:split_point]
test_data = data_matrix[split_point:]
print(f"\nTrain shape: {train_data.shape}, Test shape: {test_data.shape}")

# --- Apply different filters together ---
# e.g. rows where feature_0 is above its mean AND feature_1 is below its mean
combined_filter = (data_matrix[:, 0] > mean_f0) & (data_matrix[:, 1] < data_matrix[:, 1].mean())
filtered_rows = data_matrix[combined_filter]
print(f"\nRows matching combined filter: {filtered_rows.shape[0]} out of {n_samples}")


print("\n" + "=" * 80)
print("PART 9: COMMON MISTAKES")
print("=" * 80)

print("""
1. SHAPE CONFUSION -- (rows, columns). shape[0] is ALWAYS rows, shape[1]
   is ALWAYS columns for a 2D array. It's easy to accidentally transpose
   your mental model when reading .shape output.

2. INDEXING vs SLICING -- arr[2] returns a single ELEMENT (scalar, lower
   dimension). arr[2:3] returns an ARRAY containing that one element
   (same dimension, just length 1). These look similar but behave very
   differently in further operations.

3. COPY vs REFERENCE (VIEWS) -- basic slicing (arr[2:5], matrix[:, 0])
   returns a VIEW into the SAME underlying memory, not a copy. Modifying
   a slice modifies the original array too! Use .copy() when you need an
   independent copy.

4. BOOLEAN INDEXING SYNTAX -- you MUST use & / | (not Python's `and`/`or`)
   and wrap each condition in parentheses: (arr > 5) & (arr < 10). Using
   `and`/`or` on arrays raises a ValueError about ambiguous truth values.
""")

# Demonstrating view vs copy
print("--- View vs copy demo ---")
original = np.array([1, 2, 3, 4, 5])
view_slice = original[1:4]       # this is a VIEW, not independent
view_slice[0] = 999              # modifying the view...
print("Original AFTER modifying the slice:", original, " <- changed too! (shared memory)")

original2 = np.array([1, 2, 3, 4, 5])
copy_slice = original2[1:4].copy()  # explicit copy -- now independent
copy_slice[0] = 999
print("Original AFTER modifying a .copy():", original2, " <- unchanged (independent memory)")

# Demonstrating indexing vs slicing dimension difference
print("\n--- Indexing vs slicing dimension demo ---")
sample = np.array([10, 20, 30])
print("sample[1]   ->", sample[1], " | type/ndim:", type(sample[1]).__name__)
print("sample[1:2] ->", sample[1:2], "| ndim:", sample[1:2].ndim, "(still an array!)")

# Demonstrating the `and`/`or` error on boolean arrays (caught safely here)
print("\n--- Boolean indexing syntax error demo ---")
test_arr = np.array([1, 2, 3, 4, 5])
try:
    bad = test_arr[(test_arr > 1) and (test_arr < 4)]  # WRONG -- raises error
except ValueError as e:
    print("Using `and` on arrays raises:", type(e).__name__, "-", str(e)[:60], "...")
good = test_arr[(test_arr > 1) & (test_arr < 4)]  # CORRECT
print("Using `&` instead works fine:", good)


print("\n" + "=" * 80)
print("PART 10: PRACTICE EXERCISES (with solutions)")
print("=" * 80)

# Exercise 1: Create 1D, 2D, 3D arrays
ex1_1d = np.array([1, 2, 3, 4, 5])
ex1_2d = np.array([[1, 2, 3], [4, 5, 6]])
ex1_3d = np.arange(8).reshape(2, 2, 2)
print("\n1) 1D:", ex1_1d)
print("   2D:\n", ex1_2d)
print("   3D:\n", ex1_3d)

# Exercise 2: Extract elements, rows, columns
ex2_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2) Matrix:\n", ex2_matrix)
print("   Element at [1,2]:", ex2_matrix[1, 2])
print("   Row 0:", ex2_matrix[0, :])
print("   Column 1:", ex2_matrix[:, 1])

# Exercise 3: Slice specific ranges
ex3_arr = np.arange(20)
print("\n3) Array:", ex3_arr)
print("   Slice [5:15:2]:", ex3_arr[5:15:2])

# Exercise 4: Filter arrays with conditions
ex4_arr = np.array([4, 17, 8, 23, 42, 9, 6])
print("\n4) Array:", ex4_arr)
print("   Values > 10:", ex4_arr[ex4_arr > 10])

# Exercise 5: Extract sub-matrices
ex5_matrix = np.arange(1, 26).reshape(5, 5)
print("\n5) 5x5 matrix:\n", ex5_matrix)
print("   Sub-matrix [1:4, 1:4]:\n", ex5_matrix[1:4, 1:4])

# Exercise 6: Use boolean indexing for real data (temperatures example)
temps = np.array([18, 22, 35, 40, 15, 28, 33])
print("\n6) Temperatures:", temps)
print("   Hot days (> 30):", temps[temps > 30])


print("\n" + "=" * 80)
print("PART 11: MINI-PROJECT -- Student Scores Matrix (100 students x 5 subjects)")
print("=" * 80)

np.random.seed(7)
n_students = 100
subjects = ["Math", "Science", "English", "History", "Art"]
scores = np.random.randint(50, 101, size=(n_students, 5))  # scores 50-100

print(f"\nScore matrix shape: {scores.shape}  (rows=students, cols=subjects)")
print("Subjects (columns, in order):", subjects)
print("First 5 students' scores:\n", scores[:5])

# --- Extract a specific student's scores (e.g. student index 42) ---
student_42_scores = scores[42, :]
print("\nStudent #42 scores (all 5 subjects):", student_42_scores)

# --- Get all Math scores (column 0) ---
math_scores = scores[:, 0]
print("\nAll Math scores (first 10 shown):", math_scores[:10])
print("Math average across all students:", round(math_scores.mean(), 2))

# --- Find students scoring > 80 in Math ---
high_math_scorers_mask = math_scores > 80
high_math_scorers_indices = np.where(high_math_scorers_mask)[0]
print(f"\nStudents scoring > 80 in Math: {len(high_math_scorers_indices)} students")
print("Their indices (first 10 shown):", high_math_scorers_indices[:10])

# --- Extract first 30 students, all subjects ---
first_30 = scores[:30, :]
print("\nFirst 30 students, all subjects -- shape:", first_30.shape)

# --- Find top 10 students by average score across all subjects ---
student_averages = scores.mean(axis=1)  # axis=1 -> average ACROSS columns, per row
top_10_indices = np.argsort(student_averages)[::-1][:10]  # sort ascending, reverse, take top 10
print("\nTop 10 student indices (by average score):", top_10_indices)
print("Their averages:", np.round(student_averages[top_10_indices], 2))
print("Their full score rows:\n", scores[top_10_indices])

print("""
--- Key takeaway ---
axis=1 in .mean(axis=1) means "collapse across columns, keep one result
PER ROW" -- i.e. one average per student. axis=0 would instead average
DOWN each column, giving one average per subject across all students.
This axis convention (0=down rows, 1=across columns) is used constantly
in NumPy/Pandas and is worth memorizing early.
""")

subject_averages = scores.mean(axis=0)
print("Subject averages (axis=0, one per subject):")
for subj, avg in zip(subjects, subject_averages):
    print(f"   {subj}: {avg:.2f}")

print("\n" + "=" * 80)
print("END OF MASTERCLASS -- run sections individually to experiment!")
print("=" * 80)