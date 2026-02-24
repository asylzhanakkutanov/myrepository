#1
import math

degree = float(input("Degree: "))

radian = math.radians(degree)

print("Radian:", radian)
#2
import math

height = float(input())
base1 = float(input())
base2 = float(input())

area = ((base1 + base2) / 2) * height

print(round(area, 2))
#3
import math

n = int(input())
s = float(input())

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(area)
#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)