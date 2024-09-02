# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:25:37 2024

@author: linh
"""
def in_n_so_fibonacci(n):
  if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0.")
    return
  fibo1, fibo2 = 0, 1
  print(fibo1, end=' ')
  for _ in range(1, n):
    print(fibo2, end=' ')
    fibo1, fibo2 = fibo2, fibo1 + fibo2
in_n_so_fibonacci(10)
