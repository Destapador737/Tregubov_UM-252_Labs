#y**(math.sqrt(abs(x))) + (math.cos(y)**3) * (abs(x - y) * (1 + (math.sin(z)**2) / math.sqrt(x + y))) / (math.exp(abs(x - y)) + x / 2)
import math

#const
x = 6.251
y = 0.827
z = 25.001

# 1 первое слагаемое y^sqrt3|x|
term1 = y ** (abs(x) ** (1/3))

# 2.1 числитель |x-y|
abs_xy = abs(x - y)

# 2.2 числитель в скобках sinz^2
sin2_z = (math.sin(z)) ** 2

# 2.3 знаменатель сверху sqrt(x + y)
sqrt_xy = math.sqrt(x + y)

# 2.4 Скобки в числителе (1 + sin^2(z)/sqrt(x+y)
num_vn = 1 + sin2_z / sqrt_xy

# 2.6 числитель полностью |x - y| * (1 + sin^2(z)/sqrt(x+y))
num = abs_xy * num_vn

# 2.7 Знаменатель e^|x - y| + x/2
den = math.exp(abs_xy) + x / 2

# 2.8 Вся дробь:
fraction = num / den

# 2.9 cos^3(y)
cos3_y = (math.cos(y)) ** 3

# 2.9. Второе слагаемое целиком:
term2 = cos3_y * fraction

# Итоговое значение s
s = term1 + term2

# Вывод результата
print("x =", x)
print("y =", y)
print("z =", z)
print("s =", s)
print("s = {:.6f}".format(s)) #с точностью до 6 знаков
