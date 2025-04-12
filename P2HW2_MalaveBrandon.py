#Brandon Malave
#04/05/2025
#P1HW2
#Displaying and calculating travel expenses


print("This program calculates and displays expenses")
budget= float(input("Enter your budget: "))
location= input("Enter your travel location: ")
gas=float(input("How much do you think you spend on gas?: "))
accommodation= float(input("Approximately, how much will you for accommodation/hotel: "))
food= float(input("Last, how much do you need for food?: "))

print("-------Travel Expenses-------")
print(f"{'Location:':<20}{location}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("---------------------------------")
remaining_balance = budget - (gas + accommodation + food)
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")