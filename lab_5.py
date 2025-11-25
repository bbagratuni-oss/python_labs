# Нарек Аветисян, группа ИУ7-12Б
# Назначение: программа по введенным данным(начальное значение аргумента, конечное значение аргумента, шаг разбиения
# выводит таблицу, потом пользователем вводится количество засечек и программа выводит график функции,
# где каждой точке соответствует символ '*' и если 0 попадает в диапазон области значений, то выводится еще ось абсцисс

# ширина области построения графика
width = 80

w_a = 14
w_c = 14
header = f"| {'a':^{w_a}} | {'c':^{w_c}} |"
line = '-' * len(header)

a_first = float(input('Введите начальное значение аргумента: '))
a_last = float(input('Введите конечное значение аргумента: '))
a_step = float(input('Введите шаг разбиения: '))
while a_first == a_last or (a_first > a_last and a_step >= 0) or (a_first < a_last and a_step <= 0):
    print('Введите другие значения!')
    a_first = float(input('Введите начальное значение аргумента: '))
    a_last = float(input('Введите конечное значение аргумента: '))
    a_step = float(input('Введите шаг разбиения: '))

# вывод таблицы значений
print(line)
print(header)
print('|' + '-' * (w_a + 2) + '+' + '-' * (w_c + 2) + '|')

n_steps = int(abs(a_last - a_first) / abs(a_step))
# вычислим минимум и максимум значения функции
a = a_first
c = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1
min_val = c
max_val = c

for i in range(n_steps + 1):
    a = a_first + a_step * i
    c = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1
    print(f'| {a:>{w_a}.7g} | {c:>{w_c}.7g} |')
    if c < min_val:
        min_val = c
    if c > max_val:
        max_val = c
print(line)

# ввод количества засечек на оси ординат (от 4 до 8)
ticks = int(input('Введите количество засечек (от 4 до 8): '))
while ticks < 4 or ticks > 8:
    ticks = int(input('Введите количество засечек (от 4 до 8): '))

# вычисляем масштаб
if max_val == min_val:
    delta = 1
else:
    delta = (max_val - min_val) / width

# позиция оси абсцисс, если 0 входит в диапазон значений
zero_in_range = (min_val <= 0 <= max_val)
if zero_in_range:
    axis_pos = int((0 - min_val) / delta)
else:
    axis_pos = -1

# печатаем линейку значений (засечки)
# разбиваем ширину на (ticks-1) промежутков
step_x = width / (ticks - 1)
print(' ', end='')
for i in range(ticks):
    tick_val = min_val + (max_val - min_val) * i / (ticks - 1)
    seg_width = int(step_x)
    zasechka = f"{tick_val:.5g}"
    if seg_width < len(zasechka):
        seg_width = len(zasechka) + 1
    left_spaces = (seg_width - len(zasechka)) // 2
    right_spaces = seg_width - len(zasechka) - left_spaces
    print(' ' * left_spaces + zasechka + ' ' * right_spaces, end='')
print()

# строим график построчно
for i in range(n_steps + 1):
    a = a_first + a_step * i
    c = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1
    if max_val != min_val:
        pos = int((c - min_val) / delta)
    else:
        pos = 0
    # выводим значение аргумента слева
    print(f'{a:<{10}.7g}', end='')
    # строим строку с нужным символом
    for col in range(width + 1):
        if col == pos:
            # звёздочка для значения функции
            print('*', end='')
        elif zero_in_range and col == axis_pos:
            # вертикальная ось, если ноль входит в диапазон
            print('|', end='')
        else:
            print(' ', end='')
    print()
print()
print('-'*(width+20))
print(f'Дополнительное задание c_max - c_min: {(max_val - min_val):.7g}')













# Запрос начального и конечного значения X, а также шага разбиения
while True:
    X_start = float(input("Введите начальное значение X: "))
    X_end   = float(input("Введите конечное значение X: "))
    step    = float(input("Введите шаг разбиения: "))
    # Проверка шага
    if step == 0:
        print("Шаг не должен быть 0. Повторите ввод.")
        continue
    if (X_end - X_start) * step < 0:
        print("Шаг имеет неверный знак (не ведёт от начального к конечному). Повторите ввод.")
        continue
    break

# Запрос количества засечек на оси ординат
N_ticks = 0
while N_ticks < 4 or N_ticks > 8:
    N_ticks = int(input("Введите количество засечек на оси ординат (4-8): "))
    if N_ticks < 4 or N_ticks > 8:
        print("Число засечек должно быть от 4 до 8!")

# Вычисление диапазона значений функции (min_y и max_y) на заданном отрезке
min_y = None
max_y = None
x = X_start
# Итерация по x с помощью while, учитывая знак шага
while (step > 0 and x <= X_end) or (step < 0 and x >= X_end):
    y = -x**2 + 4  # значение функции
    if min_y is None or y < min_y:
        min_y = y
    if max_y is None or y > max_y:
        max_y = y
    # Увеличение (или уменьшение) x на шаг
    x += step

# Защита от вырожденного случая, когда все y равны (например, шаг очень большой)
if min_y == max_y:
    min_y -= 1
    max_y += 1

# Ширина области графика в символах
width = 80

# Определение позиции вертикальной оси Y (для y = 0), если 0 входит в диапазон значений y
axis_col = None
if min_y <= 0 <= max_y:
    # Линейное преобразование 0 -> столбец (0 ... width-1)
    axis_col = int(round((0 - min_y) / (max_y - min_y) * (width - 1)))

# Формирование линейки значений (засечек) над графиком
# Начально заполняем линейку пробелами
ruler = " " * width
if N_ticks > 1:
    step_y = (max_y - min_y) / (N_ticks - 1)
else:
    step_y = 0  # особый случай, хотя N_ticks всегда >=4 по условию
i = 0
while i < N_ticks:
    # Вычисляем значение засечки и его текстовое представление
    tick_value = min_y + i * step_y
    if i == N_ticks - 1:   # последнее значение точно равно max_y (из-за округлений)
        tick_value = max_y
    # Форматируем число (убираем лишние нули после запятой)
    tick_label = str(round(tick_value, 2))  # округляем до 2 знаков для красоты
    # Если число целое (например, "4.0"), уберём десятичную точку
    if tick_label.endswith(".0"):
        tick_label = tick_label[:-2]
    # Вычисляем позицию в строке для этой засечки
    col = int(round((tick_value - min_y) / (max_y - min_y) * (width - 1)))
    if i == N_ticks - 1:
        # Сдвигаем последнюю метку влево, чтобы она полностью поместилась
        col = max(0, width - len(tick_label))
    # Вставляем метку в строку ruler на вычисленную позицию
    # (формируем новую строку, заменяя фрагмент на tick_label)
    left_part  = ruler[:col]
    right_part = ruler[col + len(tick_label):] if col + len(tick_label) < len(ruler) else ""
    ruler = left_part + tick_label + right_part
    i += 1

# Вывод линейки засечек с отступом слева (под значения X)
# Определяем максимальную ширину для печати X (чтобы выровнять по правому краю)
max_x_len = 0
x = X_start
while (step > 0 and x <= X_end) or (step < 0 and x >= X_end):
    # Подготовим строковое представление x (уберём .0 для целых значений)
    x_label = str(x if x % 1 != 0 else int(x))
    if len(x_label) > max_x_len:
        max_x_len = len(x_label)
    x += step

# Печать линейки (значения засечек) с отступом для размещения значений X слева
print(" " * (max_x_len + 1) + ruler)

# Построение и вывод строк графика для каждого значения x
x = X_start
while (step > 0 and x <= X_end) or (step < 0 and x >= X_end):
    y = -x**2 + 4
    # Вычисляем позицию столбца для значения y
    star_col = int(round((y - min_y) / (max_y - min_y) * (width - 1)))
    # Формируем строку графика из 80 символов
    line = ""
    col = 0
    while col < width:
        if axis_col is not None and col == axis_col:
            # Отметка оси Y
            line += "|"
        elif col == star_col:
            # Точка графика
            line += "*"
        else:
            line += " "
        col += 1
    # Если звёздочка совпала с осью, заменим её на ось (ось видима непрерывно)
    if axis_col is not None and star_col == axis_col:
        # Заменим символ в позиции axis_col на '|'
        line = line[:axis_col] + "|" + line[axis_col+1:]
    # Формируем метку X слева (выравнивание по правому краю max_x_len)
    x_label = str(x if x % 1 != 0 else int(x))
    x_label = x_label.rjust(max_x_len)
    # Выводим строку: значение x и график
    print(f"{x_label} {line}")
    x += step

