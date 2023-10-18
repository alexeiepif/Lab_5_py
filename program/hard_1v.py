#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Составить UML-диаграмму деятельности, программу и произвести
# вычисление значения специальной функции по ее разложению в ряд
# с точностью e = 10^-10, аргумент функции вводится с клавиатуры.
# Номер варианта необходимо получить у преподавателя.
# 1. Интегральный синус.

import scipy.special
import sys


def factorial(n):
    if n < 0:
        print("Отрицательное число!", file=sys.stderr)
        exit(1)
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result


def si(x, eps=1e-10):
    result = 0
    n = 0
    term = 0

    while True:
        term = (pow(-1, n) * pow(x, 2*n + 1)) / ((2*n+1)*factorial(2*n + 1))
        result += term

        if abs(term) < eps:
            break

        n += 1

    return result


x = float(input("Введите значение x: "))
print("Вычисление с использованием scipy.special.sici: ",
      scipy.special.sici(x)[0])
print("Вычисление с использованием разложения в ряд: ", si(x))
