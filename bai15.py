# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:33:57 2024

@author: linh
"""

a=float(input("nhập a: "))
b=float(input("nhập b: "))
X = (a+b/(a**3+b**3)-(a*b)**3)/(a**3-b**3)**2
print("kết quả: ",X)