#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вывести на экран большее из трёх заданных чисел.

if __name__ == "__main__":
    a1, a2, a3 = map(float, input("Введите 3 числа через пробел\n").split())
    print(f"Большее из трех чисел: {a1, a2, a3} = {max(a1, a2, a3)}")