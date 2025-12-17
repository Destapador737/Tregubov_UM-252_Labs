"""1. Два простых числа называются «близнецами», если они отличаются друг от 
друга на 2 (например, 41 и 43). Напечатать все пары «близнецов» из отрезка [n, 
2n], где n — заданное натуральное число, большее 2."""
import math
print("=== ЗАДАНИЕ 1 ===")
print("Найти все пары 'близнецов' на отрезке [n, 2n]")

def is_prime(num):
    """Проверка, является ли число простым"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(n):
    """Нахождение пар простых чисел-близнецов на отрезке [n, 2n]"""
    twins = []
    for i in range(n, 2 * n - 1):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

# Ввод данных
n = int(input("Введите натуральное число n (>2): "))
if n <= 2:
    print("n должно быть больше 2")
else:
    twin_pairs = find_twin_primes(n)
    if twin_pairs:
        print(f"Пары 'близнецов' на отрезке [{n}, {2*n}]:")
        for a, b in twin_pairs:
            print(f"{a} и {b}")
    else:
        print(f"На отрезке [{n}, {2*n}] нет пар 'близнецов'")

print()
"""2. Даны две матрицы А и В. Написать программу, меняющую местами 
максимальные элементы этих матриц. Нахождение максимального элемента 
матрицы оформить в виде процедуры."""
print("=== ЗАДАНИЕ 2 ===")
print("Поменять местами максимальные элементы двух матриц")

def input_matrix(rows, cols):
    """Ввод матрицы заданного размера"""
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Элемент [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix, name):
    """Вывод матрицы на экран"""
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(' '.join(map(str, row)))

def find_max_element(matrix):
    """Нахождение максимального элемента и его позиции в матрице"""
    max_val = matrix[0][0]
    max_pos = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)
    return max_val, max_pos

def swap_max_elements(matrix_a, matrix_b):
    """Обмен максимальными элементами двух матриц"""
    max_a, pos_a = find_max_element(matrix_a)
    max_b, pos_b = find_max_element(matrix_b)
    
    # Меняем элементы местами
    matrix_a[pos_a[0]][pos_a[1]], matrix_b[pos_b[0]][pos_b[1]] = \
    matrix_b[pos_b[0]][pos_b[1]], matrix_a[pos_a[0]][pos_a[1]]
    
    return matrix_a, matrix_b

# Ввод размеров матриц
rows = int(input("Введите количество строк матриц: "))
cols = int(input("Введите количество столбцов матриц: "))

# Ввод матриц
print("\n--- Матрица A ---")
A = input_matrix(rows, cols)
print("\n--- Матрица B ---")
B = input_matrix(rows, cols)

# Вывод исходных матриц
print("\nИсходные матрицы:")
print_matrix(A, "A")
print_matrix(B, "B")

# Обмен максимальными элементами
A_new, B_new = swap_max_elements(A, B)

# Вывод результатов
print("\nМатрицы после обмена максимальными элементами:")
print_matrix(A_new, "A'")
print_matrix(B_new, "B'")

