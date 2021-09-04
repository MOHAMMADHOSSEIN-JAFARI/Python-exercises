# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:31:47 2021

@author: Jafari
"""
a = int(input())
b = a % 10
b = str(b)
c = a % 100
c = c // 10
c= str(c)
d = a // 100
d = str(d)
e = b + c + d
e= int(e)
f= 2 * e
print(f)



