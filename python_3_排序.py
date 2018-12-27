# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:54:40 2018

@author: goodboyycb
"""

##排序排序
l=[]##这是一个 列表
print("说明：每次输入一个数，输入三次，从小到大进行排序")
for i in range(3): ##range(3),包含0,1,2
    x=int(input('integer:\n'))
    l.append(x) # 使用列表的 添加因素。对就是添加因素。
l.sort()
print (l)
