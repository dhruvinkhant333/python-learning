"""
================================================================================
PANDAS BASICS - COMPLETE GUIDE FOR AI/ML
================================================================================
Covers: Series, DataFrames, Creation, Reading Data
Learn how to load, inspect, and prepare data for machine learning
"""

import pandas as pd
import numpy as np
from io import StringIO
import os

print("=" * 80)
print("PANDAS BASICS - COMPLETE GUIDE FOR AI/ML")
print("=" * 80)

# =============================================================================
# 1. PANDAS OVERVIEW
# =============================================================================
print("\n" + "=" * 80)
print("1. PANDAS OVERVIEW - What is Pandas?")
print("=" * 80)

print("""
WHAT IS PANDAS?
- Library for working with tabular (2D) data
- Think of it like Excel/SQL but in Python
- Built on top of NumPy (uses NumPy arrays internally)
- Essential tool for data cleaning, exploration, preparation

PANDAS vs NumPy:
╔════════════════════════════════════════════════════════════════╗
║ Dimension │ NumPy              │ Pandas                        ║
╠════════════════════════════════════════════════════════════════╣
║ 1D        │ ndarray (array)    │ Series (labeled array)        ║
║ 2D        │ ndarray (matrix)   │ DataFrame (table)             ║
║ Labels    │ Numeric indices    │ Column names + row indices    ║
║ Data type │ Single (all same)  │ Mixed (columns differ)        ║
║ Speed     │ Faster (NumPy)     │ Slightly slower (convenience) ║
╚════════════════════════════════════════════════════════════════╝

WHEN TO USE PANDAS:
✓ Loading CSV/Excel files
✓ Data with column names (labeled data)
✓ Mixed data types (int, float, string, date in same table)
✓ Exploratory data analysis (inspection, statistics)
✓ Data cleaning and preparation
✓ Time series data

WHEN TO USE NUMPY:
✓ Fast numerical computations
✓ Homogeneous data (all same type)
✓ Heavy mathematical operations
✓ Working with arrays directly

WHY ESSENTIAL FOR ML:
1. Real-world data comes as CSV/Excel files
2. Need to inspect and clean data before training
3. Feature engineering requires table manipulation
4. Scikit-learn expects pandas DataFrames
5. Data exploration is critical ML step
""")

print("\n--- Installation & Import ---")
print("pip install pandas")
print("import pandas as pd")

# =============================================================================
# 2. SERIES (1D Labeled Array)
# =============================================================================
print("\n" + "=" * 80)
print("2. SERIES - 1D Labeled Array")
print("=" * 80)

print("""
SERIES OVERVIEW:
- 1D array with labels (index)
- Like a column in Excel
- Has index (row labels) and values
""")

# Creating from list
print("\n--- Creating from List ---")
s1 = pd.Series([1, 2, 3, 4, 5])
print("pd.Series([1, 2, 3, 4, 5]):")
print(s1)
print(f"Type: {type(s1)}")
print(f"  ↳ Numeric index (0, 1, 2, 3, 4) created automatically")

# Creating from list with custom index
print("\n--- Creating with Custom Index ---")
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']):")
print(s2)
print("  ↳ Custom string index (a, b, c, d, e)")

# Creating from dict
print("\n--- Creating from Dictionary ---")
s3 = pd.Series({'name': 'Leo', 'age': 20, 'city': 'Rajkot'})
print("pd.Series({'name': 'Leo', 'age': 20, 'city': 'Rajkot'}):")
print(s3)
print("  ↳ Dict keys become index, values become data")

# Creating from numpy array
print("\n--- Creating from NumPy Array ---")
arr = np.array([10, 20, 30, 40])
s4 = pd.Series(arr, index=['A', 'B', 'C', 'D'])
print("pd.Series(np.array([10, 20, 30, 40]), index=['A', 'B', 'C', 'D']):")
print(s4)

# Series properties
print("\n--- Series Properties ---")
s = pd.Series([100, 200, 300], index=['First', 'Second', 'Third'], name='Revenue')
print(f"Series:\n{s}")

print(f"\n.values - Get raw values:")
print(f"  {s.values}")
print(f"  Type: {type(s.values)} (NumPy array)")

print(f"\n.index - Get index labels:")
print(f"  {s.index}")
print(f"  {list(s.index)}")

print(f"\n.name - Series name:")
print(f"  {s.name}")

print(f"\n.dtype - Data type:")
print(f"  {s.dtype}")

print(f"\n.shape - Shape (1D):")
print(f"  {s.shape}")

# Accessing elements
print("\n--- Accessing Series Elements ---")
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(f"Series:\n{s}")

print(f"\nAccess by numeric position (use .iloc):")
print(f"  s.iloc[0] = {s.iloc[0]}")
print(f"  s.iloc[2] = {s.iloc[2]}")

print(f"\nAccess by index label (use .loc or direct):")
print(f"  s['a'] = {s['a']}")
print(f"  s['c'] = {s['c']}")
print(f"  s.loc['a'] = {s.loc['a']}")

print(f"\nAccess multiple elements by label:")
print(f"  s[['a', 'c', 'e']] =")
print(s[['a', 'c', 'e']])

print(f"\nSlicing by label:")
print(f"  s['b':'d'] (includes endpoints):")
print(s['b':'d'])

# Series operations
print("\n--- Series Operations (NumPy-like) ---")
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([10, 20, 30])

result = s1 + s2
print(f"s1 + s2:\n{result}")

result = s1 * 2
print(f"\ns1 * 2:\n{result}")

result = s1.sum()
print(f"\ns1.sum(): {result}")

result = s1.mean()
print(f"s1.mean(): {result}")

# =============================================================================
# 3. DATAFRAME (2D Table)
# =============================================================================
print("\n" + "=" * 80)
print("3. DATAFRAME - 2D Table")
print("=" * 80)

print("""
DATAFRAME OVERVIEW:
- 2D table (rows and columns)
- Like Excel spreadsheet or SQL table
- Each column can have different data type
- Both rows and columns have labels
""")

# Creating from dict of lists
print("\n--- Creating from Dict of Lists ---")
data = {
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23],
    'City': ['Rajkot', 'Mumbai', 'Delhi']
}
df1 = pd.DataFrame(data)
print("pd.DataFrame({'Name': [...], 'Age': [...], 'City': [...]})")
print(df1)
print(f"  ↳ Columns: Name, Age, City")
print(f"  ↳ Rows: 3 students")

# Creating from list of dicts
print("\n--- Creating from List of Dictionaries ---")
data = [
    {'Name': 'Leo', 'Age': 20, 'City': 'Rajkot'},
    {'Name': 'Alice', 'Age': 25, 'City': 'Mumbai'},
    {'Name': 'Bob', 'Age': 23, 'City': 'Delhi'}
]
df2 = pd.DataFrame(data)
print("pd.DataFrame([{'Name': 'Leo', 'Age': 20, ...}, ...])")
print(df2)

# Creating from 2D numpy array
print("\n--- Creating from 2D NumPy Array ---")
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print("pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=['A','B','C'])")
print(df3)

# Creating from Series
print("\n--- Creating from Series ---")
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
df4 = pd.concat([s1, s2], axis=1)
print("pd.concat([s1, s2], axis=1)")
print(df4)

# Reading CSV (MOST IMPORTANT!)
print("\n--- Reading CSV (Most Common!) ---")
print("df = pd.read_csv('file.csv')")
print("df = pd.read_csv('file.csv', sep=',')  # Specify delimiter")
print("df = pd.read_csv('file.csv', index_col=0)  # First column as index")
print("df = pd.read_csv('file.csv', encoding='utf-8')  # Specify encoding")
print("  ↳ We'll create example CSV below!")

# Reading other formats
print("\n--- Reading Other Formats ---")
print("df = pd.read_excel('file.xlsx')  # Excel file")
print("df = pd.read_json('file.json')  # JSON file")
print("df = pd.read_sql('SELECT * FROM table', connection)  # SQL database")
print("df = pd.read_html('url')  # Web table from HTML")

# =============================================================================
# 4. DATAFRAME STRUCTURE
# =============================================================================
print("\n" + "=" * 80)
print("4. DATAFRAME STRUCTURE - Understanding Your Data")
print("=" * 80)

# Create sample dataframe
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob', 'Carol', 'David'],
    'Age': [20, 25, 23, 28, 21],
    'Score': [85.5, 92.0, 78.5, 88.0, 95.5],
    'Passed': [True, True, False, True, True]
})

print("Sample DataFrame:")
print(df)

# .shape
print("\n--- .shape - Dimensions ---")
print(f"df.shape: {df.shape}")
print("  ↳ 5 rows, 4 columns")

# .columns
print("\n--- .columns - Column Names ---")
print(f"df.columns:\n{df.columns}")
print(f"df.columns.tolist(): {df.columns.tolist()}")

# .index
print("\n--- .index - Row Indices ---")
print(f"df.index:\n{df.index}")
print(f"df.index.tolist(): {df.index.tolist()}")

# .dtypes
print("\n--- .dtypes - Data Types per Column ---")
print("df.dtypes:")
print(df.dtypes)
print("  ↳ object = string, int64 = integer, float64 = float, bool = boolean")

# .info()
print("\n--- .info() - Summary Information ---")
print("df.info():")
df.info()
print("  ↳ Shows column names, non-null counts, data types, memory")

# .head(n)
print("\n--- .head(n) - First N Rows ---")
print("df.head(2):")
print(df.head(2))

# .tail(n)
print("\n--- .tail(n) - Last N Rows ---")
print("df.tail(2):")
print(df.tail(2))

# .describe()
print("\n--- .describe() - Statistical Summary ---")
print("df.describe():")
print(df.describe())
print("  ↳ Shows count, mean, std, min, 25%, 50%, 75%, max for numeric columns")

# =============================================================================
# 5. CREATING FROM DIFFERENT SOURCES
# =============================================================================
print("\n" + "=" * 80)
print("5. CREATING FROM DIFFERENT SOURCES - Common Patterns")
print("=" * 80)

# a) From dict
print("\n--- a) From Dictionary of Lists (Most Common) ---")
data = {
    'Product': ['A', 'B', 'C'],
    'Price': [100, 200, 150],
    'Quantity': [5, 3, 8]
}
df = pd.DataFrame(data)
print("data = {'Product': [...], 'Price': [...], 'Quantity': [...]}")
print("df = pd.DataFrame(data)")
print(df)

# b) From list of dicts
print("\n--- b) From List of Dictionaries ---")
data = [
    {'Product': 'A', 'Price': 100, 'Quantity': 5},
    {'Product': 'B', 'Price': 200, 'Quantity': 3},
    {'Product': 'C', 'Price': 150, 'Quantity': 8}
]
df = pd.DataFrame(data)
print("data = [{'Product': 'A', ...}, {'Product': 'B', ...}, ...]")
print("df = pd.DataFrame(data)")
print(df)

# c) From CSV (simulate)
print("\n--- c) From CSV File (Simulated) ---")
csv_data = """Name,Age,Score
Leo,20,85.5
Alice,25,92.0
Bob,23,78.5"""

df = pd.read_csv(StringIO(csv_data))
print("CSV content:")
print(csv_data)
print("\ndf = pd.read_csv('file.csv')")
print(df)

# d) From lists with columns
print("\n--- d) From Lists with Column Names ---")
df = pd.DataFrame(
    data=[[1, 2], [3, 4], [5, 6]],
    columns=['X', 'Y']
)
print("df = pd.DataFrame([[1,2], [3,4], [5,6]], columns=['X', 'Y'])")
print(df)

# =============================================================================
# 6. VIEWING DATA
# =============================================================================
print("\n" + "=" * 80)
print("6. VIEWING DATA - Inspection Methods")
print("=" * 80)

df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 25, 23, 28, 21, 24],
    'Score': [85.5, 92.0, 78.5, 88.0, 95.5, 89.0]
})

# .head()
print("\n--- .head() - First Rows ---")
print("df.head(3):")
print(df.head(3))

# .tail()
print("\n--- .tail() - Last Rows ---")
print("df.tail(2):")
print(df.tail(2))

# .sample(n)
print("\n--- .sample(n) - Random Rows ---")
np.random.seed(42)
print("df.sample(2):")
print(df.sample(2))

# .info()
print("\n--- .info() - Detailed Information ---")
print("df.info():")
df.info()

# .describe()
print("\n--- .describe() - Statistics ---")
print("df.describe():")
print(df.describe())

# .value_counts()
print("\n--- .value_counts() - Frequency of Values ---")
s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])
print("s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])")
print("s.value_counts():")
print(s.value_counts())

# =============================================================================
# 7. DATA TYPES
# =============================================================================
print("\n" + "=" * 80)
print("7. DATA TYPES - Understanding Data")
print("=" * 80)

print("""
PANDAS DATA TYPES:
- int64: Integer numbers (no decimal)
- float64: Decimal numbers
- object: Strings or mixed data
- bool: Boolean (True/False)
- datetime64: Dates and times
- category: Categorical (limited distinct values)
""")

# Creating with different types
print("\n--- Different Data Types ---")
df = pd.DataFrame({
    'ID': [1, 2, 3],                          # int64
    'Name': ['Leo', 'Alice', 'Bob'],         # object (string)
    'Score': [85.5, 92.0, 78.5],            # float64
    'Passed': [True, True, False]            # bool
})
print("DataFrame:")
print(df)
print("\nData types:")
print(df.dtypes)

# Detecting wrong types
print("\n--- Detecting Wrong Types ---")
df = pd.DataFrame({
    'Age': ['20', '25', '23'],  # ❌ Should be int, but is string!
    'Score': [85.5, 92.0, 78.5]
})
print("df with Age as strings:")
print(df)
print("\ndf.dtypes:")
print(df.dtypes)
print("  ↳ Age is object (string), should be int64!")

# .astype() to convert
print("\n--- .astype() - Convert Types ---")
df['Age'] = df['Age'].astype(int)
print("df['Age'] = df['Age'].astype(int)")
print(df)
print("\ndf.dtypes:")
print(df.dtypes)
print("  ↳ Age is now int64 ✓")

# String to numeric
print("\n--- String to Numeric ---")
df = pd.DataFrame({
    'Price': ['$100', '$200', '$150']
})
print("Original (strings with $):")
print(df)

# Remove $ and convert
df['Price'] = df['Price'].str.replace('$', '').astype(float)
print("\nAfter removing $ and converting:")
print(df)
print(df.dtypes)

# datetime
print("\n--- Datetime Type ---")
df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03']
})
print("Original (strings):")
print(df)
print(df.dtypes)

df['Date'] = pd.to_datetime(df['Date'])
print("\nAfter pd.to_datetime():")
print(df)
print(df.dtypes)

# Why types matter
print("\n--- Why Types Matter ---")
print("❌ If Age is string, can't do: df['Age'].mean()")
print("✓ If Age is int, can do: df['Age'].mean()")
print("   Correct types = correct operations!")

# =============================================================================
# 8. INDEX (Row Labels)
# =============================================================================
print("\n" + "=" * 80)
print("8. INDEX - Row Labels")
print("=" * 80)

print("""
INDEX OVERVIEW:
- Default: numeric index (0, 1, 2, ...)
- Can be: strings, dates, or custom values
- Used for labeling and accessing rows
""")

# Default numeric index
print("\n--- Default Numeric Index ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23]
})
print("Default DataFrame:")
print(df)
print("  ↳ Index: 0, 1, 2 (automatic)")

# Custom index
print("\n--- Custom Index ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23]
}, index=['Student1', 'Student2', 'Student3'])
print("With custom index:")
print(df)

# Accessing by index
print("\n--- Accessing Rows by Index ---")
print("df.loc['Student1']:")
print(df.loc['Student1'])

print("\ndf.loc[['Student1', 'Student3']]:")
print(df.loc[['Student1', 'Student3']])

# .set_index() - Change index
print("\n--- .set_index() - Set Column as Index ---")
df = pd.DataFrame({
    'ID': ['S1', 'S2', 'S3'],
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23]
})
print("Original:")
print(df)

df_indexed = df.set_index('ID')
print("\ndf.set_index('ID'):")
print(df_indexed)
print("  ↳ ID is now index, not a column")

# .reset_index() - Remove custom index
print("\n--- .reset_index() - Convert Index to Column ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23]
}, index=['S1', 'S2', 'S3'])
print("With custom index:")
print(df)

df_reset = df.reset_index()
print("\ndf.reset_index():")
print(df_reset)
print("  ↳ Index becomes a column, numeric index created")

# =============================================================================
# 9. PRACTICAL EXAMPLES
# =============================================================================
print("\n" + "=" * 80)
print("9. PRACTICAL EXAMPLES - Real-World Scenarios")
print("=" * 80)

# Example 1: Student records
print("\n--- Example 1: Student Records ---")
student_data = {
    'StudentID': [101, 102, 103, 104],
    'Name': ['Leo', 'Alice', 'Bob', 'Carol'],
    'Math': [85.5, 92.0, 78.5, 88.0],
    'English': [80.0, 88.5, 85.0, 92.0],
    'Science': [88.0, 95.5, 82.0, 89.5]
}
df_students = pd.DataFrame(student_data)
print("Student Data:")
print(df_students)

print("\nBasic inspection:")
print(f"Shape: {df_students.shape}")
print(f"Columns: {list(df_students.columns)}")
print(f"Data types:\n{df_students.dtypes}")

# Example 2: Product sales
print("\n--- Example 2: Product Sales Data ---")
sales_csv = """Product,Date,Price,Quantity,Category
Laptop,2024-01-01,50000,2,Electronics
Mouse,2024-01-01,500,10,Electronics
Chair,2024-01-01,5000,3,Furniture
Desk,2024-01-02,15000,1,Furniture
Keyboard,2024-01-02,2000,5,Electronics"""

df_sales = pd.read_csv(StringIO(sales_csv))
print("Sales Data:")
print(df_sales)

print("\nData types:")
print(df_sales.dtypes)

# Fix date type
df_sales['Date'] = pd.to_datetime(df_sales['Date'])
print("\nAfter fixing Date column:")
print(df_sales.dtypes)

# Example 3: Time series
print("\n--- Example 3: Time Series Data ---")
dates = pd.date_range('2024-01-01', periods=5, freq='D')
data = {
    'Date': dates,
    'Temperature': [20.5, 21.0, 19.5, 22.0, 20.8],
    'Humidity': [65, 68, 70, 62, 66]
}
df_weather = pd.DataFrame(data)
print("Weather Data:")
print(df_weather)

print("\nData types:")
print(df_weather.dtypes)

# Example 4: Inspect loaded data
print("\n--- Example 4: Complete Data Inspection ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob'],
    'Age': [20, 25, 23],
    'Score': [85.5, 92.0, 78.5]
})

print("Dataset Overview:")
print(f"1. Shape: {df.shape}")
print(f"2. Columns: {list(df.columns)}")
print(f"3. Data types:\n{df.dtypes}")
print(f"4. Head:\n{df.head(2)}")
print(f"5. Info:")
df.info()
print(f"6. Statistics:\n{df.describe()}")

# =============================================================================
# 10. COMMON MISTAKES
# =============================================================================
print("\n" + "=" * 80)
print("10. COMMON MISTAKES - Avoid These!")
print("=" * 80)

# Mistake 1: Wrong file path
print("\n--- MISTAKE 1: Wrong File Path ---")
print("❌ WRONG:")
print("  df = pd.read_csv('student_data.csv')")
print("  FileNotFoundError: [Errno 2] No such file or directory")

print("\n✓ RIGHT:")
print("  df = pd.read_csv('./data/student_data.csv')  # Correct path")
print("  df = pd.read_csv('/home/leo/data/student_data.csv')  # Absolute path")

# Mistake 2: Data type mismatches
print("\n--- MISTAKE 2: Data Type Mismatches ---")
df = pd.DataFrame({
    'ID': ['1', '2', '3'],  # ❌ String, should be int
    'Score': [85, 92, 78]
})
print("❌ WRONG - ID as string:")
print(df)
print(f"Types: {df.dtypes.to_dict()}")

print("\nCan't do: df['ID'].sum()  # Error!")

print("\n✓ RIGHT - Convert to int:")
df['ID'] = df['ID'].astype(int)
print(df)
print(f"Types: {df.dtypes.to_dict()}")
print(f"df['ID'].sum() = {df['ID'].sum()}  # Works! ✓")

# Mistake 3: Encoding issues
print("\n--- MISTAKE 3: Encoding Issues with CSV ---")
print("❌ WRONG (encoding error with non-ASCII characters):")
print("  df = pd.read_csv('file.csv')")
print("  UnicodeDecodeError: 'utf-8' codec can't decode...")

print("\n✓ RIGHT (specify encoding):")
print("  df = pd.read_csv('file.csv', encoding='utf-8')")
print("  df = pd.read_csv('file.csv', encoding='latin-1')")
print("  df = pd.read_csv('file.csv', encoding='iso-8859-1')")

# Mistake 4: Index confusion
print("\n--- MISTAKE 4: Index Confusion ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice', 'Bob']
}, index=['A', 'B', 'C'])
print("DataFrame with custom index:")
print(df)

print("\n❌ WRONG (position instead of label):")
print("  df.loc[0]  # KeyError: 0")

print("\n✓ RIGHT (use label):")
print(f"  df.loc['A'] = {df.loc['A'].values[0]}")

print("\n✓ OR (use position with iloc):")
print(f"  df.iloc[0] = {df.iloc[0].values[0]}")

# =============================================================================
# 11. PRACTICE EXERCISES
# =============================================================================
print("\n" + "=" * 80)
print("11. PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 80)

# Exercise 1: Create Series
print("\n--- Exercise 1: Create Series from Different Sources ---")

# From list
s1 = pd.Series([10, 20, 30])
print("From list:")
print(s1)

# From dict
s2 = pd.Series({'a': 100, 'b': 200, 'c': 300})
print("\nFrom dict:")
print(s2)

# From numpy array
s3 = pd.Series(np.array([1.5, 2.5, 3.5]), index=['x', 'y', 'z'])
print("\nFrom NumPy array with index:")
print(s3)

# Exercise 2: Create DataFrame
print("\n--- Exercise 2: Create DataFrame from Dict/List ---")

# From dict of lists
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print("From dict of lists:")
print(df1)

# From list of dicts
df2 = pd.DataFrame([
    {'X': 10, 'Y': 20},
    {'X': 30, 'Y': 40}
])
print("\nFrom list of dicts:")
print(df2)

# Exercise 3: Access elements and index
print("\n--- Exercise 3: Access Series Elements and Index ---")
s = pd.Series([100, 200, 300], index=['First', 'Second', 'Third'])
print(f"Series:\n{s}")

print(f"\nAccess by position: s.iloc[0] = {s.iloc[0]}")
print(f"Access by label: s['First'] = {s['First']}")
print(f"Get index: {list(s.index)}")
print(f"Get values: {list(s.values)}")

# Exercise 4: DataFrame shape, columns, dtypes
print("\n--- Exercise 4: Get DataFrame Info ---")
df = pd.DataFrame({
    'Name': ['Leo', 'Alice'],
    'Age': [20, 25],
    'Score': [85.5, 92.0]
})
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Index: {list(df.index)}")
print(f"Data types:\n{df.dtypes}")

# Exercise 5: View first/last rows
print("\n--- Exercise 5: View First and Last Rows ---")
df = pd.DataFrame({
    'ID': range(1, 6),
    'Value': [10, 20, 30, 40, 50]
})
print("DataFrame:")
print(df)

print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

# Exercise 6: Load and inspect CSV
print("\n--- Exercise 6: Load and Inspect CSV ---")
csv_data = """StudentID,Name,Math,English
101,Leo,85.5,80.0
102,Alice,92.0,88.5
103,Bob,78.5,85.0"""

df = pd.read_csv(StringIO(csv_data))
print("Loaded CSV:")
print(df)

print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("Data types:\n", df.dtypes)
print("\nFirst row:\n", df.head(1))

# Exercise 7: Understand .info()
print("\n--- Exercise 7: Understand .info() Output ---")
df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Leo', 'Alice', 'Bob', None, 'Eve'],  # Note: None in Name
    'Score': [85.5, 92.0, 78.5, 88.0, 95.5]
})

print("DataFrame:")
print(df)

print("\nInfo:")
df.info()
print("  ↳ Shows:")
print("  - Column names and data types")
print("  - Non-null counts (Name has 4 non-null, not 5 - missing one!)")
print("  - Memory usage")

# =============================================================================
# 12. MINI-PROJECT: STUDENT DATA ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("12. MINI-PROJECT: Student Data Analysis")
print("=" * 80)

print("\n=== Step 1: Create Synthetic Student Data ===")
student_data = {
    'StudentID': [101, 102, 103, 104, 105],
    'Name': ['Leo', 'Alice', 'Bob', 'Carol', 'David'],
    'Age': [20, 25, 23, 28, 21],
    'Math': [85.5, 92.0, 78.5, 88.0, 95.5],
    'English': [80.0, 88.5, 85.0, 92.0, 89.5],
    'Science': [88.0, 95.5, 82.0, 89.5, 92.0],
    'GPA': [3.5, 3.9, 3.2, 3.7, 3.8]
}

df = pd.DataFrame(student_data)
print("Created DataFrame:")
print(df)

print("\n=== Step 2: Create DataFrame and Inspect ===")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Index: {list(df.index)}")

print("\n=== Step 3: Load a 'Real' CSV ===")
# Simulate loading from CSV
csv_content = """StudentID,Name,Age,Math,English,Science,GPA
101,Leo,20,85.5,80.0,88.0,3.5
102,Alice,25,92.0,88.5,95.5,3.9
103,Bob,23,78.5,85.0,82.0,3.2
104,Carol,28,88.0,92.0,89.5,3.7
105,David,21,95.5,89.5,92.0,3.8"""

df_loaded = pd.read_csv(StringIO(csv_content))
print("Loaded from CSV:")
print(df_loaded)

print("\n=== Step 4: Inspect Using .info() and .describe() ===")
print("Info:")
df_loaded.info()

print("\n" + "-" * 50)
print("Describe (Statistics):")
print(df_loaded.describe())

print("\n=== Step 5: Check Data Types ===")
print("Data types:")
print(df_loaded.dtypes)
print("\n  All types are correct:")
print("  ✓ StudentID, Age: int64")
print("  ✓ Name: object (string)")
print("  ✓ Math, English, Science, GPA: float64")

print("\n=== Step 6: Fix Any Type Issues ===")
# In this case, no issues, but demonstrate:
print("No type issues found!")
print("If Name was numeric, would do: df['Name'] = df['Name'].astype(str)")

print("\n=== Step 7: Set Appropriate Index ===")
df_indexed = df_loaded.set_index('StudentID')
print("Set StudentID as index:")
print(df_indexed)
print("\nNow can access by student ID:")
print(f"Student 103 (Bob):\n{df_indexed.loc[103]}")

print("\n=== Step 8: Calculate Basic Statistics ===")
print("Statistics for numeric columns:")
print(f"Math average: {df_loaded['Math'].mean():.2f}")
print(f"English average: {df_loaded['English'].mean():.2f}")
print(f"Science average: {df_loaded['Science'].mean():.2f}")

print(f"\nAge statistics:")
print(f"  Min age: {df_loaded['Age'].min()}")
print(f"  Max age: {df_loaded['Age'].max()}")
print(f"  Average age: {df_loaded['Age'].mean():.1f}")

print(f"\nGPA statistics:")
print(f"  Highest GPA: {df_loaded['GPA'].max():.2f}")
print(f"  Lowest GPA: {df_loaded['GPA'].min():.2f}")
print(f"  Average GPA: {df_loaded['GPA'].mean():.2f}")

print(f"\nStudent with highest Math score:")
top_math_idx = df_loaded['Math'].idxmax()
print(df_loaded.loc[top_math_idx])

print("\n=== Summary ===")
print("✓ Created DataFrame from dict")
print("✓ Loaded CSV using pd.read_csv()")
print("✓ Inspected with .info() and .describe()")
print("✓ Verified data types")
print("✓ Set index for better data access")
print("✓ Calculated statistics")
print("\nReady for data analysis and ML!")

print("\n" + "=" * 80)
print("END OF PANDAS BASICS GUIDE")
print("=" * 80)







# ---------------------------------------------------------------------------- #
#                               PANDAS CHEATSHEET                              #
# ---------------------------------------------------------------------------- #

"""
PANDAS QUICK REFERENCE - Fast Lookup for Common Operations
"""



# =============================================================================
# PANDAS SERIES - 1D Labeled Array
# =============================================================================

# Creating Series
s = pd.Series([1, 2, 3])                    # From list
s = pd.Series({'a': 1, 'b': 2})            # From dict
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # Custom index
s = pd.Series(np.array([1, 2, 3]))         # From NumPy

# Series properties
s.values                                    # Get raw values (NumPy array)
s.index                                     # Get index
s.name = 'revenue'                          # Set name
s.dtype                                     # Data type
s.shape                                     # Shape (1D)

# Accessing elements
s.iloc[0]                                   # By position
s['a']                                      # By label
s.loc['a']                                  # By label (explicit)
s[['a', 'c']]                              # Multiple elements
s['a':'c']                                  # Slicing by label

# Operations
s.sum(), s.mean(), s.std()                 # Statistics
s + 5                                       # Broadcasting
s * 2                                       # Element-wise multiply

# =============================================================================
# PANDAS DATAFRAME - 2D Table
# =============================================================================

# Creating DataFrames
df = pd.DataFrame({
    'Name': ['Leo', 'Alice'],
    'Age': [20, 25],
    'Score': [85.5, 92.0]
})                                          # From dict of lists

df = pd.DataFrame([
    {'Name': 'Leo', 'Age': 20},
    {'Name': 'Alice', 'Age': 25}
])                                          # From list of dicts

df = pd.DataFrame(np.array([[1, 2], [3, 4]]),
                  columns=['A', 'B'])       # From NumPy array

# Reading data (MOST IMPORTANT!)
df = pd.read_csv('file.csv')               # CSV
df = pd.read_csv('file.csv', sep=';')      # Different delimiter
df = pd.read_csv('file.csv', index_col=0) # First column as index
df = pd.read_excel('file.xlsx')            # Excel
df = pd.read_json('file.json')             # JSON
df = pd.read_sql('SELECT * FROM table', csv_content)  # SQL database

# =============================================================================
# DATAFRAME INSPECTION
# =============================================================================

# Basic info
df.shape                                    # (rows, columns)
df.columns                                  # Column names
df.columns.tolist()                         # As list
df.index                                    # Row indices
df.dtypes                                   # Data type per column

# Viewing data
df.head(5)                                  # First 5 rows
df.tail(5)                                  # Last 5 rows
df.sample(3)                                # Random 3 rows
df.info()                                   # Column info, dtypes, non-null counts
df.describe()                               # Statistics for numeric columns
df.value_counts()                           # Frequency (Series only)

# =============================================================================
# DATA TYPES & CONVERSION
# =============================================================================

# Check types
df.dtypes                                   # All columns
df['Name'].dtype                            # Single column

# Convert types
df['Age'] = df['Age'].astype(int)          # To integer
df['Score'] = df['Score'].astype(float)    # To float
df['Passed'] = df['Passed'].astype(bool)   # To boolean
df['Date'] = pd.to_datetime(df['Date'])    # To datetime

# Handling strings
df['Price'] = df['Price'].str.replace('$', '')  # Remove character
df['Price'] = df['Price'].astype(float)         # Convert after cleaning

# =============================================================================
# INDEX - ROW LABELS
# =============================================================================

# Working with index
df.index                                    # Get current index
df.set_index('ID')                         # Set column as index
df.reset_index()                           # Convert index to column
df.index.tolist()                          # Index as list

# Accessing by index
df.loc['row_label']                         # By index label
df.loc[['label1', 'label2']]               # Multiple rows
df.loc['a':'c']                            # Slicing by label (inclusive!)
df.iloc[0]                                  # By position
df.iloc[0:3]                                # Rows 0-2

# =============================================================================
# ACCESSING DATA
# =============================================================================

# Columns
df['Name']                                  # Get column (Series)
df['Name'].values                           # As NumPy array
df[['Name', 'Age']]                         # Multiple columns (DataFrame)

# Rows
df.iloc[0]                                  # First row by position
df.iloc[0:5]                                # Rows 0-4
df.loc['label']                             # Row by index label

# Single element
df['Name'][0]                               # Column then position
df.loc[0, 'Name']                           # Row then column
df.iloc[0, 1]                               # Position-based

# Boolean indexing (filtering)
mask = df['Age'] > 25
df[mask]                                    # Rows where Age > 25
df[df['Score'] >= 90]                      # Score >= 90

# =============================================================================
# BASIC OPERATIONS
# =============================================================================

# Column operations
df['Name'].unique()                         # Unique values
df['Age'].value_counts()                    # Frequency
df['Age'].sum(), df['Age'].mean()          # Aggregations
df['Age'].min(), df['Age'].max()           # Min/max

# DataFrame operations
df.sum()                                    # Sum per column
df.mean()                                   # Mean per column
df.std()                                    # Std per column
df.groupby('Category').sum()                # Group by

# Sorting
df.sort_values('Age')                       # Sort by column
df.sort_values('Age', ascending=False)     # Descending
df.sort_index()                             # Sort by index

# =============================================================================
# PRACTICAL PATTERNS
# =============================================================================

# Load, inspect, clean
df = pd.read_csv('data.csv')
print(df.head())                            # See first rows
print(df.info())                            # Check dtypes
print(df.describe())                        # Statistics

# Fix data types
df['Age'] = df['Age'].astype(int)
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
df.isnull()                                 # Find missing
df.dropna()                                 # Remove rows with NaN
df.fillna(0)                                # Replace NaN with 0

# Create new columns
df['FullName'] = df['First'] + ' ' + df['Last']
df['Age_squared'] = df['Age'] ** 2

# Filter and select
above_25 = df[df['Age'] > 25]
young_high_score = df[(df['Age'] < 25) & (df['Score'] > 90)]

# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================

# ❌ WRONG: Wrong file path
# df = pd.read_csv('student_data.csv')  # FileNotFoundError!

# ✓ RIGHT: Correct path
# df = pd.read_csv('./data/student_data.csv')

# ❌ WRONG: Type mismatch
# df['Age'] = ['20', '25', '23']  # Strings, can't sum!

# ✓ RIGHT: Convert to correct type
# df['Age'] = df['Age'].astype(int)

# ❌ WRONG: Access numeric index with string index
# df = df.set_index('Name')
# df[0]  # KeyError!

# ✓ RIGHT: Use iloc or access by label
# df.iloc[0]  # By position
# df.loc['Leo']  # By label

# ❌ WRONG: Forget axis parameter
# df.sum()  # Sums all columns

# ✓ RIGHT: Specify axis when needed
# df.sum(axis=0)  # Sum down rows (per column)
# df.sum(axis=1)  # Sum across columns (per row)

# =============================================================================
# USEFUL PATTERNS
# =============================================================================

# Display options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)

# Data info
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Missing: {df.isnull().sum()}")

# Statistics by group
df.groupby('Category')['Price'].mean()     # Mean price per category
df.groupby('Category').agg({'Price': 'mean', 'Quantity': 'sum'})

# Create features
df['IsExpensive'] = df['Price'] > 100
df['LogPrice'] = np.log(df['Price'])
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

print("=" * 60)
print("PANDAS QUICK REFERENCE LOADED")
print("=" * 60)
print("""
KEY PATTERNS:

1. LOAD CSV:
   df = pd.read_csv('file.csv')

2. INSPECT:
   df.head(), df.info(), df.describe()

3. CHECK TYPES:
   df.dtypes

4. FIX TYPES:
   df['Age'] = df['Age'].astype(int)
   df['Date'] = pd.to_datetime(df['Date'])

5. FILTER:
   df[df['Age'] > 25]
   df[(df['Age'] > 25) & (df['Score'] >= 90)]

6. AGGREGATE:
   df['Age'].mean()
   df.groupby('Category')['Price'].sum()

7. SET INDEX:
   df.set_index('ID')

8. ACCESS:
   df['Name']           # Column
   df.loc[0, 'Name']   # Row & column by label
   df.iloc[0, 1]       # Row & column by position

Remember: .loc uses labels, .iloc uses positions!
""")