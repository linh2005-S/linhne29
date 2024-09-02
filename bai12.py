# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:33:07 2024

@author: linh
"""

import random

def random_0_100():
    return random.randint(0, 100)
def random_50_99():
  return random.randint(50, 99)
def random_am39_79():
  return random.randint(-39, 79)
def random_am79_am39():
  return random.randint(-79, -39)
print("Số ngẫu nhiên từ 0 đến 100: ", random_0_100())
print("Số ngẫu nhiên từ 50 đến 99: ", random_50_99())
print("Số ngẫu nhiên từ -39 đến 79: ", random_am39_79())
print("Số ngẫu nhiên từ -79 đến -39: ", random_am79_am39())