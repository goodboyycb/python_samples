# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:22:30 2018

@author: goodboyycb
"""

for i in range(1,10):
  #  print()
    for j in range (1,i+1): 
        print("%d*%d=%d"%(i,j,i*j),end=" ")
        ## python 默认情况是：换行的！换行的！  后面加end=“”，可以保证不黄航
       # print("%d*%d=%d"%(i,j,i*j)) 
    print("")
   # print("")## 该语句 表示换行的意思！