"""1. В данной действительной квадратной матрице порядка п найти сумму 
элементов строки, в которой расположен элемент с наименьшим 
значением. Предполагается, что такой элемент единственный."""
print("=== ЗАДАНИЕ 1 ===")
print("Найти сумму элементов строки с наименьшим элементом матрицы")

def input_matrix(n):
    """Ввод квадратной матрицы порядка n"""
    matrix = []
    print(f"Введите элементы матрицы {n}x{n}:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f"Элемент [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Вывод матрицы на экран"""
    for row in matrix:
        print(' '.join([f"{elem:6.2f}" for elem in row]))

# Ввод порядка матрицы
n = int(input("Введите порядок матрицы n: "))
A = input_matrix(n)

print("\nИсходная матрица:")
print_matrix(A)

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

print("\n" + "="*50 + "\n")
"""2. Среди столбцов заданной целочисленной матрицы, содержащих 
только такие элементы, которые по модулю не больше 10, найти столбец 
с минимальным произведением элементов и поменять местами с 
соседним."""
print("=== ЗАДАНИЕ 2 ===")
print("Найти столбец с минимальным произведением элементов (|элементы| ≤ 10) и поменять его с соседним")

def input_int_matrix(m, n):
    """Ввод целочисленной матрицы размером m x n"""
    matrix = []
    print(f"Введите элементы целочисленной матрицы {m}x{n}:")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def print_int_matrix(matrix):
    """Вывод целочисленной матрицы"""
    for row in matrix:
        print(' '.join([f"{elem:4}" for elem in row]))

# Ввод размеров матрицы
m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))
B = input_int_matrix(m, n)

print("\nИсходная матрица:")
print_int_matrix(B)

# Находим столбцы, где все элементы по модулю ≤ 10
valid_columns = []
for j in range(n):
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
    if min_col < n - 1:
        swap_col = min_col + 1
        print(f"Меняем местами столбцы {min_col + 1} и {swap_col + 1}")
        
        # Меняем столбцы местами
        for i in range(m):
            B[i][min_col], B[i][swap_col] = B[i][swap_col], B[i][min_col]
        
        print("\nМатрица после замены столбцов:")
        print_int_matrix(B)
    else:
        print(f"Столбец {min_col + 1} последний, нет соседнего справа для замены")
