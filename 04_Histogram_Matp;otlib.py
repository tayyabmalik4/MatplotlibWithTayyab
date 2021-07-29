# *************************************Histogram in matplotlib*****************************

import matplotlib.pyplot as plt
import numpy as np 
import random

np.random.seed(250)
ml_student_age=np.random.randint(20,50, (100))
py_student_age=np.random.randint(10,40, (100))
# print(ml_student_age)
# print(py_student_age)

# /////starting ploting the graph in histogram
# plt.hist(ml_student_age)

# /////if we want to change the graph category wise than we use bin function
bins=[10,15,20,25,30,35,40,45,50]
# plt.hist(ml_student_age,bins)

# /////When we want to seperate the lines of graphs than we use rwidth function
# plt.hist(ml_student_age,bins,rwidth=0.8) 

# ////when we want to style of the graph then we use histtypes and the default type is bar
# plt.hist(ml_student_age, bins, rwidth=0.8, histtype='step')

# /////when we want to change the graph means horizontal or vertical(bydefault)
# plt.hist(ml_student_age,bins, rwidth=0.8, orientation='horizontal')

# ////if we want to change the color of the graph lines than we use the color function
# plt.hist(ml_student_age,bins,rwidth=0.8, orientation='vertical', color='red')

# ////When we WANT to creat the name of the table than we use label function and also use the lagend function spacificly
plt.hist(ml_student_age,bins,rwidth=0.8, orientation='vertical', color='red',label='ML Students',align='right',stacked=True)
plt.hist(py_student_age,bins,rwidth=0.5, orientation='vertical', color='black',label='py Student Age')
plt.legend(loc=1)
# ////crating title of the graph
plt.title("Machine Learning Student age in histogram")
# /////creating the name of x and y axis
plt.xlabel('Student age category')
plt.ylabel('No. of Students Age')
plt.show()
