# Аветисян Нарек, ИУ7-12Б
# Назначение программы: Демонстрация и исследование шейкерной сортировки, сортирует введённый пользователем массив и
# измеряет время работы и число перестановок на случайных, упорядоченных и обратно упорядоченных списках трёх размерностей с выводом таблицы

import time
import random
import is_number_check

# Декоратор который измеряет время выполнения функции и добавляет его к результату
def to_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        return *res, end - start
    return wrapper

@to_time
def coctail_sort(arr):
    length = len(arr)
    swapped = True
    start_idx = 0
    end_idx = length - 1
    swaps = 0
    while swapped:
        swapped = False
        for i in range(start_idx, end_idx):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1

        if not swapped:
            break

        swapped = False
        end_idx -= 1
        for i in range(end_idx, start_idx - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1
        start_idx += 1

    return arr, swaps

# ЧАСТЬ 1
print('Часть 1')
n = int(input('Введите размер массива: '))
while n <= 0:
    n = int(input('Размер не может быть меньше или равен нулю: '))

a = [0]*n
for i in range(n):
    a[i] = input(f'Введите {i}-й элемент: ')
    while not is_number_check.is_signed_integer(a[i]):
        a[i] = input(f'Ошибка, введите целое число: ')
    a[i] = int(a[i])

print('Введённый массив:             ', a)
sorted_arr, _, _ = coctail_sort(a)
print('Отсортированный массив:       ', sorted_arr)

# ЧАСТЬ 2
print('\nЧасть 2')
N1 = int(input('Введите N1: '))
while N1 <= 0: N1 = int(input('N1 > 0: '))

N2 = int(input('Введите N2: '))
while N2 <= 0: N2 = int(input('N2 > 0: '))

N3 = int(input('Введите N3: '))
while N3 <= 0: N3 = int(input('N3 > 0: '))

def list_for(n, kind):
    if kind == 'sorted':
        arr = list(range(n))
    elif kind == 'random':
        arr = [random.random() for _ in range(n)]
    else:  # 'reverse'
        arr = list(range(n, 0, -1))
    _, k, t_sec = coctail_sort(arr)
    return k, t_sec * 1000.0

(k1, t1) = list_for(N1, 'sorted')
(k2, t2) = list_for(N2, 'sorted')
(k3, t3) = list_for(N3, 'sorted')

(k4, t4) = list_for(N1, 'random')
(k5, t5) = list_for(N2, 'random')
(k6, t6) = list_for(N3, 'random')

(k7, t7) = list_for(N1, 'reverse')
(k8, t8) = list_for(N2, 'reverse')
(k9, t9) = list_for(N3, 'reverse')

w_left = 28
w_cell = 16

line = "+" + "-"*(w_left+2) + "+" + ("-"*(w_cell*2+5) + "+")*3

print("\n" + line)
# Первая строка
print("| " + " " * w_left + " | "
      + f"{'N1':^{35}} | "
      + f"{'N2':^{35}} | "
      + f"{'N3':^{35}} |")
print(line)
# Вторая строка
print("| " + " " * w_left + " | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} |")
print(line)

def row(title, tA,kA, tB,kB, tC,kC):
    print("| " + f"{title:<{w_left}}" + " | "
          + f"{tA:>{w_cell}.7g} | {kA:>{w_cell}.7g} | "
          + f"{tB:>{w_cell}.7g} | {kB:>{w_cell}.7g} | "
          + f"{tC:>{w_cell}.7g} | {kC:>{w_cell}.7g} |")
    print(line)

row("Упорядоченный список",       t1,k1, t2,k2, t3,k3)
row("Случайный список",           t4,k4, t5,k5, t6,k6)
row("Упорядоченный в обратном",   t7,k7, t8,k8, t9,k9)






# ТРЕМЯ СПИСКАМИ В ЧАСТИ ДВА А НЕ ДВУМЯ

# Аветисян Нарек, ИУ7-12Б
# Назначение программы: Демонстрация и исследование шейкерной сортировки, сортирует введённый пользователем массив и
# измеряет время работы и число перестановок на случайных, упорядоченных и обратно упорядоченных списках трёх размерностей с выводом таблицы

import time
import random
import is_number_check

# Декоратор который измеряет время выполнения функции и добавляет его к результату
def to_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        return *res, end - start
    return wrapper

@to_time
def coctail_sort(arr):
    length = len(arr)
    swapped = True
    start_idx = 0
    end_idx = length - 1
    swaps = 0
    while swapped:
        swapped = False
        # слева направо
        for i in range(start_idx, end_idx):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1
        if not swapped:
            break
        swapped = False
        end_idx -= 1
        # справа налево
        for i in range(end_idx, start_idx - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1
        start_idx += 1
    return arr, swaps

# ЧАСТЬ 1
print('Часть 1')
n = int(input('Введите размер массива: '))
while n <= 0:
    n = int(input('Размер не может быть меньше или равен нулю: '))

a = [0]*n
for i in range(n):
    a[i] = input(f'Введите {i}-й элемент: ')
    while not is_number_check.is_signed_integer(a[i]):
        a[i] = input('Ошибка, введите целое число: ')
    a[i] = int(a[i])

print('Введённый массив:             ', a)
sorted_arr, _, _ = coctail_sort(a)
print('Отсортированный массив:       ', sorted_arr)

# ЧАСТЬ 2
print('\nЧасть 2')
N1 = int(input('Введите N1: '))
while N1 <= 0:
    N1 = int(input('N1 > 0: '))
N2 = int(input('Введите N2: '))
while N2 <= 0:
    N2 = int(input('N2 > 0: '))
N3 = int(input('Введите N3: '))
while N3 <= 0:
    N3 = int(input('N3 > 0: '))

def lsts_for(n):
    arr = [random.random() for _ in range(n)]        # случайный
    _, k_rand, t_rand = coctail_sort(arr)            # теперь arr отсортирован
    _, k_sorted, t_sorted = coctail_sort(arr)        # отсортированный
    arr.reverse()                                    # обратно отсортированный
    _, k_rev, t_rev = coctail_sort(arr)
    ms = 1000
    return (t_sorted*ms, k_sorted, t_rand*ms, k_rand, t_rev*ms, k_rev)

# замеры: в памяти на каждом шаге только один список
t1, k1, t4, k4, t7, k7 = lsts_for(N1)
t2, k2, t5, k5, t8, k8 = lsts_for(N2)
t3, k3, t6, k6, t9, k9 = lsts_for(N3)
w_left = 28
w_cell = 16

line = "+" + "-"*(w_left+2) + "+" + ("-"*(w_cell*2+5) + "+")*3

print("\n" + line)
# Первая строка
print("| " + " " * w_left + " | "
      + f"{'N1':^{35}} | "
      + f"{'N2':^{35}} | "
      + f"{'N3':^{35}} |")
print(line)
# Вторая строка
print("| " + " " * w_left + " | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} | "
      + f"{'время':^{w_cell}} | {'перестановки':^{w_cell}} |")
print(line)

def row(title, tA,kA, tB,kB, tC,kC):
    print("| " + f"{title:<{w_left}}" + " | "
          + f"{tA:>{w_cell}.7g} | {kA:>{w_cell}.7g} | "
          + f"{tB:>{w_cell}.7g} | {kB:>{w_cell}.7g} | "
          + f"{tC:>{w_cell}.7g} | {kC:>{w_cell}.7g} |")
    print(line)

row("Упорядоченный список",       t1,k1, t2,k2, t3,k3)
row("Случайный список",           t4,k4, t5,k5, t6,k6)
row("Упорядоченный в обратном",   t7,k7, t8,k8, t9,k9)