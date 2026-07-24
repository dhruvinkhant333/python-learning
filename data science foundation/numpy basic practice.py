# ---------------------------------------------------------------------------- #
#                               🟢 Beginner (1–5)                              #
# ---------------------------------------------------------------------------- #
# Create a 1D NumPy array containing the numbers 10 to 50.
import numpy as np

oneD = np.arange(10,51)
print(oneD)

# Create a 4×5 array filled with zeros.
Zeros = np.zeros((4, 5))
print(Zeros
      )
# Create a 3×3 identity matrix.
IDENTITY_MATRIX = np.identity((3)) # or np.eye((3))

print(IDENTITY_MATRIX)

# Create 8 evenly spaced numbers between 0 and 100 using linspace().
EVENLY_PLACED = np.linspace(0, 100, 8)
print(EVENLY_PLACED)

# Print the .shape, .size, .dtype, and .ndim of a 2×6 array.
np.random.seed(100)
arr = np.random.rand(2, 6)
print("shape : ", arr.shape)
print("size : ", arr.size)
print("dtype : ", arr.dtype)
print("ndim : ", arr.ndim)


# ---------------------------------------------------------------------------- #
#                           Indexing & Slicing (6–10)                          #
# ---------------------------------------------------------------------------- #
# From np.arange(1,21), extract the last five elements.
ex1_arr = np.arange(1, 21)
print("array" , ex1_arr)
print("last five elements : " , ex1_arr[-5:])

# Reverse an array without using a loop.
print("reverse array : " , ex1_arr[::-1])

# From a 5×5 matrix, extract the third row.
matrix = np.arange(1,26).reshape(5,5)
print(matrix[2])

# Extract the second column of a matrix.
print("second column of matrix :", matrix[:,1])

# Extract the center 3×3 submatrix from a 5×5 matrix.
print("3x3 matrix of the 5x5 matrix is : " , matrix[1:4, 1:4])

# ---------------------------------------------------------------------------- #
#                          🟠 Boolean Indexing (11–15)                         #
# ---------------------------------------------------------------------------- #
# Select all elements greater than 50.
arr1 = np.array([10, 25, 34, 50, 55, 70, -8, -15, 42, 60])
print("element greater than 50 : ", arr1[arr1 > 50])

# Select all even numbers.
print("even number in that array :", arr1[arr1 % 2 ==0])

# Select values between 20 and 40 (inclusive).
print("value between 20 and 40 : ", arr1[(arr1 >= 20) & (arr1 <= 40)])

# Remove all negative numbers from an array.
print("positive numbers :", arr1[arr1 >= 0])

# From student marks, find all scores greater than the class average.
marks = np.array([45, 65, 70, 80, 55, 90, 40])
average = marks.mean()
print("score greater than class average marks : ", marks[marks > average])

# ---------------------------------------------------------------------------- #
#                           🔵 Fancy Indexing (16–18)                          #
# ---------------------------------------------------------------------------- #
# Select indices [0, 3, 7, 9] from an array.
arr2 = np.arange(0,10)
print("indices [0, 3, 7, 9] from an array :", arr2[[0, 3, 7, 9]])

# From a matrix, select rows [1, 3].
matrix = np.arange(1,26).reshape(5,5)
print("rows 1 and 3 : " , matrix[[1,3]])

# Extract elements (0,2), (2,1), and (3,3) using fancy indexing.
print("elements (0,2), (2,1), and (3,3) :", matrix[[0,2,3], [2,1,3]])

# ---------------------------------------------------------------------------- #
#                        🔴 AI/ML Style Problems (19–20)                       #
# ---------------------------------------------------------------------------- #
# Generate a (100, 5) feature matrix of random numbers, split it into 80 training samples and 20 testing samples, then extract only features 2–4 from the training data.
raw_data = np.random.rand(100,5) *10 + 50
training_data = raw_data[:80]
testing_data = raw_data[80:] 
train_features = training_data[:,2:5]
print(train_features.shape)
print(train_features)




# Create a (100, 5) student score matrix. Compute each student's average, identify the top 10 students, and list those whose Math score is above 90 and whose average score exceeds 80.
student_score = np.random.randint(1,101,(100,5))
student_score_average = student_score.mean(axis=1)
top10 = np.argsort(student_score_average)[-10:][::-1]
print(top10)
qualified = student_score[(student_score[:,0] > 90) & (student_score_average > 80)]