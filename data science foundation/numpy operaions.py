"""
================================================================================
COMPLETE NUMPY OPERATIONS GUIDE FOR AI/ML
Covers: Arithmetic, Broadcasting, Statistics, Linear Algebra, ML Applications
================================================================================
"""

import numpy as np
import time
from typing import Tuple

print("=" * 80)
print("NUMPY OPERATIONS COMPLETE GUIDE FOR AI/ML")
print("=" * 80)

# =============================================================================
# 1. ELEMENT-WISE ARITHMETIC OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("1. ELEMENT-WISE ARITHMETIC OPERATIONS")
print("=" * 80)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(f"\narr1: {arr1}")
print(f"arr2: {arr2}")

# Addition
result_add = arr1 + arr2
print(f"\nAddition (arr1 + arr2): {result_add}")

# Subtraction
result_sub = arr1 - arr2
print(f"Subtraction (arr1 - arr2): {result_sub}")

# Multiplication (element-wise, NOT matrix multiplication)
result_mul = arr1 * arr2
print(f"Multiplication (arr1 * arr2): {result_mul}")

# Division
result_div = arr2 / arr1
print(f"Division (arr2 / arr1): {result_div}")

# Power
result_pow = arr1 ** 2
print(f"Power (arr1 ** 2): {result_pow}")

# ===== SCALAR OPERATIONS (Broadcasting at work!) =====
print("\n--- Scalar Operations (First example of broadcasting!) ---")
arr = np.array([1, 2, 3, 4, 5])

result_scalar_add = arr + 5
print(f"arr + 5: {result_scalar_add}")
print("  ↳ Broadcasting: scalar 5 becomes [5, 5, 5, 5, 5] then adds element-wise")

result_scalar_mul = arr * 2
print(f"arr * 2: {result_scalar_mul}")
print("  ↳ Each element multiplied by 2")

result_scalar_pow = arr ** 2
print(f"arr ** 2: {result_scalar_pow}")

# =============================================================================
# 2. BROADCASTING (CORE NUMPY CONCEPT!)
# =============================================================================
print("\n" + "=" * 80)
print("2. BROADCASTING - The Heart of NumPy Operations")
print("=" * 80)

print("""
BROADCASTING RULES (in order):
1. If arrays have different # of dimensions, pad the smaller one with 1s on the left
2. Check each dimension: they must be equal OR one must be 1
3. If one dimension is 1, stretch it to match the other (without copying!)

WHY IT MATTERS FOR ML:
- Operate on different-shaped data without explicit loops
- Efficient memory usage (no actual copying)
- Makes ML operations concise and fast
""")

# Example a: (3,) + scalar → (3,)
print("\n--- Example a: (3,) + scalar → (3,) ---")
vec = np.array([1, 2, 3])
scalar = 5
result_a = vec + scalar
print(f"Shape of vec: {vec.shape}")
print(f"Shape of scalar: () [scalar has no shape]")
print(f"vec + scalar: {result_a}")
print(f"Result shape: {result_a.shape}")
print("  ↳ Scalar broadcasts to [5, 5, 5], then adds element-wise")

# Example b: (3,1) + (1,3) → (3,3) (Most important for ML!)
print("\n--- Example b: (3,1) + (1,3) → (3,3) [CRITICAL FOR ML] ---")
col = np.array([[1], [2], [3]])  # Shape: (3, 1)
row = np.array([[10, 20, 30]])   # Shape: (1, 3)
result_b = col + row
print(f"col shape: {col.shape}")
print(f"  col:\n{col}")
print(f"row shape: {row.shape}")
print(f"  row: {row}")
print(f"\ncol + row (broadcasts to (3,3)):")
print(result_b)
print("  ↳ col broadcasts across 3 columns, row broadcasts across 3 rows")

# Example c: (100, 5) - (1, 5) → subtract mean from each column
print("\n--- Example c: (100, 5) - (1, 5) → Subtract column means ---")
data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15]])  # Shape: (3, 5)
means = data.mean(axis=0, keepdims=True)  # Shape: (1, 5)
print(f"data shape: {data.shape}")
print(f"  data:\n{data}")
print(f"means shape: {means.shape}")
print(f"  means: {means}")
centered = data - means
print(f"\ndata - means (broadcasts means to all rows):")
print(centered)
print("  ↳ Each row gets the same (1,5) means subtracted → centering data!")

# Example d: (100, 1) * (1, 5) → Scale each row differently
print("\n--- Example d: (3,1) * (1,5) → Scale rows differently ---")
row_scales = np.array([[1], [2], [3]])  # Shape: (3, 1)
col_weights = np.array([[10, 20, 30, 40, 50]])  # Shape: (1, 5)
print(f"row_scales shape: {row_scales.shape}")
print(f"  row_scales:\n{row_scales}")
print(f"col_weights shape: {col_weights.shape}")
print(f"  col_weights: {col_weights}")
result_d = row_scales * col_weights
print(f"\nrow_scales * col_weights:")
print(result_d)
print("  ↳ Row 0 multiplied by 1, Row 1 by 2, Row 2 by 3")

# =============================================================================
# 3. MATHEMATICAL FUNCTIONS
# =============================================================================
print("\n" + "=" * 80)
print("3. MATHEMATICAL FUNCTIONS")
print("=" * 80)

arr = np.array([1.0, 4.0, 9.0, 16.0])
print(f"\narr: {arr}")

# Square root
sqrt_result = np.sqrt(arr)
print(f"np.sqrt(arr): {sqrt_result}")

# Exponential
exp_arr = np.array([0, 1, 2])
exp_result = np.exp(exp_arr)
print(f"\nnp.exp([0, 1, 2]): {exp_result}")
print("  ↳ Used in sigmoid, softmax in neural networks")

# Logarithm
log_arr = np.array([1, 10, 100])
log_result = np.log(log_arr)  # Natural log (base e)
log10_result = np.log10(log_arr)  # Log base 10
print(f"\nnp.log([1, 10, 100]): {log_result}")
print(f"np.log10([1, 10, 100]): {log10_result}")
print("  ↳ Used in loss functions (cross-entropy)")

# Trigonometric
angles = np.array([0, np.pi/4, np.pi/2, np.pi])
sin_result = np.sin(angles)
cos_result = np.cos(angles)
print(f"\nnp.sin([0, π/4, π/2, π]): {sin_result}")
print(f"np.cos([0, π/4, π/2, π]): {cos_result}")

# Absolute value
abs_arr = np.array([-3, -1, 0, 1, 3])
abs_result = np.abs(abs_arr)
print(f"\nnp.abs([-3, -1, 0, 1, 3]): {abs_result}")
print("  ↳ Used in L1 loss, regularization")

# Rounding
vals = np.array([1.3, 1.5, 1.7, 2.5])
ceil_result = np.ceil(vals)
floor_result = np.floor(vals)
round_result = np.round(vals)
print(f"\nOriginal: {vals}")
print(f"np.ceil(): {ceil_result}")
print(f"np.floor(): {floor_result}")
print(f"np.round(): {round_result}")

# =============================================================================
# 4. STATISTICAL FUNCTIONS
# =============================================================================
print("\n" + "=" * 80)
print("4. STATISTICAL FUNCTIONS")
print("=" * 80)

data_2d = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15]])
print(f"data_2d shape: {data_2d.shape}")
print(f"data_2d:\n{data_2d}")

# Mean (average)
mean_all = np.mean(data_2d)
mean_axis0 = np.mean(data_2d, axis=0)  # Mean down rows (per column)
mean_axis1 = np.mean(data_2d, axis=1)  # Mean across columns (per row)
print(f"\nnp.mean(data_2d)                 = {mean_all:.2f}")
print(f"np.mean(data_2d, axis=0)         = {mean_axis0} [mean per column]")
print(f"np.mean(data_2d, axis=1)         = {mean_axis1} [mean per row]")

# Median (middle value)
median_all = np.median(data_2d)
median_axis0 = np.median(data_2d, axis=0)
print(f"\nnp.median(data_2d)               = {median_all:.2f}")
print(f"np.median(data_2d, axis=0)       = {median_axis0}")

# Standard Deviation (spread around mean)
std_all = np.std(data_2d)
std_axis0 = np.std(data_2d, axis=0)
std_axis1 = np.std(data_2d, axis=1)
print(f"\nnp.std(data_2d)                  = {std_all:.2f}")
print(f"np.std(data_2d, axis=0)          = {std_axis0}")
print(f"np.std(data_2d, axis=1)          = {std_axis1}")

# Variance (standard deviation squared)
var_all = np.var(data_2d)
var_axis0 = np.var(data_2d, axis=0)
print(f"\nnp.var(data_2d)                  = {var_all:.2f}")
print(f"np.var(data_2d, axis=0)          = {var_axis0}")
print("  ↳ Variance = (Std Dev)²")

# Sum
sum_all = np.sum(data_2d)
sum_axis0 = np.sum(data_2d, axis=0)
sum_axis1 = np.sum(data_2d, axis=1)
print(f"\nnp.sum(data_2d)                  = {sum_all}")
print(f"np.sum(data_2d, axis=0)          = {sum_axis0}")
print(f"np.sum(data_2d, axis=1)          = {sum_axis1}")

# Product (multiply all elements)
prod_axis0 = np.prod(data_2d, axis=0)
print(f"\nnp.prod(data_2d, axis=0)         = {prod_axis0}")

# Min and Max
min_all = np.min(data_2d)
max_all = np.max(data_2d)
min_axis0 = np.min(data_2d, axis=0)
max_axis1 = np.max(data_2d, axis=1)
print(f"\nnp.min(data_2d)                  = {min_all}")
print(f"np.max(data_2d)                  = {max_all}")
print(f"np.min(data_2d, axis=0)          = {min_axis0}")
print(f"np.max(data_2d, axis=1)          = {max_axis1}")

# Percentile (value at given percentage)
p25 = np.percentile(data_2d, 25)
p50 = np.percentile(data_2d, 50)  # Same as median
p75 = np.percentile(data_2d, 75)
print(f"\nnp.percentile(data_2d, 25)       = {p25}")
print(f"np.percentile(data_2d, 50)       = {p50} [25th, 50th, 75th percentiles]")
print(f"np.percentile(data_2d, 75)       = {p75}")

# Sort
data_1d = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr = np.sort(data_1d)
sorted_indices = np.argsort(data_1d)  # Indices that would sort the array
print(f"\nOriginal:       {data_1d}")
print(f"np.sort():      {sorted_arr}")
print(f"np.argsort():   {sorted_indices}")

# =============================================================================
# 5. AXIS OPERATIONS (CRITICAL FOR 2D DATA!)
# =============================================================================
print("\n" + "=" * 80)
print("5. AXIS OPERATIONS (Critical for 2D/3D Data!)")
print("=" * 80)

print("""
AXIS MEANINGS:
- axis=0: Operate DOWN (across rows) → returns 1D array of column results
- axis=1: Operate ACROSS (across columns) → returns 1D array of row results
- No axis (default): Flatten entire array, operate on all elements
- axis=None: Same as no axis parameter

For shape (3, 5):
- axis=0: reduces to (5,) [3 rows become 1]
- axis=1: reduces to (3,) [5 columns become 1]
""")

data_3x5 = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15]])
print(f"\ndata shape: {data_3x5.shape}")
print(f"data:\n{data_3x5}")

print("\n--- axis=0 (down, reduces rows) ---")
sum_axis0 = np.sum(data_3x5, axis=0)
print(f"np.sum(axis=0): {sum_axis0} [shape: {sum_axis0.shape}]")
print("  ↳ Sum down each column (3 rows → 1 value per column)")

print("\n--- axis=1 (across, reduces columns) ---")
sum_axis1 = np.sum(data_3x5, axis=1)
print(f"np.sum(axis=1): {sum_axis1} [shape: {sum_axis1.shape}]")
print("  ↳ Sum across each row (5 columns → 1 value per row)")

print("\n--- No axis (flatten entire array) ---")
sum_no_axis = np.sum(data_3x5)
print(f"np.sum(): {sum_no_axis}")
print("  ↳ Single value from all 15 elements")

# =============================================================================
# 6. LINEAR ALGEBRA (FOR ML)
# =============================================================================
print("\n" + "=" * 80)
print("6. LINEAR ALGEBRA (Foundation for Neural Networks)")
print("=" * 80)

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
v = np.array([1, 2])

print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Vector v: {v}")

# Dot product (matrix multiplication) - MOST IMPORTANT for ML!
print("\n--- np.dot() (Matrix Multiplication) ---")
dot_result = np.dot(A, B)
print(f"np.dot(A, B):\n{dot_result}")
print("  ↳ Used in neural network: output = np.dot(input, weights) + bias")

# Vector-matrix multiplication
vec_mat = np.dot(v, A)
print(f"\nnp.dot(v, A): {vec_mat}")
print("  ↳ v is (2,), A is (2,2) → result is (2,)")

# Element-wise multiplication (different from dot!)
elementwise = A * B
print(f"\nA * B (element-wise):\n{elementwise}")
print("  ↳ Different from np.dot()! This is Hadamard product")

# Transpose (flip matrix)
print("\n--- Transpose ---")
print(f"A:\n{A}")
print(f"A.T:\n{A.T}")
print(f"A.T is same as np.transpose(A): {np.array_equal(A.T, np.transpose(A))}")

# Matrix Inverse (solve Ax = b)
print("\n--- Matrix Inverse ---")
try:
    A_inv = np.linalg.inv(A)
    print(f"np.linalg.inv(A):\n{A_inv}")
    identity = np.dot(A, A_inv)
    print(f"A × A⁻¹ (should be identity):\n{identity}")
except np.linalg.LinAlgError:
    print("  ↳ Matrix is singular (not invertible)")

# Determinant (tells if matrix is invertible)
det_A = np.linalg.det(A)
print(f"\nnp.linalg.det(A): {det_A}")
print("  ↳ If det = 0, matrix is not invertible")

# Solve linear equations: Ax = b
print("\n--- Solve Linear Equations ---")
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print(f"Solve Ax = b where A = {A.tolist()}, b = {b.tolist()}")
print(f"x = {x}")
verification = np.dot(A, x)
print(f"Verification: A × x = {verification} (should equal b)")

# =============================================================================
# 7. PRACTICAL ML EXAMPLES
# =============================================================================
print("\n" + "=" * 80)
print("7. PRACTICAL ML EXAMPLES")
print("=" * 80)

# Setup sample data
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]], dtype=float)
print(f"Raw data X shape: {X.shape}")
print(f"X:\n{X}")

# a) Normalize data (Z-score normalization) - Used in most ML models!
print("\n--- a) Z-Score Normalization: (X - mean) / std ---")
X_mean = X.mean(axis=0, keepdims=True)
X_std = X.std(axis=0, keepdims=True)
X_normalized = (X - X_mean) / X_std
print(f"Mean per column: {X_mean}")
print(f"Std per column: {X_std}")
print(f"Normalized X:\n{X_normalized}")
print(f"Verification - normalized mean: {X_normalized.mean(axis=0)}")
print(f"Verification - normalized std: {X_normalized.std(axis=0)}")

# b) Min-Max scaling (0-1 range) - Used for bounded data
print("\n--- b) Min-Max Scaling: (X - min) / (max - min) → [0, 1] ---")
X_min = X.min(axis=0, keepdims=True)
X_max = X.max(axis=0, keepdims=True)
X_minmax = (X - X_min) / (X_max - X_min)
print(f"Min per column: {X_min}")
print(f"Max per column: {X_max}")
print(f"Min-max scaled X:\n{X_minmax}")
print(f"Verification - scaled min: {X_minmax.min(axis=0)}")
print(f"Verification - scaled max: {X_minmax.max(axis=0)}")

# c) Calculate Euclidean distances (L2 norm)
print("\n--- c) Euclidean Distance between points ---")
p1 = np.array([1, 2, 3])
p2 = np.array([4, 5, 6])
distance = np.sqrt(np.sum((p1 - p2) ** 2))
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"Distance: {distance}")
print("  ↳ Used in KNN, clustering, etc.")

# Also using np.linalg.norm (cleaner)
distance_norm = np.linalg.norm(p1 - p2)
print(f"Using np.linalg.norm(): {distance_norm}")

# d) Matrix operations for neural networks
print("\n--- d) Neural Network Forward Pass ---")
X_batch = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])  # 3 samples, 2 features
W = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6]])  # 2 inputs × 3 neurons
b = np.array([0.01, 0.02, 0.03])  # 3 biases

print(f"X_batch shape: {X_batch.shape}")
print(f"W shape: {W.shape}")
print(f"b shape: {b.shape}")

# Forward pass: Z = X @ W + b
Z = np.dot(X_batch, W) + b  # Broadcasting: b added to each row
print(f"\nZ = X @ W + b:")
print(Z)
print(f"Z shape: {Z.shape}")
print("  ↳ 3 samples → 3 neurons output")

# e) Dot product for predictions
print("\n--- e) Making Predictions with Weights ---")
x_single = np.array([1, 2])  # Single sample
prediction = np.dot(x_single, W)  # No need for keepdims
print(f"Single sample: {x_single}")
print(f"Prediction (output): {prediction}")

# =============================================================================
# 8. COMPARISON & LOGICAL OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("8. COMPARISON & LOGICAL OPERATIONS")
print("=" * 80)

arr = np.array([1, 2, 3, 4, 5])
print(f"arr: {arr}")

# Comparison operators (return boolean arrays)
print("\n--- Comparison Operators ---")
print(f"arr > 2:  {arr > 2}")
print(f"arr == 3: {arr == 3}")
print(f"arr != 3: {arr != 3}")
print(f"arr >= 3: {arr >= 3}")

# Logical operations
print("\n--- Logical Operations ---")
cond1 = arr > 2
cond2 = arr < 5
logical_and = np.logical_and(cond1, cond2)
logical_or = np.logical_or(cond1, cond2)
print(f"(arr > 2): {cond1}")
print(f"(arr < 5): {cond2}")
print(f"(arr > 2) AND (arr < 5): {logical_and}")
print(f"(arr > 2) OR (arr < 5):  {logical_or}")

# Combining conditions (alternative syntax)
combined = (arr > 2) & (arr < 5)
print(f"\nAlternative: (arr > 2) & (arr < 5): {combined}")

# Using conditions to filter
print("\n--- Filtering with Conditions ---")
above_3 = arr[arr > 3]
print(f"Values > 3: {above_3}")
between = arr[(arr > 2) & (arr < 5)]
print(f"Values between 2 and 5: {between}")

# =============================================================================
# 9. PRACTICE EXERCISES WITH SOLUTIONS
# =============================================================================
print("\n" + "=" * 80)
print("9. PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 80)

print("\n--- Exercise 1: Element-wise Operations ---")
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
print(f"a = {a}, b = {b}")
print(f"a * b = {a * b}")
print(f"(a + b) * 2 = {(a + b) * 2}")
print(f"a ** b = {a ** b}")

print("\n--- Exercise 2: Fix Broadcasting Shape Mismatch ---")
X = np.random.rand(5, 3)  # 5 samples, 3 features
print(f"X shape: {X.shape}")
# Problem: Subtract column means
col_means = X.mean(axis=0)
print(f"col_means shape: {col_means.shape}")
X_centered = X - col_means  # Broadcasting fixes shape mismatch!
print(f"X_centered shape: {X_centered.shape}")
print(f"X_centered means per column: {X_centered.mean(axis=0)}")

print("\n--- Exercise 3: Statistics ---")
data = np.array([1, 5, 3, 8, 2, 9, 4])
print(f"data: {data}")
print(f"mean: {data.mean():.2f}")
print(f"std:  {data.std():.2f}")
print(f"min:  {data.min()}, max: {data.max()}")
print(f"median: {np.median(data)}")

print("\n--- Exercise 4: Normalize 2D Array (Z-score) ---")
data_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], dtype=float)
print(f"Original:\n{data_2d}")
mean = data_2d.mean()
std = data_2d.std()
normalized = (data_2d - mean) / std
print(f"Normalized:\n{normalized}")
print(f"Normalized mean: {normalized.mean():.2f}, std: {normalized.std():.2f}")

print("\n--- Exercise 5: Matrix Multiplication ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B:\n{result}")

print("\n--- Exercise 6: Axis Operations on 3D Data ---")
data_3d = np.arange(24).reshape(2, 3, 4)  # 2 samples, 3 rows, 4 cols
print(f"3D data shape: {data_3d.shape}")
print(f"Sum along axis=0: {np.sum(data_3d, axis=0).shape}")
print(f"Sum along axis=1: {np.sum(data_3d, axis=1).shape}")
print(f"Sum along axis=2: {np.sum(data_3d, axis=2).shape}")

print("\n--- Exercise 7: Complex Transformation (ML Pipeline) ---")
X = np.random.randn(10, 4)  # 10 samples, 4 features
print(f"Raw data shape: {X.shape}")

# 1. Center
X_centered = X - X.mean(axis=0)
# 2. Scale
X_scaled = X_centered / X_centered.std(axis=0)
# 3. Add polynomial features: include X² terms
X_poly = np.hstack([X_scaled, X_scaled ** 2])
print(f"After augmentation shape: {X_poly.shape}")
print("  ↳ 4 original + 4 squared = 8 features")

# =============================================================================
# 10. MINI-PROJECT: STUDENT EXAM SCORES
# =============================================================================
print("\n" + "=" * 80)
print("10. MINI-PROJECT: STUDENT EXAM ANALYSIS")
print("=" * 80)

# Dataset: 100 students, 3 exams
np.random.seed(42)
num_students = 100
exam_scores = np.random.normal(loc=75, scale=15, size=(num_students, 3))
exam_scores = np.clip(exam_scores, 0, 100)  # Clip to [0, 100]

print(f"\nDataset: {num_students} students × 3 exams")
print(f"Shape: {exam_scores.shape}")
print(f"\nFirst 5 students (scores for Exam 1, 2, 3):")
print(exam_scores[:5])

# ===== CALCULATIONS =====
# 1. Mean score per exam
mean_per_exam = exam_scores.mean(axis=0)
print(f"\n1. Mean score per exam: {mean_per_exam}")

# 2. Std dev per exam
std_per_exam = exam_scores.std(axis=0)
print(f"2. Std deviation per exam: {std_per_exam}")

# 3. Z-score normalization (standardization)
print("\n3. Z-Score Normalized Scores:")
exam_scores_zscore = (exam_scores - mean_per_exam) / std_per_exam
print(f"   Normalized means: {exam_scores_zscore.mean(axis=0)}")
print(f"   Normalized stds: {exam_scores_zscore.std(axis=0)}")

# 4. Min-max scaling to [0, 1]
print("\n4. Min-Max Scaled Scores (0-1 range):")
min_per_exam = exam_scores.min(axis=0)
max_per_exam = exam_scores.max(axis=0)
exam_scores_minmax = (exam_scores - min_per_exam) / (max_per_exam - min_per_exam)
print(f"   Scaled mins: {exam_scores_minmax.min(axis=0)}")
print(f"   Scaled maxs: {exam_scores_minmax.max(axis=0)}")

# 5. Find students above mean
print("\n5. Students Above Mean (per exam):")
above_mean = exam_scores > mean_per_exam
num_above = above_mean.sum(axis=0)
print(f"   # of students above mean: Exam1={num_above[0]}, Exam2={num_above[1]}, Exam3={num_above[2]}")

# 6. Calculate average score per student
student_avg = exam_scores.mean(axis=1)
print(f"\n6. Average Score Per Student (first 10):")
print(f"   {student_avg[:10]}")

# 7. Rank students by average score
student_ranks = np.argsort(-student_avg)  # Negative for descending order
print(f"\n7. Top 5 Students by Average Score:")
for rank, student_id in enumerate(student_ranks[:5], 1):
    print(f"   Rank {rank}: Student {student_id} (avg={student_avg[student_id]:.2f})")

# 8. Calculate pairwise distances between all students
print("\n8. Pairwise Distances Between Students:")
# Using vectorized distance calculation
diff = exam_scores[:5, :] - exam_scores[0:1, :]  # First 5 students vs student 0
distances = np.sqrt((diff ** 2).sum(axis=1))
print(f"   Distance from student 0 to:")
for i, dist in enumerate(distances[:5]):
    print(f"      Student {i}: {dist:.2f}")

# Bonus: Similarity matrix (cosine similarity)
print("\n   Cosine Similarity between first 5 students:")
first_5 = exam_scores[:5]
norms = np.linalg.norm(first_5, axis=1, keepdims=True)
normalized = first_5 / norms
similarity = np.dot(normalized, normalized.T)
print(similarity)

# =============================================================================
# 11. PERFORMANCE BENCHMARKING
# =============================================================================
print("\n" + "=" * 80)
print("11. PERFORMANCE BENCHMARKING (1 Million Rows)")
print("=" * 80)

# Create large dataset
n_rows = 1_000_000
n_cols = 10
large_data = np.random.randn(n_rows, n_cols)

print(f"\nDataset: {n_rows:,} rows × {n_cols} columns")
print(f"Memory usage: {large_data.nbytes / 1e9:.2f} GB")

# Benchmark 1: Mean calculation
start = time.time()
result = large_data.mean(axis=0)
elapsed = time.time() - start
print(f"\n1. np.mean(axis=0):        {elapsed*1000:.3f} ms")

# Benchmark 2: Std calculation
start = time.time()
result = large_data.std(axis=0)
elapsed = time.time() - start
print(f"2. np.std(axis=0):         {elapsed*1000:.3f} ms")

# Benchmark 3: Element-wise operations
start = time.time()
result = large_data + 5
elapsed = time.time() - start
print(f"3. Add scalar:             {elapsed*1000:.3f} ms")

# Benchmark 4: Broadcasting (shape mismatch)
scale = np.random.randn(1, n_cols)
start = time.time()
result = large_data * scale
elapsed = time.time() - start
print(f"4. Broadcasting ({n_rows}x{n_cols}) * (1x{n_cols}): {elapsed*1000:.3f} ms")

# Benchmark 5: Normalization (combined operations)
start = time.time()
mean = large_data.mean(axis=0)
std = large_data.std(axis=0)
result = (large_data - mean) / std
elapsed = time.time() - start
print(f"5. Z-score normalization:  {elapsed*1000:.3f} ms")

# Benchmark 6: Sorting
start = time.time()
result = np.sort(large_data, axis=0)
elapsed = time.time() - start
print(f"6. np.sort(axis=0):        {elapsed*1000:.3f} ms")

# Benchmark 7: Matrix multiplication (smaller matrices)
A = np.random.randn(1000, 1000)
B = np.random.randn(1000, 100)
start = time.time()
result = np.dot(A, B)
elapsed = time.time() - start
print(f"7. Matrix mult (1000×1000)@(1000×100): {elapsed*1000:.3f} ms")

print("\n" + "=" * 80)
print("WHY THESE OPERATIONS MATTER FOR ML:")
print("=" * 80)
print("""
1. BROADCASTING: Eliminates loops, makes vectorized operations possible
   → 100x-1000x faster than Python loops

2. ELEMENT-WISE OPERATIONS: Core to forward/backward passes in neural nets
   → Z = X * W + b uses these at massive scale

3. STATISTICAL FUNCTIONS: Feature normalization is critical preprocessing
   → Poorly scaled features = poor model convergence

4. AXIS OPERATIONS: Handle batch dimensions correctly
   → Compute statistics per sample vs globally has huge impact

5. LINEAR ALGEBRA: Neural networks are matrix operations
   → Forward pass = np.dot(X, W) + b
   → Backprop = matrix derivatives

6. COMPARISON/LOGICAL: Masking, filtering, attention mechanisms
   → Used in data preprocessing and advanced architectures

Remember: NumPy operations are C-optimized!
Use them instead of Python loops for 100-1000x speedup.
""")

print("\n" + "=" * 80)
print("END OF NUMPY OPERATIONS GUIDE")
print("=" * 80)