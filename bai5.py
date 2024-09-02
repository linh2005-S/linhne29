# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:26:09 2024

@author: linh
"""
time=input("nhập thời gian theo định dạng hh:mm:ss: ")
gio, phut, giay=map(int, time.split(":"))
tong_giay= gio*3600+phut*60+giay
print("tống số giây là: ", tong_giay ,"giây")