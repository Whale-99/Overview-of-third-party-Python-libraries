import requests

# 1. Выполняем GET-запрос
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# 2. Проверяем статус ответа
if response.status_code == 200:
    # 3. Выводим данные в JSON формате
    data = response.json()
    print("Пример полученных данных:", data[:2])  # Выводим первые два элемента для примера
else:
    print("Ошибка при получении данных:", response.status_code)

print()
print()

import numpy as np

# 1. Создание массива
arr = np.array([1, 2, 3, 4, 5])

# 2. Операции с массивом
arr_squared = arr ** 2
print("Квадраты элементов массива:", arr_squared)

# 3. Среднее значение
mean_value = np.mean(arr)
print("Среднее значение массива:", mean_value)

# 4. Генерация случайных чисел
random_array = np.random.rand(3, 3)
print("Случайный массив 3x3:\n", random_array)

print()
print()

import matplotlib.pyplot as plt
import numpy as np

# 1. Создаём массив данных для осей X и Y
x = np.linspace(0, 10, 100)  # Массив из 100 чисел от 0 до 10
y = np.sin(x)                # Функция синуса от x

# 2. Строим линейный график
plt.plot(x, y, label="sin(x)", color="blue")
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.title("График функции sin(x)")

# 3. Добавляем сетку и легенду
plt.grid(True)
plt.legend()

# 4. Показываем график
plt.show()
