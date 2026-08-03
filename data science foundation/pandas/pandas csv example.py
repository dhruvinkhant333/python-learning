"""
Pandas CSV Example - Load and Analyze Student Data
Demonstrates real-world workflow with the sample_student_data.csv file
"""

import pandas as pd
import numpy as np
from pathlib import Path

print("=" * 80)
print("PANDAS CSV EXAMPLE - Student Data Analysis")
print("=" * 80)

# =============================================================================
# Step 1: Load CSV File
# =============================================================================
print("\n" + "=" * 80)
print("Step 1: Load CSV File")
print("=" * 80)

# Load the student data CSV
base_dir = Path(__file__).parent
csv_path = base_dir/'sample_student_data.csv'
df = pd.read_csv(csv_path)

print("\nLoaded DataFrame:")
print(df)

# =============================================================================
# Step 2: Inspect Data Structure
# =============================================================================
print("\n" + "=" * 80)
print("Step 2: Inspect Data Structure")
print("=" * 80)

print(f"\n1. Shape: {df.shape}")
print(f"   → {df.shape[0]} rows (students), {df.shape[1]} columns (attributes)")

print(f"\n2. Column Names:")
print(f"   {list(df.columns)}")

print(f"\n3. Data Types:")
print(df.dtypes)

print(f"\n4. Index (Row labels):")
print(f"   {list(df.index)}")

# =============================================================================
# Step 3: View Data
# =============================================================================
print("\n" + "=" * 80)
print("Step 3: View Data")
print("=" * 80)

print("\nFirst 3 students:")
print(df.head(3))

print("\nLast 3 students:")
print(df.tail(3))

print("\nRandom 2 students:")
np.random.seed(42)
print(df.sample(2))

# =============================================================================
# Step 4: Get Detailed Information
# =============================================================================
print("\n" + "=" * 80)
print("Step 4: Get Detailed Information (.info())")
print("=" * 80)

df.info()
print("\n  Interpretation:")
print("  - RangeIndex: rows 0-9 (10 students)")
print("  - 9 columns (StudentID through Attendance)")
print("  - All columns have 10 non-null values (no missing data)")
print("  - Memory usage: ~928 bytes (very small)")

# =============================================================================
# Step 5: Statistical Summary
# =============================================================================
print("\n" + "=" * 80)
print("Step 5: Statistical Summary (.describe())")
print("=" * 80)

print("\nBasic statistics for numeric columns:")
print(df.describe())

print("\nKey insights:")
print(f"  - Student IDs: {df['StudentID'].min()} to {df['StudentID'].max()}")
print(f"  - Ages: {df['Age'].min()} to {df['Age'].max()} years old")
print(f"  - Average Math score: {df['Math'].mean():.2f}")
print(f"  - Average English score: {df['English'].mean():.2f}")
print(f"  - Average Science score: {df['Science'].mean():.2f}")
print(f"  - Average GPA: {df['GPA'].mean():.2f}")
print(f"  - Average Attendance: {df['Attendance'].mean():.1f}%")

# =============================================================================
# Step 6: Check for Missing Values
# =============================================================================
print("\n" + "=" * 80)
print("Step 6: Check for Missing Values")
print("=" * 80)

print("\nNull values per column:")
print(df.isnull().sum())

print("\nTotal missing values: ", df.isnull().sum().sum())
print("  → No missing data, dataset is clean! ✓")

# =============================================================================
# Step 7: Access Specific Data
# =============================================================================
print("\n" + "=" * 80)
print("Step 7: Access Specific Data")
print("=" * 80)

# Single column
print("\nAll student names (column access):")
print(df['Name'].values)

# Multiple columns
print("\nStudent names and math scores:")
print(df[['Name', 'Math']])

# Specific row
print("\nStudent at index 0 (Leo):")
print(df.iloc[0])

# Specific cell
print(f"\nLeo's Math score: {df.iloc[0]['Math']}")

# =============================================================================
# Step 8: Filtering (Boolean Indexing)
# =============================================================================
print("\n" + "=" * 80)
print("Step 8: Filtering Data (Boolean Indexing)")
print("=" * 80)

# Students with GPA >= 3.7
print("\nStudents with GPA >= 3.7:")
high_gpa = df[df['GPA'] >= 3.7]
print(high_gpa[['Name', 'GPA', 'Grade']])

# Students younger than 23
print("\nStudents younger than 23:")
young = df[df['Age'] < 23]
print(young[['Name', 'Age']])

# Grade A students
print("\nGrade A students:")
grade_a = df[df['Grade'] == 'A']
print(grade_a[['Name', 'Grade', 'GPA']])

# Combined condition
print("\nGrade A students with attendance >= 95%:")
excellent = df[(df['Grade'] == 'A') & (df['Attendance'] >= 95)]
print(excellent[['Name', 'Grade', 'Attendance']])

# =============================================================================
# Step 9: Aggregate & Calculate Statistics
# =============================================================================
print("\n" + "=" * 80)
print("Step 9: Aggregate & Calculate Statistics")
print("=" * 80)

# Average scores by grade
print("\nAverage scores by grade level:")
grade_stats = df.groupby('Grade')[['Math', 'English', 'Science']].mean()
print(grade_stats)

# Attendance statistics
print(f"\nAttendance statistics:")
print(f"  Highest: {df['Attendance'].max()}%")
print(f"  Lowest: {df['Attendance'].min()}%")
print(f"  Average: {df['Attendance'].mean():.1f}%")

# Score ranges
print(f"\nMath scores - Min: {df['Math'].min()}, Max: {df['Math'].max()}, Avg: {df['Math'].mean():.2f}")
print(f"English scores - Min: {df['English'].min()}, Max: {df['English'].max()}, Avg: {df['English'].mean():.2f}")
print(f"Science scores - Min: {df['Science'].min()}, Max: {df['Science'].max()}, Avg: {df['Science'].mean():.2f}")

# =============================================================================
# Step 10: Sorting
# =============================================================================
print("\n" + "=" * 80)
print("Step 10: Sorting Data")
print("=" * 80)

# Top 3 students by GPA
print("\nTop 3 students by GPA:")
top_gpa = df.nlargest(3, 'GPA')[['Name', 'GPA', 'Grade']]
print(top_gpa)

# Lowest 3 by Math score
print("\nLowest 3 students in Math:")
low_math = df.nsmallest(3, 'Math')[['Name', 'Math', 'Grade']]
print(low_math)

# Sort by Age
print("\nStudents sorted by age (youngest first):")
by_age = df.sort_values('Age')[['Name', 'Age']]
print(by_age)

# =============================================================================
# Step 11: Data Type Verification & Conversion
# =============================================================================
print("\n" + "=" * 80)
print("Step 11: Data Type Verification")
print("=" * 80)

print("Current data types:")
print(df.dtypes)

print("\n✓ All types are correct:")
print("  - StudentID: int64 (integer) ✓")
print("  - Name: object (string) ✓")
print("  - Age: int64 (integer) ✓")
print("  - Grade: object (string) ✓")
print("  - Math, English, Science: float64 (decimal) ✓")
print("  - GPA: float64 (decimal) ✓")
print("  - Attendance: int64 (integer) ✓")

# =============================================================================
# Step 12: Set Index for Better Data Access
# =============================================================================
print("\n" + "=" * 80)
print("Step 12: Set Index for Better Access")
print("=" * 80)

# Set StudentID as index
df_indexed = df.set_index('StudentID')

print("\nDataFrame with StudentID as index:")
print(df_indexed.head(3))

print("\nNow access students by ID:")
print(f"Student 103 (Bob):")
print(df_indexed.loc[103])

print(f"\nStudent 102 Math score: {df_indexed.loc[102, 'Math']}")

# =============================================================================
# Step 13: Create New Columns
# =============================================================================
print("\n" + "=" * 80)
print("Step 13: Create New Columns")
print("=" * 80)

# Average score per student
df['Average_Score'] = (df['Math'] + df['English'] + df['Science']) / 3

# Performance category
df['Performance'] = df['Average_Score'].apply(
    lambda x: 'Excellent' if x >= 90 else 'Good' if x >= 80 else 'Fair' if x >= 70 else 'Needs Improvement'
)

print("\nNew columns added:")
print(df[['Name', 'Math', 'English', 'Science', 'Average_Score', 'Performance']])

# =============================================================================
# Step 14: Save Processed Data
# =============================================================================
print("\n" + "=" * 80)
print("Step 14: Save Processed Data")
print("=" * 80)

# Save to new CSV
output_file = base_dir / 'student_data_processed.csv'
df.to_csv(output_file, index=False)
print(f"\n✓ Saved processed data to '{output_file}'")

# Display summary
print("\n" + "=" * 80)
print("SUMMARY - Data Analysis Complete!")
print("=" * 80)
print(f"""
Dataset: Student Grades (10 students)

Findings:
- Total students: {len(df)}
- Average age: {df['Age'].mean():.1f} years
- Average GPA: {df['GPA'].mean():.2f}
- Top performers: {', '.join(df.nlargest(2, 'GPA')['Name'].values)}
- Grade A students: {len(df[df['Grade'] == 'A'])}
- Grade B students: {len(df[df['Grade'] == 'B'])}
- Grade C students: {len(df[df['Grade'] == 'C'])}

Skills demonstrated:
✓ Loading CSV with pd.read_csv()
✓ Inspecting data with .info(), .describe(), .head()
✓ Checking data types
✓ Filtering with boolean indexing
✓ Aggregating with .groupby()
✓ Calculating statistics
✓ Sorting with .sort_values()
✓ Creating new columns
✓ Saving processed data to CSV

Next steps:
- Use this data for visualization with Matplotlib
- Feature engineering for machine learning
- Statistical analysis and hypothesis testing
""")

print("\n" + "=" * 80)
print("END OF CSV EXAMPLE")
print("=" * 80)