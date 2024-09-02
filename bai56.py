# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:35:25 2024

@author: linh
"""
import math
def tinh(*args, hinh='vuong', tinh='cv'):
  if hinh == 'vuong':
    canh = args[0]
    if tinh == 'cv':
      return 4 * canh
    elif tinh == 'dt':
      return canh ** 2
  elif hinh == 'chu_nhat':
    chieu_dai, chieu_rong = args
    if tinh == 'cv':
      return 2 * (chieu_dai + chieu_rong)
    elif tinh == 'dt':
      return chieu_dai * chieu_rong
  elif hinh == 'tron':
    ban_kinh = args[0]
    if tinh == 'cv':
      return 2 * math.pi * ban_kinh
    elif tinh == 'dt':
      return math.pi * ban_kinh ** 2
  else:
    return "Hình không hợp lệ"
print(tinh(10, hinh='vuong', tinh='cv')) 
print(tinh(50, hinh='vuong', tinh='dt'))
print(tinh(18, hinh='tron', tinh='cv'))
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))