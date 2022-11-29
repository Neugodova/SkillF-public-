while True:  #цикл, который запрашивает данные каждый раз
    try:
        spisok = [int(i) for i in input("Введите последовательность чисел через пробел: ").split()]   # записыпаем введенные числа в список, при этом сразу разделяя их посимвольно
        if not spisok:   # если нет данных, вывод подсказки
            print('Вы не ввели числа\n'
                  '(необходимо ввести только цифры через пробел)')
        else:
            break
    except ValueError as exp:  # назначаем исключение
        print('Вы ввели недопустимые символы\n'
              '(необходимо ввести только цифры через пробел)')

while True:  #цикл, который запрашивает данные каждый раз
    try:
        num = [int(i) for i in input("Введите целое число: ").split()]  # записыпаем введенные числа в список, при этом сразу разделяя их посимвольно
        if not num:  # если нет данных, вывод подсказки
            print('Вы не ввели число\n'
                  '(необходимо ввести целое число)')
        else:
            break
    except ValueError as exp:  # назначаем исключение
        print('Вы ввели недопустимые символы\n'
              '(необходимо ввести только целое число)')


def my_sort(spisok): # функция сортировки выбором
    for i in range(len(spisok)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(spisok)):
            if spisok[j] < spisok[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            spisok[i], spisok[idx_min] = spisok[idx_min], spisok[i]
    return spisok


print("Список после сортировки:", my_sort(spisok))


def binary_search(spisok, num, low, high):
    middle = (low + high) // 2
    if min(spisok) >= num[0]:
        return f'Элемент меньше введенного числа отсутствует\n' \
               f'Номер позиции элемента, который больше или равен введенному числу: {low}'
    elif max(spisok) < num[0]:
        return f'Элемент больше введенного числа отсутствует\n' \
               f'Номер позиции элемента, который меньше введенного числа: {high}'
    else:
        if low > high:
            return f'Номер позиции элемента, который меньше введенного числа: {middle}\n' \
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle + 1}'
        elif spisok[middle] == num[0]:
            return f'Номер позиции элемента, который меньше введенного числа: {middle - 1}\n' \
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle}'
        elif spisok[middle] > num[0]:
            return binary_search(spisok, num, low, middle - 1)
        else:
            return binary_search(spisok, num, middle + 1, high)


print(binary_search(spisok, num, 0, len(spisok) - 1))
