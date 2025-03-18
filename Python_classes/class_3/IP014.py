import math
"""
This script performs calculations related to a circle based on user input.
The user is prompted to select an option and provide the radius of the circle.
The available options are:
1 - Calculate the diameter of the circle.
2 - Calculate the perimeter (circumference) of the circle.
3 - Calculate the area of the circle.
The script then performs the corresponding calculation and prints the result rounded to two decimal places.
Functions:
- None
Variables:
- option (str): The user's choice of calculation.
- radius (float): The radius of the circle provided by the user.
- diameter (float): The calculated diameter of the circle (if option 1 is selected).
- perimeter (float): The calculated perimeter of the circle (if option 2 is selected).
- area (float): The calculated area of the circle (if option 3 is selected).
Usage:
Run the script and follow the prompts to input the desired option and radius.
"""

option = input()   # não pode ser int() pois se ele receber outro input qqr, crasha
# 1 - calculate diameter
# 2 - calculate perimeter
# 3 - calculate area
radius = float(input())

if option == str("1"):   #em cima recebe str, temos de converter aqui para str
    diameter = 2 * radius
    print(f"Diameter: {round(diameter, ndigits=2)}")
elif option == str("2"):
    perimeter = 2 * math.pi * radius
    print(f"Perimeter: {round(perimeter, ndigits=2)}")
elif option == str("3"):
    area = math.pi * (radius ** 2)
    print(f"Area: {round(area, ndigits=2)}")
else:
    print("Invalid Option.")