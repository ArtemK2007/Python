import pandas as pd
import matplotlib.pyplot as plt

# 1. Завантаження та базова перевірка
df_wide = pd.read_csv('comptage_velo_2018.csv')
print(df_wide.head())
print(df_wide.info())
print(df_wide.describe())

df_wide['Date'] = pd.to_datetime(df_wide['Date'], errors='coerce')
df_wide['Month'] = df_wide['Date'].dt.month

# 2. Melt у long-формат
sensor_cols = df_wide.columns[2:]
df_long = df_wide.melt(
    id_vars=['Date', 'Month'],
    value_vars=sensor_cols,
    var_name='id_compteur',
    value_name='nb_passages'
)
df_long['nb_passages'] = df_long['nb_passages'].fillna(0).astype(int)

# 3. Аналіз
print("\nЗагальна кількість велосипедистів:", df_long['nb_passages'].sum())

cyclists_per_path = df_long.groupby('id_compteur')['nb_passages'].sum().sort_values(ascending=False)
print("\nПо кожній доріжці:")
print(cyclists_per_path)

selected_paths = cyclists_per_path.head(3).index.tolist()
monthly_traffic = df_long[df_long['id_compteur'].isin(selected_paths)]\
    .groupby(['id_compteur','Month'])['nb_passages'].sum()
most_popular_month = monthly_traffic.groupby(level=0).idxmax()

month_names = {
    1:'Січень',2:'Лютий',3:'Березень',4:'Квітень',5:'Травень',6:'Червень',
    7:'Липень',8:'Серпень',9:'Вересень',10:'Жовтень',11:'Листопад',12:'Грудень'
}

print("\nНайпопулярніші місяці:")
for sensor, month in most_popular_month.items():
    print(sensor, "—", month_names[month[1]])

# 4. Графік
plot_id = selected_paths[0]
plot_data = monthly_traffic.loc[plot_id].reset_index()
plot_data['Month Name'] = plot_data['Month'].map(month_names)

plt.figure(figsize=(10,5))
plt.plot(plot_data['Month Name'], plot_data['nb_passages'], marker='o')
plt.title(f'Місячна завантаженість "{plot_id}"')
plt.xlabel('Місяць')
plt.ylabel('Кількість')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_traffic_plot_2018.png')

print("\nГрафік збережено як monthly_traffic_plot_2018.png")
