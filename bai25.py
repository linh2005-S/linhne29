# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:56:21 2024

@author: linh
"""
chu_cai = input("Nhập một chữ cái: ")
def doi_chu_cai(chu_cai):
  if chu_cai.islower():
    return chu_cai.upper()
  elif chu_cai.isupper():
    return chu_cai.lower()
  else:
    print("Không phải chữ cái")
print("Kết quả: ", doi_chu_cai(chu_cai))
