#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вывести на экран большее из трёх заданных чисел.

import sys

if __name__ == "__main__":
    a1, a2, a3 = map(float, input("Введите 3 числа через пробел\n").split())

    if a1 > a2:
        if a1 > a3:
            maximum = a1
        else:
            maximum = a3
    else:
        if a2 > a3:
            maximum = a2
        else:
            maximum = a3
        
    print(f"Большее из трех чисел: {a1, a2, a3} = {maximum}")
