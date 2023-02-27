# code by : SALMAN MALLAH
import math

"""# Task 1
# Design a calculator that takes 2 values from user to apply mathematical
# operations Addition, subtraction, and division, multiplication, floor
# division.
"""
# taking inputs from user:
number_one = int(input('Enter first number: '))
number_two = int(input('Enter second number: '))

print(f"addition of {number_one} and {number_two} = {number_one + number_two}")
print(f"subtraction of {number_one} from {number_two} = {number_one - number_two}")
print(f"Multiplication of {number_one} and {number_two} = {number_one * number_two}")
print(f"Division of {number_one} by {number_two} = {number_one / number_two}")


"""# Task 2
# Takes 2 arguments from user and check whether they are equal or no
"""
# taking two integers from user
int_one = int(input('enter a number: '))
int_two = int(input('enter anohter number: '))
print(f"Is {int_one} and {int_two} are equal?: {int_one == int_two} ")


"""
# Task 3
# Design a system that calculates the area of a plot.
# code:
# as we know area can be find with product of length and width:
"""
# taking width and length from user
width = int(input('Enter the width of plot: '))
length = int(input('Enter the width of plot: '))
print(f"If the width: {width} and length: {length} the area will be: {width*length}")



"""# Task 4
# Design a BMI system both in (US and Metric unit) .
# Just like this
# https://www.calculator.net/bmi-calculator.html
# You can search the formula by yourself. This system only calculates the
# BMI. You don’t need to predict whether the BMI is normal,
# underweight or overweight. Just BMI indicator.

# formula: BMI = weight (kg) / (height (m))^2
"""
# taking inputs from user
weight = int(input('Enter weight in Kg: '))
height = int(input('Enter height in Meters: '))
result = weight / ((height)**2)
print(result)

"""
# Task 5
# Create a program that convert –
# User weight in kG into pounds , and
# height into inches
# Radian to degree
# Area of a trapezoid –
# Area of a parallelogram
# Calculate surface volume and area of a cylinder.
"""
# kg into pounds
# to convert kg into pound: formula: pounds = kg * 2.20462
# taking the input from user
kg = float(input('Enter the kilograms to convert it into pounds: '))
result = kg * 2.20462
print(f'{kg} Kg in pounds is: {result}')

# height(meters) into inches 
# formula: inches = meters * 39.370
meter = float(input('enter height to convert into inches: '))
result = meter * 39.370
print(f"{meter} meter is equal to {result} inches")

# radian into degree
#degree = 1rad × 180/π = 57.296°
radian = float(input('Enter radian to convert it into degree: '))
degree = radian * (180/math.pi)
print(f"{radian} Radian into {degree:.2f} Degree")


# Area of a trapezoid
# Area = (lengthOne + LengthTwo) * height / 2
length_one = float(input('Enter first length: '))
length_two = float(input('Enter second legnth: '))
height = float(input('Enter height '))
area = (length_one + length_two) * height /2
print(f'The area of Trapezoid is {area}')


# Area of a parallelogram
# formula: A = base x height
basogram = float(input('Enter The base of parallelogram: '))
heightogram = float(input('Enter the height of parallelogram: '))
area = basogram * heightogram
print(f"The area of parallelogram is: {area}")




"""# Calculate surface volume and area of a cylinder.
# To calculate the surface area and volume of a cylinder,
# you need to know the radius of the base (r) and the height (h) of the cylinder.
# The formula for the surface area (A) of a cylinder is:
"""
# Surface Area:
# A = 2π*radius² + 2π*radius*height
height_of_cylinder = float(input("Enter the height of cylinder: "))
radius_of_base = float(input('Enter the radius of the base: '))
area_of_cylinder = 2*(math.pi)*(radius_of_base**2) + 2*(math.pi)*radius_of_base*height_of_cylinder
print(f"The area of cylinder is :{area_of_cylinder}")

# Volume:
# V = π*radius²*height
volume_of_cylinder = math.pi*(radius_of_base**2)*height_of_cylinder
print(f"The volume of cylinder: {volume_of_cylinder}")


