# *************line plot in matplotlib*************
# ///////to show the graphical line plot than we use line plot function in matplotlib

# ////import matplotlib
import matplotlib.pyplot as plt

days =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tem=[36.6,37,37.7,39,40,36.8,43,44,45,45.5,40,44,34,47,46] 

# //////start the ploting using matplotlib
plt.plot(days,tem)
# ////when we want to determine the axis lengh than we use axis function
# -----------plt.axis([xmin,xmax,ymin,ymax])
plt.axis([0,20,30,50])
# /////to creating the title
plt.title("Kara Temperature")
# ////showuing name of x-axis and y-axis
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
