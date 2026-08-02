"""
================================================================================
NUMPY RESHAPING & RANDOM NUMBER GENERATION - COMPLETE GUIDE FOR AI/ML
================================================================================
Covers: Reshaping, Concatenation, Splitting, Random Generation, Distributions
Learn how to prepare data and initialize models correctly
"""

import numpy as np
import time
from typing import Tuple

print("=" * 80)
print("NUMPY RESHAPING & RANDOM NUMBER GENERATION - COMPLETE GUIDE")
print("=" * 80)

# =============================================================================
# 1. RESHAPING (Essential for ML Data Preparation!)
# =============================================================================
print("\n" + "=" * 80)
print("1. RESHAPING - Change Array Dimensions")
print("=" * 80)

print("""
RESHAPING CONCEPTS:
- Change dimensions WITHOUT changing data
- Original data order preserved (C-order)
- Important: Total elements must stay the same!
  Example: (6,) can reshape to (2,3), (3,2), (1,6), (6,1)
  But NOT (2,4) - wrong size!
""")

# ===== np.reshape() =====
print("\n--- np.reshape(arr, shape) ---")
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(f"Original 1D array: {arr_1d}")
print(f"Shape: {arr_1d.shape}")

arr_2d = np.reshape(arr_1d, (2, 3))
print(f"\nnp.reshape(arr_1d, (2, 3)):")
print(arr_2d)
print(f"Shape: {arr_2d.shape}")
print("  ↳ 6 elements → (2 rows, 3 columns)")

arr_3d = np.reshape(arr_1d, (1, 2, 3))
print(f"\nnp.reshape(arr_1d, (1, 2, 3)):")
print(arr_3d)
print(f"Shape: {arr_3d.shape}")
print("  ↳ 6 elements → (1 depth, 2 rows, 3 columns)")

# ===== .reshape() method (same operation, different syntax) =====
print("\n--- .reshape() Method (In-place) ---")
arr_reshaped = arr_1d.reshape(3, 2)
print(f"arr_1d.reshape(3, 2):")
print(arr_reshaped)
print(f"Shape: {arr_reshaped.shape}")
print("  ↳ Same result as np.reshape(), different syntax")

# ===== The -1 Parameter (IMPORTANT!) =====
print("\n--- The -1 Parameter (Infer Dimension!) ---")
arr = np.arange(24)  # [0, 1, 2, ..., 23]
print(f"Original array: {arr}")
print(f"Shape: {arr.shape}")

# Reshape to (2, -1): NumPy calculates second dimension
result = arr.reshape(2, -1)
print(f"\narr.reshape(2, -1):")
print(result)
print(f"Result shape: {result.shape}")
print("  ↳ NumPy calculates: 24 / 2 = 12, so shape is (2, 12)")

# Reshape to (-1, 4): NumPy calculates first dimension
result = arr.reshape(-1, 4)
print(f"\narr.reshape(-1, 4):")
print(result)
print(f"Result shape: {result.shape}")
print("  ↳ NumPy calculates: 24 / 4 = 6, so shape is (6, 4)")

# Reshape to (-1,): Flatten to 1D
result = arr.reshape(-1)
print(f"\narr.reshape(-1):")
print(result)
print(f"Result shape: {result.shape}")
print("  ↳ Flattens to 1D (equivalent to .flatten())")

print("\nWHY -1 MATTERS FOR ML:")
print("  When you have unknown batch size: reshape(-1, 784) for MNIST")
print("  -1 automatically adapts to any batch size!")

# ===== np.flatten() - Convert to 1D =====
print("\n--- np.flatten() - Convert to 1D ---")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"Original 2D array:")
print(arr_2d)
print(f"Shape: {arr_2d.shape}")

flattened = arr_2d.flatten()
print(f"\narr_2d.flatten():")
print(flattened)
print(f"Shape: {flattened.shape}")
print("  ↳ Always returns a COPY (not view!)")

# ===== np.ravel() - Flatten (View vs Copy) =====
print("\n--- np.ravel() - Flatten (View vs Copy) ---")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"Original 2D array:")
print(arr_2d)

raveled = arr_2d.ravel()
print(f"\narr_2d.ravel():")
print(raveled)
print(f"  ↳ Returns a VIEW (not copy!) - more memory efficient")

# Proof: modifying ravel output changes original
raveled[0] = 999
print(f"\nAfter raveled[0] = 999:")
print(f"Original arr_2d (modified!):")
print(arr_2d)
print("  ↳ .ravel() is a view, so changes affect original!")

# Restore and show flatten() difference
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr_2d.flatten()
flattened[0] = 999
print(f"\nAfter flattened[0] = 999 (using .flatten()):")
print(f"Original arr_2d (NOT modified!):")
print(arr_2d)
print("  ↳ .flatten() is a copy, original stays unchanged")

# ===== np.expand_dims() - Add Dimension =====
print("\n--- np.expand_dims() - Add a Dimension ---")
arr = np.array([1, 2, 3, 4, 5])
print(f"Original shape: {arr.shape}")
print(f"Original: {arr}")

# Add dimension at axis 0 (prepend)
expanded = np.expand_dims(arr, axis=0)
print(f"\nnp.expand_dims(arr, axis=0):")
print(expanded)
print(f"Shape: {expanded.shape}")
print("  ↳ Added dimension at beginning: (5,) → (1, 5)")

# Add dimension at axis 1 (append)
expanded = np.expand_dims(arr, axis=1)
print(f"\nnp.expand_dims(arr, axis=1):")
print(expanded)
print(f"Shape: {expanded.shape}")
print("  ↳ Added dimension at end: (5,) → (5, 1)")

print("\nWHY THIS MATTERS:")
print("  For broadcasting! (5,) + (5, 1) fails")
print("  But (1, 5) + (5, 1) works via broadcasting!")

# ===== np.squeeze() - Remove Dimensions =====
print("\n--- np.squeeze() - Remove Dimensions ---")
arr = np.array([[[1, 2, 3]]])
print(f"Original shape: {arr.shape}")
print(f"Original: {arr}")

squeezed = np.squeeze(arr)
print(f"\nnp.squeeze(arr):")
print(squeezed)
print(f"Shape: {squeezed.shape}")
print("  ↳ Removed all dimensions of size 1: (1, 1, 3) → (3,)")

# Squeeze specific axis
arr = np.array([[1, 2, 3]])
print(f"\nOriginal: {arr}, shape: {arr.shape}")

squeezed_axis0 = np.squeeze(arr, axis=0)
print(f"np.squeeze(arr, axis=0): {squeezed_axis0}, shape: {squeezed_axis0.shape}")
print("  ↳ Removed dimension at axis 0: (1, 3) → (3,)")

try:
    squeezed_axis1 = np.squeeze(arr, axis=1)
except ValueError as e:
    print(f"Cannot squeeze axis 1: {e}")
    print("  ↳ Can only squeeze dimensions of size 1")

# =============================================================================
# 2. CONCATENATION & SPLITTING
# =============================================================================
print("\n" + "=" * 80)
print("2. CONCATENATION & SPLITTING - Combine and Divide Arrays")
print("=" * 80)

# ===== np.concatenate() - Join Arrays =====
print("\n--- np.concatenate(arrays, axis=0) - Join Arrays ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a: {a}")
print(f"b: {b}")

result = np.concatenate([a, b])
print(f"\nnp.concatenate([a, b]):")
print(result)
print("  ↳ Joined along axis 0 (default for 1D): [1 2 3 4 5 6]")

# 2D concatenation
print("\n--- 2D Concatenation ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A shape: {A.shape}\n{A}")
print(f"B shape: {B.shape}\n{B}")

concat_axis0 = np.concatenate([A, B], axis=0)
print(f"\nnp.concatenate([A, B], axis=0) - Stack vertically:")
print(concat_axis0)
print(f"Shape: {concat_axis0.shape}")
print("  ↳ (2,2) + (2,2) along axis 0 → (4, 2)")

concat_axis1 = np.concatenate([A, B], axis=1)
print(f"\nnp.concatenate([A, B], axis=1) - Stack horizontally:")
print(concat_axis1)
print(f"Shape: {concat_axis1.shape}")
print("  ↳ (2,2) + (2,2) along axis 1 → (2, 4)")

# ===== np.vstack() - Vertical Stack (Rows) =====
print("\n--- np.vstack() - Vertical Stack (Stack Rows) ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a: {a}")
print(f"b: {b}")

vstacked = np.vstack([a, b])
print(f"\nnp.vstack([a, b]):")
print(vstacked)
print(f"Shape: {vstacked.shape}")
print("  ↳ Stacked as rows: (2, 3)")

# ===== np.hstack() - Horizontal Stack (Columns) =====
print("\n--- np.hstack() - Horizontal Stack (Stack Columns) ---")
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
print(f"a shape: {a.shape}\n{a}")
print(f"b shape: {b.shape}\n{b}")

hstacked = np.hstack([a, b])
print(f"\nnp.hstack([a, b]):")
print(hstacked)
print(f"Shape: {hstacked.shape}")
print("  ↳ Stacked as columns: (3, 2)")

# ===== np.dstack() - Depth Stack =====
print("\n--- np.dstack() - Depth Stack (Stack Along 3rd Axis) ---")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(f"a shape: {a.shape}\n{a}")
print(f"b shape: {b.shape}\n{b}")

dstacked = np.dstack([a, b])
print(f"\nnp.dstack([a, b]):")
print(dstacked)
print(f"Shape: {dstacked.shape}")
print("  ↳ (2,2) + (2,2) stacked at depth → (2, 2, 2)")

# ===== np.split() - Divide Array =====
print("\n--- np.split(array, indices_or_sections, axis=0) ---")
arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Original array: {arr}")

# Split into 3 equal parts
split_result = np.split(arr, 3)
print(f"\nnp.split(arr, 3) - Split into 3 equal parts:")
for i, part in enumerate(split_result):
    print(f"  Part {i}: {part}")

# Split at specific indices
split_result = np.split(arr, [2, 4])
print(f"\nnp.split(arr, [2, 4]) - Split at indices 2 and 4:")
for i, part in enumerate(split_result):
    print(f"  Part {i}: {part}")

# ===== 2D Split =====
print("\n--- 2D Split ---")
arr_2d = np.arange(12).reshape(3, 4)
print(f"Original shape: {arr_2d.shape}")
print(arr_2d)

split_rows = np.split(arr_2d, 3, axis=0)
print(f"\nnp.split(arr_2d, 3, axis=0) - Split into 3 rows:")
for i, part in enumerate(split_rows):
    print(f"  Part {i} shape: {part.shape}\n{part}")

# ===== np.array_split() - Unequal Splits =====
print("\n--- np.array_split() - Handle Unequal Splits ---")
arr = np.arange(7)  # 7 elements, can't split into 3 equal parts
print(f"Original array: {arr}")

try:
    result = np.split(arr, 3)
    print("Split succeeded")
except ValueError as e:
    print(f"np.split() fails: {e}")
    print("  ↳ 7 elements can't divide evenly into 3 parts")

# Use array_split for unequal splits
result = np.array_split(arr, 3)
print(f"\nnp.array_split(arr, 3) - Handles unequal splits:")
for i, part in enumerate(result):
    print(f"  Part {i}: {part}")
print("  ↳ Distributes remaining elements across parts")

# ===== np.hsplit() and np.vsplit() =====
print("\n--- np.hsplit() and np.vsplit() (Convenience functions) ---")
arr_2d = np.arange(12).reshape(3, 4)
print(f"Original shape: {arr_2d.shape}\n{arr_2d}")

# Horizontal split (split columns)
hsplit_result = np.hsplit(arr_2d, 2)
print(f"\nnp.hsplit(arr_2d, 2) - Split columns into 2 parts:")
for i, part in enumerate(hsplit_result):
    print(f"  Part {i} shape: {part.shape}\n{part}")

# Vertical split (split rows)
vsplit_result = np.vsplit(arr_2d, 3)
print(f"\nnp.vsplit(arr_2d, 3) - Split rows into 3 parts:")
for i, part in enumerate(vsplit_result):
    print(f"  Part {i} shape: {part.shape}\n{part}")

# =============================================================================
# 3. RANDOM NUMBER GENERATION (For ML Initialization & Simulation)
# =============================================================================
print("\n" + "=" * 80)
print("3. RANDOM NUMBER GENERATION - Initialize & Simulate Data")
print("=" * 80)

# RANDOM NUMBERS

# ├── Generate Random Numbers
# │      │
# │      ├── Floats
# │      │      ├── rand()
# │      │      ├── randn()
# │      │      ├── uniform()
# │      │      └── normal()
# │      │
# │      └── Integers
# │             ├── randint()
# │             └── choice()
# │
# └── Rearrange Existing Data
#        ├── shuffle()
#        └── permutation()


print("""
RANDOM FUNCTIONS OVERVIEW:
- np.random.rand(): Uniform [0, 1)
- np.random.randn(): Standard normal (mean=0, std=1)
- np.random.randint(): Random integers
- np.random.choice(): Random selection
- np.random.normal(): Normal with custom mean/std
- np.random.uniform(): Uniform with custom range
""")

# ===== np.random.seed() - Reproducibility =====
print("\n--- np.random.seed() - Reproducibility (CRITICAL!) ---")
print("\nWithout seed (different each time):")
print(f"Run 1: {np.random.rand(5)}")
print(f"Run 2: {np.random.rand(5)}")

print("\nWith seed (same each time):")
np.random.seed(42)
print(f"Run 1: {np.random.rand(5)}")

np.random.seed(42)  # Reset seed
print(f"Run 2: {np.random.rand(5)}")

print("  ↳ Same seed → same random numbers!")
print("  ↳ Essential for reproducible ML experiments")

# ===== np.random.rand() - Uniform [0, 1) =====
print("\n--- np.random.rand(shape) - Uniform [0, 1) ---")
np.random.seed(42)

rand_1d = np.random.rand(5)
print(f"np.random.rand(5):")
print(rand_1d)
print("  ↳ 5 random values between 0 and 1 (exclusive)")

rand_2d = np.random.rand(3, 4)
print(f"\nnp.random.rand(3, 4) - Shape (3, 4):")
print(rand_2d)

rand_3d = np.random.rand(2, 3, 4)
print(f"\nnp.random.rand(2, 3, 4) - Shape (2, 3, 4):")
print(f"Shape: {rand_3d.shape}")

# ===== np.random.randn() - Standard Normal N(0, 1) =====
print("\n--- np.random.randn(shape) - Standard Normal N(0, 1) ---")
np.random.seed(42)

randn_1d = np.random.randn(5)
print(f"np.random.randn(5):")
print(randn_1d)
print("  ↳ 5 random values from normal distribution")
print(f"  ↳ Mean: {randn_1d.mean():.3f}, Std: {randn_1d.std():.3f}")

randn_2d = np.random.randn(1000, 100)
print(f"\nnp.random.randn(1000, 100) statistics:")
print(f"  Mean: {randn_2d.mean():.4f} (should be ~0)")
print(f"  Std: {randn_2d.std():.4f} (should be ~1)")
print("  ↳ Perfect for neural network weight initialization!")

# ===== np.random.randint() - Random Integers =====
print("\n--- np.random.randint(low, high, size) - Random Integers ---")
np.random.seed(42)

randint_1d = np.random.randint(0, 10, 5)
print(f"np.random.randint(0, 10, 5) - Random ints [0, 10):")
print(randint_1d)

randint_2d = np.random.randint(1, 100, (3, 4))
print(f"\nnp.random.randint(1, 100, (3, 4)) - Random ints [1, 100):")
print(randint_2d)
print(f"Shape: {randint_2d.shape}")

# ===== np.random.choice() - Random Selection =====
print("\n--- np.random.choice(a, size) - Random Selection ---")
np.random.seed(42)

choices = np.random.choice([1, 2, 3, 4, 5], size=10)
print(f"np.random.choice([1,2,3,4,5], size=10):")
print(choices)
print("  ↳ Randomly select 10 values from the list (with replacement)")

# Without replacement
choices_no_replace = np.random.choice(5, size=5, replace=False)
print(f"\nnp.random.choice(5, size=5, replace=False):")
print(choices_no_replace)
print("  ↳ Select 5 unique values from 0-4 (like shuffling)")

# With probabilities
probs = [0.1, 0.2, 0.3, 0.2, 0.2]
choices_prob = np.random.choice([1, 2, 3, 4, 5], size=10, p=probs)
print(f"\nnp.random.choice([1,2,3,4,5], size=10, p={probs}):")
print(choices_prob)
print("  ↳ Higher probability → selected more often")

# ===== np.random.shuffle() - In-Place Shuffle =====
print("\n--- np.random.shuffle() - Shuffle In-Place ---")
arr = np.arange(10)
print(f"Original: {arr}")

np.random.seed(42)
np.random.shuffle(arr)
print(f"After np.random.shuffle(): {arr}")
print("  ↳ Modifies array IN-PLACE!")

# ===== np.random.permutation() - Shuffled Copy =====
print("\n--- np.random.permutation() - Return Shuffled Copy ---")
arr = np.arange(10)
print(f"Original: {arr}")

np.random.seed(42)
shuffled = np.random.permutation(arr)
print(f"After shuffled = np.random.permutation(): {shuffled}")
print(f"Original unchanged: {arr}")
print("  ↳ Returns NEW array (doesn't modify original)")

# ===== np.random.normal() - Normal with Custom Parameters =====
print("\n--- np.random.normal(loc, scale, size) - Custom Normal ---")
np.random.seed(42)

normal_default = np.random.randn(5)
print(f"np.random.randn(5):")
print(normal_default)

normal_custom = np.random.normal(loc=100, scale=15, size=5)
print(f"\nnp.random.normal(loc=100, scale=15, size=5):")
print(normal_custom)
print("  ↳ Mean=100, Std=15 (like IQ scores)")

stats = np.random.normal(loc=100, scale=15, size=10000)
print(f"\nWith 10000 samples:")
print(f"  Mean: {stats.mean():.1f} (target: 100)")
print(f"  Std: {stats.std():.1f} (target: 15)")

# ===== np.random.uniform() - Uniform with Custom Range =====
print("\n--- np.random.uniform(low, high, size) - Custom Uniform ---")
np.random.seed(42)

uniform_default = np.random.rand(5)
print(f"np.random.rand(5) - [0, 1):")
print(uniform_default)

uniform_custom = np.random.uniform(-5, 5, size=5)
print(f"\nnp.random.uniform(-5, 5, size=5):")
print(uniform_custom)
print("  ↳ Custom range: [-5, 5)")

# =============================================================================
# 4. WHY SEEDING MATTERS (Reproducibility in ML)
# =============================================================================
print("\n" + "=" * 80)
print("4. WHY SEEDING MATTERS - Reproducibility in ML")
print("=" * 80)

print("""
WHY SEEDING IS CRITICAL:
1. Reproducibility: Share results, others get same output
2. Debugging: Consistent behavior when tracking down bugs
3. Research: Compare algorithms fairly with same random data
4. Collaboration: Team members run same experiment, same results
""")

print("\n--- EXAMPLE: Train/Test Split Reproducibility ---")

def create_dataset_with_seed(seed):
    """Generate dataset with given seed"""
    np.random.seed(seed)
    X = np.random.randn(100, 5)
    y = np.random.randint(0, 2, 100)
    
    # Shuffle
    indices = np.random.permutation(100)
    X_shuffled = X[indices]
    y_shuffled = y[indices]
    
    # Split
    split_idx = 80
    X_train, X_test = X_shuffled[:split_idx], X_shuffled[split_idx:]
    y_train, y_test = y_shuffled[:split_idx], y_shuffled[split_idx:]
    
    return X_train, X_test, y_train, y_test

# Run with seed 42 twice
X_train1, X_test1, y_train1, y_test1 = create_dataset_with_seed(42)
X_train2, X_test2, y_train2, y_test2 = create_dataset_with_seed(42)

print("Dataset generation with seed=42 (run twice):")
print(f"First run - X_train[0]: {X_train1[0]}")
print(f"Second run - X_train[0]: {X_train2[0]}")
print(f"Are they identical? {np.array_equal(X_train1, X_train2)}")
print("  ↳ Same seed = reproducible results!")

# =============================================================================
# 5. PROBABILITY DISTRIBUTIONS
# =============================================================================
print("\n" + "=" * 80)
print("5. PROBABILITY DISTRIBUTIONS - Choose Wisely for ML")
print("=" * 80)

print("""
COMMON DISTRIBUTIONS IN ML:

1. UNIFORM - Equal probability across range
   When: Random sampling, shuffling, dropout
   np.random.uniform(low, high, size)
   
2. NORMAL/GAUSSIAN - Bell curve distribution
   When: Weight initialization, simulating real-world data
   np.random.randn() or np.random.normal(loc, scale)
   
3. BINOMIAL - Number of successes in n trials
   When: Simulating coin flips, classification labels
   np.random.binomial(n, p, size)
   
4. POISSON - Count of events in fixed interval
   When: Simulating rare events, count data
   np.random.poisson(lam, size)
""")

# ===== Uniform Distribution =====
print("\n--- UNIFORM DISTRIBUTION ---")
np.random.seed(42)

uniform_samples = np.random.uniform(0, 10, 1000)
print(f"np.random.uniform(0, 10, 1000)")
print(f"  Min: {uniform_samples.min():.2f}")
print(f"  Max: {uniform_samples.max():.2f}")
print(f"  Mean: {uniform_samples.mean():.2f} (should be ~5)")
print(f"  Std: {uniform_samples.std():.2f}")
print("  ↳ Flat distribution across [0, 10)")

# ===== Normal Distribution =====
print("\n--- NORMAL (GAUSSIAN) DISTRIBUTION ---")
np.random.seed(42)

# Standard normal
normal_samples = np.random.randn(1000)
print(f"np.random.randn(1000) - Standard normal N(0,1)")
print(f"  Mean: {normal_samples.mean():.4f} (target: 0)")
print(f"  Std: {normal_samples.std():.4f} (target: 1)")

# Custom normal
normal_custom = np.random.normal(loc=70, scale=10, size=1000)
print(f"\nnp.random.normal(loc=70, scale=10, 1000) - Height in cm")
print(f"  Mean: {normal_custom.mean():.2f} (target: 70)")
print(f"  Std: {normal_custom.std():.2f} (target: 10)")

# Why normal for weight initialization
print(f"\nWhy Normal for Neural Network Weights:")
print(f"  He initialization: N(0, sqrt(2/n_in))")
print(f"  Xavier initialization: N(0, sqrt(1/n_in))")
print("  ↳ Proper initialization critical for training!")

# ===== Binomial Distribution =====
print("\n--- BINOMIAL DISTRIBUTION ---")
np.random.seed(42)

# Flip coin 10 times, count heads (p=0.5)
binomial_samples = np.random.binomial(n=10, p=0.5, size=1000)
print(f"np.random.binomial(n=10, p=0.5, size=1000)")
print(f"  Simulates: 1000 experiments of 10 coin flips")
print(f"  Mean: {binomial_samples.mean():.2f} (expect: 5)")
print(f"  Unique values: {np.unique(binomial_samples)}")
print("  ↳ Integer values (# of heads in 10 trials)")

# Simulating classification labels
print(f"\nSimulating binary classification (p=0.3 positive):")
labels = np.random.binomial(n=1, p=0.3, size=1000)
print(f"  Class 0: {(labels == 0).sum()}, Class 1: {(labels == 1).sum()}")
print(f"  Distribution: {(labels == 1).sum() / len(labels):.1%} positive")

# ===== Poisson Distribution =====
print("\n--- POISSON DISTRIBUTION ---")
np.random.seed(42)

# Events per interval (lambda=5 events on average)
poisson_samples = np.random.poisson(lam=5, size=1000)
print(f"np.random.poisson(lam=5, size=1000)")
print(f"  Simulates: Count of events (avg 5 per interval)")
print(f"  Mean: {poisson_samples.mean():.2f} (expect: 5)")
print(f"  Unique values: {sorted(np.unique(poisson_samples))[:10]}... (counts)")
print("  ↳ Used for rare event simulation, count data")

# =============================================================================
# 6. PRACTICAL ML EXAMPLES
# =============================================================================
print("\n" + "=" * 80)
print("6. PRACTICAL ML EXAMPLES - Real-World Usage")
print("=" * 80)

# a) Initialize neural network weights
print("\n--- a) Initialize Neural Network Weights ---")
np.random.seed(42)

n_input = 784   # MNIST: 28×28 = 784
n_hidden = 128  # Hidden layer neurons
n_output = 10   # 10 digit classes

# He initialization: scale by sqrt(2/n_in)
W_he = np.random.randn(n_input, n_hidden) * np.sqrt(2 / n_input)
b_hidden = np.zeros(n_hidden)

print(f"Neural network architecture:")
print(f"  Input: {n_input} → Hidden: {n_hidden} → Output: {n_output}")

print(f"\nWeight matrix (He initialization):")
print(f"  Shape: {W_he.shape}")
print(f"  Mean: {W_he.mean():.4f} (close to 0)")
print(f"  Std: {W_he.std():.4f} (scaled appropriately)")

print(f"\nBias (initialized to 0):")
print(f"  Shape: {b_hidden.shape}")
print(f"  Values: {b_hidden[:5]}... (all zeros)")

# b) Generate training data
print("\n--- b) Generate Synthetic Training Data ---")
np.random.seed(42)

n_samples = 1000
n_features = 20

# Generate features from normal distribution
X_train = np.random.randn(n_samples, n_features)

# Generate labels (binary classification)
y_train = np.random.binomial(n=1, p=0.5, size=n_samples)

print(f"Synthetic training data:")
print(f"  Features: {X_train.shape}")
print(f"  Mean: {X_train.mean():.4f}, Std: {X_train.std():.4f}")
print(f"  Labels: {y_train.shape}")
print(f"  Class 0: {(y_train == 0).sum()}, Class 1: {(y_train == 1).sum()}")

# c) Monte Carlo simulation
print("\n--- c) Monte Carlo Simulation (Estimate π) ---")
np.random.seed(42)

n_simulations = 1_000_000

# Generate random points in [0,1] × [0,1] square
x = np.random.uniform(0, 1, n_simulations)
y = np.random.uniform(0, 1, n_simulations)

# Calculate distance from origin
distance = np.sqrt(x**2 + y**2)

# Count points inside unit circle
inside_circle = (distance <= 1).sum()

# Estimate π
pi_estimate = 4 * inside_circle / n_simulations
print(f"Monte Carlo π estimation ({n_simulations:,} samples):")
print(f"  Points inside circle: {inside_circle:,}")
print(f"  Estimated π: {pi_estimate:.4f}")
print(f"  Actual π: {np.pi:.4f}")
print(f"  Error: {abs(pi_estimate - np.pi):.4f}")

# d) Data augmentation (add noise)
print("\n--- d) Data Augmentation (Add Noise) ---")
np.random.seed(42)

# Original image (small example)
original = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]], dtype=float)
print(f"Original data:\n{original}")

# Add Gaussian noise
noise = np.random.normal(0, 0.1, original.shape)
augmented = original + noise
print(f"\nWith Gaussian noise (std=0.1):\n{augmented.round(2)}")

# Add salt-and-pepper noise (random pixels set to 0 or 1)
augmented_sp = original.copy()
noise_mask = np.random.rand(*original.shape) < 0.1  # 10% of pixels
augmented_sp[noise_mask] = np.random.choice([0, 1], noise_mask.sum())
print(f"\nWith salt-and-pepper noise (10% pixels):\n{augmented_sp}")

# e) Train/test random split
print("\n--- e) Train/Test Random Split (Reproducible) ---")
np.random.seed(42)

# Dataset
n_samples = 100
X = np.random.randn(n_samples, 10)
y = np.random.randint(0, 2, n_samples)

# Shuffle indices
indices = np.random.permutation(n_samples)
X_shuffled = X[indices]
y_shuffled = y[indices]

# Split
split_idx = int(0.8 * n_samples)
X_train, X_test = X_shuffled[:split_idx], X_shuffled[split_idx:]
y_train, y_test = y_shuffled[:split_idx], y_shuffled[split_idx:]

print(f"Original: {n_samples} samples")
print(f"Train: {X_train.shape[0]} samples (80%)")
print(f"Test: {X_test.shape[0]} samples (20%)")
print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# f) Shuffle dataset
print("\n--- f) Shuffle Dataset (In-Place vs Copy) ---")
X = np.arange(10)
y = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(f"Original X: {X}")
print(f"Original y: {y}")

# Option 1: Shuffle indices, apply to both
np.random.seed(42)
indices = np.random.permutation(len(X))
X_shuffled = X[indices]
y_shuffled = y[indices]

print(f"\nShuffled X: {X_shuffled}")
print(f"Shuffled y: {y_shuffled}")
print("  ↳ X and y shuffled together (preserves correspondence)")

# =============================================================================
# 7. COMMON MISTAKES (And How to Avoid Them)
# =============================================================================
print("\n" + "=" * 80)
print("7. COMMON MISTAKES - Avoid These!")
print("=" * 80)

# MISTAKE 1: Forgetting to seed
print("\n--- MISTAKE 1: Forgetting to seed (Non-reproducible) ---")
print("Without seed:")
r1 = np.random.rand(5)
r2 = np.random.rand(5)
print(f"  Run 1: {r1}")
print(f"  Run 2: {r2}")
print(f"  Are they equal? {np.array_equal(r1, r2)}")
print("  ❌ WRONG: Different results every time!")

print("\nWith seed:")
np.random.seed(42)
r1 = np.random.rand(5)
np.random.seed(42)
r2 = np.random.rand(5)
print(f"  Run 1: {r1}")
print(f"  Run 2: {r2}")
print(f"  Are they equal? {np.array_equal(r1, r2)}")
print("  ✓ RIGHT: Same results, reproducible!")

# MISTAKE 2: Wrong reshape size
print("\n--- MISTAKE 2: Wrong reshape size ---")
arr = np.arange(10)
print(f"Array with 10 elements: {arr}")

try:
    result = arr.reshape(3, 4)  # 3*4=12, not 10!
    print(result)
except ValueError as e:
    print(f"  ❌ WRONG: {e}")
    print("  → Total elements must match!")

# Correct:
result = arr.reshape(2, 5)  # 2*5=10 ✓
print(f"  ✓ RIGHT: arr.reshape(2, 5):")
print(result)

# MISTAKE 3: Modifying vs creating new array
print("\n--- MISTAKE 3: Modifying vs creating new array ---")
arr = np.array([[1, 2], [3, 4]])

# Using flatten() - creates new array
flattened = arr.flatten()
flattened[0] = 999
print(f"After modifying flatten(): {arr}")
print("  ✓ CORRECT: Original unchanged (flatten creates copy)")

# Using ravel() - creates view
arr = np.array([[1, 2], [3, 4]])
raveled = arr.ravel()
raveled[0] = 999
print(f"After modifying ravel(): {arr}")
print("  ⚠ WARNING: Original modified! (ravel returns view)")

# Restore
arr[0, 0] = 1

# Using reshape - also creates view
reshaped = arr.reshape(-1)
reshaped[0] = 999
print(f"After modifying reshape(): {arr}")
print("  ⚠ WARNING: Original modified! (reshape returns view)")

print("\nBest practice: Use .copy() if unsure:")
arr = np.array([[1, 2], [3, 4]])
safe_flat = arr.flatten().copy()  # Explicit copy
safe_flat[0] = 999
print(f"After modifying with .copy(): {arr}")
print("  ✓ CORRECT: Original unchanged")

# MISTAKE 4: Reshaping without -1
print("\n--- MISTAKE 4: Not using -1 when shape is unknown ---")
arr = np.arange(24)

# If batch size varies, hardcoding dimension fails!
print("Hardcoding dimensions:")
print(f"  arr.reshape(3, 8) works for this array")
print("  But if arr size changes, reshape breaks!")

print("\nUsing -1:")
result = arr.reshape(-1, 8)
print(f"  arr.reshape(-1, 8) automatically adapts")
print(f"  Shape: {result.shape}")
print("  ✓ CORRECT: Flexible to any batch size!")

# =============================================================================
# 8. PRACTICE EXERCISES WITH SOLUTIONS
# =============================================================================
print("\n" + "=" * 80)
print("8. PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 80)

# Exercise 1: Reshape 1D to 2D and back
print("\n--- Exercise 1: Reshape 1D to 2D and back ---")
arr_1d = np.arange(12)
print(f"Original 1D: {arr_1d}")

arr_2d = arr_1d.reshape(3, 4)
print(f"Reshaped to 2D (3, 4):\n{arr_2d}")

arr_1d_back = arr_2d.reshape(-1)
print(f"Reshaped back to 1D: {arr_1d_back}")
print(f"Matches original? {np.array_equal(arr_1d, arr_1d_back)}")

# Exercise 2: Concatenate multiple arrays
print("\n--- Exercise 2: Concatenate multiple arrays ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat = np.concatenate([a, b, c])
print(f"Concatenate [a, b, c]: {concat}")

vstack = np.vstack([a, b, c])
print(f"Vstack [a, b, c]:\n{vstack}")

# Exercise 3: Split array into train/test
print("\n--- Exercise 3: Split array into train/test ---")
data = np.arange(100)
split_idx = 80

train, test = np.split(data, [split_idx])
print(f"Original: {len(data)} samples")
print(f"Train: {len(train)} samples")
print(f"Test: {len(test)} samples")

# Exercise 4: Generate random data with specific shape
print("\n--- Exercise 4: Generate random data with shape (100, 5) ---")
np.random.seed(42)

X = np.random.randn(100, 5)
print(f"Shape: {X.shape}")
print(f"First 3 samples:\n{X[:3]}")
print(f"Mean per feature: {X.mean(axis=0).round(3)}")
print(f"Std per feature: {X.std(axis=0).round(3)}")

# Exercise 5: Shuffle dataset
print("\n--- Exercise 5: Shuffle dataset ---")
np.random.seed(42)

X = np.arange(10).reshape(5, 2)
y = np.array(['a', 'b', 'c', 'd', 'e'])

print(f"Original X:\n{X}")
print(f"Original y: {y}")

indices = np.random.permutation(len(X))
X_shuffled = X[indices]
y_shuffled = y[indices]

print(f"\nShuffled X:\n{X_shuffled}")
print(f"Shuffled y: {y_shuffled}")

# Exercise 6: Generate from different distributions
print("\n--- Exercise 6: Generate from different distributions ---")
np.random.seed(42)

uniform = np.random.uniform(0, 10, 1000)
normal = np.random.randn(1000)
binomial = np.random.binomial(10, 0.5, 1000)

print(f"Uniform [0, 10]: mean={uniform.mean():.2f}, std={uniform.std():.2f}")
print(f"Normal N(0,1): mean={normal.mean():.2f}, std={normal.std():.2f}")
print(f"Binomial(10, 0.5): mean={binomial.mean():.2f}, std={binomial.std():.2f}")

# Exercise 7: Fix reshape errors
print("\n--- Exercise 7: Fix reshape errors ---")

# Problem: Reshape with wrong size
arr = np.arange(15)

# ❌ WRONG: reshape(3, 4) - size is 12, not 15
# ✓ RIGHT:
result = arr.reshape(3, 5)
print(f"Reshape {arr.shape} to {result.shape}: ✓")

# Problem: Reshape with unknown dimension
# ✓ RIGHT: Use -1
result = arr.reshape(-1, 5)
print(f"Reshape with -1: {result.shape}")

# =============================================================================
# 9. MINI-PROJECT: SYNTHETIC ML DATASET
# =============================================================================
print("\n" + "=" * 80)
print("9. MINI-PROJECT: Generate Synthetic ML Dataset")
print("=" * 80)

np.random.seed(42)

print("\n=== Step 1: Create features (1000 samples, 5 features) ===")
n_samples = 1000
n_features = 5

# Generate from normal distribution
X = np.random.randn(n_samples, n_features)
print(f"Shape: {X.shape}")
print(f"First 3 samples:\n{X[:3]}")
print(f"Mean per feature: {X.mean(axis=0).round(3)}")

print("\n=== Step 2: Generate labels (1000, 1) ===")
# Binary classification
y = np.random.binomial(n=1, p=0.5, size=n_samples)
print(f"Label shape: {y.shape}")
print(f"Class distribution: 0={( y==0).sum()}, 1={(y==1).sum()}")

# Reshape to (1000, 1) for concatenation
y_reshaped = y.reshape(-1, 1)
print(f"Reshaped label: {y_reshaped.shape}")

print("\n=== Step 3: Concatenate features and labels ===")
dataset = np.hstack([X, y_reshaped])
print(f"Full dataset shape: {dataset.shape}")
print(f"First 3 rows (features + label):\n{dataset[:3]}")

print("\n=== Step 4: Shuffle entire dataset ===")
# Get random permutation
indices = np.random.permutation(len(dataset))
dataset_shuffled = dataset[indices]
print(f"Shuffled dataset shape: {dataset_shuffled.shape}")
print(f"First 3 rows after shuffle:\n{dataset_shuffled[:3]}")

print("\n=== Step 5: Split into train (80%) and test (20%) ===")
split_idx = int(0.8 * len(dataset_shuffled))
train_data = dataset_shuffled[:split_idx]
test_data = dataset_shuffled[split_idx:]

print(f"Train set: {train_data.shape}")
print(f"Test set: {test_data.shape}")
print(f"Train/test ratio: {len(train_data)}/{len(test_data)} = {len(train_data)/len(test_data):.2f}")

# Separate features and labels
X_train, y_train = train_data[:, :-1], train_data[:, -1]
X_test, y_test = test_data[:, :-1], test_data[:, -1]

print(f"\nX_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

print("\n=== Step 6: Add noise to simulate real data ===")
# Add small Gaussian noise
noise_level = 0.05
X_train_noisy = X_train + np.random.normal(0, noise_level, X_train.shape)

print(f"Original X_train mean: {X_train.mean():.4f}")
print(f"Noisy X_train mean: {X_train_noisy.mean():.4f}")
print(f"Noise level (std): {noise_level}")

print("\n=== Step 7: Verify reproducibility with seed ===")
# Re-generate with same seed
np.random.seed(42)
X_check = np.random.randn(n_samples, n_features)
print(f"First element of original X: {X[0, 0]:.4f}")
print(f"First element of re-generated X: {X_check[0, 0]:.4f}")
print(f"Reproducible? {np.array_equal(X, X_check)}")

print("\n=== Summary ===")
print(f"✓ Created synthetic ML dataset")
print(f"  - Features: {X_train.shape[0]} train + {X_test.shape[0]} test samples")
print(f"  - Dimensions: {n_features} features per sample")
print(f"  - Labels: Binary classification (0/1)")
print(f"  - Reproducible: seed ensures same results")

# =============================================================================
# 10. PERFORMANCE BENCHMARKING
# =============================================================================
print("\n" + "=" * 80)
print("10. PERFORMANCE BENCHMARKING - Random Number Generation")
print("=" * 80)

print("\nGenerating random data of different sizes...")

# Benchmark 1: Small dataset (1M elements)
n_elements_small = 1_000_000
start = time.time()
data_small = np.random.randn(n_elements_small)
elapsed_small = time.time() - start
print(f"\n1. np.random.randn(1,000,000):")
print(f"   Time: {elapsed_small*1000:.2f} ms")

# Benchmark 2: Large dataset (100M elements)
n_elements_large = 100_000_000
start = time.time()
data_large = np.random.randn(n_elements_large)
elapsed_large = time.time() - start
print(f"\n2. np.random.randn(100,000,000):")
print(f"   Time: {elapsed_large*1000:.2f} ms")
print(f"   Memory: {data_large.nbytes / 1e9:.2f} GB")

# Benchmark 3: Different distributions
print(f"\n3. Time comparison (1M elements):")
distributions = [
    ("randn (normal)", lambda s: np.random.randn(s)),
    ("rand (uniform)", lambda s: np.random.rand(s)),
    ("randint", lambda s: np.random.randint(0, 100, s)),
]

for name, func in distributions:
    start = time.time()
    func(n_elements_small)
    elapsed = time.time() - start
    print(f"   {name:20s}: {elapsed*1000:.2f} ms")

# Benchmark 4: Reshape operations
print(f"\n4. Reshape operations (1M elements):")
data = np.arange(1000000)

operations = [
    ("reshape(-1)", lambda d: d.reshape(-1)),
    ("reshape(1000, 1000)", lambda d: d.reshape(1000, 1000)),
    ("reshape(100, 100, 100)", lambda d: d.reshape(100, 100, 100)),
    ("flatten", lambda d: d.flatten()),
    ("ravel", lambda d: d.ravel()),
]

for name, func in operations:
    start = time.time()
    func(data)
    elapsed = time.time() - start
    print(f"   {name:30s}: {elapsed*1000:.2f} ms")

print("\n" + "=" * 80)
print("WHY THIS MATTERS FOR ML:")
print("=" * 80)
print("""
1. RESHAPING: Essential for batch processing
   - Different frameworks expect different shapes
   - TensorFlow: (batch, height, width, channels)
   - PyTorch: (batch, channels, height, width)
   - -1 parameter is your friend!

2. RANDOM GENERATION: Critical for:
   - Weight initialization (determines training success)
   - Data augmentation (improve model robustness)
   - Train/test splits (ensure fair evaluation)
   - Simulations and experiments

3. SEEDING: Non-negotiable for:
   - Reproducible research
   - Sharing results with collaborators
   - Debugging (consistent behavior)
   - Publication (reviewers can replicate)

4. CONCATENATION/SPLITTING:
   - Combine features, labels, metadata
   - Organize batch data
   - Create train/val/test sets

5. PERFORMANCE:
   - Random generation: ~1ms for 1M elements
   - Reshape: ~0.1-1ms for 1M elements
   - NumPy operations are extremely fast!
""")

print("\n" + "=" * 80)
print("END OF RESHAPING & RANDOM GENERATION GUIDE")
print("=" * 80)