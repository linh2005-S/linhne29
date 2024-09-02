# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:59:07 2024

@author: linh
"""
def liet_ke_nghiem(a, b, c, d):
  for x in range(1, d//a + 1):
    for y in range(1, (d - a*x)//b + 1):
      z = (d - a*x - b*y) // c
      if z > 0 and (a*x + b*y + c*z) == d:
        print(f"({x}, {y}, {z})")
liet_ke_nghiem(2, 7, 9, 979)
