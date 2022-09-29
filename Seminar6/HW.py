# Найти сумму чисел списка стоящих на нечетной позиции
# n = int(input('n = '))
# print(sum(list(filter(lambda x: x%2, [x for x in range(1, n + 1)]))))


# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# lst = [2, 3, 4, 2, 5]

# def multy_bi(lst):
#   return [lst[i] * lst[len(lst)-1 -i] for i in range(len(lst)//2 + len(lst)%2)]

# print(multy_bi(lst))


# Подсчитать сумму цифр в вещественном числе
# n = input('Введите вещественное число: ')
# sum = sum(map(int, n.replace('.', '')))
# print (sum)


#6 Сформировать список из  N членов последовательности
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input('Введите количество членов последовательности: '))

# list = [3**i if i % 2 == 0 else -3**i for i in range (N)]
# print(list)