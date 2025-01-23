import requests
from bs4 import BeautifulSoup
url = "https://urban-university.ru/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')

    lists = soup.find_all(['ul', 'ol'])
    for lst in lists:
        items = lst.find_all('li')
        for item in items:
            print(item.text.strip())
else:
    print(f'Ошибка: {response.status_code}')



import pandas as pd

file_path = "data.csv"
df = pd.read_csv(file_path, delimiter=';')

print("Первые 5 строк данных:")
print(df.head())

print("Названия столбцов в DataFrame:")
print(df.columns)
df.columns = df.columns.str.strip()

print("\nСредняя зарплата по отделам:")
print(df.columns.tolist())
print(df.groupby('Department')['Salary'].mean())

print("\nСотрудники старше 30 лет:")
print(df[df['Age'] > 30])

print("\nОбщая сумма зарплат:")
print(df['Salary'].sum())

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
max_arr = np.max(arr)
min_arr = np.min(arr)
arr_mult = arr * 2
arr_div = arr / 2

print(f"Массив: {arr}")
print(f"Сумма элементов: {sum_arr}")
print(f"Среднее значение: {mean_arr}")
print(f"Максимальное значение: {max_arr}")
print(f"Минимальное значение: {min_arr}")
print(f"Массив, умноженный на 2: {arr_mult}")
print(f"Массив, деленный на 2: {arr_div}")

from PIL import Image, ImageEnhance

image = Image.open("example.jpg")

resized_image = image.resize((1100, 1000))
bw_image = resized_image.convert("L")
bw_image.save("bw_image.png")

enhancer = ImageEnhance.Contrast(bw_image)
enhanced_image = enhancer.enhance(2)

enhanced_image.save("enhanced_bw_image.png")

bw_image.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # Синус от x

plt.figure(figsize=(10, 6))  # Задаем размер фигуры
plt.plot(x, y, label='sin(x)', color='b', linewidth=2)  # Строим график
plt.title('Линейный график: sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

data = np.random.randn(1000)  # Генерируем случайные данные
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='g', edgecolor='black')  # Строим гистограмму
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x_scatter, y_scatter, color='r', alpha=0.6, edgecolors='b')  # Строим диаграмму рассеяния
plt.title('Диаграмма рассеяния')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()