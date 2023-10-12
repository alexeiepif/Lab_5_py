#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вводится число карандашей . Вывести фразу
# Я купил N карандашей , согласовав слово
# "карандаш" с числом .

import math
import sys


if __name__ == '__main__':
    count = int(input("Введите число карандашей: "))
    if count <= 0:
        print("Неправильное число", file=sys.stderr)
        exit(1)
    elif count == 1:
        temp = "карандаш"
    elif count < 5:
        temp = "карандаша"
    elif count <= 10:
        temp = "карандашей"
    else:
        print("Слишком много карандашей", file=sys.stderr)
        exit(1)
    print(f"Я купил {count} {temp}")
