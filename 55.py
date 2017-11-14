import pandas as pd
from pandas import DataFrame
import numpy as np
import random
list_0=[[-1,1,-1,-1,-1],[1,-1,1,-1,-1],[1,-1,-1,1,-1],[-1,1,1,-1,1],[-1,-1,1,-1,1]]
list_1=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
list_01=[[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
a0=DataFrame(list_0).T
a1=DataFrame(list_1)
a01=DataFrame(list_01)
n=0
m=0
way=[]
while a0.items() !=a1.items():
    i=random.randint(0,4)
    j=random.randint(0,4)
    a0[i][j]=-a0[i][j]
    if (i,j) not in way:
        way.append((i,j))
        n+=1
        if i>0:
            a0[i-1][j]=-a0[i-1][j]
            if j>0:
                a0[i][j-1]=-a0[i][j-1]
            if j<4:
                a0[i][j+1]=-a0[i][j+1]
        if i<4:
            a0[i+1][j]=-a0[i+1][j]
    if n==25:
        way=[]
        n=0
        m+=1
    if m==10000:
        break
print(m)
print(n)
print(a0)
print(way)
