# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:26:17 2024

@author: linh
"""
def so_ngay_trong_thang(thang, nam):
    so_ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if thang == 2:
        if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
            so_ngay[1] = 29
    return so_ngay[thang - 1]
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if 1 <= thang <= 12 and nam >= 1:
  so_ngay = so_ngay_trong_thang(thang, nam)
  print("Tháng", thang, "năm", nam, "có", so_ngay, "ngày.")
else:
  print("Tháng hoặc năm không hợp lệ.")
