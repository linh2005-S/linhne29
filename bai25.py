# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:56:21 2024

@author: linh
"""
chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    print("Ký tự chữ hoa:", chu_cai.upper())
else:
    print("Ký tự chữ thường:", chu_cai.lower())