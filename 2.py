"""
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""

import random


class BufferSearch:
    def __init__(self, bufferSize):
        self._bufferSize = bufferSize
        self._buffer = [None for i in range(self._bufferSize)]
        self._currentPosition = 1
        self._oldPosition = 0

    @property
    def cP(self):
        return self._currentPosition

    @cP.setter
    def cP(self, value):
        if value >= self._bufferSize:
            value = 0

        if self._currentPosition == self.oP and self._buffer[value] is not None:
            self.oP += 1

        self._currentPosition = value

    @property
    def oP(self):
        return self._oldPosition

    @oP.setter
    def oP(self, value):
        if value >= self._bufferSize:
            value = 0
        self._oldPosition = value

    def add(self, value):
        self._buffer[self.cP] = value
        self.cP += 1

    def remove(self):
        if self._buffer[self.oP] is not None:
            self._buffer[self.oP] = None
            self.oP += 1

    def print(self):
        print(self._buffer)


a = BufferSearch(5)
for i in range(7):
    a.add(random.randint(-100, 100))
    a.print()
for i in range(6):
    a.remove()
    a.print()
for i in range(1):
    a.add(random.randint(-100, 100))
    a.print()
for i in range(2):
    a.remove()
    a.print()
for i in range(1):
    a.add(random.randint(-100, 100))
    a.print()

print("\n\n")


class BufferShift:
    def __init__(self, bufferSize):
        self._bufferSize = bufferSize
        self._buffer = [None for i in range(self._bufferSize)]
        self._currentPosition = 0

    def add(self, value):
        if self._currentPosition < self._bufferSize:
            self._buffer[self._currentPosition] = value
            self._currentPosition += 1
        else:
            self.remove(True)
            self._buffer[self._bufferSize - 1] = value

    def remove(self, fromAdd=False):
        if self._buffer[0] is not None:
            i = 0
            while self._buffer[i] is not None and i < self._bufferSize - 1:
                self._buffer[i] = self._buffer[i + 1]
                i += 1
            if i < self._bufferSize - 1:
                self._buffer[i + 1] = None
            else:
                self._buffer[self._bufferSize - 1] = None

            if not fromAdd:
                self._currentPosition -= 1

    def print(self):
        print(self._buffer)


a = BufferShift(5)
for i in range(7):
    a.add(random.randint(-100, 100))
    a.print()
for i in range(6):
    a.remove()
    a.print()
for i in range(1):
    a.add(random.randint(-100, 100))
    a.print()
for i in range(2):
    a.remove()
    a.print()
for i in range(1):
    a.add(random.randint(-100, 100))
    a.print()

"""
Первая реализация (BufferSearch)

Отслеживаются как позиция для записи, так и позиция для удаления, благодаря чему можно избежать сдвига всех значений буфера при переполнении или удалении. 
Однако для определения самой старой записи нужно учесть ряд моментов и написать сравнительно много кода, что может привести к большему количеству багов.

Плюсы: Быстро.
Минусы: Сложно, много кода.

Вторая реализация (BufferShift)

Отслеживается лишь позиция для записи, а самая старая запись — это всегда первый элемент буфера. 
При переполнении или удалении первый элемент уходит, и весь массив сдвигается налево. 
Благодаря простоте схемы кода немного, и он понятен, но производительность страдает из-за сдвига.

Плюсы: Интуитивно понятно, кратко.
Минусы: Медленно.


Еще можно было воспользоваться deque, но это было бы слишком просто и контроля над алгоритмом было бы мало,
хотя по скорости этот вариант должен быть сравним с первой реализацией (правда, из-за многих лет оптимизации deque может быть гораздо быстрее), а по объему кода — со второй.

from collections import deque

class BufferDeque:
    def __init__(self, bufferSize):
        self._buffer = deque(maxlen=bufferSize)

    def add(self, value):
        self._buffer.append(value)

    def remove(self):
        if self._buffer:
            self._buffer.popleft()

    def print(self):
        print(self._buffer)

"""
