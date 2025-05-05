# Brandon Malave 
# P3HW1
#04/19/2025
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grades for Module 1: "))
mod_2 = float(input("Enter grades for Module 2: "))
mod_3 = float(input("Enter grades for Module 3: "))
mod_4 = float(input("Enter grades for Module 4: "))
mod_5 = float(input("Enter grades for Module 5: "))
mod_6 = float(input("Enter grades for Module 6: "))


# add grades entered to a list

mod_grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

lowest = min(mod_grades)
highest = max(mod_grades)
total = sum(mod_grades)
avg = total/ len(mod_grades)

#results 
print("------------Results------------")
print(f"Lowest Grade:        {lowest:.2f}")
print(f"Highest Grade:       {highest:.2f}")
print(f"Sum of Grades:       {total:.2f}")
print(f"Average:             {avg:.2f}")
print("--------------------------------")

# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
 print('Your grade is: B')
elif avg >= 70:
 print('Your grade is: C')
elif avg >= 60:
 print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this




