# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


d={'x':1,'y':2,'z':3}
print("1 print字典d为：",d)
print()
print("2 直接获取value值：{}".format("x",d['x']))
print()
print("3 直接打印values值：",d.values())
v=list(d.values()) ## 将字典的values变成列表的形式
print("将value值变成列表：",v)
print()


print("4 直接打印keys值：",d.keys())
k=list(d.keys())## 将字典的vkeys变成列表的形式
print("将key值变成列表：",k)

print()
print("5 由value 2在 'value列表'中的位置：",v.index(2))
print("key列表中 1位置的 值为：",k[v.index(2)])





print(d.items())


#print(d.keys().[0])

for i in range(1,4):
    for j in range(1,4):
        for m in range(1,4):
            if i!=j and i!=m and m!=j:
                if i!=1 and m!=1 and m!=3:
                    print(list(d.keys())[list(d.values()).index(i)])
                    print(list(d.keys())[list(d.values()).index(j)])
                    print(list(d.keys())[list(d.values()).index(m)])