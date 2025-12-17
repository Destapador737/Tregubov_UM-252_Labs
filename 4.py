#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B 
#включительно.
A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A <= B:
    for i in range(A, B + 1):
        print(i, end=' ')
else:
    print("Ошибка: A должно быть ≤ B")
