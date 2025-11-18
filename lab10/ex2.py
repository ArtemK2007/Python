import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_216063.csv' 
try:
    data = pd.read_csv(FILE_PATH, skiprows=4)
except FileNotFoundError:
    print(f"Помилка: Файл '{FILE_PATH}' не знайдено. Переконайтеся, що файл існує та шлях правильний.")
    exit()

COUNTRIES = ['Ukraine', 'Poland']
YEAR_START = 2000
YEAR_END = 2023

year_cols = [col for col in data.columns if col.isdigit() and int(col) >= YEAR_START and int(col) <= YEAR_END]


df_filtered = data[data['Country Name'].isin(COUNTRIES)]
df_ready = df_filtered[['Country Name'] + year_cols].set_index('Country Name').transpose()

df_ready = df_ready.fillna(0)

df_ready.index = df_ready.index.astype(str)

def plot_gdp_dynamics(df):
    """Будує лінійний графік динаміки ВВП (Gross Domestic Product)."""
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(df.index, df['Ukraine'] / 1e9, 
             marker='o', linestyle='-', color='blue', linewidth=2, 
             label='Україна')
             
    plt.plot(df.index, df['Poland'] / 1e9, 
             marker='s', linestyle='--', color='green', linewidth=2, 
             label='Польща')
    
    plt.title('Динаміка ВВП (у поточних цінах, 2000-2023)', fontsize=16)
    plt.xlabel('Рік', fontsize=12)
    plt.ylabel('ВВП, млрд. USD', fontsize=12)
    plt.legend(fontsize=10, loc='best')
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.xticks(df.index[::3], rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bar_chart_gdp(df):
    """Будує стовпчасту діаграму для обраної користувачем країни."""
    
    country_name = input("Введіть назву країни для стовпчастої діаграми (Ukraine або Poland): ").strip()
    
    if country_name not in df.columns:
        print(f"Дані для країни '{country_name}' не знайдено в наборі.")
        return

    values_billion = df[country_name].values / 1e9 
    years = df.index
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(years, values_billion, color='#FFC300', alpha=0.8) 
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5, 
                 f'{yval:.1f}', ha='center', va='bottom', fontsize=9, rotation=45)

    plt.title(f'ВВП для {country_name} (2000-2023)', fontsize=16)
    plt.xlabel('Рік', fontsize=12)
    plt.ylabel('ВВП, млрд. USD', fontsize=12)
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show() 

def plot_pie_gdp(df):
    """Будує кругову діаграму, порівнюючи частку ВВП двох країн в останньому році."""
    
    YEAR = df.index[-1]

    ukraine_gdp = df['Ukraine'][YEAR]
    poland_gdp = df['Poland'][YEAR]

    labels = ['Україна', 'Польща']
    sizes = [ukraine_gdp, poland_gdp]

    non_zero_sizes = [size for size in sizes if size > 0]
    non_zero_labels = [label for size, label in zip(sizes, labels) if size > 0]
    
    if not non_zero_sizes:
        print(f"Дані ВВП для {YEAR} року відсутні.")
        return

    colors = ['#0057B8', '#DC143C']
    explode = (0.05, 0) 
    
    plt.figure(figsize=(8, 8))

    plt.pie(non_zero_sizes, 
            explode=explode[:len(non_zero_sizes)], 
            labels=non_zero_labels, 
            colors=colors[:len(non_zero_sizes)],
            autopct='%1.1f%%',       
            shadow=True,             
            startangle=90)           
    
    plt.title(f'Співвідношення ВВП України та Польщі у {YEAR} році', fontsize=14)
    plt.axis('equal') 
    plt.show()


print("--- Завдання 2.1: Лінійний графік динаміки ВВП ---")
plot_gdp_dynamics(df_ready)

print("\n--- Завдання 2.2: Стовпчаста діаграма ВВП ---")
plot_bar_chart_gdp(df_ready)

print("\n--- Завдання 3: Кругова діаграма співвідношення ВВП ---")
plot_pie_gdp(df_ready)