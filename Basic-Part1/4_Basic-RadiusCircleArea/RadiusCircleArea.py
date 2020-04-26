'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
'''

from math import pi
radius = float(input("\nEnter radius of circle:"))
area = pi * radius * radius
print("Area:" + str(area))