# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:26:36 2024

@author: linh
"""
def tim_uoc_so(n):
  uoc_so = []
  for i in range(1, n+1):
    if n % i == 0:
      uoc_so.append(i)
  return uoc_so
while True:
  try:
    n = int(input("Nhập số nguyên dương N: "))
    if n <= 0:
      print("Vui lòng nhập số nguyên dương.")
    else:
      break
  except ValueError:
    print("Vui lòng nhập số nguyên.")
if n > 0:
  print("Các ước số của", n, "là:", tim_uoc_so(n))