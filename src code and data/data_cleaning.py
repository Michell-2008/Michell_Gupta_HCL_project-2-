
import pandas as pd

# 1. Load the dataset
data = pd.read_csv("02_student_performance.csv")

# 2. Inspect the dataset
print("Dataset shape:", data.shape)
print(data.head())
print(data.info())

# 3. Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# 4. Check duplicate Student IDs
duplicates = data[data["Student_ID"].duplicated(keep=False)]

print("\nDuplicate Student IDs:")
print(duplicates)

# 5. Fill missing attendance values with median
median_attendance = data["Attendance_Percent"].median()

data["Attendance_Percent"] = data["Attendance_Percent"].fillna(
    median_attendance
)

print("\nMedian attendance used:", median_attendance)

# 6. Check marks outside the range 0–100
for column in ["Python_Marks", "Maths_Marks", "Physics_Marks"]:
    invalid = data[(data[column] < 0) | (data[column] > 100)]

    print("\nInvalid values in", column)
    print(invalid[["Student_ID", column]])

# 7. Check missing values after cleaning
print("\nMissing values after cleaning:")
print(data.isnull().sum())

# 8. Save the cleaned dataset
data.to_csv("cleaned_student_performance.csv", index=False)

print("\nData cleaning completed!")
