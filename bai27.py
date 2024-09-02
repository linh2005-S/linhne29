# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:23:03 2024

@author: linh
"""

import math
def tinh_dien_tich_chu_vi(hinh):
  if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    dien_tich = canh * canh
    chu_vi = 4 * canh
  elif hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
  elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    dien_tich = math.pi * ban_kinh**2
    chu_vi = 2 * math.pi * ban_kinh
  else:
    print("Hình không hợp lệ!")
    return 
    print("Diện tích: ", dien_tich)
    print("Chu vi: ", chu_vi)
hinh = input("Nhập hình (v: vuông, n: chữ nhật, t: tròn): ")
tinh_dien_tich_chu_vi(hinh)
