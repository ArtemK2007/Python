def remove_odd_index_elements(lst):
    result = [lst[i] for i in range(len(lst)) if i % 2 != 1]
    return result

user_input = input("Введіть елементи списку через пробіл: ")
my_list = user_input.split()

new_list = remove_odd_index_elements(my_list)

print("Список після видалення непарних елементів:", new_list)
