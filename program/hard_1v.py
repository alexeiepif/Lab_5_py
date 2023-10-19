#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Составить UML-диаграмму деятельности, программу и произвести
# вычисление значения специальной функции по ее разложению в ряд
# с точностью e = 10^-10, аргумент функции вводится с клавиатуры.
# Номер варианта необходимо получить у преподавателя.
# 1. Интегральный синус.

import scipy.special
import math
import sys


if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    result = x
    n = 0
    EPS = 10e-10
    term = result
    while math.fabs(term) > EPS:
        term *= -x**2*(2*n+1)/((2*n+3)**2*(2*n+2))
        result += term
        n += 1

    print("Вычисление с использованием scipy.special.sici: ",
        scipy.special.sici(x)[0])
    print("Вычисление с использованием разложения в ряд: ", result)
