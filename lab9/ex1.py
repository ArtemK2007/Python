import csv
import sys
import io

def process_gdp_life_expectancy(input_filename="API_SP.DYN.LE00.IN_DS2_en_csv_v2_736603.csv", output_filename="Life_Expectancy_2019_Selected_Countries.csv"):
    """
    Обробляє CSV-файл з даними про тривалість життя,
    фільтрує їх за 2019 роком для обраних країн та зберігає результат.
    """

    try:
        with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
            csv_reader = csv.reader(infile)
            
            for _ in range(4):
                try:
                    next(csv_reader)
                except StopIteration:
                    print(f"Помилка: Файл {input_filename} містить менше 5 рядків.")
                    return

            header = next(csv_reader)
            
            try:
                year_2019_index = header.index('2019')
                country_name_index = header.index('Country Name')
                country_code_index = header.index('Country Code')
            except ValueError as e:
                print(f"Помилка: Не знайдено необхідну колонку в заголовку. {e}")
                print(f"Очікувались: '2019', 'Country Name', 'Country Code'. Наявні: {header[:5]}...")
                return

            all_data = list(csv_reader)
            
            print("## 📄 Вміст .csv файлу (Обрані колонки та рядки) ##")
            print("-" * 50)
            print(f"{'Країна':<35} | {'Код':<4} | {'Тривалість життя (2019)':<25}")
            print("-" * 50)

            count = 0
            for row in all_data:
                if row[year_2019_index].strip():
                    country = row[country_name_index]
                    code = row[country_code_index]
                    le_2019 = row[year_2019_index]
                    print(f"{country:<35} | {code:<4} | {le_2019:<25}")
                    count += 1

                if count >= 10:
                    print("...")
                    break
            
            print("-" * 50)
            print(f"Показано {count} перших країн із наявними даними за 2019 рік.")
            print("\n")

            country_input = input("🌍 Введіть назви країн через кому для пошуку (наприклад: Ukraine, Poland, Germany, World): ")
            countries_to_find = [c.strip() for c in country_input.split(',') if c.strip()]
            
            if not countries_to_find:
                print("Пошук не виконано: Не введено жодної назви країни.")
                return
            
            print("\n")
            print(f"🔍 Пошук даних за 2019 рік для країн: {', '.join(countries_to_find)}")
            data_map = {row[country_name_index].upper(): row for row in all_data}
            
            found_data = []
            
            for country_name in countries_to_find:
                key = country_name.upper()
                if key in data_map:
                    row = data_map[key]
                    le_2019 = row[year_2019_index]               
                    if le_2019.strip():
                        found_data.append([row[country_name_index], '2019', le_2019])
                        print(f"✅ Знайдено: {row[country_name_index]} - {le_2019} років")
                    else:
                        found_data.append([row[country_name_index], '2019', 'N/A'])
                        print(f"⚠️ Немає даних за 2019 рік для: {row[country_name_index]}")
                else:
                    print(f"❌ Країну не знайдено: {country_name}")

            
            if found_data:
                try:
                    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
                        csv_writer = csv.writer(outfile)
                        csv_writer.writerow(['Country Name', 'Year', 'Life Expectancy (years)'])
                        csv_writer.writerows(found_data)
                        
                    print("\n")
                    print(f"🎉 Результати пошуку успішно записано до файлу: **{output_filename}**")
                except IOError as e:
                    print(f"Помилка запису файлу {output_filename}: {e}")
            else:
                print("⚠️ Немає даних для запису в новий файл.")

    except FileNotFoundError:
        print(f"🚨 Помилка: Файл **{input_filename}** не знайдено.")
        print("Переконайтеся, що файл завантажено з порталу і знаходиться в тій же папці, що і програма.")
    except Exception as e:
        print(f"🚨 Виникла неочікувана помилка: {e}")

INPUT_FILE = "API_SP.DYN.LE00.IN_DS2_en_csv_v2_736603.csv"


if __name__ == "__main__":
    process_gdp_life_expectancy(input_filename=INPUT_FILE)