import math
import os
import random
import datetime
from datetime import time
from datetime import date
from datetime import datetime
'''
#lambda 函数

#常用标准库:
#math 模块：
a=math.ceil(3.6)#向上取整
b=math.floor(3.6)#向下取整
math.pi
math.e
math.degrees(3.14)#弧度到角度
math.radians(180)#角度到弧度

#os模块：
os.getcwd()#获取当前地址
os.chdir()#改变文档目录

#random模块：
L=['a','b','c','d']
random.choice(L)#从列表元素中随机选择（L为非空序列即可）
random.randint(1,100)#整数
random.randrange(0,20,2)#始终步长
random.random()#0到1
random.uniform(1,100)#浮点数
random.sample(range(100),10)#从给定样本中选n个数
random.shuffle(L)#打乱顺序

#datetime模块：
tm=time(23,20,35)
print(tm)'''
dt=datetime.now()
#print(dt.strftime('????'))
ts=dt.timestamp()#时间戳：1970.1.1到现在的时间，时间戳在全球是一样的
print(dt)
print(ts)
print(datetime.fromtimestamp(ts))#将时间戳转化为人能看懂的时间
#新纪元时间1970-1-1 08:00:00
print(datetime.fromtimestamp(0))