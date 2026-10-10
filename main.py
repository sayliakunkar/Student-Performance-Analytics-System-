
import pandas as pd
import numpy as np

# Read student data
df = pd.read_csv("students.csv")

subjects = ["Python", "SQL", "Excel", "PowerBI"]


# Function to calculate total and average
def calculate_marks(data):
    data["Total"] = np.sum(data[subjects].values, axis=1)
    data["Average"] = np.mean(data[subjects].values, axis=1).round(2)
    return data


# Function to assign grades
def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to check pass or fail
def check_result(row):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"

    if row["Attendance"] < 75:
        return "Fail"

    return "Pass"


# Process student records
df = calculate_marks(df)

df["Grade"] = df["Average"].apply(assign_grade)
df["Result"] = df.apply(check_result, axis=1)

# Display student performance
print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

# Class statistics
print("\n===== CLASS STATISTICS =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())

# Pass and fail statistics
print("\n===== PASS / FAIL STATISTICS =====")
print(df["Result"].value_counts())

# Subject-wise analysis
print("\n===== SUBJECT-WISE AVERAGE =====")
for subject in subjects:
    print(subject, ":", round(df[subject].mean(), 2))

# Top-performing students
print("\n===== TOP 3 STUDENTS =====")
top_students = df.nlargest(3, "Average")
print(top_students[["Name", "Average", "Grade"]].to_string(index=False))

# Save analyzed data
df.to_csv("student_analysis_report.csv", index=False)

print("\nAnalysis report saved successfully!")
