# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:13:27 2024

@author: linh
"""
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))
max_number = a
if b > max_number:
      max_number = b
if c > max_number:
      max_number = c
if d > max_number:
      max_number = d
print("số lớn nhất là: ", max_number)

