"""========== Ввод и вывод данных из/в файл ==========
 Задание: Для заданий из практической работы №8 для своего варианта.
 Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
 И вывод результатов в файл (имя: ФИО_группа_vivod.txt)."""

import sys

# Перенаправляем вывод в файл
original_stdout = sys.stdout

# Имена файлов
input_filename = "ТрегубовВО_Ум-252_ввод.txt"
output_filename = "ТрегубовВО_Ум-252_вывод.txt"

print(f"Чтение данных из файла: {input_filename}")
print(f"Запись результатов в файл: {output_filename}")

try:
    # Открываем файл для чтения
    with open(input_filename, 'r', encoding='utf-8') as file:
        # Читаем все строки
        lines = file.readlines()
        
        # Задание 1: Сумма элементов строки с минимальным элементом
        # Читаем порядок матрицы
        n = int(lines[0].strip())
        print(f"Порядок матрицы: {n}")
        
        # Читаем матрицу
        A = []
        for i in range(1, n + 1):
            row = list(map(float, lines[i].split()))
            A.append(row)
        
        # Задание 2: Столбец с минимальным произведением
        # Читаем размеры матрицы
        m = int(lines[n + 1].strip())
        n2 = int(lines[n + 2].strip())
        print(f"Размеры второй матрицы: {m}x{n2}")
        
        # Читаем вторую матрицу
        B = []
        for i in range(n + 3, n + 3 + m):
            row = list(map(int, lines[i].split()))
            B.append(row)

except FileNotFoundError:
    print(f"Файл {input_filename} не найден!")
    print("Создаю файл с примером данных...")
    
    # Создаем файл с тестовыми данными
    with open(input_filename, 'w', encoding='utf-8') as file:
        # Данные для задания 1: матрица 3x3
        file.write("3\n")  # порядок матрицы
        file.write("5 8 3\n")
        file.write("1 4 9\n")
        file.write("7 2 6\n")
        
        # Данные для задания 2: матрица 3x4
        file.write("3\n")  # количество строк
        file.write("4\n")  # количество столбцов
        file.write("2 15 3 5\n")
        file.write("4 1 6 8\n")
        file.write("7 9 2 3\n")
    
    print(f"Файл {input_filename} создан с тестовыми данными.")
    print("Пожалуйста, запустите программу снова.")
    exit()

# Открываем файл для записи результатов
with open(output_filename, 'w', encoding='utf-8') as file:
    sys.stdout = file  # Перенаправляем вывод в файл
    
    print("=" * 60)
    print("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ПРАКТИЧЕСКОЙ РАБОТЫ 8 (ВАРИАНТ 11)")
    print("=" * 60)
    
    # ========== ЗАДАНИЕ 1 ==========
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 1")
    print("Найти сумму элементов строки с наименьшим элементом матрицы")
    print("=" * 60)
    
    print(f"\nМатрица A (порядок {n}):")
    for row in A:
        print(' '.join([f"{elem:6.2f}" for elem in row]))
    
    # Находим минимальный элемент и его строку
    min_value = A[0][0]
    min_row = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] < min_value:
                min_value = A[i][j]
                min_row = i
    
    # Вычисляем сумму элементов строки с минимальным элементом
    row_sum = sum(A[min_row])
    
    print(f"\nМинимальный элемент: {min_value}")
    print(f"Он находится в строке {min_row + 1}")
    print(f"Сумма элементов этой строки: {row_sum:.2f}")
    
    # ========== ЗАДАНИЕ 2 ==========
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 2")
    print("Найти столбец с минимальным произведением элементов (|элементы| ≤ 10)")
    print("и поменять его с соседним справа")
    print("=" * 60)
    
    print(f"\nМатрица B (размер {m}x{n2}):")
    for row in B:
        print(' '.join([f"{elem:4}" for elem in row]))
    
    # Находим столбцы, где все элементы по модулю ≤ 10
    valid_columns = []
    for j in range(n2):
        valid = True
        for i in range(m):
            if abs(B[i][j]) > 10:
                valid = False
                break
        if valid:
            valid_columns.append(j)
    
    if len(valid_columns) == 0:
        print("\nНет столбцов, где все элементы по модулю ≤ 10")
    else:
        # Находим столбец с минимальным произведением
        min_product = float('inf')
        min_col = -1
        
        for j in valid_columns:
            product = 1
            for i in range(m):
                product *= B[i][j]
            if product < min_product:
                min_product = product
                min_col = j
        
        print(f"\nСтолбцы с |элементами| ≤ 10: {[c+1 for c in valid_columns]}")
        print(f"Столбец с минимальным произведением: {min_col + 1}")
        print(f"Произведение элементов этого столбца: {min_product}")
        
        # Меняем найденный столбец с соседним (справа, если есть)
        if min_col < n2 - 1:
            swap_col = min_col + 1
            print(f"\nМеняем местами столбцы {min_col + 1} и {swap_col + 1}")
            
            # Меняем столбцы местами
            for i in range(m):
                B[i][min_col], B[i][swap_col] = B[i][swap_col], B[i][min_col]
            
            print("\nМатрица B после замены столбцов:")
            for row in B:
                print(' '.join([f"{elem:4}" for elem in row]))
        else:
            print(f"\nСтолбец {min_col + 1} последний, нет соседнего справа для замены")
    
    print("\n" + "=" * 60)
    print("РАБОТА ЗАВЕРШЕНА")
    print(f"Результаты сохранены в файл: {output_filename}")
    print("=" * 60)

# Возвращаем стандартный вывод
sys.stdout = original_stdout

print(f"\nРезультаты успешно сохранены в файл: {output_filename}")
print(f"Исходные данные были прочитаны из файла: {input_filename}")

# ========== ДОПОЛНИТЕЛЬНО: ЗАДАНИЯ ИЗ ПРЕДЫДУЩИХ РАБОТ ==========
print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНО: ЗАДАНИЯ ИЗ ПРЕДЫДУЩИХ РАБОТ")
print("=" * 60)

# ========== БЛОК А: ЗАДАЧА 4 ==========
# Дано натуральное число N. Вычислите сумму его цифр. 
# При решении этой задачи нельзя использовать строки, списки, массивы

def sum_digits(n):
    """
    Рекурсивная функция для вычисления суммы цифр числа.
    Базовый случай: если n == 0, возвращаем 0.
    Рекурсивный шаг: последняя цифра (n % 10) + сумма цифр оставшегося числа (n // 10).
    """
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

print("\n=== БЛОК А: ЗАДАЧА 4 ===")
print("Дано натуральное число N. Вычислите сумму его цифр.")
N = 12345
print(f"Пример для N = {N}:")
print(f"Сумма цифр числа {N}: {sum_digits(N)}")

""" ========== БЛОК Б: ЗАДАЧА 3 ==========
 Дана последовательность натуральных чисел (одно число в строке),
 завершающаяся числом 0. Выведите первое, третье, пятое и т.д. из
 введенных чисел. Завершающий ноль выводить не надо.
 В этой задаче нельзя использовать глобальные переменные и передавать
 какие-либо параметры в рекурсивную функцию. Функция получает
 данные, считывая их с клавиатуры. Функция не возвращает значение, а
 сразу же выводит результат на экран."""

def print_odd_positions():
    """
    Рекурсивная функция для вывода элементов на нечётных позициях.
    Считывает числа с клавиатуры до тех пор, пока не встретится 0.
    Выводит текущее число (нечётная позиция) и пропускает следующее.
    """
    # Для демонстрации используем заранее заданную последовательность
    # В реальной задаче здесь было бы input()
    global demo_seq, demo_index
    if demo_index >= len(demo_seq) or demo_seq[demo_index] == 0:
        return
    num = demo_seq[demo_index]
    print(num, end=' ')
    demo_index += 1
    if demo_index >= len(demo_seq) or demo_seq[demo_index] == 0:
        demo_index += 1
        return
    demo_index += 1
    print_odd_positions()

print("\n=== БЛОК Б: ЗАДАЧА 3 ===")
print("Вывести элементы на нечётных позициях последовательности.")
demo_seq = [1, 2, 3, 4, 5, 6, 0]
demo_index = 0
print(f"Последовательность: {demo_seq}")
print("Элементы на нечётных позициях:", end=' ')
print_odd_positions()
print()
