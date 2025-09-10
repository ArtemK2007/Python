def sum_list_elements(lst):
    return sum(lst)

user_input = input("Введіть числа списку через пробіл: ").split()

# перевірка на букви
if all(x.lstrip('-').isdigit() for x in user_input):  # підтримка від’ємних чисел
    my_list = [int(x) for x in user_input]
    total = sum_list_elements(my_list)
    print("Сума елементів списку:", total)
else:
    print("Помилка: введено не число!")
