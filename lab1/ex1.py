while True:
    a = int(input("Введіть a (від 1 до 100): "))
    b = int(input("Введіть b (від 1 до 100): "))
    if 1 <= a <= 100 and 1 <= b <= 100:
        break
    else:
        print("Обидва числа повинні бути в діапазоні від 1 до 100.")


if a > b:
    X = 2 * a + b
elif a == b:
    X = -2
else:  # a < b
    X = (a - 5) / b

print(f"X = {X}")