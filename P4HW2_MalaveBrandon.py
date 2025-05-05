# Brandon Malave 
# 04/26/2025
# P4HW2
# This program employee salary, including reg pay overtime pay
# Totals for overtime, regular, gross pay, and employee count
# User inputs employeee name 
# Display results for employee 
# Updated totals 
# Next employee 
# Loop ends, displaying totals


total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for the first employee's name
employee_name = input("Enter the employee's name or 'Done' to terminate: ")

# Start the loop
while employee_name != "Done":
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked  # ← small correction here too, it should be hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Display individual employee's pay
    print("--------------------------------------------------")
    print(f"Employee name:    {employee_name}")
    print("--------------------------------------------------")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("--------------------------------------------------")
    print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask for the next employee
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")

# After loop ends, display totals
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")