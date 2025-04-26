#Brandon Malave
#P4HW1
#04/26/2025
#Collects scores, drops lowest score, calculates average, and displays letter grade
score_num = int(input("How many scores do you want to enter? "))
print()

# Empty list
scores = []

for num in range(1, score_num + 1):
    # Collect scores
    score = float(input("Enter score #" + str(num) + ": "))
    # Validate entry
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) + " again: "))
    scores.append(score)

print()

# Drop lowest score
lowest = min(scores)
scores_modified = scores.copy()
scores_modified.remove(lowest)

# Calculate average
avg = sum(scores_modified) / len(scores_modified)

# Determine letter grade
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("-------------Results------------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {scores_modified}")
print(f"Scores Average: {avg:.2f}")
print(f"Grade         : {grade}")
print("---------------------------------")
