#program that asks the user for the radius of a circle and the prints out the area of the circle.

import math

radius_str = input("Enter the radius of the circle: ")
radius = float(radius_str)
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is:{area:.2f}")