#Brandon Malave 
#04/12/2025
#P2HW2 (CTI-110)
#Module(1-6) Grades List
#Module 1-6 grade submission from user
#User input converted to float data type
#All grades in a list labled "module_grades"
#Calculate lowest grade, highest grade, sum of grades, and average of grades
#Display results

module_grade1 = float(input("Enter grades for Module 1:"))
module_grade2 = float(input("Enter grades for Module 2:"))
module_grade3 = float(input("Enter grades for Module 3:"))
module_grade4 = float(input("Enter grades for Module 4:"))
module_grade5 = float(input("Enter grades for Module 5:"))
module_grade6 = float(input("Enter grades for Module 6:"))

module_grades = [module_grade1, module_grade2, module_grade3, module_grade4, module_grade5, module_grade6]

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total/ len(module_grades)

print("------------Results------------")
print(f"Lowest Grade:        {lowest:.2f}")
print(f"Highest Grade:       {highest:.2f}")
print(f"Sum of Grades:       {total:.2f}")
print(f"Average:             {average:.2f}")
print("--------------------------------")