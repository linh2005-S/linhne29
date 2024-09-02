# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:21:54 2024

@author: linh
"""

N=int(input("nhập số nguyên dương N có 2 chữ số: "))
if 9<N<100:
    chuc=N//10
    don_vi=N%10
print("kết quả: ", chuc+don_vi)