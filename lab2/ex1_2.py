p = int(input("Введіть число p: "))

a, b = 1, 1
while b <= p:
    a, b = b, a + b

print("Перше число Фібоначчі більше за", p, "це:", b)
