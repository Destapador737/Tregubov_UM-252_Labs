"""
​x+x⋅y если x=4 и y<2
y^2+1 если x<y
y^2+4 в остальных случаях
"""
​# ввод
x = float(input("Введите x: "))
y = float(input("Введите y: "))

# main
if x == 4 and y < 2:
    q = x + x * y
elif x < y:
    q = y**2 + 1
else:
    q = y**2 + 4

# вывод
print(f"x = {x}, y = {y}")
print(f"q = {q}")
