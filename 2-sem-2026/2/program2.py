"""
Практическая работа №2 - Классификация цифр MNIST
Файлы MNIST лежат в той же папке, что и программа
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
import gzip
import os

# ========== 1. Загрузка MNIST из файлов в той же папке ==========
def load_mnist_from_folder():
    """Загрузка MNIST из .gz файлов в текущей папке"""
    
    # Текущая папка, где лежит программа
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    files = {
        'x_train': 'train-images-idx3-ubyte.gz',
        'y_train': 'train-labels-idx1-ubyte.gz',
        'x_test': 't10k-images-idx3-ubyte.gz',
        'y_test': 't10k-labels-idx1-ubyte.gz'
    }
    
    def load_images(filename):
        filepath = os.path.join(current_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл не найден: {filepath}")
        print(f"  Загружаю: {filename}")
        with gzip.open(filepath, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
        return data.reshape(-1, 28, 28)
    
    def load_labels(filename):
        filepath = os.path.join(current_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл не найден: filepath")
        with gzip.open(filepath, 'rb') as f:
            return np.frombuffer(f.read(), np.uint8, offset=8)
    
    print("Загрузка MNIST из локальных файлов...")
    print(f"Папка: {current_dir}")
    
    x_train = load_images(files['x_train'])
    y_train = load_labels(files['y_train'])
    x_test = load_images(files['x_test'])
    y_test = load_labels(files['y_test'])
    
    print(f"Обучающая выборка: {x_train.shape}")
    print(f"Тестовая выборка: {x_test.shape}")
    
    return (x_train, y_train), (x_test, y_test)

# ========== 2. Загрузка данных ==========
print("=" * 70)
print("Практическая работа №2 - Классификация цифр MNIST")
print("=" * 70)

try:
    (x_train, y_train), (x_test, y_test) = load_mnist_from_folder()
except FileNotFoundError as e:
    print(f"\n❌ ОШИБКА: {e}")
    print("\nРешение: положи 4 файла MNIST в папку с программой:")
    print("  - train-images-idx3-ubyte.gz")
    print("  - train-labels-idx1-ubyte.gz")
    print("  - t10k-images-idx3-ubyte.gz")
    print("  - t10k-labels-idx1-ubyte.gz")
    exit(1)

# ========== 3. Предобработка ==========
print("\nПредобработка данных...")

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

print(f"Нормализация: диапазон [0, {x_train.max()}]")

# ========== 4. Создание модели ==========
model = Sequential([
    Flatten(input_shape=(28, 28), name='input_flatten'),
    Dense(64, activation='relu', name='hidden_1'),
    Dense(32, activation='relu', name='hidden_2'),
    Dense(10, activation='softmax', name='output')
])

print("\n" + "=" * 70)
print("СТРУКТУРА НЕЙРОННОЙ СЕТИ (Вариант 1)")
print("=" * 70)
model.summary()

# Пояснение количества весов
print("\n" + "=" * 70)
print("ПОЯСНЕНИЕ КОЛИЧЕСТВА ВЕСОВ")
print("=" * 70)
print("""
Слой Flatten:
- Преобразует 28x28 → 784 пикселя
- Обучаемых параметров: 0

Слой Dense (64 нейрона):
- Веса: 784 × 64 = 50176
- Смещения: 64
- Итого: 50240

Слой Dense (32 нейрона):
- Веса: 64 × 32 = 2048
- Смещения: 32
- Итого: 2080

Слой Dense (10 нейронов, выход):
- Веса: 32 × 10 = 320
- Смещения: 10
- Итого: 330

ВСЕГО: 50240 + 2080 + 330 = 52650 параметров
""")

# ========== 5. Компиляция и обучение ==========
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("\n" + "=" * 70)
print("ОБУЧЕНИЕ МОДЕЛИ")
print("=" * 70)

history = model.fit(x_train, y_train_cat,
                    epochs=15,
                    batch_size=128,
                    validation_split=0.1,
                    verbose=1)

# ========== 6. Оценка качества ==========
print("\n" + "=" * 70)
print("РЕЗУЛЬТАТЫ")
print("=" * 70)

test_loss, test_accuracy = model.evaluate(x_test, y_test_cat, verbose=0)
print(f"Точность на тестовой выборке: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

if test_accuracy >= 0.97:
    print("\n✅ ЦЕЛЬ ДОСТИГНУТА! Точность >= 97%")
else:
    print(f"\n⚠️ Точность {test_accuracy*100:.2f}% ниже 97%")

# ========== 7. Графики ==========
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Обучающая', linewidth=2)
plt.plot(history.history['val_accuracy'], label='Валидационная', linewidth=2)
plt.title('Точность модели')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Обучающая', linewidth=2)
plt.plot(history.history['val_loss'], label='Валидационная', linewidth=2)
plt.title('Функция потерь')
plt.xlabel('Эпоха')
plt.ylabel('Loss')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('mnist_training_history.png', dpi=150)
plt.show()

# ========== 8. Демонстрация ==========
indices = np.random.choice(len(x_test), 10, replace=False)

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
axes = axes.flatten()

for idx, ax in enumerate(axes):
    i = indices[idx]
    pred = model.predict(x_test[i:i+1], verbose=0)
    pred_class = np.argmax(pred)
    true_class = y_test[i]
    
    ax.imshow(x_test[i], cmap='gray')
    ax.set_title(f'Пред: {pred_class} | Истина: {true_class}',
                 color='green' if pred_class == true_class else 'red')
    ax.axis('off')

plt.tight_layout()
plt.savefig('mnist_predictions.png', dpi=150)
plt.show()

model.save('mnist_classifier.h5')
print("\nМодель сохранена в 'mnist_classifier.h5'")
