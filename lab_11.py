# Аветисян Нарек Корюнович, ИУ7-12Б
# Программа для приближённого вычисления определённого интеграла методами левых прямоугольников и 3/8 с оценкой погрешностей и
# подбором числа разбиений для менее точного метода.

import is_number_check
def f(x):
    return x**2
def F(x):
    return x**3 / 3

def left_rectangles(a, b, n):
    h = (b - a) / n
    sm = 0
    x = a
    for i in range(n):
        sm += f(x)
        x += h
    return sm * h
def method_3_8(a, b, n):
    if n % 3 != 0:
        return None
    h = (b - a) / n
    sm = 0
    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            k = 1
        elif i % 3 == 0:
            k = 2
        else:
            k = 3
        sm += k * f(x)
    return (3 * h / 8) * sm

while True:
    a_str = input("Введите значение a (начало отрезка): ")
    if is_number_check.is_number(a_str):
        a = float(a_str)
        break
    print("Ошибка! Введено не числовое значение.")
while True:
    b_str = input("Введите значение b (конец отрезка): ")
    if not is_number_check.is_number(b_str):
        print("Ошибка! Введено не числовое значение.")
        continue
    b = float(b_str)
    if b > a:
        break
    print("Ошибка! Значение b должно быть больше a.")
while True:
    n1_str = input("Введите значение N1 (количество участков разбиения): ")
    if is_number_check.is_pos_integer(n1_str):
        n1 = int(n1_str)
        break
    print("Ошибка! Введите целое положительное число.")
while True:
    n2_str = input("Введите значение N2 (количество участков разбиения): ")
    if is_number_check.is_pos_integer(n2_str):
        n2 = int(n2_str)
        break
    print("Ошибка! Введите целое положительное число.")
while True:
    eps_str = input("Введите требуемую точность: ")
    if not is_number_check.is_number(eps_str):
        print("Ошибка! Введите числовое значение.")
        continue
    eps = float(eps_str)
    if eps > 0:
        break
    print("Ошибка! Точность должна быть положительным числом.")

I1 = left_rectangles(a, b, n1)
I2 = left_rectangles(a, b, n2)
I3 = method_3_8(a, b, n1)
I4 = method_3_8(a, b, n2)

def fv(value, width):
    if value is None:
        return f'{"-":^{width}}'
    return f'{value:^{width}.7g}'
w_meth = 17
w_n = 17
line = "+" + "-" * w_meth + "+" + "-" * w_n + "+" + "-" * w_n + "+"
print("\nТаблица приближённых значений интеграла:")
print(line)
print("|" + " " * w_meth + "|" + f'{"N1":^{w_n}}' + "|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' + "|" + fv(I1, w_n) + "|" + fv(I2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' + "|" + fv(I3, w_n) + "|" + fv(I4, w_n) + "|")
print(line)

I_real = F(b) - F(a)
print(f"\nТочное значение интеграла: {I_real:.7g}")

abs_err_1 = None if I1 is None else abs(I1 - I_real)
abs_err_2 = None if I2 is None else abs(I2 - I_real)
abs_err_3 = None if I3 is None else abs(I3 - I_real)
abs_err_4 = None if I4 is None else abs(I4 - I_real)

if I_real != 0:
    rel_err_1 = None if abs_err_1 is None else abs_err_1 / abs(I_real)
    rel_err_2 = None if abs_err_2 is None else abs_err_2 / abs(I_real)
    rel_err_3 = None if abs_err_3 is None else abs_err_3 / abs(I_real)
    rel_err_4 = None if abs_err_4 is None else abs_err_4 / abs(I_real)
else:
    rel_err_1 = rel_err_2 = rel_err_3 = rel_err_4 = None

print("\nТаблица абсолютных погрешностей:")
print(line)
print("|" + " " * w_meth + "|" + f'{"N1":^{w_n}}' + "|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' + "|" + fv(abs_err_1, w_n) + "|" + fv(abs_err_2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' + "|" + fv(abs_err_3, w_n) + "|" + fv(abs_err_4, w_n) + "|")
print(line)

print("\nТаблица относительных погрешностей:")
print(line)
print("|" + " " * w_meth + "|" + f'{"N1":^{w_n}}' + "|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' + "|" + fv(rel_err_1, w_n) + "|" + fv(rel_err_2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' + "|" + fv(rel_err_3, w_n) + "|" + fv(rel_err_4, w_n) + "|")
print(line)

methods = {1: {"name": "метод левых прямоугольников", "func": left_rectangles},2: {"name": "метод 3/8", "func": method_3_8},}

mas = [
    {"method": 1, "n": n1, "value": I1, "abs_err": abs_err_1},{"method": 1, "n": n2, "value": I2, "abs_err": abs_err_2},
    {"method": 2, "n": n1, "value": I3, "abs_err": abs_err_3},{"method": 2, "n": n2, "value": I4, "abs_err": abs_err_4},
]

best = None

for m in mas:
    if m["abs_err"] is not None:
        if best is None or m["abs_err"] < best["abs_err"]:
            best = m

if best is None:
    print("\nНе удалось вычислить погрешности ни для одного метода.")
else:
    best_method = best["method"]
    best_N = best["n"]
    best_abs_err = best["abs_err"]

    print(f"\nНаиболее точный метод: {methods[best_method]['name']}, N = {best_N}, абсолютная погрешность = {best_abs_err:.7g}")

    worst_method = 2 if best_method == 1 else 1

    print(f"\nУточнение для менее точного метода {methods[worst_method]['name']}:")
    start = None
    for m in mas:
        if m["method"] == worst_method and m["value"] is not None:
            if start is None or m["n"] < start["n"]:
                start = {"n": m["n"], "value": m["value"]}
    if worst_method == 2 and start is None:
        current_n = 3
        current_I = methods[worst_method]["func"](a, b, current_n)
    elif start is None:
        current_n = None
        current_I = None
    else:
        current_n = start["n"]
        current_I = start["value"]
    max_iterations = 30
    iterations = 0
    if current_I is None:
        print("Не удалось вычислить значение интеграла менее точным методом.")
    else:
        current_abs_err = abs(current_I - I_real)
        while current_abs_err > eps and iterations < max_iterations:
            next_n = current_n * 2
            next_I = methods[worst_method]["func"](a, b, next_n)
            current_n = next_n
            current_I = next_I
            iterations += 1
            current_abs_err = abs(current_I - I_real)

        if current_abs_err <= eps:
            print(f"Приближённое значение интеграла: {current_I:.7g}")
            print(f"Количество участков разбиения: {current_n}")
            print(f"Абсолютная погрешность: {abs(current_I - I_real):.7g}")
        else:
            print(f"Не удалось достичь заданной точности за {max_iterations} итераций.")




# Аветисян Нарек Корюнович, ИУ7-12Б
# Программа для приближённого вычисления определённого интеграла методами левых прямоугольников и 3/8 с оценкой погрешностей и
# подбором числа разбиений для менее точного метода.
import math

import is_number_check

def f(x):
    return x**2
def F(x):
    return x**3/3

def left_rectangles(a, b, n):
    h = (b - a) / n
    sm = 0
    x = a
    for i in range(n):
        sm += f(x)
        x += h
    return sm * h

def method_3_8(a, b, n):
    if n % 3 != 0:
        return None
    h = (b - a) / n
    sm = 0
    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            k = 1
        elif i % 3 == 0:
            k = 2
        else:
            k = 3
        sm += k * f(x)
    return (3 * h / 8) * sm

while True:
    a_str = input("Введите значение a (начало отрезка): ")
    if is_number_check.is_number(a_str):
        a = float(a_str)
        break
    print("Ошибка! Введено не числовое значение.")

while True:
    b_str = input("Введите значение b (конец отрезка): ")
    if not is_number_check.is_number(b_str):
        print("Ошибка! Введено не числовое значение.")
        continue
    b = float(b_str)
    if b > a:
        break
    print("Ошибка! Значение b должно быть больше a.")

while True:
    n1_str = input("Введите значение N1 (количество участков разбиения): ")
    if is_number_check.is_pos_integer(n1_str):
        n1 = int(n1_str)
        break
    print("Ошибка! Введите целое положительное число.")

while True:
    n2_str = input("Введите значение N2 (количество участков разбиения): ")
    if is_number_check.is_pos_integer(n2_str):
        n2 = int(n2_str)
        break
    print("Ошибка! Введите целое положительное число.")

while True:
    eps_str = input("Введите требуемую точность ε: ")
    if not is_number_check.is_number(eps_str):
        print("Ошибка! Введите числовое значение.")
        continue
    eps = float(eps_str)
    if eps > 0:
        break
    print("Ошибка! Точность должна быть положительным числом.")

I1 = left_rectangles(a, b, n1)
I2 = left_rectangles(a, b, n2)
I3 = method_3_8(a, b, n1)
I4 = method_3_8(a, b, n2)

def fv(value, width):
    if value is None:
        return f'{"-":^{width}}'
    return f'{value:^{width}.7g}'
w_meth = 17
w_n = 17
line = "+" + "-" * w_meth + "+" + "-" * w_n + "+" + "-" * w_n + "+"
print("\nТаблица приближённых значений интеграла:")
print(line)
print("|" + " " * w_meth +"|" + f'{"N1":^{w_n}}' +"|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' +"|" + fv(I1, w_n) +"|" + fv(I2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' +"|" + fv(I3, w_n) +"|" + fv(I4, w_n) + "|")
print(line)

I_real = F(b) - F(a)
print(f"\nТочное значение интеграла: {I_real:.7g}")

abs_err_1 = None if I1 is None else abs(I1 - I_real)
abs_err_2 = None if I2 is None else abs(I2 - I_real)
abs_err_3 = None if I3 is None else abs(I3 - I_real)
abs_err_4 = None if I4 is None else abs(I4 - I_real)

if I_real != 0:
    rel_err_1 = None if abs_err_1 is None else abs_err_1 / abs(I_real)
    rel_err_2 = None if abs_err_2 is None else abs_err_2 / abs(I_real)
    rel_err_3 = None if abs_err_3 is None else abs_err_3 / abs(I_real)
    rel_err_4 = None if abs_err_4 is None else abs_err_4 / abs(I_real)
else:
    rel_err_1 = rel_err_2 = rel_err_3 = rel_err_4 = None

print("\nТаблица абсолютных погрешностей:")
print(line)
print("|" + " " * w_meth +"|" + f'{"N1":^{w_n}}' +"|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' +"|" + fv(abs_err_1, w_n) +"|" + fv(abs_err_2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' +"|" + fv(abs_err_3, w_n) +"|" + fv(abs_err_4, w_n) + "|")
print(line)

print("\nТаблица относительных погрешностей:")
print(line)
print("|" + " " * w_meth +"|" + f'{"N1":^{w_n}}' +"|" + f'{"N2":^{w_n}}' + "|")
print(line)
print("|" + f'{"Метод 1":<{w_meth}}' +"|" + fv(rel_err_1, w_n) +"|" + fv(rel_err_2, w_n) + "|")
print(line)
print("|" + f'{"Метод 2":<{w_meth}}' +"|" + fv(rel_err_3, w_n) +"|" + fv(rel_err_4, w_n) + "|")
print(line)

# определяем наиболее точный метод
best_method = None
best_N = None
best_abs_err = None

# метод 1, N1
if abs_err_1 is not None:
    best_method = 1
    best_N = n1
    best_abs_err = abs_err_1

# метод 1, N2
if abs_err_2 is not None:
    if best_abs_err is None or abs_err_2 < best_abs_err:
        best_method = 1
        best_N = n2
        best_abs_err = abs_err_2

# метод 2, N1
if abs_err_3 is not None:
    if best_abs_err is None or abs_err_3 < best_abs_err:
        best_method = 2
        best_N = n1
        best_abs_err = abs_err_3

# метод 2, N2
if abs_err_4 is not None:
    if best_abs_err is None or abs_err_4 < best_abs_err:
        best_method = 2
        best_N = n2
        best_abs_err = abs_err_4

if best_method is None:
    print("\nНе удалось вычислить погрешности ни для одного метода.")
else:
    if best_method == 1:
        best_method_name = "метод левых прямоугольников"
    else:
        best_method_name = "метод 3/8"
    print(f"\nНаиболее точный метод: {best_method_name}, N = {best_N}, абсолютная погрешность = {best_abs_err:.7g}")

    # Менее точный метод т.е противоположный
    worst_method = 2 if best_method == 1 else 1
    if worst_method == 1:
        worst_method_name = "метод левых прямоугольников"
    else:
        worst_method_name = "метод 3/8"

    # Уточнение для менее точного метода (шаг уменьшаем в 2 раза)

    # Стартовое N и значение для менее точного метода
    if worst_method == 1:
        # для левых прямоугольников значения всегда есть
        if n1 <= n2:
            current_n = n1
            current_I = I1
        else:
            current_n = n2
            current_I = I2
    else:
        # метод 3/8: ищем минимальное доступное N из N1, N2
        current_n = None
        current_I = None
        if I3 is not None:
            current_n = n1
            current_I = I3
        if I4 is not None:
            if current_n is None or n2 < current_n:
                current_n = n2
                current_I = I4
        # Если ни N1, ни N2 не подходят (оба не делятся на 3),
        # начинаем с N = 3
        if current_n is None:
            current_n = 3
            current_I = method_3_8(a, b, current_n)

    print(f"\nУточнение для менее точного метода {worst_method_name}:")

    max_iterations = 30 # максимальное количество шагов уточнения
    iterations = 0 # счетчик сделанных итераций
    is_reached = False

    # Если нет начального значения то не уточняем
    if current_I is None:
        print("Не удалось вычислить значение интеграла менее точным методом.")
    else:
        while True:
            current_abs_err = abs(current_I - I_real)
            if current_abs_err <= eps:
                is_reached = True
                break

            if iterations >= max_iterations:
                break

            next_n = current_n * 2
            if worst_method == 1:
                next_I = left_rectangles(a, b, next_n)
            else:
                next_I = method_3_8(a, b, next_n)

            current_n = next_n
            current_I = next_I
            iterations += 1

        if is_reached:
            print(f"Приближённое значение интеграла: {current_I:.7g}")
            print(f"Количество участков разбиения: {current_n}")
            print(f"Абсолютная погрешность: {(abs(current_I - I_real)):.7g}")
        else:
            print(f"Не удалось достичь заданной точности за {max_iterations} итераций.")
