# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:20:05 2024

@author: linh
"""
n = int(input("Nhập số nguyên dương N: "))
def tinh_tong_chu_so(n):
  tong = 0
  while n > 0:
    tong += n % 10
    n //= 10
  return tong
print("Tổng các chữ số của", n, "là:", tinh_tong_chu_so(n))
