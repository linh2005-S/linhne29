# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:28:13 2024

@author: linh
"""

time=input("nhập thời gian theo định dạng giờ/phút/giây: ")
gio, phut, giay=map(int, time.split("/"))
tong_giay= gio*3600+phut*60+giay
print("sau khi đổi thành giây là: ", tong_giay ,"giây")