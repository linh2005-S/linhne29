# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:14:40 2024

@author: linh
"""
def classify_number(number):
  if number < 0 and number % 2 != 0:
    return -1
  elif number > 0 and number % 2 == 0:
    return 1
  else:
    return 0
