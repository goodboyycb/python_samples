# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 08:54:23 2018

@author: goodboyycb
"""

def fib(n):## n的取值为1,2,3,4是第几个数列，最小值为1
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b ## 原来还可以这样寸进行赋值，两个一起赋值
    return a
#print(fib(2))

for i in range(1,19):
    
    print(i,fib(i))
    ##print(fib(i))