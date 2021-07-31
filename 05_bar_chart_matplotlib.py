# (5)*********************************Bar chart using matplotlib**********************
# ///////this is the use to creat the grasph using some arguments

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# //////starting the values
classes=['python','Machine Learning','Data Science','Robotics','Deep learning']
np.random.seed(100)
class1=np.random.randint(10,30,(5))
class2=np.random.randint(10,30,(5))
class3=np.random.randint(15,30,(5))
# plt.bar(classes,class1)

# /////when we want to plot the bar chart in horizontal than we use barh function
# plt.barh(classes,class1)

# //////these are the functions of the bar chart
# /////width is use to define the width along lines
# /////align is use to define the place
# ////color ios use to define the color
# ////edgecolor is use to define the edge color
# /////linewidth is use to define the wedth in the line
# /////alpha is use to minmize the opacity
# /////linestyle is use to style of the lines
# /////label is use to creat name of the chart 
# ////visible is use to define that the chart is visible or nor if visible False chart is not visible-----default(visible=True) 
plt.bar(classes,class1, width=0.5, align='edge', color='yellow',edgecolor='m',linewidth=5,alpha=0.5,linestyle='--',label='Class 1 Students',visible=True)
plt.legend(loc=2)

plt.show()