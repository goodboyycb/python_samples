# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:39:30 2018

@author: goodboyycb
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:29:24 2018

@author: goodboyycb
"""
##判断101-200之间有多少个素数，并输出所有素数。
n=0 
leap=1
for i in range(101,201):
    #n=0
   # print("~~~~~~~")
    for j in range(2,i):
        #print("i为：",i)
        #print("j为：",j)
        if i%j == 0:
            leap=0
            break
    if leap == 1:
        print (i)
        n+=1
    leap=1
print("total",n)
    



        
        