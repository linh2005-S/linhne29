# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:28:35 2024

@author: linh
"""
def tinh_chu_vi(chieu_dai, chieu_rong):
  return 2 * (chieu_dai + chieu_rong)
def tinh_dien_tich(chieu_dai, chieu_rong):
  return chieu_dai * chieu_rong
def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
  for _ in range(chieu_rong):
    print('*' * chieu_dai)
chieu_dai = int(input("nhập chiều dài: "))
chieu_rong = int(input("nhập chiều rộng: "))
chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)
print("Chu vi hình chữ nhật:", chu_vi)
print("Diện tích hình chữ nhật:", dien_tich)
print("Hình chữ nhật:")
ve_hinh_chu_nhat(chieu_dai, chieu_rong)
