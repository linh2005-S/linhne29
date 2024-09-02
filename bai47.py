# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:02:25 2024

@author: linh
"""
def liet_ke_nghiem_tong_lon_nhat(a, b, c, d):
  max_sum = 0
  max_solution = None
  for x in range(1, d//a + 1):
    for y in range(1, (d - a*x)//b + 1):
      z = (d - a*x - b*y) // c
      if z > 0 and (a*x + b*y + c*z) == d:
        current_sum = x + y + z
        if current_sum > max_sum:
          max_sum = current_sum
          max_solution = (x, y, z)
  print("Bộ nghiệm có tổng lớn nhất:", max_solution)
liet_ke_nghiem_tong_lon_nhat(2, 7, 9, 979)
