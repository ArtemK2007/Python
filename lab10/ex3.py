import pandas as pd
import matplotlib.pyplot as plt
import json

file_path = 'magazines_data_lab9.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    print(f"Помилка: Файл {file_path} не знайдено.")
    exit()

labels = df['title']
sizes = df['circulation']

plt.figure(figsize=(10, 8))

colors = plt.cm.tab20.colors[:len(labels)]

plt.pie(sizes, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',      
        startangle=140,        
        shadow=True,           
        wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True}
       )

plt.title('Частка тиражу (Circulation) журналів', fontsize=16)

plt.axis('equal') 

plt.show()