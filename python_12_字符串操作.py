# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:39:53 2018

@author: goodboyycb
"""

#import string
s=input("请输入一个字符串：\n")
letter=0
space=0
digit=0
others=0
i=0
while i <len(s):
    
    c=s[i]  ## 是不是c就是一个 字符了。
    print("i为{}，s[i]为{}".format(i,s[i])) ## 格式化输出，我有点灵活了呢，哈哈！
    i+=1
    
print("char={},space={},digit={},others={}".format(letter,space,digit,others))

for c in s: ##(相当于在前面的基础上又进行了一遍啊！！) s 是一个字符串啊，啊啊啊。是一个列表吧。
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print("char1={},space1={},digit1={},others1={}".format(letter,space,digit,others))