"""
NUMPY RESHAPING & RANDOM GENERATION - QUICK REFERENCE
Fast lookup for common operations
"""

import numpy as np

# =============================================================================
# RESHAPING OPERATIONS
# =============================================================================

# Basic reshape
arr = np.arange(12)
arr_2d = arr.reshape(3, 4)          # (12,) → (3, 4)
arr_3d = arr.reshape(2, 3, 2)       # (12,) → (2, 3, 2)

# The -1 parameter (infer dimension)
arr_reshaped = arr.reshape(-1, 4)   # NumPy calculates first dimension: (3, 4)
arr_reshaped = arr.reshape(3, -1)   # NumPy calculates second dimension: (3, 4)
arr_flat = arr.reshape(-1)          # Flatten to 1D: (12,)

# Flatten to 1D
arr_2d = np.arange(12).reshape(3, 4)
flat_copy = arr_2d.flatten()        # Returns COPY (safe!)
flat_view = arr_2d.ravel()          # Returns VIEW (efficient!)
flat_reshape = arr_2d.reshape(-1)   # Returns VIEW

# Add/Remove dimensions
arr = np.array([1, 2, 3])           # Shape: (3,)
expanded_0 = np.expand_dims(arr, axis=0)  # (1, 3)
expanded_1 = np.expand_dims(arr, axis=1)  # (3, 1)

arr_2d = np.array([[1, 2, 3]])      # Shape: (1, 3)
squeezed = np.squeeze(arr_2d)       # (3,) - remove all size-1 dims
squeezed_axis = np.squeeze(arr_2d, axis=0)  # (3,)

# =============================================================================
# CONCATENATION
# =============================================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1D concatenation
result = np.concatenate([a, b])     # [1 2 3 4 5 6]

# 2D concatenation
A = np.array([[1, 2], [3, 4]])      # (2, 2)
B = np.array([[5, 6], [7, 8]])      # (2, 2)

result_v = np.concatenate([A, B], axis=0)  # (4, 2) - vertical
result_h = np.concatenate([A, B], axis=1)  # (2, 4) - horizontal

# Convenient stacking functions
vstacked = np.vstack([A, B])        # Vertical (same as axis=0)
hstacked = np.hstack([A, B])        # Horizontal (same as axis=1)
dstacked = np.dstack([A, B])        # Depth (3rd axis)

# =============================================================================
# SPLITTING
# =============================================================================

arr = np.arange(6)
parts = np.split(arr, 3)            # Split into 3 equal parts
parts = np.split(arr, [2, 4])       # Split at indices 2 and 4

arr_2d = np.arange(12).reshape(3, 4)
split_rows = np.split(arr_2d, 3, axis=0)   # Split 3 rows
split_cols = np.split(arr_2d, 2, axis=1)   # Split 4 columns

# Unequal splits
arr = np.arange(7)
parts = np.array_split(arr, 3)      # Handles 7 elements → 3 parts

# Convenience functions
hsplit = np.hsplit(arr_2d, 2)       # Split columns
vsplit = np.vsplit(arr_2d, 3)       # Split rows

# =============================================================================
# RANDOM NUMBER GENERATION
# =============================================================================

# ALWAYS SET SEED FOR REPRODUCIBILITY!
np.random.seed(42)

# Uniform [0, 1)
rand_uniform = np.random.rand(10)           # Shape (10,)
rand_2d = np.random.rand(3, 4)              # Shape (3, 4)
rand_custom = np.random.uniform(0, 10, 100)  # Custom range

# Normal/Gaussian N(0, 1)
rand_normal = np.random.randn(100)          # Shape (100,)
rand_normal_2d = np.random.randn(10, 5)     # Shape (10, 5)
rand_custom_normal = np.random.normal(loc=100, scale=15, size=1000)

# Random integers
rand_int = np.random.randint(0, 10, 100)    # 0-9, shape (100,)
rand_int_2d = np.random.randint(1, 100, (5, 5))  # (5, 5)

# Random selection
choices = np.random.choice([1, 2, 3, 4, 5], size=10)  # With replacement
unique = np.random.choice(10, size=10, replace=False)  # Without replacement
weighted = np.random.choice([1, 2, 3], size=100, p=[0.5, 0.3, 0.2])

# Shuffle
arr = np.arange(10)
np.random.shuffle(arr)              # In-place shuffle
shuffled = np.random.permutation(arr)  # Return shuffled copy

# =============================================================================
# DISTRIBUTIONS
# =============================================================================

# Uniform distribution
uniform = np.random.uniform(0, 1, 1000)    # [0, 1)

# Normal distribution
normal = np.random.randn(1000)              # Mean=0, Std=1
normal = np.random.normal(loc=0, scale=1, size=1000)

# Binomial (number of successes)
binomial = np.random.binomial(n=10, p=0.5, size=1000)

# Poisson (count of events)
poisson = np.random.poisson(lam=5, size=1000)

# =============================================================================
# PRACTICAL ML PATTERNS
# =============================================================================

# Neural network weight initialization (He)
n_in, n_out = 784, 128
W = np.random.randn(n_in, n_out) * np.sqrt(2 / n_in)
b = np.zeros(n_out)

# Generate synthetic dataset
np.random.seed(42)
X = np.random.randn(1000, 20)       # Features
y = np.random.randint(0, 2, 1000)   # Labels

# Shuffle and split
indices = np.random.permutation(len(X))
X_shuffled = X[indices]
y_shuffled = y[indices]

split_idx = int(0.8 * len(X))
X_train, X_test = X_shuffled[:split_idx], X_shuffled[split_idx:]
y_train, y_test = y_shuffled[:split_idx], y_shuffled[split_idx:]

# Data augmentation (add noise)
noise = np.random.normal(0, 0.1, X_train.shape)
X_augmented = X_train + noise

# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ WRONG: Forget to seed
# r1 = np.random.rand(5)  # Different each time!

# ✓ RIGHT: Always seed
np.random.seed(42)
r1 = np.random.rand(5)  # Same every time

# ❌ WRONG: Wrong reshape size
# arr = np.arange(10)
# arr.reshape(3, 4)  # Error! 10 ≠ 12

# ✓ RIGHT: Use -1 to infer
arr = np.arange(12)
arr.reshape(-1, 4)  # Automatically calculates: (3, 4)

# ❌ WRONG: Modify without realizing side effects
# arr = np.array([[1, 2], [3, 4]])
# view = arr.ravel()
# view[0] = 999  # Modifies original!

# ✓ RIGHT: Use .copy() when unsure
arr = np.array([[1, 2], [3, 4]])
safe = arr.flatten().copy()  # Explicit copy
safe[0] = 999  # Original unchanged

# ❌ WRONG: Separate shuffling of X and y
# X_shuffled = np.random.permutation(X)
# y_shuffled = np.random.permutation(y)  # Different shuffle!

# ✓ RIGHT: Use same indices for both
indices = np.random.permutation(len(X))
X_shuffled = X[indices]
y_shuffled = y[indices]  # Same shuffle order

# =============================================================================
# PERFORMANCE TIPS
# =============================================================================

# reshape() and ravel() are fast (views)
# flatten() is slower (copies) - avoid in tight loops

# Use seedable random generation for reproducible results
# np.random.seed() at start of script

# Pre-allocate arrays instead of building them
# Fast: arr = np.zeros((1000, 1000))
# Slow: arr = []; for i in range(...): arr.append(...)

print("=" * 60)
print("NUMPY RESHAPING & RANDOM GENERATION QUICK REFERENCE LOADED")
print("=" * 60)
print("""
KEY PATTERNS:

1. RESHAPE WITH UNKNOWN DIMENSION:
   arr.reshape(-1, n_features)  # Flexible to any batch size

2. REPRODUCIBLE RANDOM DATA:
   np.random.seed(42)
   X = np.random.randn(n_samples, n_features)

3. SHUFFLE AND SPLIT:
   indices = np.random.permutation(len(X))
   X_train = X[indices[:80%]]
   X_test = X[indices[80%:]]

4. FLATTEN SAFELY:
   safe_flat = arr.flatten()  # Creates copy
   efficient_flat = arr.ravel()  # Creates view (careful!)

5. INITIALIZE NEURAL NET WEIGHTS:
   W = np.random.randn(n_in, n_out) * np.sqrt(2/n_in)
   b = np.zeros(n_out)

Remember: NumPy operations are C-optimized!
Use vectorized operations instead of Python loops.
Always seed for reproducible research!
""")