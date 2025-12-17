#Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н».
#Преобразовать ее, заменив  точками все восклицательные знаки.
# Ввод 
s = input("Введите строку: ")

# 1 Подсчёт 
max_count = 0
current_count = 0

for char in s:
    if char == 'н':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(f"Самая длинная последовательность букв 'н': {max_count}")

# 2 Замена 
new_s = s.replace('!', '.')
print(f"Преобразованная строка: {new_s}")
