# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 09:53:35 2018

@author: goodboyycb
"""

n=45# n由质数相乘的形式表示
leap=1
x=1
print ('{} = '.format(n),end="")
while x==1:
    for i in range(2,n+1):# 判断i是否为质数
        for j in range(2,i):
            if i%j == 0:A
                leap =0
               
        if leap==1:  ## 说明i为质数
            if n%i==0:  ## 说明n能够被i整除，比如45除以3,15*3， 新的n等于15，此时i=3
                n=n/i ## 15作为新的n 
                n=int(n)  ## 因为有了除法，所以说n得取整，变成了15.0
                if n==1:  ## 如果n等1，说明是3/3，或者5/5这种情况了，无法再分解了。
                   x=0   ## 控制while循环的
                   print(i) ## 这是结果最后输出的质数或素数！
                else:   ## 就是n=15的时候
                    x=1 ## 这时候x=1,然后重复循环的条件 x==1, 这样i(2,16),i从头开始的
                    print ('{} *'.format(i),end="") #此时i=3
                    break
        leap=1

