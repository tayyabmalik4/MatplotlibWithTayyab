# (10)**************************Subplot in matplotlib*************************

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# /////this is the subplot function arguments first arg is rows, 2nd arg is colmns and 3rd arg is indexs
# plt.subplot(2,2,1)
# plt.pie([1])

# plt.subplot(2,2,2)
# plt.pie([1,2])

# plt.subplot(2,2,3) 
# plt.pie([1,2,3])

# plt.subplot(2,2,4)
# plt.pie([1,2,3,4])
# plt.show()

# ////if we want to 6 graphs than we creat the function as following
plt.figure(figsize=(13,13))

plt.subplot(3,2,1)
classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
plt.bar(classes,class1, width=0.5, align='edge', color='yellow',edgecolor='m',linewidth=5,alpha=0.5,linestyle='--',label='Class 1 Students',visible=True)
plt.legend(loc=2)

plt.subplot(3,2,2)
days =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tem=[36.6,37,37.7,39,40,36.8,43,44,45,45.5,40,44,34,47,46] 
plt.plot(days,tem)

plt.subplot(3,2,3)
df1=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore.csv',nrows=1000)
x=df1['Rating']
y1=df1['Installs']
plt.scatter(x,y1, c='g',marker='o', s=200,alpha=0.3,linewidths=10,edgecolors='y')

plt.subplot(3,2,4)
classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
class1_students=[40,27,34,30,37]
explode=[0,0,0.2,0,0.1]
colors=['c','b','r','y','g']
textprops={"fontsize":15}
plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops)


plt.subplot(3,2,5)
plt.pie([1],colors='b',radius=1.9)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=1.7)
plt.pie([1],colors='y',radius=1.5)
plt.pie([1],colors='c',radius=1.4)
plt.pie([1],colors='b',radius=1.2)
plt.pie([1],colors='g',radius=1.1)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=0.5)
plt.pie([1],colors='k',radius=0.2)


plt.subplot(3,2,6)
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[33,34,35,36,37,37.6,41,39,41,36,39,45,35,45,39]
plt.plot(days,temp,'go--',linewidth=2,markersize=10,label='Karachi Temperature')
plt.legend(loc=4)

plt.show()


# /////if we want to plot the 9 graphs than we use this function
# plt.subplot(331)
# plt.subplot(332)
# plt.subplot(333)
# plt.subplot(334)
# plt.subplot(335)
# plt.subplot(336)
# plt.subplot(337)
# plt.subplot(338)
# plt.subplot(339)
# plt.show()