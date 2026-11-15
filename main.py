import pandas as pd
import matplotlib.pyplot as plt

def analyze_employee_data(file_path):
    # 2. Load the CSV file using Pandas
    df = pd.read_csv(file_path)
    
    # Clean duplicate values
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    
    # Clean missing values: fill missing salaries with the mean of valid salaries
   
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    mean_salary = df['Salary'].mean()
    df['Salary'] = df['Salary'].fillna(mean_salary)
    
    print(f"--- Data Cleansing Report ---")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Missing Salary filled with mean: {mean_salary:.2f}")
    print(f"Cleaned total rows: {len(df)}\n")

    while True:
        print("==============================")
        print("   EMPLOYEE DATA ANALYZER     ")
        print("==============================")
        print("1. Summary (Total employees, Average salary, Highest paid, Total payroll)")
        print("2. Department-wise analysis and filter above salary limit")
        print("3. Exit")
        
        choice = input("Enter your menu option choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            total_employees = len(df)
            avg_salary = df['Salary'].mean()
            max_row = df.loc[df['Salary'].idxmax()]
            highest_paid = f"{max_row['Name']} ({int(max_row['Salary'])})"
            total_payroll = df['Salary'].sum()
            
            print("\n[Test Case Output - Summary]")
            print(f"Employees: {total_employees} | Average salary: {avg_salary:.2f}")
            print(f"Highest paid: {highest_paid}")
            print(f"Total payroll: {int(total_payroll)}\n")
            
        elif choice == '2':
            print("\n--- Department-wise Count and Average Salary ---")
            dept_summary = df.groupby('Department').agg(
                Employee_Count=('Emp_ID', 'count'),
                Avg_Salary=('Salary', 'mean')
            ).reset_index()
            
            for _, row in dept_summary.iterrows():
                print(f"{row['Department']}: {row['Employee_Count']} employee(s) | Avg salary: {row['Avg_Salary']:.2f}")
            
            # 4. Use boolean filtering to list employees above a given salary
            try:
                limit = float(input("\nEnter salary limit to filter employees above: "))
                filtered_df = df[df['Salary'] > limit]
                print(f"\nEmployees earning above {limit}:")
                if filtered_df.empty:
                    print("No employees found above this salary limit.")
                else:
                    for _, row in filtered_df.iterrows():
                        print(f"- {row['Name']} ({int(row['Salary'])})")
            except ValueError:
                print("Invalid input for salary limit.")
            
            # 5. Calculate highest paid employee and plot Matplotlib bar chart
            print("\nGenerating Department-wise Average Salary Bar Chart...")
            plt.figure(figsize=(8, 5))
            plt.bar(dept_summary['Department'], dept_summary['Avg_Salary'], color=['#3498db', '#e74c3c'])
            plt.xlabel('Department')
            plt.ylabel('Average Salary')
            plt.title('Department-wise Average Salary')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print("Bar chart 'Department-wise Average Salary' displayed.\n")
            
        elif choice == '3':
            print("Exiting program. Good luck with your project submission!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    analyze_employee_data("employees.csv")