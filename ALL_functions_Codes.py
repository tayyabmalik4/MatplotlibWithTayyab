# (1)*************matplotlib introduction******************
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
import matplotlib.image as mpimg
from matplotlib import colors
import random

# (2)*************line plot in matplotlib*************

days =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tem=[36.6,37,37.7,39,40,36.8,43,44,45,45.5,40,44,34,47,46] 
plt.plot(days,tem)
plt.axis([0,20,30,50])
plt.title("Kara Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()


# (3)******************line plot using matplotlib part 2****************

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[33,34,35,36,37,37.6,41,39,41,36,39,45,35,45,39]
# -----2nd temoerature
l_temp=[34,35,36,37,38,36,39,36,40,41,43,42,45,44,43]
style.use('ggplot')
plt.grid(color='b', linestyle='-',linewidth=2)
plt.plot(days,temp,color='r')
plt.plot(days,temp,color='g',marker='o')
plt.plot(days,temp,color='r',marker='o',linestyle='--')
plt.plot(days,temp,color='r',marker='o',linestyle='--',linewidth=2)
plt.plot(days,temp,color='r',marker='o',linestyle='--',linewidth=2,markersize=10)
plt.plot(days,temp,'go--',linewidth=2,markersize=10)
plt.plot(days,temp,'go--',linewidth=2,markersize=10,label='Karachi Temperature')
plt.plot(days,l_temp,'ro:',linewidth=2,markersize=10,label='Lahore Temperature')
plt.axis([0,20,30,50])
plt.title("Karachi Ands Temperature",fontsize=15)
plt.xlabel("Days",fontsize=15)
plt.ylabel("Temperature",fontsize=20)
plt.legend("Tem Line")
plt.legend(["Tem Line"], loc=4)
plt.legend(loc=4)
plt.show()



# (4)*************************************Histogram in matplotlib*****************************


np.random.seed(250)
ml_student_age=np.random.randint(20,50, (100))
py_student_age=np.random.randint(10,40, (100))
print(ml_student_age)
print(py_student_age)
# plt.hist(ml_student_age)
bins=[10,15,20,25,30,35,40,45,50]
plt.figure(figsize=(16,9))
style.use('ggplot')
plt.grid(color='k')
plt.hist(ml_student_age,bins)
plt.hist(ml_student_age,bins,rwidth=0.8) 
plt.hist(ml_student_age, bins, rwidth=0.8, histtype='step')
plt.hist(ml_student_age,bins, rwidth=0.8, orientation='horizontal')
plt.hist(ml_student_age,bins,rwidth=0.8, orientation='vertical', color='red')
plt.hist(ml_student_age,bins,rwidth=0.8, orientation='vertical', color='red',label='ML Students',align='right',stacked=True)
plt.hist(py_student_age,bins,rwidth=0.5, orientation='horizontal', color='black',label='py Student Age')
plt.hist([ml_student_age,py_student_age], bins, rwidth=0.8,orientation='vertical', color=['r','y'],label=['ML Students', 'PY students'])
plt.legend(loc=1)
plt.title("Machine Learning Student age in histogram")
plt.xlabel('Student age category')
plt.ylabel('No. of Students Age')
plt.show()


# (5)*********************************Bar chart using matplotlib**********************

classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
plt.bar(classes,class1)
plt.barh(classes,class1)
plt.bar(classes,class1, width=0.5, align='edge', color='yellow',edgecolor='m',linewidth=5,alpha=0.5,linestyle='--',label='Class 1 Students',visible=True)
plt.legend(loc=2)
plt.show()


# (6)******************************bar chart part 2 in matplotlib*********************

classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
plt.figure(figsize=(13,13))
style.use('ggplot')
plt.grid(color='y')
class_index=np.arange(len(classes))
class_index=classes
width=0.2
plt.bar(class_index,class1,width, color='g',label='Class 1 Students')
plt.bar(class_index+width,class2,width,color='b',label='Class 2 Students')
plt.bar(class_index+(2*width),class3,width,color='orange',label='Class 3 Students')
plt.xticks(class_index+width,classes,rotation=20)
plt.title("Class 1 Student",fontsize=20)
plt.xlabel("Classes", fontsize=15)
plt.ylabel("Students",fontsize=15)
plt.legend(loc=3)
plt.show()


# (7)***********************Scatter Plot in Matplotlib*********************************


df=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore_user_reviews.csv')
df1=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore.csv',nrows=1000)
df1.shape
print(df1)
plt.figure(figsize=(13,13))
x=df1['Rating']
y=df1['Reviews']
y1=df1['Installs']
plt.scatter(x,y, c='r',marker='*', s=200,alpha=0.7,linewidths=10,edgecolors='b')
plt.scatter(x,y1, c='g',marker='o', s=200,alpha=0.3,linewidths=10,edgecolors='y')
plt.title("PLAY STORE DATA")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.ylabel("Reviews And Installs")
plt.show()


# (08)***************************Pie_chart_Matplotlib***********************************

classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
class1_students=[40,27,34,30,37]
explode=[0,0,0.2,0,0.1]
colors=['c','b','r','y','g']
textprops={"fontsize":15}
plt.pie([1])
plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops)
plt.show()


# (09)*********************************Pie Chart part 2 *******************************

classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
class1_students=[40,27,34,30,37]
explode=[0,0,0.2,0,0.1]
colors=['c','b','r','y','g']
textprops={"fontsize":15}
plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops,pctdistance=0.6,frame=True,counterclock=True)
plt.legend(loc=2)
plt.show()
plt.figure(figsize=(8,5))
plt.pie([1],colors='b',radius=1.9)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=1.7)
plt.pie([1],colors='y',radius=1.5)
plt.pie([1],colors='c',radius=1.4)
plt.pie([1],colors='b',radius=1.2)
plt.pie([1],colors='g',radius=1.1)
plt.pie([1,1,1,1,1,1,1,1],colors=['r','w','r','w','r','w','r','w'],radius=0.5)
plt.pie([1],colors='k',radius=0.2)
plt.show()


# (10)**************************Subplot in matplotlib*************************

plt.subplot(2,2,1)
plt.pie([1])

plt.subplot(2,2,2)
plt.pie([1,2])

plt.subplot(2,2,3) 
plt.pie([1,2,3])

plt.subplot(2,2,4)
plt.pie([1,2,3,4])
plt.show()

plt.subplot(331)
plt.subplot(332)
plt.subplot(333)
plt.subplot(334)
plt.subplot(335)
plt.subplot(336)
plt.subplot(337)
plt.subplot(338)
plt.subplot(339)
plt.show()


# (11)********************************Saving figure**************************************

plt.pie([40,30,20],autopct="%0.1f%%")
plt.savefig('pie_chart', dpi=100,quality=99,facecolor='g',)
plt.show()
plt.figure(figsize=(13,13))

plt.subplot(3,2,1)
classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
plt.bar(classes,class1, width=0.5, align='edge', color='yellow',edgecolor='m',linewidth=5,alpha=0.5,linestyle='--',label='Class 1 Students',visible=True)
plt.legend(loc=2)\

plt.subplot(3,2,2, projection='polar',facecolor='k')

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

plt.savefig('All figures are in one figure')
plt.show()


# (12)*********************Show Image And colorbar in matplotlib********

img=mpimg.imread('11.2_Figure_2.png')
img1=mpimg.imread('11.1_Figure_1.png')
print(img)
print(type(img))
print(img.shape)
print(img.ndim)
plt.figure(figsize=(13,13))
plt.axis('off')
""""'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 
'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 
'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'"""
arr2d=img1[:,:,2]
plt.imshow(arr2d,cmap='hot')
plt.colorbar()
plt.figure(figsize=(13,13))
img2=mpimg.imread('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\images\\tayyab chaye.jpg')
plt.axis('off')
plt.imshow(img2)
plt.colorbar()
plt.show()


# (13)*******************Show Image part 2 and color bar in matploltlib******************

img3=mpimg.imread('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\images\\tayyab chaye.jpg')
plt.figure(figsize=(13,13))
plt.axis('off')
single_channal_img=img3[:,:,1]
plt.imshow(img3,cmap='hot')
plt.imshow(single_channal_img,cmap='nipy_spectral')
plt.colorbar()
cmap="""'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 
'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 
'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'"""
split_elements=cmap.split(' , ')
print(split_elements)
save_image_list=[]
split_elements=[]
for i in range(len(split_elements)):
    cmap_str=split_elements[i]
    plt.figure(figsize=(13,13))
    plt.axis('off')
    single_channal_img=img3[:,:,1]
    plt.imshow(single_channal_img,cmap=cmap_str)
    plt.colorbar()
    save_image_list.append('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\images\\converting images\\'+'new_'+split_elements[i]+'.jpg')
    print(split_elements[i])

    plt.savefig('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\images\\converting images\\new.png')
    plt.show()
plt.savefig('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\images\\converting images\\new.png')
plt.show()






