"""
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
"""

import random


def quickSort(list, start, end):
    if start < end:
        partitionIndex = partition(list, start, end)

        quickSort(list, start, partitionIndex)
        quickSort(list, partitionIndex + 1, end)


def partition(list, start, end):
    middle = (end + start) // 2
    pivot = list[middle]
    leftIndex = start - 1
    rightIndex = end + 1

    while True:
        while True:
            leftIndex += 1
            if list[leftIndex] >= pivot:
                break

        while True:
            rightIndex -= 1
            if list[rightIndex] <= pivot:
                break

        if leftIndex >= rightIndex:
            return rightIndex

        list[leftIndex], list[rightIndex] = list[rightIndex], list[leftIndex]


exampleSize = 10
exampleList = [random.randint(-100, 100) for i in range(exampleSize)]
print(exampleList)
quickSort(exampleList, 0, exampleSize - 1)
print(exampleList)

"""
Это классический QuickSort с серединным опорным элементом — стандартный, понятный и быстрый алгоритм. 
Серединный опорный элемент должен помочь в случае неслучайного массива. 

В контексте этой задачи у него было всего два реальных конкурента: TimSort и Radix. 

TimSort сложнее, больше подходит для отсортированных или почти отсортированных массивов, а также совершенно проигрывает QuickSort в случае полностью случайного набора элементов. 
Если появится необходимость использовать именно TimSort, то достаточно просто вызвать стандартную функцию list.sort(). 

Radix же по идее работает быстрее в случае массивов чисел или строк, но он слишком специфичен и непонятен для широкого применения.
"""