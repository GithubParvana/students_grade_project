![](cover_page.jpg)



## Students Grade and Programs


## Overview
This project analyzes student performance data from multiple schools to uncover insights about grades, demographic factors, and program participation. By examining trends and relationships between academic performance and variables like grade levels, demographics, and specialized programs, the project aims to provide actionable isnights for improving student outcomes.

By leveraging Python libraries such as Pandas, Numpy, and Matplotlib, this project provides a comprehensive analysis of a dataset containing 22,000 student records from 17 schools.



## Features
- Demographic Analysis: Explore how SPED, ELL, and migrant statuses influence performance.
- Program Participation: Evaluate the impact of AVID participation on student grades.
- School Comparisons: Compare performance trends between schools and class types.
- Grade-Level Insights: Identify which grade levels perform better across schools.
- Visualizations: Generate clear and insightful visual representations, such as boxplots, bar charts, and line graphs.



## Technologies Used

- **Python**

- **Libraries:**
    - **Pandas:** Data manipulation and analysis

    - **Matplotlib** Data Visualization.

    - **Numpy:** Numerical computations.

- **Jupyter Notebook:** Interactive data explaration.

- **Microsoft Excel:** Initial data inspection and formatting.




## Data Description

The dataset includes 22,000 records of student performance from 17 schools. Key columns include:

- *schoolName:* Name of the school.
- *gradeLevel:* Grade level (e.g., 1, 2, 3, KG)
- *classType:* Subject area (e.g., MAT, ENG, SCI).
- *gradePercentage:* Final grade percentage for the student.
- *avid:* Indicates if the student participates in the AVID program (Y/N).
- *sped:* Indicates if the student has special education needs (Y/N).
- *ell:* Indicates if the student is and English Language Learner (Y/N).
- *migrant:* Indicates if the student is a migrant (Y/N).



## Visualizations
Key visualizations include:

- **Boxplots:** Compares grades for SPED vs. Non-SPED students or AVID participants.
- **Bar Charts:** Show average performance by grade level or school



## How to Use
1. Clone the repository:
``` bash
git clone https://github.com/GithubParvana/students_grade_project.git

Navigate to the project directory:
``` bash
cd students_grade_project


2. Install dependencies:
pip install -r requirements.txt


3. Run the provided script to analyze and visualize results:
python analysis.py



4. Explore the visualizations in "figures_pictures" folder and results in the .txt files: For example, "data_table_file.txt" and etc.



Dataset Sources:
# Kaggle Dataset
![](https://www.kaggle.com/datasets/marmarplz/student-academic-grades-and-programs/data)


Special thanks to:
- Matplotlib for data visualization tools.
- Educational data provided by Kaggle.
