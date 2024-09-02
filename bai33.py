# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:40:45 2024

@author: linh
"""
import math
def is_perfect_square(n):
  sqrt_n = int(math.sqrt(n))
  return sqrt_n * sqrt_n == n
n = int(input("Nhập số nguyên dương n: "))
if is_perfect_square(n):
  print(n, "là số chính phương.")
else:
  print(n, "không phải là số chính phương.")
