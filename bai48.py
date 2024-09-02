# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:03:31 2024

@author: linh
"""
def find_min_sum_solution(a, b, c, d):
  dp = [[float('inf')] * (d+1) for _ in range(d+1)]
  dp[0][0] = 0
  for x in range(1, d//a + 1):
    for y in range(1, (d - a*x)//b + 1):
      z = (d - a*x - b*y) // c
      if z > 0 and a*x + b*y + c*z == d:
        dp[x][y] = x + y + z
  min_sum = float('inf')
  min_x, min_y = None, None
  for x in range(d//a + 1):
    for y in range(d//b + 1):
      if dp[x][y] < min_sum:
        min_sum = dp[x][y]
        min_x = x
        min_y = y
  min_z = (d - a*min_x - b*min_y) // c
  return min_x, min_y, min_z
a, b, c, d = 2, 7, 9, 979
print("Bộ nghiệm có tổng nhỏ nhất:", find_min_sum_solution(a, b, c, d))
