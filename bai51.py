# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:15:48 2024

@author: linh
"""

def kiem_tra_gia_tri(min_value, max_value):
  while True:
    try:
      value = int(input(f"Nhập giá trị trong khoảng [{min_value}, {max_value}]: "))
      if min_value <= value <= max_value:
        return value
      else:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
      print("Giá trị nhập vào không phải là số nguyên. Vui lòng nhập lại.")