# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:34:55 2018

@author: goodboyycb
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2018个税计算方法
i=float(input('税前收入：'))
arr=[80000,55000,35000,25000,12000,3000,0]

rat=[0.45,0.35,0.3,0.25,0.2,0.1,0.03]
r=0
t=0
m=i-5000## mmoney 应该纳税的部分
for idx in range(0,7):##按照最复杂的来，比如应应该缴税81000元
    if m>arr[idx]:
        r=(m-arr[idx])*rat[idx]
        t=t+r
        m=arr[idx]##这一步简直不能更精彩啊， 把80000作为新的收入标准

print(t)