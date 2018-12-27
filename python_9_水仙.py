# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 09:15:17 2018

@author: goodboyycb
"""
##所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。

for i in range(101,1000):
    a=int(i/100)#a为百位数字
    #print(a)
    b=int((i%100)/10) #b为十位上的数字
    c=i%10
   # print("a,b,c=",a,b,c)
    if a**3+b**3+c**3==i:
        print(i)
        

  