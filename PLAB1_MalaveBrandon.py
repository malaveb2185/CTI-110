#Brandon Malave
#04/12/2025
#CTI-110
#Using Math Expressions
import math 

#Get radius user
radius = float(input("Enter the radius: "))

#Calculate cicumfrance, diameter, area
cir = 2 * math.pi  * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print (f"The diamter of the circle is {diam:.1f}")
print (f"The circumference of the circle is {cir:.2f}")
print (f"The area of the circle is {area:.3f}")
