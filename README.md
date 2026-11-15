# Employee Data Analyzer

A simple Python tool I built to clean and analyze employee records from a CSV file. It takes raw employee data, fixes missing or duplicate entries, calculates basic payroll stats, and plots department salary averages using Pandas and Matplotlib.

## What it does
- **Cleans the data**: Removes any duplicate rows and fills in missing salary spots using the average of the valid salaries.
- **Interactive console menu**:
  - **Option 1**: Shows total headcount, overall average salary, the highest-paid employee, and total payroll.
  - **Option 2**: Breaks down employee counts and average pay by department, lets you filter out employees earning above a specific limit, and pops up a bar chart comparing departmental averages.

## Setup
Make sure you have Python 3 installed. Before running the code, install Pandas and Matplotlib from your terminal:
```bash
pip install pandas matplotlib