# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(1,5):
    for j in range(1,5):
        for k in range (1,5):
            if (i!=j) and (i!=k) and (k!=j):
                print(i,j,k)
                print (i*100+j*10+k)