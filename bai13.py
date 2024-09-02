# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:41:01 2024

@author: linh
"""
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
cau_a = f"{ngay}/{thang}/{nam}"
print("ta được: ", cau_a)
cau_b = f"{ngay}/{thang}/{str(nam)[-2:]}"
print("ta được: ", cau_b)
cau_c = f"{nam}/{thang}/{ngay}"
print("ta được: ", cau_c)
