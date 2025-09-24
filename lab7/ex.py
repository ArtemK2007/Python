import re

def create_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Привіт 123 текст\n")
            f.write("Рядок з числом 45.67 і ще -89\n")
            f.write("Дійсні числа: 3.14 -2.71 0.001\n")
            f.write("Ще трохи тексту без чисел\n")
            f.write("Ще рядок з числами: 1200 -4.5\n")
        print(f"Файл {filename} успішно створено.")
    except Exception as e:
        print("Помилка при створенні файлу:", e)


def extract_numbers(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        numbers = re.findall(r"[-+]?\d*\.?\d+(?:[-+]?\d+)?", text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(" ".join(numbers))

        print(f"Числа з {input_file} збережено у {output_file}.")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print("Помилка при обробці файлу:", e)

def find_max_number(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                print("Файл порожній.")
                return None

            numbers = list(map(float, content.split()))
            max_num = max(numbers)
            print(f"Найбільше число у файлі {filename}: {max_num}")
            return max_num
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print("Помилка при читанні файлу:", e)


file1 = "TF14_1.txt"
file2 = "TF14_2.txt"

create_file(file1)
extract_numbers(file1, file2)
find_max_number(file2)
