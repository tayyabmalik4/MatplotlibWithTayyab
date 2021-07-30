# (11)********************************Saving figure**************************************
# ///////when we want to save the graph than we use savefig function 
# //////we also the save figure directly when figure is showing


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.pie([40,30,20],autopct="%0.1f%%")
# //////we must input the name of the file and if we want to save the figure in spacific directry than we also input the path
# //////if we don't input the file than default save in the current directry which we work now
# /////dpi(dot per inch) function is use to manage the resolution
#  //////quality means that the save figure quality
# //////facecolor means the background color of the figure
# plt.savefig('pie_chart', dpi=100,quality=99,facecolor='g',)
# plt.show()



# ////////previous data-------------------------------
plt.figure(figsize=(13,13))
# //////1st
plt.subplot(3,2,1)
classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
plt.bar(classes,class1, width=0.5, align='edge', color='yellow',edgecolor='m',linewidth=5,alpha=0.5,linestyle='--',label='Class 1 Students',visible=True)
plt.legend(loc=2)

# //////2nd
# /////by the use of projection function we creat the bydefault graph
# /////and by the use of facecolor use creat the color and change the color
plt.subplot(3,2,2, projection='polar',facecolor='k')

# /////3ed
plt.subplot(3,2,3)
df1=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore.csv',nrows=1000)
x=df1['Rating']
y1=df1['Installs']
plt.scatter(x,y1, c='g',marker='o', s=200,alpha=0.3,linewidths=10,edgecolors='y')

# /////4th
plt.subplot(3,2,4)
classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
class1_students=[40,27,34,30,37]
explode=[0,0,0.2,0,0.1]
colors=['c','b','r','y','g']
textprops={"fontsize":15}
plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops)

# ///////5th 
plt.subplot(3,2,5)
plt.pie([1],colors='b',radius=1.9)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=1.7)
plt.pie([1],colors='y',radius=1.5)
plt.pie([1],colors='c',radius=1.4)
plt.pie([1],colors='b',radius=1.2)
plt.pie([1],colors='g',radius=1.1)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=0.5)
plt.pie([1],colors='k',radius=0.2)


# //////6th
plt.subplot(3,2,6)
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[33,34,35,36,37,37.6,41,39,41,36,39,45,35,45,39]
plt.plot(days,temp,'go--',linewidth=2,markersize=10,label='Karachi Temperature')
plt.legend(loc=4)

# //////to saving the figure 
# plt.savefig('All figures are in one figure')
plt.show()
