#Brandon Malave
#04/05/2025
#P1HW2
#Displaying and calculating travel expenses

print("This program calculates and displays expenses")
budget= int(input("Enter your budget: "))
location= input("Enter your travel location: ")
gas=int(input("How much do you think you spend on gas?: "))
accomadation= int(input("Approximately, how much will you for accomadation/hotel: "))
food= int(input("Last, how much do you need for food?: "))

print("-------Travel Expenses-------")
print(f"Location:{location}")
print(f"Initial Budget:{budget}")
print("\n")
print(f"Fuel:{gas}")
print(f"Accomadation:{accomadation}")
print(f"Food:{food}")
remaining_balance= (budget)-(gas + accomadation + food)
print(f"Remaining Balance:", remaining_balance)