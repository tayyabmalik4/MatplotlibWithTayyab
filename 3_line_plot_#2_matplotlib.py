# ******************line plot using matplotlib part 2****************

# ////import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib import style

# ////////////previos data 
# ////////////creating variables x and y 
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[33,34,35,36,37,37.6,41,39,41,36,39,45,35,45,39]
# -----2nd temoerature
l_temp=[34,35,36,37,38,36,39,36,40,41,43,42,45,44,43]

# ////start ploting
# plt.plot(days,temp)

# /////starting style function use
style.use('ggplot')
# /////when we want to chnage the backgroud style than we use grid function
plt.grid(color='b', linestyle='-',linewidth=2) 

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
# plt.plot(days,temp,'go--',linewidth=2,markersize=10)
plt.plot(days,temp,'go--',linewidth=2,markersize=10,label='Karachi Temperature')
plt.plot(days,l_temp,'ro:',linewidth=2,markersize=10,label='Lahore Temperature')

 
# //////When we want to change the fontsize of title and xy variables than we use fontsize function\
# /////linit of the axis
plt.axis([0,20,30,50])
# /////creating table
plt.title("Karachi Ands Temperature",fontsize=15)
# ////creating x and y names
plt.xlabel("Days",fontsize=15)
plt.ylabel("Temperature",fontsize=20)
# //////when we want to creat name of the line plot than we use legend function
# /////this is also use in the plot function using labal attribute 
# plt.legend("Tem Line")
# //////when we want to change the location of the name of line then we use loc in legend function
# plt.legend(["Tem Line"], loc=4)
plt.legend(loc=4)
# /////to showing the graph 
plt.show()