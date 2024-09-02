# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:18:01 2024

@author: linh
"""
N = int(input("Nhập số nguyên N: "))
def sap_xep_so(N):
  chuoi_so = list(str(N))
  chuoi_so.sort()
  so_moi = int("".join(chuoi_so))
  return so_moi
print("Số sau khi sắp xếp:", sap_xep_so(N))