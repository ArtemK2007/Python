import numpy as np
import matplotlib.pyplot as plt
def Y(x):
    denominator = np.power(x, x)
    return -5 * np.cos(10 * x) * np.sin(3 * x) / denominator

x_start = 0.01
x_end = 5
num_points = 500

x_values = np.linspace(x_start, x_end, num_points)

y_values = Y(x_values)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values, 
         linestyle='-',      
         color='blue',
         linewidth=2.5,
         label='$Y(x) = -5 \cdot \cos(10x) \cdot \sin(3x) / (x^x)$')


plt.title('Графік функції $Y(x)$', fontsize=16) 
plt.xlabel('Вісь X', fontsize=12)
plt.ylabel('Вісь Y', fontsize=12)

plt.legend(fontsize=10, loc='best') 
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()