# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:38:05 2024

@author: linh
"""
def tinh_so_nut(bien_so):
  if len(bien_so) != 4 or not bien_so.isdigit():
    return "Biển số xe không hợp lệ. Vui lòng nhập đúng 4 chữ số."
  chu_so = [int(ch) for ch in bien_so]
  tong = sum(chu_so)
  so_nut = tong % 10
  return so_nut
bien_so = input("Nhập biển số xe (4 chữ số): ")
print(f"Số nút của biển số xe {bien_so} là: {tinh_so_nut(bien_so)}")