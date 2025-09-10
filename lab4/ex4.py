def sum_list_elements(lst):
    return sum(lst)

user_input = input("Введіть числа списку через пробіл: ")
my_list = [int(x) for x in user_input.split()]
total = sum_list_elements(my_list)

print("Сума елементів списку:", total)
