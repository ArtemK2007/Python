import json
import os
from typing import List, Dict, Any

DATA_FILE = "magazines_data.json"
RESULT_FILE = "magazines_result.json"
SEARCH_FIELD = "title"

def load_data(filename: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filename):
        print(f"Попередження: Файл '{filename}' не знайдено. Створюється порожній список.")
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print(f"Попередження: Файл '{filename}' містить некоректний формат (очікується список).")
                return []
    except json.JSONDecodeError:
        print(f"Помилка: Некоректний JSON-формат у файлі '{filename}'.")
        return []
    except Exception as e:
        print(f"Неочікувана помилка при читанні файлу '{filename}': {e}")
        return []

def save_data(data: List[Dict[str, Any]], filename: str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Дані успішно збережено у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі файлу '{filename}': {e}")

def initialize_data():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        initial_magazines = [
            {"title": "Наука та Життя", "price": 120.50, "circulation": 15000, "year": 2024},
            {"title": "IT-Огляд", "price": 95.00, "circulation": 8500, "year": 2024},
            {"title": "Економіст", "price": 150.00, "circulation": 9900, "year": 2024},
            {"title": "Популярна Фізика", "price": 110.00, "circulation": 10000, "year": 2024},
            {"title": "Мандрівник", "price": 80.00, "circulation": 5000, "year": 2024},
        ]
        save_data(initial_magazines, DATA_FILE)
        print(f"Створено початковий файл '{DATA_FILE}' з 5 записами.")

def display_data(data: List[Dict[str, Any]]):
    if not data:
        print("📁 Файл порожній або не містить даних для відображення.")
        return
    print("\n" + "="*50)
    print("## Вміст JSON файлу з даними про журнали ##")
    print(f"{'Назва':<25} | {'Ціна (грн.)':<15} | {'Тираж (прим.)':<15}")
    print("-"*50)
    for item in data:
        title = item.get('title', 'N/A')
        price = item.get('price', 'N/A')
        circulation = item.get('circulation', 'N/A')
        
        price_str = f"{price:.2f}" if isinstance(price, (int, float)) else str(price)
        circ_str = str(circulation)
        
        print(f"{title:<25} | {price_str:<15} | {circ_str:<15}")
    print("="*50 + "\n")

def add_record(data: List[Dict[str, Any]]):
    print("\n--- Додавання нового запису ---")
    try:
        title = input("Введіть назву журналу: ").strip()
        price = float(input("Введіть ціну журналу (наприклад, 120.50): "))
        circulation = int(input("Введіть тираж журналу (наприклад, 15000): "))
        year = int(input("Введіть рік випуску (наприклад, 2024): "))
        
        if not title or price <= 0 or circulation <= 0 or year < 1900:
            print("Помилка: Введено некоректні дані. Запис не додано.")
            return

        new_record = {
            "title": title,
            "price": price,
            "circulation": circulation,
            "year": year
        }
        data.append(new_record)
        save_data(data, DATA_FILE)
    except ValueError:
        print("Помилка: Некоректний формат числа для ціни, тиражу або року.")

def delete_record(data: List[Dict[str, Any]]):
    print("\n--- Видалення запису ---")
    search_value = input(f"Введіть назву журналу для видалення (поле '{SEARCH_FIELD}'): ").strip()
    
    initial_length = len(data)
    new_data = [item for item in data if item.get(SEARCH_FIELD).strip().lower() != search_value.lower()]
    
    deleted_count = initial_length - len(new_data)
    
    if deleted_count > 0:
        data[:] = new_data
        save_data(data, DATA_FILE)
        print(f"✅ Успішно видалено {deleted_count} запис(ів) з назвою '{search_value}'.")
    else:
        print(f"⚠️ Жодного запису з назвою '{search_value}' не знайдено.")

def search_data(data: List[Dict[str, Any]]):
    if not data:
        print("Пошук неможливий: Дані відсутні.")
        return
        
    print(f"\n--- Пошук за полем '{SEARCH_FIELD}' ---")
    search_value = input(f"Введіть значення для пошуку (Назва журналу): ").strip()
    
    results = [
        item for item in data 
        if item.get(SEARCH_FIELD) and search_value.lower() in item[SEARCH_FIELD].lower()
    ]
    
    if results:
        print(f"\nЗнайдено {len(results)} запис(ів):")
        display_data(results)
    else:
        print(f"❌ Жодних записів, що містять '{search_value}', не знайдено.")

def solve_variant_task(data: List[Dict[str, Any]]):
    print("\n--- Виконання завдання за варіантом (Середня вартість) ---")
    
    filtered_magazines = []
    
    for item in data:
        if isinstance(item.get('circulation'), int) and item['circulation'] < 10000:
            if isinstance(item.get('price'), (int, float)):
                filtered_magazines.append(item)
    
    total_cost = sum(item['price'] for item in filtered_magazines)
    count = len(filtered_magazines)
    
    if count > 0:
        average_cost = total_cost / count
        
        print(f"Журналів з тиражем < 10000: {count}")
        print(f"Загальна вартість: {total_cost:.2f} грн")
        print(f"✅ Середня вартість журналів з тиражем < 10000: **{average_cost:.2f} грн**")
        
        result_data = {
            "task_description": "Середня вартість журналів, тираж яких менше 10000 примірників.",
            "threshold": 10000,
            "filtered_count": count,
            "average_cost": round(average_cost, 2),
            "magazines_included": [
                {"title": mag['title'], "price": mag['price'], "circulation": mag['circulation']}
                for mag in filtered_magazines
            ]
        }
        
        save_data(result_data, RESULT_FILE)
    else:
        print("⚠️ Жодного журналу з тиражем менше 10000 примірників не знайдено.")

def main():
    initialize_data()
    data = load_data(DATA_FILE)
    
    while True:
        print("\n" + "*"*50)
        print("МЕНЮ РОБОТИ З JSON-ДАНИМИ ПРО ЖУРНАЛИ")
        print("*"*50)
        print("1. Вивести вміст JSON файлу на екран")
        print("2. Додати новий запис")
        print("3. Видалити запис (за назвою)")
        print(f"4. Пошук даних (за полем '{SEARCH_FIELD}')")
        print("5. Розв'язати завдання варіанту (Середня вартість)")
        print("0. Вихід")
        print("-" * 50)
        
        choice = input("Оберіть дію (0-5): ").strip()
        
        if choice == '1':
            display_data(data)
        elif choice == '2':
            add_record(data)
        elif choice == '3':
            delete_record(data)
        elif choice == '4':
            search_data(data)
        elif choice == '5':
            solve_variant_task(data)
        elif choice == '0':
            print("Завершення роботи програми. До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")
        
        data = load_data(DATA_FILE)

if __name__ == "__main__":
    main()