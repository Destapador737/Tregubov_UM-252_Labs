"""
Лабораторная работа №1
Вариант 1: Вычислить сумму двух произвольных действительных чисел
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Фиксируем random seed для воспроизводимости результатов
np.random.seed(42)

print("=" * 60)
print("Лабораторная работа №1")
print("Задача: обучить нейросеть вычислять сумму двух чисел")
print("=" * 60)

# ========== 1. Генерация обучающей выборки ==========
# Создаем 500 случайных пар чисел от -100 до 100
n_samples = 500
x1 = np.random.uniform(-100, 100, n_samples)
x2 = np.random.uniform(-100, 100, n_samples)

# Формируем входные данные (матрица 500x2)
X_train = np.column_stack((x1, x2))

# Формируем целевые значения (сумма)
y_train = x1 + x2

print(f"\nОбучающая выборка: {n_samples} примеров")
print(f"Вход: два числа (x1, x2)")
print(f"Выход: сумма (x1 + x2)")

# ========== 2. Создание модели нейросети ==========
# Sequential - последовательная модель (слои идут друг за другом)
model = Sequential()

# Добавляем полносвязный слой:
# - units=1: один выходной нейрон
# - input_shape=(2,): на вход подается 2 числа
# - activation='linear': линейная функция активации (для регрессии)
model.add(Dense(units=1, input_shape=(2,), activation='linear'))

print("\nАрхитектура сети:")
print("  - Входной слой: 2 нейрона (x1, x2)")
print("  - Выходной слой: 1 нейрон (линейная активация)")
print("  - Всего обучаемых параметров: 3 (2 веса + 1 смещение)")

# ========== 3. Компиляция модели ==========
# loss='mean_squared_error' - среднеквадратичная ошибка (подходит для регрессии)
# optimizer=Adam(learning_rate=0.01) - Adam оптимизатор с шагом 0.01
model.compile(loss='mean_squared_error', 
              optimizer=Adam(learning_rate=0.01))

print("\nПараметры обучения:")
print("  - Функция потерь: MSE (mean_squared_error)")
print("  - Оптимизатор: Adam")
print("  - Скорость обучения: 0.01")

# ========== 4. Обучение сети ==========
print("\nНачало обучения...")
print("-" * 60)

history = model.fit(X_train, y_train, 
                    epochs=500,      # 500 эпох обучения
                    verbose=1)       # показываем прогресс

print("-" * 60)
print("Обучение завершено!")

# ========== 5. Визуализация процесса обучения ==========
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], linewidth=2)
plt.title('График функции потерь (MSE) при обучении', fontsize=14)
plt.xlabel('Эпоха', fontsize=12)
plt.ylabel('Среднеквадратичная ошибка', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('loss_plot_lab1.png', dpi=150)
plt.show()

print("\nГрафик сохранен как 'loss_plot_lab1.png'")

# ========== 6. Анализ обученных весов ==========
weights = model.get_weights()
print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ ОБУЧЕНИЯ")
print("=" * 60)

print("\nНайденные веса сети:")
print(f"  - Вес для x1 (w1): {weights[0][0][0]:.8f}")
print(f"  - Вес для x2 (w2): {weights[0][1][0]:.8f}")
print(f"  - Смещение (bias): {weights[1][0]:.8f}")

print("\nИдеальные значения (по формуле суммы):")
print(f"  - w1 = 1.0")
print(f"  - w2 = 1.0")
print(f"  - bias = 0.0")

# Вычисляем погрешность
w1_error = abs(weights[0][0][0] - 1.0)
w2_error = abs(weights[0][1][0] - 1.0)
bias_error = abs(weights[1][0] - 0.0)

print("\nПогрешность найденных весов:")
print(f"  - Ошибка w1: {w1_error:.8f}")
print(f"  - Ошибка w2: {w2_error:.8f}")
print(f"  - Ошибка bias: {bias_error:.8f}")

# ========== 7. Тестирование на новых примерах ==========
print("\n" + "=" * 60)
print("ТЕСТИРОВАНИЕ НА НОВЫХ ПРИМЕРАХ")
print("=" * 60)

# Тестовые примеры (которые не участвовали в обучении)
test_pairs = [
    (10, 5),
    (-10, 7),
    (3.5, 2.5),
    (-20, -30),
    (0, 100),
    (15.8, -5.3),
    (100, 200),
    (-50, 50)
]

print("\n  x1     x2    |  Предсказание  |  Ожидание  |  Ошибка")
print("-" * 65)

for x1_test, x2_test in test_pairs:
    # Предсказание сети
    prediction = model.predict(np.array([[x1_test, x2_test]]), verbose=0)[0][0]
    true_value = x1_test + x2_test
    error = abs(prediction - true_value)
    print(f"{x1_test:6.1f}  {x2_test:6.1f}   |   {prediction:9.4f}     |   {true_value:7.1f}   |   {error:.6f}")

# ========== 8. Сохранение модели ==========
model.save('lab1_sum_model.h5')
print("\nМодель сохранена в файл 'lab1_sum_model.h5'")

# ========== 9. Итоговый вывод ==========
print("\n" + "=" * 60)
print("ВЫВОД")
print("=" * 60)
print("Нейросеть успешно обучилась вычислять сумму двух чисел!")
print("Найденные веса (w1, w2, bias) близки к идеальным (1, 1, 0).")
print("Ошибка на тестовых примерах стремится к нулю.")
