import math

x = float(input("Введіть число x: "))

if x > 45:
    z = -math.sqrt(x)
else:
    z = math.sin(2 * x)

print("z =", z)
