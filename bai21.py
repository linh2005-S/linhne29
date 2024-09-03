# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:28:50 2024

@author: linh
"""
so = int(input("Nhập một số từ 0 đến 9: "))
chuoi_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if 0 <= so <= 9:
    print(chuoi_so[so])
else:
    print("Khong doc duoc")