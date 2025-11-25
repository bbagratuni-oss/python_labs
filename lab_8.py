from is_number_check import is_number
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while n <= 0:
    print('Количество строк не может быть меньше или равно нулю!')
    n = int(input('Введите количество строк матрицы: '))

while m <= 0:
    print('Количество столбцов не может быть меньше или равно нулю!')
    m = int(input('Введите количество столбцов матрицы: '))

A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица:')

max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * len(A[0]) + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

# Находим максимальное среднее арифметическое
sr_ar = None
for rows in A:
    cur_sr_ar = sum(rows) / len(rows)
    if sr_ar is None or cur_sr_ar > sr_ar:
        sr_ar = cur_sr_ar

# Выводим все строки, у которых среднее совпадает с максимальным
print(f"\nНаибольшее среднее арифметическое: {sr_ar:.6g}")
print("Строка с наибольшим средним арифметическим:")

for rows in A:
    if abs(sum(rows)/len(rows) - sr_ar) < 1e-9:
        print(rows)
        break



from is_number_check import is_number
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while n <= 0:
    print('Количество строк не может быть меньше или равно нулю!')
    n = int(input('Введите количество строк матрицы: '))

while m <= 0:
    print('Количество столбцов не может быть меньше или равно нулю!')
    m = int(input('Введите количество столбцов матрицы: '))

A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица:')

max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * len(A[0]) + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

# Находим максимальное среднее арифметическое
sr_ar = None
for rows in A:
    cur_sr_ar = sum(rows) / len(rows)
    if sr_ar is None or cur_sr_ar > sr_ar:
        sr_ar = cur_sr_ar

# Выводим все строки, у которых среднее совпадает с максимальным
print(f"\nНаибольшее среднее арифметическое: {sr_ar:.6g}")
print("Строка с наибольшим средним арифметическим:")

for rows in A:
    if abs(sum(rows)/len(rows) - sr_ar) < 1e-9:
        print(rows)
        break










from is_number_check import is_number
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while n <= 0:
    print('Количество строк не может быть меньше или равно нулю!')
    n = int(input('Введите количество строк матрицы: '))

while m <= 0:
    print('Количество столбцов не может быть меньше или равно нулю!')
    m = int(input('Введите количество столбцов матрицы: '))

A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):  # используем твою проверку
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break

print('\nВведённая матрица:')

max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * m + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

max_k = min_k = None
max_row = min_row = 0

for i, row in enumerate(A):
    k = 0
    for v in row:
        if v < 0:
            k += 1

    if max_k is None or k > max_k:
        max_k = k
        max_row = i
    if min_k is None or k < min_k:
        min_k = k
        min_row = i

# если отрицательных нигде нет
if max_k == 0:
    print("\nВ матрице нет отрицательных элементов, обмен строк не требуется.")
else:
    A[max_row], A[min_row] = A[min_row], A[max_row]
    print("\nМатрица после обмена строк:")
    print(line)
    for row in A:
        print('|', end='')
        for x in row:
            print(f" {x:^{max_width+1}.6g} |", end='')
        print()
        print(line)









from is_number_check import is_number
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while n <= 0:
    print('Количество строк не может быть меньше или равно нулю!')
    n = int(input('Введите количество строк матрицы: '))

while m <= 0:
    print('Количество столбцов не может быть меньше или равно нулю!')
    m = int(input('Введите количество столбцов матрицы: '))

A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица')

max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * m + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

# Первый столбец с наибольшим количеством простых чисел
max_primes = -1
best_col = None

for j in range(m):
    cnt = 0
    for i in range(n):
        x = A[i][j]
        ix = int(x)

        # число целое, если x == int(x), и больше 1
        if x == ix and ix > 1:
            # проверка на простоту
            prime = True
            for d in range(2, int(ix ** 0.5) + 1):
                if ix % d == 0:
                    prime = False
                    break
            if prime:
                cnt += 1

    if cnt > max_primes:  # берём первый столбец при равенстве
        max_primes = cnt
        best_col = j

if max_primes == 0:
    print("\nВ матрице нет простых чисел.")
else:
    print(f"\nСтолбец с наибольшим количеством простых чисел: {best_col + 1}")
    print("Элементы столбца:")
    for i in range(n):
        print(A[i][best_col])
    print(f"\nКоличество простых чисел в нём: {max_primes}")






from is_number_check import is_number
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

while n <= 0:
    print('Количество строк не может быть меньше или равно нулю!')
    n = int(input('Введите количество строк матрицы: '))

while m <= 0:
    print('Количество столбцов не может быть меньше или равно нулю!')
    m = int(input('Введите количество столбцов матрицы: '))

A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица')

max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * m + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

max_sum = -float('inf')
min_sum = float('inf')
max_col = min_col = 0

for j in range(m):
    s = sum(A[i][j] for i in range(n))  # сумма элементов j-го столбца

    if s > max_sum:
        max_sum = s
        max_col = j
    if s < min_sum:
        min_sum = s
        min_col = j

# Меняем столбцы местами
for i in range(n):
    A[i][max_col], A[i][min_col] = A[i][min_col], A[i][max_col]

# Вывод результата
print(f"\nСтолбцы с наибольшей и наименьшей суммой элементов: {max_col + 1} и {min_col + 1}")
print("\nМатрица после обмена столбцов:")

print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)






from is_number_check import is_number
n = int(input('Введите размер квадратной матрицы: '))
while n <= 0:
    print('Размер не может быть меньше или равен нулю!')
    n = int(input('Введите размер квадратной матрицы: '))
m = n
A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица')

# Находим максимальную ширину среди всех чисел
max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * m + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

N = n  # размер
# Макс над главной диагональю (i < j)
max_above = None
pos_max = None
for i in range(N):
    for j in range(i + 1, N):  # только над диагональю
        x = A[i][j]
        if (max_above is None) or (x > max_above):
            max_above = x
            pos_max = (i, j)

# Мин под побочной диагональю (i + j > N - 1)
min_below_sec = None
pos_min = None
for i in range(N):
    for j in range(N):
        if i + j > N - 1:  # строго под побочной
            x = A[i][j]
            if (min_below_sec is None) or (x < min_below_sec):
                min_below_sec = x
                pos_min = (i, j)

if max_above is None:
    print("\nНад главной диагональю элементов нет.")
else:
    i, j = pos_max
    print(f"\nМаксимум над главной диагональю: {max_above:.6g} (строка {i+1}, столбец {j+1})")

if min_below_sec is None:
    print("Под побочной диагональю элементов нет.")
else:
    i, j = pos_min
    print(f"Минимум под побочной диагональю: {min_below_sec:.6g} (строка {i+1}, столбец {j+1})")





from is_number_check import is_number
n = int(input('Введите размер квадратной матрицы: '))
while n <= 0:
    print('Размер не может быть меньше или равен нулю!')
    n = int(input('Введите размер квадратной матрицы: '))
m = n
A = []
for i in range(n):
    while True:
        val = input(f"Строка {i + 1}: ").strip().split()
        if len(val) != m:
            print(f"Ошибка: нужно {m} значения, а введено {len(val)}.")
            continue

        ok = True
        for t in val:
            if not is_number(t):
                print(f"Ошибка: '{t}' не распознано как число.")
                ok = False
                break

        if not ok:
            continue

        row = [float(t) for t in val]
        A.append(row)
        break
print('\nВведённая матрица')

# Находим максимальную ширину среди всех чисел
max_width = max(len(f"{x:.6g}") for row in A for x in row)

line = '-' * ((max_width + 3) * m + 4)

# Вывод таблицы
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)

# Меняем элементы местами относительно главной диагонали
for i in range(n):
    for j in range(i + 1, n):  # только над главной диагональю
        A[i][j], A[j][i] = A[j][i], A[i][j]

# Вывод результата
print("\nТранспонированная матрица:")
print(line)
for row in A:
    print('|', end='')
    for x in row:
        print(f" {x:^{max_width+1}.6g} |", end='')
    print()
    print(line)