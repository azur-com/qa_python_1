import math
from random import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Hi {name}! You are {age} y.a."
    print (output)
    # Проверяем результат
    assert output == "Hi Анна! You are 25 y.a."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a+b)*2

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a*b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r**2

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = math.pi * 2 * r

    assert length == 144.51326206513048

import random


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список

    # создаём список из 10 случайных чисел от 1 до 100
    l = [random.randint(1, 100) for X in range(10)]



    # сортируем список по возрастанию
    l = sorted(l)
    print("Случайные числа:", l)
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 1, 5, 5, 6, 7, 8, 8, 9, 10, 10, 1]
    # TODO удалите повторяющиеся элементы
    j = 0
    for j in range(len(l)):
        #print(j)
        x_len = len(l)
        i = j+1
        while  i < len(l):
            #print(f"{j}:{i}:{l[i]}")
            if l[j] == l[i]:
                l.pop(i)
                i = i-1
            i= i + 1


    print(l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    print(first)
    d={}
    for key, value in zip(first, second):
        d[key] = value
    print(d)


    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
