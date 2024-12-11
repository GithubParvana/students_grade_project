import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functools import reduce
from tabulate import tabulate


# Load the Excel file
input_file = "datasets/StudentGradesAndPrograms.xlsx"
output_file = "formatted_file.csv"


# Read the CSV file
df = pd.read_excel(input_file)

# Save it as a CSV
df.to_csv(output_file, index=False)

print(f"File successfully converted to {output_file}")


#    --- Tabular format  ---
dataset = pd.read_csv(output_file, header=1, names=["schoolyear", "gradeLevel", "classPeriod", "classType", "schoolName", "gradePercentage", "avid", "sped", "migrant", "ell", "student_ID"])

# get the headers (column names)
dataset_headers = df.columns.tolist()
print(dataset_headers)

# Create the tabular table
table = tabulate(dataset, headers=dataset_headers, tablefmt="grid")

file = open('table_file.txt', 'w', encoding='utf-8')
file.write(table)
file.close()


# ---   Some operation on Datset   ---

# Get a count of rows
print(len(df))  # 200994


# Get the size (rows, columns)
print(f"The number of rows is: {df.shape[0]}\nThe number of columns is: {df.shape[1]}")


# Get data types of the columns
data_types = df.dtypes
print(data_types)


"""
How does the average grade percentage vary across different class types (e.g., ENG, MAT, SCI, SOC)?

"""
# Group by classType and calculate the average gradePercentage
average_grades = dataset.groupby('classType')['gradePercentage'].mean()

print(average_grades)

# Format the numbers to 2 d.p. with a % symbol
average_grades_percent = average_grades.map("{:.2f}%".format)


with open('average_grade_percent.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(average_grades_percent.to_string(index=False, header=True))
    outfile.close()


# Visualization
average_grades.plot(kind='bar', color='skyblue', figsize=(8, 5))
plt.title('Average Grade Percentage by Class Type')
plt.xlabel('Class Type')
plt.ylabel('Average Grade Percentage (%)')
plt.xticks(rotation=0)
plt.show()


""" 
What is the grade percentage distribution for each school?

"""
import seaborn as sns
import plotly.express as px

# Load the data
dataset = pd.read_csv(output_file, header=1, names=["schoolyear", "gradeLevel", "classPeriod", "classType", "schoolName", "gradePercentage", "avid", "sped", "migrant", "ell", "student_ID"])


# Group by school and calculate summary statistics
summary_stats = dataset.groupby('schoolName')['gradePercentage'].agg(['mean', 'median', 'std', 'count'])


# Print the summary table
print(summary_stats)

# Aggregate the Data

""" 
Group the data by school and compute summary statistics
like the average, median, or standard deviation of grade percentages. 
This provides an overview without visualizing each individual grade.

"""
with open('summary_stats.txt', 'w', encoding='utf-8') as statfile:
    statfile.write(summary_stats.to_string(index=False, header=True))
    statfile.close()



"""
Do students with special education needs (sped = Y) perform differently compared to other students?
"""
# Create the plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='sped', y='gradePercentage', data=dataset, palette='Set2')


# Add labels and title
plt.title('Grade Percentage Distribution by Special Education Needs', fontsize=14)
plt.xlabel('Special Education Needs (sped)', fontsize=12)
plt.ylabel('Grade Percentage', fontsize=12)

"""
This boxplot will show the distribution of grade percentages 
for students with and without special education needs(sped = Y and sped = N)

"""
plt.show()


# Group the data by 'sped' and calculate the mean grade percentage
mean_grades = dataset.groupby('sped')['gradePercentage'].mean()


# Create the bar chart
mean_grades.plot(kind='bar', color=['skyblue', 'salmon'], figsize=(8, 6))


# Add labels and title
plt.title('Mean Grade Percentage by Special Education Needs', fontsize=14)
plt.xlabel('Special Education Needs (sped)', fontsize=12)
plt.ylabel('Mean Grade Percentage', fontsize=12)
plt.xticks(rotation=0)
plt.show()


"""
How do grade percentages differ for English learners (ell = Y) versus non-English learners?

"""

# Calculate average grade percentages for ELL and non-ELL students
ell_comparison = df.groupby('ell')['gradePercentage'].mean()


# Format the numbers to 2 d.p. with a % symbol
ell_comparison_percent = ell_comparison.map("{:.2f}%".format)
print(ell_comparison_percent)


with open('average_grade_ell_and_non_ell.txt', 'w', encoding='utf-8') as ellfile:
    ellfile.write(ell_comparison_percent.to_string(index=False, header=True))
    ellfile.close()


# The Bar chart will help us visually compare the performance of English learners and non-English learners.
ell_comparison.plot(kind='bar', color=['skyblue', 'orange'], figsize=(8, 6))
plt.title('Grade Percentage Comparison: ELL vs Non-ELL Students', fontsize=14)
plt.xlabel('ELL Status (Y/N)', fontsize=12)
plt.ylabel('Average Grade Percentage', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


""" 
Which grade level performs better overall across the two schools?
"""

# Calculate average grade % grouped by school and grade level
grade_level_performance = df.groupby(['schoolName', 'gradeLevel'])['gradePercentage'].mean().reset_index()

print(grade_level_performance)

grade_level_performance['gradePercentage'] = grade_level_performance['gradePercentage'].round(2)

# Create a bar plot to compare grade-level performance across schools
plt.figure(figsize=(12, 8))
sns.barplot(x='gradeLevel', y='gradePercentage', hue='schoolName', data=grade_level_performance, palette='Set2')


# Add labels and title
plt.title('Grade-Level Performance Across Schools', fontsize=16)
plt.xlabel('Grade Level', fontsize=14)
plt.ylabel('Average Grade Percentage', fontsize=14)
plt.legend(title='School Name', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


with open('grade_level_performance.txt', 'w', encoding='utf-8') as levelfile:
    levelfile.write(grade_level_performance.to_string(index=False, header=True))
    levelfile.close()


""" 
How does performance differ between Online Learning School and Allfeather Middle School for specific class types (e.g., ENG, MAT)?
"""

# Grouping by schoolName and classType, then calculating the mean gradePercentage
school_performance = df.groupby(['schoolName', 'classType'])['gradePercentage'].mean().reset_index()


# Format the 'gradePercentage' column to 2 d.p.
school_performance['gradePercentage'] = school_performance['gradePercentage'].round(2)


# Creating a grouped bar chart using Plotly
fig = px.bar(
    school_performance,
    x='classType',
    y='gradePercentage',
    color='schoolName',
    barmode='group',
    title='Average Grade Percentage by Class Type Across Schools',
    labels={'gradePercentage': 'Average Grade (%)', 'classType': 'Class Type'},
    text='gradePercentage'
)


# Add data labels
fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')


# Adjust layout for better readability
fig.update_layout(
    xaxis=dict(title='Class Type'),
    yaxis=dict(title='Average Grade (%)'),
    legend_title='School Name',
    legend=dict(orientation='v', title_font=dict(size=10)),
    width=1200, 
    height=600
)
fig.show()


""" 
Are students who participate in the AVID program (avid = Y) performing better overall?
"""

avid_performance = df.groupby('avid')['gradePercentage'].mean().reset_index()

avid_performance['gradePercentage'] = avid_performance['gradePercentage'].round(2)

avid_performance['avid'] = avid_performance['avid'].map({1: 'AVID (Yes)', 0: 'AVID (No)'})

plt.figure(figsize=(8, 6))
sns.barplot(data=avid_performance, x='avid', y='gradePercentage', palette='coolwarm')

plt.title('Comaprison of Grade Percentages by AVID Participation', fontsize=16)
plt.xlabel('AVID Participation', fontsize=12)
plt.ylabel('Average Grade Percentage', fontsize=12)

for i, row in avid_performance.iterrows():
    plt.text(i, row['gradePercentage'] + 1, f"{row['gradePercentage']}%", ha='center', fontsize=10)


plt.ylim(1, 100)
plt.show()
