# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:34:09 2024

@author: linh
"""
quang_duong = float(input("Nhập quãng đường di chuyển (km): "))
def tinh_tien_taxi(quang_duong):
  tong_tien = 0
  if quang_duong <= 0:
    return "Quãng đường không hợp lệ."
  tong_tien += 15000
  if quang_duong > 1:
    tong_tien += 13500 * min(quang_duong - 1, 4)
  if quang_duong > 5:
    tong_tien += 11000 * (quang_duong - 5)
  if quang_duong > 120:
    tong_tien *= 0.9
  return tong_tien
print("Tiền cước taxi:", tinh_tien_taxi(quang_duong), "đồng")
