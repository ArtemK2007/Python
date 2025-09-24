def print_magazines(magazines):
    if not magazines:
        print("Журналів немає.")
    else:
        for name in magazines:
            info = magazines[name]
            print(f"{name}: ціна {info['price']} грн, тираж {info['circulation']}")


def add_magazine(magazines):
    name = input("Назва журналу: ")
    while True:
        try:
            price = float(input("Ціна: "))
            price = round(price, 2)
            break
        except ValueError:
            print("Помилка! Введіть число для ціни.")
    while True:
        try:
            circulation = int(input("Тираж: "))
            break
        except ValueError:
            print("Помилка! Введіть число для тиражу.")
    magazines[name] = {"price": price, "circulation": circulation}
    print("Додано журнал", name, ".")


def del_magazine(magazines):
    name = input("Назва журналу для видалення: ")
    if name in magazines:
        del magazines[name]
        print("Видалено журнал", name, ".")
    else:
        print("Журнал не знайдено.")


def print_sorted_magazines(magazines):
    sorted_magazines = {k: magazines[k] for k in sorted(magazines)}
    print("Відсортований словник журналів:")
    for name in sorted_magazines:
        info = sorted_magazines[name]
        print(f"{name}: ціна {info['price']} грн, тираж {info['circulation']}")


def avg_price_low_circulation(magazines):
    prices = [info['price'] for info in magazines.values() if info['circulation'] < 10000]
    if prices:
        avg = sum(prices) / len(prices)
        print(f"Середня ціна журналів з малим тиражем: {avg:.2f} грн")
    else:
        print("Немає журналів з малим тиражем.")


def main():
    magazines = {
        'Журнал "Наука"': {'price': 85.50, 'circulation': 12000},
        'Журнал "Техніка"': {'price': 50.00, 'circulation': 8500},
        'Журнал "Історія"': {'price': 92.75, 'circulation': 15000},
        'Журнал "Природа"': {'price': 65.20, 'circulation': 9800},
        'Журнал "Мистецтво"': {'price': 110.00, 'circulation': 7000}
    }

    while True:
        print("\n--- Меню ---")
        print("1. Переглянути всі журнали")
        print("2. Додати журнал")
        print("3. Видалити журнал")
        print("4. Переглянути журнали відсортовано")
        print("5. Середня ціна журналів з малим тиражем")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print_magazines(magazines)
        elif choice == "2":
            add_magazine(magazines)
        elif choice == "3":
            del_magazine(magazines)
        elif choice == "4":
            print_sorted_magazines(magazines)
        elif choice == "5":
            avg_price_low_circulation(magazines)
        elif choice == "6":
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
