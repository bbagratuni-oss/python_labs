# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа из двух одномерным массивов А и В сформировывает матрицу М
# такую что m[i][j] = a[i] * b[j]. Определяет количество полных квадратов в каждой строке матрицы.

from is_number_check import is_signed_integer

n = int(input('Введите размер массива А: '))
while n <= 0:
    n = int(input('Размер должен быть больше нуля: '))

a = [0] * n
for i in range(n):
    a[i] = input(f'Введите {i}-й элемент массива А: ')
    while not is_signed_integer(a[i]):
        a[i] = input('Ошибка! элемент не распознан как целое число. Введите другое значение: ')
    a[i] = int(a[i])

m = int(input('\nВведите размер массива B: '))
while m <= 0:
    m = int(input('Размер должен быть больше нуля: '))

b = [0] * m
for i in range(m):
    b[i] = input(f'Введите {i}-й элемент массива B: ')
    while not is_signed_integer(b[i]):
        b[i] = input('Ошибка! элемент не распознан как целое число. Введите другое значение: ')
    b[i] = int(b[i])

matrix = [[0] * len(b) for i in range(len(a))]
S = [0]*len(a)

for i in range(len(a)):
    for j in range(len(b)):
        val = a[i] * b[j]
        matrix[i][j] = val
        if val >= 0 and int(val ** 0.5) ** 2 == val:
            S[i] += 1

max_width = max(len(f"{x:.6g}") for row in matrix for x in row)
line = '-' * ((max_width + 3) * len(matrix[0]) + 1)
lil_line = '-' * 9
print()
print(line, end='')
print(' '*5 + lil_line)

for row in range(len(matrix)):
    print('|', end = '')
    for val in matrix[row]:
        print(f' {val:^{max_width}.6g} |', end='')
    print(f'{"|":>6} {S[row]:^5.6g} {"|":<6}')
    print(line, end='')
    print(' '*5 + lil_line)





# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа поворачивает квадратную матрицу на 90 градусов по часовой,
# затем на 90 против. Выводит исходную, промежуточную и итоговую матрицы

from is_number_check import is_signed_integer

def input_matrix_numbers(rows, cols):
    matrix = []
    print(f"Введите {rows} строк по {cols} чисел (через пробел).")
    for i in range(rows):
        while True:
            val = input(f"Строка {i + 1}: ").strip().split()
            if len(val) != cols:
                print(f"Ошибка: нужно {cols} значения, а введено {len(val)}.")
                continue
            isnum = True
            for t in val:
                if not is_signed_integer(t):
                    print(f"Ошибка: '{t}' не распознано как целое число.")
                    isnum = False
                    break
            if not isnum:
                continue
            row = [int(t) for t in val]
            matrix.append(row)
            break
    return matrix


n = int(input('Введите размер квадратной матрицы: '))
while n <= 0:
    print('Размер не может быть меньше или равен нулю!')
    n = int(input('Введите размер квадратной матрицы: '))

m = n
matrix = input_matrix_numbers(n, m)

def print_matrix(mat, title):
    width = max(len(f"{x:.7g}") for row in mat for x in row) if mat and mat[0] else 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(f"\n{title}")
    print(line)
    for row in mat:
        print("|" + "|".join(f" {x:^{width}.7g} " for x in row) + "|")
        print(line)


def rotate_clockwise(matrix):
    n = len(matrix)
    for layer in range(n // 2):  # layer - номер слоя от края к центру
        first = layer  # первый индекс текущего слоя
        last = n - 1 - layer  # последний индекс текущего слоя
        for i in range(first, last):  # пробегаем верхнюю сторону слоя слева направо
            offset = i - first  # смещение относительно левого края слоя
            # Сохраняем верхний элемент чтобы не потерять его
            top = matrix[first][i]
            # Перекладывания по часовой стрелке:
            # слева - вверх
            matrix[first][i] = matrix[last - offset][first]
            # снизу - влево
            matrix[last - offset][first] = matrix[last][last - offset]
            # справа - вниз
            matrix[last][last - offset] = matrix[i][last]
            # верхний (из top) - вправо
            matrix[i][last] = top

def rotate_counterclockwise(mat):
    N = len(mat)
    for layer in range(N // 2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            # сохраним верхний
            top = mat[first][i]
            # правый - верх
            mat[first][i] = mat[i][last]
            # нижний - правый
            mat[i][last] = mat[last][last - offset]
            # левый - нижний
            mat[last][last - offset] = mat[last - offset][first]
            # верхний (из top) - левый
            mat[last - offset][first] = top


print_matrix(matrix, "Исходная матрица:")

rotate_clockwise(matrix)
print_matrix(matrix, "После поворота на 90 градусов по часовой:")

rotate_counterclockwise(matrix)
print_matrix(matrix, "После поворота на 90 градусов против часовой (итог):")






# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа из двух матриц А и В с одинаковым количеством столбцов
# считает для каждого столбца А количество элементов больших ср.арф. элементов
# соответствующего столбца В. Затем выводит полученные значения.
# Преобразовывает матрицу В путем умножения все элементов столбца на посчитанное для этого столбца значение, если != 0

from is_number_check import is_number

def input_matrix_numbers(rows, cols):
    matrix = []
    print(f"Введите {rows} строк по {cols} чисел (через пробел).")
    for i in range(rows):
        while True:
            vals = input(f"Строка {i+1}: ").strip().split()
            if len(vals) != cols:
                print(f"Ошибка: нужно {cols} значения, а введено {len(vals)}.")
                continue
            isnum = True
            for v in vals:
                if not is_number(v):
                    print(f"Ошибка: '{v}' не распознано как число.")
                    isnum = False
                    break
            if not isnum:
                continue
            matrix.append([float(v) for v in vals])
            break
    return matrix

def print_matrix(mat, title):
    width = max(len(f"{x:.7g}") for row in mat for x in row) if mat and mat[0] else 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(f"\n{title}")
    print(line)
    for row in mat:
        print("|" + "|".join(f" {x:^{width}.7g} " for x in row) + "|")
        print(line)

ra = int(input("Введите число строк матрицы A: "))
while ra <= 0:
    ra = int(input("Ошибка! Введите положительное число строк A: "))

rb = int(input("Введите число строк матрицы B: "))
while rb <= 0:
    rb = int(input("Ошибка! Введите положительное число строк B: "))

c = int(input("Введите число столбцов (общее для A и B): "))
while c <= 0:
    c = int(input("Ошибка! Введите положительное число столбцов: "))

print("\nМатрица A:")
A = input_matrix_numbers(ra, c)
print("\nМатрица B:")
B = input_matrix_numbers(rb, c)

print_matrix(A, "Исходная матрица A:")
print_matrix(B, "Исходная матрица B:")

print("\nЗначения по столбцам: сколько элементов столбца A > среднего соответствующего столбца B")
for j in range(c):
    s = 0
    for i in range(rb):
        s += B[i][j]
    sr = s / rb

    cnt = 0
    for i in range(ra):
        if A[i][j] > sr:
            cnt += 1

    end_sep = " " if j < c - 1 else "\n"
    print(f"{cnt:.7g}", end=end_sep)

    if cnt != 0:
        for i in range(rb):
            B[i][j] = B[i][j] * cnt

print_matrix(B, "Матрица B после преобразования:")






# Нарек Аветисян, группа ИУ7-12Б
# Назначение: из матрицы D и массива I, содержащий номера строк, для которых
# нужно определить макс. элемент. Значения максимальных элементов запомнить в массиве R.
# Определить среднее арифметическое вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

from is_number_check import is_number, is_signed_integer

def input_matrix_numbers(rows, cols):
    matrix = []
    print(f"Введите {rows} строк по {cols} чисел (через пробел).")
    for i in range(rows):
        while True:
            vals = input(f"Строка {i+1}: ").strip().split()
            if len(vals) != cols:
                print(f"Ошибка: нужно {cols} значения, а введено {len(vals)}.")
                continue
            isnum = True
            for v in vals:
                if not is_number(v):
                    print(f"Ошибка: '{v}' не распознано как число.")
                    isnum = False
                    break
            if not isnum:
                continue
            matrix.append([float(v) for v in vals])
            break
    return matrix

def print_matrix(mat, title):
    width = max(len(f"{x:.7g}") for row in mat for x in row) if mat and mat[0] else 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(f"\n{title}")
    print(line)
    for row in mat:
        print("|" + "|".join(f" {x:^{width}.7g} " for x in row) + "|")
        print(line)

rows = int(input("Введите число строк матрицы D: "))
while rows <= 0:
    rows = int(input("Ошибка! Введите положительное число строк: "))

cols = int(input("Введите число столбцов матрицы D: "))
while cols <= 0:
    cols = int(input("Ошибка! Введите положительное число столбцов: "))

D = input_matrix_numbers(rows, cols)
print_matrix(D, "Матрица D:")

n = int(input("\nВведите размер массива I: "))
while n <= 0:
    n = int(input("Ошибка! Размер массива должен быть больше нуля: "))

I = [0] * n
for i in range(n):
    I[i] = input(f'Введите {i}-й элемент массива I: ')
    while not is_signed_integer(I[i]):
        I[i] = input('Ошибка! элемент не распознан как целое число. Введите другое значение: ')
    while int(I[i]) > rows or int(I[i]) <= 0:
        I[i] = input(f'Ошибка! значение должно быть в диапазоне 1..{rows}. Введите другое значение: ')
    # while int(I[i]) in I[:i]:
    #     I[i] = input('Ошибка! такой номер уже был введён. Введите другое значение: ')
    I[i] = int(I[i])
    I[i] = int(I[i])

print("\nМассив I:", I)

R = [0] * n
for k in range(n):
    row_idx = I[k] - 1
    max_el = D[row_idx][0]
    for j in range(1, cols):
        if D[row_idx][j] > max_el:
            max_el = D[row_idx][j]
    R[k] = max_el

print("\nМассив R (максимальные элементы выбранных строк):", R)

if n > 0:
    avg = sum(R) / n
else:
    avg = 0

print(f"\nСреднее арифметическое элементов массива R: {avg:.7g}")






# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа из 2 матриц А и В делает матрицу С, равную произведению матриц А и В.
# Выводит все матрицы в виде матриц

from is_number_check import is_number

def input_matrix_numbers(rows, cols, name=""):
    matrix = []
    print(f"Введите матрицу {name}, {rows} строк по {cols} чисел (через пробел).")
    for i in range(rows):
        while True:
            vals = input(f"Строка {i + 1}: ").strip().split()
            if len(vals) != cols:
                print(f"Ошибка: нужно {cols} значения, а введено {len(vals)}.")
                continue
            isnum = True
            for v in vals:
                if not is_number(v):
                    print(f"Ошибка: '{v}' не распознано как число.")
                    isnum = False
                    break
            if not isnum:
                continue
            matrix.append([float(v) for v in vals])
            break
    return matrix

def print_matrix(mat, title):
    width = max(len(f"{x:.7g}") for row in mat for x in row) if mat and mat[0] else 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(f"\n{title}")
    print(line)
    for row in mat:
        print("|" + "|".join(f" {x:^{width}.7g} " for x in row) + "|")
        print(line)

rows_a = int(input("Введите количество строк матрицы A: "))
while rows_a <= 0:
    rows_a = int(input("Ошибка! Введите положительное число строк: "))

cols_a = int(input("Введите количество столбцов матрицы A: "))
while cols_a <= 0:
    cols_a = int(input("Ошибка! Введите положительное число столбцов: "))

rows_b = int(input("Введите количество строк матрицы B: "))
while rows_b <= 0:
    rows_b = int(input("Ошибка! Введите положительное число строк: "))
while rows_b != cols_a:
    rows_b = int(input(f"Ошибка! Для умножения число строк B должно равняться числу столбцов A ({cols_a})."))

cols_b = int(input("Введите количество столбцов матрицы B: "))
while cols_b <= 0:
    cols_b = int(input("Ошибка! Введите положительное число столбцов: "))

A = input_matrix_numbers(rows_a, cols_a, 'A')
B = input_matrix_numbers(rows_b, cols_b, 'B')

C = [[0]*cols_b for _ in range(rows_a)]

for i in range(rows_a):
    for j in range(cols_b):
        s = 0
        for k in range(cols_a):
            s += A[i][k] * B[k][j]
        C[i][j] = s

print_matrix(A, "Матрица A:")
print_matrix(B, "Матрица B:")
print_matrix(C, "Матрица C = A x B:")





# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа матрицу символов преобразовывает так: заменяет все
# согласные латинские букв на заглавные, а все гласные латинские буквы на строчные

def is_latin_letter(ch):
    return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

def to_lower(ch):
    if 'A' <= ch <= 'Z':
        return chr(ord(ch) + 32)  # разница между 'A' и 'a' в ASCII = 32
    return ch

def to_upper(ch):
    if 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
    return ch

def is_vowel_latin(ch):
    # приводим к нижнему регистру и проверяем на гласную латиницу
    c = to_lower(ch)
    return c in ('a', 'e', 'i', 'o', 'u', 'y')

# ввод матрицы символов
def input_char_matrix(rows, cols):
    matrix = []
    print(f"Введите {rows} строк по {cols} символов (без пробелов между ними).")
    for i in range(rows):
        while True:
            line = input(f"Строка {i + 1}: ").rstrip("\n")
            if len(line) != cols:
                print(f"Ошибка: нужно {cols} символов, а введено {len(line)}.")
                continue
            matrix.append(list(line))
            break
    return matrix

def print_char_matrix(mat, title):
    print("\n" + title)
    if not mat or not mat[0]:
        print("Матрица пуста")
        return
    width = 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(line)
    for row in mat:
        print("|" + "|".join(f" {str(x):>{width}} " for x in row) + "|")
        print(line)

rows = int(input("Введите количество строк матрицы: "))
while rows <= 0:
    rows = int(input("Ошибка! Введите положительное число строк: "))

cols = int(input("Введите количество столбцов матрицы: "))
while cols <= 0:
    cols = int(input("Ошибка! Введите положительное число столбцов: "))

D = input_char_matrix(rows, cols)
print_char_matrix(D, "Матрица до преобразования:")

for i in range(rows):
    for j in range(cols):
        ch = D[i][j]
        if is_latin_letter(ch):
            if is_vowel_latin(ch):
                D[i][j] = to_lower(ch)
            else:
                D[i][j] = to_upper(ch)

print_char_matrix(D, "Матрица после преобразования:")





# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа из трехмерного массива выводит срез по большему из измерений(XxYxZ)

from is_number_check import is_number

def input_3d_array(X, Y, Z):
    array = [[[0]*Z for _ in range(Y)] for _ in range(X)]
    print(f"Введите элементы 3D массива размером {X}x{Y}x{Z}:")
    for x in range(X):
        print(f"\nМатрица номер {x} (слой {x+1}/{X}):")
        for y in range(Y):
            while True:
                row = input(f"Строка {y+1}: ").strip().split()
                if len(row) != Z:
                    print(f"Ошибка: нужно {Z} чисел, а введено {len(row)}.")
                    continue
                isnum = True
                for val in row:
                    if not is_number(val):
                        print(f"Ошибка: '{val}' не распознано как число.")
                        isnum = False
                        break
                if not isnum:
                    continue
                array[x][y] = [float(val) for val in row]
                break
    return array

def print_matrix(mat, title):
    width = max(len(f"{x:.7g}") for row in mat for x in row) if mat and mat[0] else 1
    line = "+" + "+".join("-" * (width + 2) for _ in range(len(mat[0]))) + "+"
    print(f"\n{title}")
    print(line)
    for row in mat:
        print("|" + "|".join(f" {x:^{width}.7g} " for x in row) + "|")
        print(line)

X = int(input("Введите X (число матриц): "))
while X <= 0:
    X = int(input("Ошибка! Введите положительное X: "))

Y = int(input("Введите Y (число строк в каждой матрице): "))
while Y <= 0:
    Y = int(input("Ошибка! Введите положительное Y: "))

Z = int(input("Введите Z (число столбцов): "))
while Z <= 0:
    Z = int(input("Ошибка! Введите положительное Z: "))

arr = input_3d_array(X, Y, Z)

# определяем по какой оси делаем срез
max_dim = max(X, Y, Z)
if max_dim == X:
    index = X // 2  # середина вниз
    print(f"\nСрез по оси X (матрица с индексом {index}):")
    print_matrix(arr[index], f"Срез X={index}")
elif max_dim == Y:
    index = Y // 2
    print(f"\nСрез по оси Y (строка номер {index} во всех матрицах):")
    # собираем все строки index из каждой матрицы (X×Z)
    slice_matrix = [arr[x][index] for x in range(X)]
    print_matrix(slice_matrix, f"Срез Y={index}")
else:
    index = Z // 2
    print(f"\nСрез по оси Z (столбец номер {index} во всех матрицах):")
    # собираем столбец index из каждой матрицы (XxY)
    slice_matrix = [[arr[x][y][index] for y in range(Y)] for x in range(X)]
    print_matrix(slice_matrix, f"Срез Z={index}")