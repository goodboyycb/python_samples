# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:20:08 2018

@author: goodboyycb
"""

from datetime import datetime
import time 
#print(time.localtime(time.time()))
print("~~~~~~~~1 time模块如下：~~~~~~~~~~~~~~~~")
print("以秒为单位的时间显示：",time.time()) #time.time()为1970年1月1日 0时候，以秒为单位进行的显示,时间戳
localtime1=time.localtime()
##print(localtime)
print("当地时间为：",localtime1)

print ("格式化当地时间为：",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("~~~~~~~~~2 datetime模块如下：~~~~~~~~~~~~~~~~~~~~~~")

dt =datetime.now()  ##创建一个datetime类对象,系统当前的时间
## 对应于from datetime import datetime


print(dt)
## 
#today = datetime.date.today()


print("今日日期为：",dt.date())
print("今年年份为：",dt.year)
print("今月月份为：",dt.month)
print(dt.time())

#print(datetime.date.day().strftime('%Y/%m/%d'))
print ("格式化当地时间为：",datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print ("格式化当地时间为：",dt.strftime('%Y/%m/%d ')) ## 不一定有秒啊！！



print("~~~~~~~~~3 日历的功能如下：~~~~~~~~~~~~~~~~~~")
## 居然还有日历的功能，强大的Python啊
import calendar
year=dt.year
month=dt.month
 
print ("以下输出%d年%d月份的日历:" %( year, month))

cal = calendar.month(year, month)
#print ("以下输出2019年1月份的日历:")
print (cal)