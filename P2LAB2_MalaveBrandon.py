#Brandon Malave
#04/12/2025
#P2LAB2
#Using dictionaries 

cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26, }
#Get keys from dict 

cars_keys = cars.keys()
print(cars_keys)
print(*cars_keys, sep = ", ")

#Get a car from user and mpg for given car  
car_name = input("Enter a car: ")
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon")

#Get miles from user 
miles_driven = float(input(f"How many miles will you drive the car {car_name}?"))
                     
#Calculations
gallons_needed = miles_driven/car_mpg

#Display
print(f"{gallons_needed:.2f} gallons of gas are need to drive the {car_name} {miles_driven} miles")