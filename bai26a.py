# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:11:45 2024

@author: linh
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
somin = min(a, b)
somin = min(somin, c)
somax = max(a, b)
somax = max(somax, c)
sogiua = (a + b + c) - somin - somax
print(somin,sogiua,somax)

