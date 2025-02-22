#Write a Python program to convert degree to radian.
import math

def degrees_to_radians(degree):
    return degree * (math.pi / 180)

degree = float(input("Введите градусы: "))
radian = degrees_to_radians(degree)
print(f"Радианы: {radian:.6f}")
