"""
NUMPY QUICK REFERENCE - Copy-Paste Examples
Fast lookup for common ML operations
"""

import numpy as np

# =============================================================================
# ELEMENT-WISE ARITHMETIC (Copy & Paste Ready)
# =============================================================================
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2          # [5 7 9]
result = arr1 - arr2          # [-3 -3 -3]
result = arr1 * arr2          # [4 10 18]
result = arr1 / arr2          # [0.25 0.4  0.5]
result = arr1 ** 2            # [1 4 9]
result = arr1 + 5             # [6 7 8] - Broadcasting!

# =============================================================================
# BROADCASTING (The Most Important Concept!)
# =============================================================================
# Pattern 1: Scalar + Array
scalar = 5
arr = np.array([1, 2, 3])
result = arr + scalar         # [6 7 8]

# Pattern 2: (3,1) + (1,3) → (3,3)
col = np.array([[1], [2], [3]])        # Shape (3,1)
row = np.array([[10, 20, 30]])         # Shape (1,3)
result = col + row                      # Shape (3,3)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# Pattern 3: Subtract column means (CRITICAL FOR ML!)
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
col_means = data.mean(axis=0, keepdims=True)  # Shape (1, 3)
centered = data - col_means              # Broadcasts (1,3) to (3,3)

# Pattern 4: Scale rows differently
row_scales = np.array([[1], [2], [3]])  # Shape (3,1)
weights = np.array([[10, 20, 30]])      # Shape (1,3)
result = row_scales * weights           # Shape (3,3)

# =============================================================================
# MATHEMATICAL FUNCTIONS
# =============================================================================
arr = np.array([1.0, 4.0, 9.0])

np.sqrt(arr)                  # [1. 2. 3.]
np.exp(np.array([0, 1, 2]))   # [1. 2.72 7.39] - Use in sigmoid
np.log(np.array([1, 10]))     # [0. 2.30] - Use in loss functions
np.sin(np.array([0, np.pi/2]))  # [0. 1.]
np.cos(np.array([0, np.pi]))    # [1. -1.]
np.abs(np.array([-1, 2, -3]))   # [1 2 3]
np.ceil(np.array([1.2, 1.7]))   # [2. 2.]
np.floor(np.array([1.2, 1.7]))  # [1. 1.]
np.round(np.array([1.5, 2.5]))  # [2. 2.]

# =============================================================================
# STATISTICAL FUNCTIONS (Always specify axis for 2D data!)
# =============================================================================
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Without axis: single value
data.mean()                   # 5.0 - mean of all elements
data.std()                    # 2.58 - std of all elements

# axis=0: operate DOWN (per column)
data.mean(axis=0)             # [4. 5. 6.] 
data.std(axis=0)              # [2.45 2.45 2.45]
data.min(axis=0)              # [1 2 3]
data.max(axis=0)              # [7 8 9]

# axis=1: operate ACROSS (per row)
data.mean(axis=1)             # [2. 5. 8.]
data.std(axis=1)              # [0.82 0.82 0.82]

# Other statistics
np.median(data, axis=0)       # [4. 5. 6.]
np.var(data, axis=0)          # [6. 6. 6.] - Variance
np.sum(data, axis=1)          # [6 15 24]
np.prod(data, axis=1)         # [6 120 504] - Product
np.percentile(data, 75)       # 6.5 - 75th percentile
np.sort(data, axis=0)         # Sort along axis

# =============================================================================
# AXIS OPERATIONS (Critical for batches!)
# =============================================================================
data = np.random.randn(100, 32)  # 100 samples, 32 features

# Calculate per-feature mean (normalize data)
mean = data.mean(axis=0)      # Shape (32,) - mean per column
std = data.std(axis=0)        # Shape (32,) - std per column
normalized = (data - mean) / std

# Calculate per-sample statistics
sample_mean = data.mean(axis=1)   # Shape (100,) - mean per row
sample_max = data.max(axis=1)     # Shape (100,) - max per row

# keepdims=True: keeps dimension for broadcasting
mean_keepdims = data.mean(axis=0, keepdims=True)  # Shape (1, 32)
normalized = data - mean_keepdims  # Broadcasting works!

# =============================================================================
# LINEAR ALGEBRA (Neural Networks!)
# =============================================================================
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
v = np.array([1, 2])

# Matrix multiplication (MOST IMPORTANT!)
result = np.dot(A, B)         # 2D @ 2D → 2D
result = A @ B                # Alternative syntax (Python 3.5+)
result = np.dot(v, A)         # 1D @ 2D → 1D

# Element-wise multiplication (different from dot!)
result = A * B                # Hadamard product

# Transpose
A_t = A.T                     # [[1 3] [2 4]]
A_t = np.transpose(A)         # Same thing

# Matrix inverse
A_inv = np.linalg.inv(A)      # A^-1

# Determinant
det = np.linalg.det(A)        # If det=0, matrix not invertible

# Solve Ax = b
b = np.array([5, 6])
x = np.linalg.solve(A, b)     # Solve for x

# =============================================================================
# NEURAL NETWORK OPERATIONS
# =============================================================================
# Forward pass
X = np.random.randn(32, 784)  # 32 samples, 784 features (MNIST)
W = np.random.randn(784, 128) # 784 inputs → 128 neurons
b = np.zeros(128)             # Bias term

# Layer output: Z = X @ W + b
Z = np.dot(X, W) + b          # Shape: (32, 128)
# Note: b broadcasts from (128,) to (32, 128)

# Activation function
A = np.maximum(0, Z)          # ReLU: max(0, Z)
A = 1 / (1 + np.exp(-Z))      # Sigmoid

# Softmax
exp_z = np.exp(Z - Z.max(axis=1, keepdims=True))  # Numerical stability
softmax = exp_z / exp_z.sum(axis=1, keepdims=True)

# =============================================================================
# DATA PREPROCESSING (MOST USED IN ML!)
# =============================================================================
X = np.random.randn(100, 20)  # 100 samples, 20 features

# Z-Score Normalization (Standard!)
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_normalized = (X - X_mean) / X_std

# Min-Max Scaling [0, 1]
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_minmax = (X - X_min) / (X_max - X_min)

# L2 Normalization (unit vectors)
X_norms = np.linalg.norm(X, axis=1, keepdims=True)
X_normalized = X / X_norms

# Remove outliers (keep within mean ± 3*std)
mean, std = X.mean(), X.std()
X_clean = X[(X > mean - 3*std) & (X < mean + 3*std)]

# =============================================================================
# COMPARISON & FILTERING
# =============================================================================
arr = np.array([1, 2, 3, 4, 5])

# Boolean indexing
mask = arr > 3                # [False False False  True  True]
result = arr[mask]            # [4 5]

# Multiple conditions
mask = (arr > 2) & (arr < 5)  # Use & for AND, | for OR
result = arr[mask]            # [3 4]

# Where (conditional selection)
result = np.where(arr > 3, arr, 0)  # [0 0 0 4 5]

# =============================================================================
# DISTANCE & SIMILARITY CALCULATIONS
# =============================================================================
p1 = np.array([1, 2, 3])
p2 = np.array([4, 5, 6])

# Euclidean distance (L2)
dist_l2 = np.sqrt(np.sum((p1 - p2) ** 2))  # 5.196
dist_l2 = np.linalg.norm(p1 - p2)          # Same, cleaner

# Manhattan distance (L1)
dist_l1 = np.sum(np.abs(p1 - p2))          # 9

# Cosine similarity
p1_norm = p1 / np.linalg.norm(p1)
p2_norm = p2 / np.linalg.norm(p2)
cosine_sim = np.dot(p1_norm, p2_norm)      # 0 to 1

# =============================================================================
# ARRAY CREATION (Setup for operations)
# =============================================================================
arr = np.zeros((3, 4))        # 3×4 array of zeros
arr = np.ones((2, 5))         # 2×5 array of ones
arr = np.eye(3)               # 3×3 identity matrix
arr = np.arange(0, 10, 2)     # [0 2 4 6 8]
arr = np.linspace(0, 1, 5)    # [0.00 0.25 0.50 0.75 1.00]
arr = np.random.randn(100, 20)  # 100×20, N(0,1)
arr = np.random.rand(50, 10)  # 50×10, uniform [0,1)
arr = np.random.randint(0, 10, (5, 5))  # 5×5, random ints 0-9

# =============================================================================
# RESHAPING & SLICING
# =============================================================================
arr = np.arange(12)           # [0 1 2 ... 11]

arr = arr.reshape(3, 4)       # (12,) → (3, 4)
arr = arr.flatten()           # (3, 4) → (12,)
arr = arr.ravel()             # Same as flatten

# Concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.concatenate([a, b])  # [1 2 3 4 5 6]
result = np.hstack([a, b])       # Horizontal stack
result = np.vstack([a, b])       # Vertical stack

# Stack along new axis
result = np.stack([a, b])     # [[1 2 3] [4 5 6]]

# =============================================================================
# PERFORMANCE TIPS
# =============================================================================
# DO: Vectorized operations
result = arr1 + arr2          # Fast! C-optimized

# DON'T: Python loops
# for i in range(len(arr1)):  # Slow!
#     result[i] = arr1[i] + arr2[i]

# DO: In-place operations for memory
arr += 5                      # Modifies arr directly (faster)

# DO: Use broadcasting for shape mismatches
data = np.random.randn(1000, 100)
mean = data.mean(axis=0, keepdims=True)  # (1, 100)
centered = data - mean        # Broadcasting (1000, 100) - (1, 100)

# DO: Specify dtype for memory efficiency
arr = np.array([1, 2, 3], dtype=np.int32)  # Smaller than int64
arr = np.array([1.0, 2.0], dtype=np.float32)  # float32 > float64

print("=" * 60)
print("NUMPY QUICK REFERENCE LOADED")
print("=" * 60)
print("""
Run this file to load all examples into memory:
    python numpy_quick_reference.py

Copy any section and modify for your needs!

Key Ideas:
1. Always use vectorized operations (avoid loops!)
2. Specify axis=0 or axis=1 for 2D data operations
3. Use keepdims=True when broadcasting matters
4. Broadcasting: (3,1) + (1,3) → (3,3)
5. Neural networks = matrix ops: Z = X @ W + b
6. Normalize before training: (X - mean) / std
7. NumPy is 100-1000x faster than Python loops!
""")