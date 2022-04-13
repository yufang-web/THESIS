import pandas as pd
import numpy as np
import matplotlib.patches as patches
import scipy.stats
data=pd.read_table('result1.xlsx',sep='\t',header=0)
data2=pd.read_table('result2.xlsx',sep='\t',header=0)
x=data['start']
query=data['pos']
x1=data2['start']
query2=data2['pos']
po0=[]
for data in x:
    j=[0,data]
    po0.append(j)
pok=[]
for data in query:
    j=[data,0]
    pok.append(j)
po1=[]
for data in x1:
    j=[0,data]
    po1.append(j)
    po0.append(j)
po2=[]
for data in query2:
    j=[data-1020,0]
    pok.append(j)
import matplotlib.pyplot as plt
plt.figure(dpi=150)
for i in range(len(po0)):
    plt.plot(po0[i], pok[i], label='sin',alpha=0.1)
plt.xlim(0,50000)
plt.ylim(-1000,1300)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')         # 将y轴刻度设在左边的坐标轴上
ax.spines['bottom'].set_position(('data', 0))   # 将两个坐标轴的位置设在数据点原点
ax.spines['left'].set_position(('data', 0))
plt.xlabel('globin gene')
plt.ylabel('HS flanking')
#rect5 = patches.Rectangle((44028,0),2453,100,fill=False, edgecolor = 'red',linewidth=1)
point1=[0 for data in x]
point2=[0 for data in x1]
plt.scatter(x,point1, c="purple",s=5)
plt.scatter(x1,point2 , c="purple",s=5)
plt.show()

###plt.annotate