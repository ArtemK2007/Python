import pandas as pd

# ==============================================================================
# 1. Словник і створення DataFrame
# ==============================================================================

# Доповнений словник (дані про журнали)
magazines_data = {
    'Журнал "Наука"': {'price': 85.50, 'circulation': 12000, 'category': 'Науковий', 'quantity_sold': 500},
    'Журнал "Техніка"': {'price': 50.00, 'circulation': 8500, 'category': 'Технічний', 'quantity_sold': 350},
    'Журнал "Історія"': {'price': 92.75, 'circulation': 15000, 'category': 'Гуманітарний', 'quantity_sold': 600},
    'Журнал "Природа"': {'price': 65.20, 'circulation': 9800, 'category': 'Науковий', 'quantity_sold': 450},
    'Журнал "Мистецтво"': {'price': 110.00, 'circulation': 7000, 'category': 'Гуманітарний', 'quantity_sold': 200},
    'Журнал "Мода"': {'price': 150.00, 'circulation': 6000, 'category': 'Лайфстайл', 'quantity_sold': 100},
    'Журнал "Спорт"': {'price': 70.00, 'circulation': 11000, 'category': 'Спортивний', 'quantity_sold': 550}
}

print("## 📚 Вміст доповненого словника ##")
for name, info in magazines_data.items():
    print(f"- {name}: ціна {info['price']} грн, тираж {info['circulation']}, категорія: {info['category']}, продано: {info['quantity_sold']}")

# Перетворення словника на DataFrame та конвертація типів
df = pd.DataFrame(magazines_data).T
df['price'] = df['price'].astype(float)
df['circulation'] = df['circulation'].astype(int)
df['quantity_sold'] = df['quantity_sold'].astype(int)

# ==============================================================================
# 2. Базовий аналіз даних
# ==============================================================================

print("\n" + "="*60 + "\n")
print("## 📊 Базовий аналіз даних ##")

print("\n### 1. Перші 3 рядки DataFrame (df.head(3)) ###")
print(df.head(3))

print("\n### 2. Типи даних (df.dtypes) ###")
print(df.dtypes)

print("\n### 3. Розмір DataFrame (df.shape) ###")
print(f"Кількість рядків і стовпців: {df.shape}")

print("\n### 4. Описова статистика (df.describe()) ###")
print(df.describe())

# ==============================================================================
# 3. Маніпуляції та агрегація даних
# ==============================================================================

print("\n" + "="*60 + "\n")
print("## ⚙️ Маніпуляції та агрегація ##")

# Додавання нового стовпця: Загальна вартість продажу
df['total_sales_uah'] = df['price'] * df['quantity_sold']

print("\n### 5. DataFrame з новим стовпцем 'total_sales_uah' ###")
print(df[['price', 'quantity_sold', 'total_sales_uah']].head())

# Фільтрація: Журнали з ціною понад 90 грн
filter_price = 90.00
df_filtered = df[df['price'] > filter_price]

print(f"\n### 6. Фільтрація: Ціна > {filter_price:.2f} грн ###")
print(df_filtered)

# Сортування: За спаданням ціни
df_sorted = df.sort_values(by='price', ascending=False)

print("\n### 7. Сортування за ціною (спадання) ###")
print(df_sorted[['price', 'circulation', 'total_sales_uah']])

# Групування: Середнє значення за категорією
df_grouped_mean = df.groupby('category')[['price', 'circulation', 'total_sales_uah']].mean().round(2)

print("\n### 8. Групування за 'category' та середнє значення ###")
print(df_grouped_mean)

# ==============================================================================
# 4. Додаткові операції агрегації
# ==============================================================================

print("\n" + "="*60 + "\n")
print("## ✨ Додаткова агрегація ##")

# Максимальна сума продажів у категорії
df_max_sales = df.groupby('category')['total_sales_uah'].max().reset_index()
df_max_sales.columns = ['Category', 'Max Total Sales (UAH)']

print("\n### 9. Максимальна сума продажів у кожній категорії ###")
print(df_max_sales)

# Кількість унікальних товарів
unique_products_count = df.index.nunique()

print("\n### 10. Кількість унікальних товарів (журналів) ###")
print(f"Кількість унікальних журналів: {unique_products_count}")