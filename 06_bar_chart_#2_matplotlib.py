# ******************************bar chart part 2 in matplotlib*********************

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# # //////starting the values
# classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
# np.random.seed(100)
# class1=np.random.randint(10,30,(5))
# class2=np.random.randint(10,30,(5))
# class3=np.random.randint(15,30,(5))
# # /////=if we want to max or min the  graph then we use figer function 
# # plt.figure(figsize=(13,13))
# # /////creating background color
# style.use('ggplot')
# # plt.grid(color='y')



# class_index=np.arange(len(classes))
# # class_index=classes
# width=0.2
# plt.bar(class_index,class1,width, color='g',label='Class 1 Students')
# plt.bar(class_index+width,class2,width,color='b',label='Class 2 Students')
# plt.bar(class_index+(2*width),class3,width,color='orange',label='Class 3 Students')
# # /////if we want to converd the index+width to classes than we use xticks fucntion
# # /////and the classes name rotated how mush angles
# plt.xticks(class_index+width,classes,rotation=20)
# # /////when we want to creat title and x lable and y label
# plt.title("Class 1 Student",fontsize=20)
# plt.xlabel("Classes", fontsize=15)
# plt.ylabel("Students",fontsize=15)
plt.legend(loc=3)

# plt.show()




# ******if we want to plot the graph in horizontal than we use just convert to x axis funcxtion names to y-axis function names and paramethers


classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
# /////if we want to max or min the  graph then we use figer function 
# plt.figure(figsize=(13,13))
# /////creating background color
style.use('ggplot')
# plt.grid(color='y')



class_index=np.arange(len(classes))
# class_index=classes
width=0.2
plt.barh(class_index,class1,width, color='g',label='Class 1 Students')
plt.barh(class_index+width,class2,width,color='b',label='Class 2 Students')
plt.barh(class_index+(2*width),class3,width,color='orange',label='Class 3 Students')
# /////if we want to converd the index+width to classes than we use xticks fucntion
# /////and the classes name rotated how mush angles
plt.yticks(class_index+width,classes,rotation=20)
# /////when we want to creat title and x lable and y label
plt.title("Class 1 Student",fontsize=20)
plt.ylabel("Classes", fontsize=15)
plt.xlabel("Students",fontsize=15)
plt.legend(loc=4)


plt.show()
