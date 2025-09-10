import math

def calculate_z(x):
    if x > 45:
        return -math.sqrt(x)
    else:
        return math.sin(2 * x)

def fibonacci_greater_than(p):
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b
    return b


x = float(input("Введіть число x: "))
z = calculate_z(x)
print("z =", z)

p = int(input("Введіть число p: "))
fib = fibonacci_greater_than(p)
print("Перше число Фібоначчі більше за", p, "це:", fib)
