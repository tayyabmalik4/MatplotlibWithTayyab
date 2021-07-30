# (09)*********************************Pie Chart part 2 *******************************

import matplotlib.pyplot as plt

# /////creating the data for appling it
# classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
# class1_students=[40,27,34,30,37]

# explode=[0,0,0.2,0,0.1]
# colors=['c','b','r','y','g']
# textprops={"fontsize":15}
#  /////pctdistance function is use the percentage of the distance about graphs
# /////if we want to wish the graph plotting in x and y shaps than we use frame=True function  
# plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops,pctdistance=0.6,frame=True,counterclock=True)
# /////if we want to show the all values in labels than we use legend function
# plt.legend(loc=2)
# plt.show()

plt.figure(figsize=(8,5))
# ///////Creating different shape of pie chart

plt.pie([1],colors='b',radius=1.9)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=1.7)
plt.pie([1],colors='y',radius=1.5)
plt.pie([1],colors='c',radius=1.4)
plt.pie([1],colors='b',radius=1.2)
plt.pie([1],colors='g',radius=1.1)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=0.5)
plt.pie([1],colors='k',radius=0.2)
plt.show()