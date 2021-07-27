# ******************line plot using matplotlib part 2****************

# ////import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt

# ////////////previos data 
# ////////////creating variables x and y 
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[33,34,35,36,37,37.6,41,39,41,36,39,45,35,45,39]

# ////start ploting
# plt.plot(days,temp)

# /////when we want to chnage the color as we wish than we color function
# plt.plot(days,temp,color='r')

# ////whne we want to creat doted or many other symbols to show the graph than we use marker function
# plt.plot(days,temp,color='g',marker='o')

# /////when we want to change the line shape than we use linestyle function used
# plt.plot(days,temp,color='r',marker='o',linestyle='--')

# /////when we want to change the linewidth than we use linewigh function
# plt.plot(days,temp,color='r',marker='o',linestyle='--',linewidth=2)

# /////when we want to chnage the marker size than we use markersize function
# plt.plot(days,temp,color='r',marker='o',linestyle='--',linewidth=2,markersize=10)

# /////when we want to code is short way than we creat shortway as following
plt.plot(days,temp,'go--',linewidth=2,markersize=10)

# //////When we want to change the fontsize of title and xy variables than we use fontsize function
plt.plot(days,temp, fontsize=10)
# /////linit of the axis
plt.axis([0,20,30,50])
# /////creating table
plt.title("Karachi Temperature")
# ////creating x and y names
plt.xlabel("Days")
plt.ylabel("Temperature")
# /////to showing the graph 
plt.show()