N = int(input("Введіть кількість елементів у масиві (N): "))
my_array = []
positive_even_sum = 0

print(f"Введіть {N} цілих чисел:")
for i in range(N):
    element = int(input(f"Елемент {i + 1}: "))
    my_array.append(element)

for number in my_array:
    if number > 0 and number % 2 == 0:
        positive_even_sum += number

print(f"\nМасив, який ви ввели: {my_array}")
print(f"Сума додатніх парних елементів: {positive_even_sum}")