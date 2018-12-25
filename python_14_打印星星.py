# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:41:39 2018

@author: goodboyycb
"""
from sys import stdout
for i in range(1,5):
    #print(i)
    a=5-i
    b=2*i
    #####  分为两步：第一步 打印空格，第二步打印**
    
    for i in range(1,a):
        print(" ",end="")
    for i in range(1,b):
        print("*",end="")
    #for i in range(1,a):
     #
     
     print(" ",end="")
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()