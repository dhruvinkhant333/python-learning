import numpy as np 

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