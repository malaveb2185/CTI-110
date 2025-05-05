#Brandon Malave
#P3HW2
#04/19/2025
#Collecting employee salary information
#Input user information name, pay, and hours worked
#Input calculations 
#Display resutls

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = overtime_pay + regular_pay


print("--------------------------------------------------")
print(f"Employee name:  {employee_name}")
print("--------------------------------------------------")
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("--------------------------------------------------")
print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")