# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:43:17 2024

@author: linh
"""
n = int(input("Nhập số nguyên dương n: "))
def is_prime(n):
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True
if is_prime(n):
  print(n, "là số nguyên tố.")
else:
  print(n, "không phải là số nguyên tố.")
