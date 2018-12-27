# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:32:06 2018

@author: goodboyycb
"""
score=float(input("请输入分数："))## 输入的input函数，取整
##score=int(input("请输入分数："))# 如果输入的是小数，则int就会报错
## 原来input函数输入的是字符串，浮点数类型的字符串是不能用int转换为整型
if score>=90:
    grade="A"
elif score >=60:  ## 不满足>=90,但是满足>=60
    grade="B"
else:
    grade="C"
print("{} 属于 {}".format(score,grade))  ## 格式化输出的应用
    