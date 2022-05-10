s = input('Введите последовательность чисел через пробел: ')
n = int(input('Введите любое число: '))

if " " not in s:
    print('\nВведите числа, согласно условиям ввода.\n')
    s = input('Введите последовательность чисел через пробел: ')

else:
    s = s.split()

list_s = [int(item) for item in s]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_s = merge_sort(list_s)

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите число поменьше.'

print(f'Список, упорядоченный по возрастанию: {list_s}')

if not binary_search(list_s, n, 0, len(list_s)):
    rI = min(list_s, key=lambda x: (abs(x - n), x))
    ind = list_s.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < n:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI} с индексом {ind}
Ближайший больший элемент: {list_s[max_ind]} с индексом {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI} с индексом {list_s.index(rI)}
В списке нет меньшего элемента''')
    elif rI > user_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI} с индексом {list_s.index(rI)}
Ближайший меньший элемент: {list_s[min_ind]} с индексом {min_ind}''')
    elif list_s.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_s.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_s, n, 0, len(list_s))}')