# ***********************Scatter Plot in Matplotlib*********************************

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ////using pandas as work import files as a csv
# df=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore_user_reviews.csv')
df1=pd.read_csv('F:\\tayyab programming\\machine learning\\Matplotlib\\matplotlibWithTayyab\\datasets\\archive\\googleplaystore.csv',nrows=1000)
# df1.shape
# print(df1)

# /////when we want to max or min the figure than we use figure function
plt.figure(figsize=(13,13))
# ////we want to plot the graph in scatter mood and we just 1000 rows of csv file we creat x and y variables x belongs to rating and y belongs to Reviews
x=df1['Rating']
y=df1['Reviews']
y1=df1['Installs']
# /////starting the scatter plot using matplotlib 
# ////c refers to color
# ////marker meand the shapes of timples
# ////s means the size of the marker
# /////alpha is minmize the opacity
# /////linewidth refers to width of the marker
# /////edgecolor refers to color of the sides of the marker
# ///// marker and vertz are the same concepts 
plt.scatter(x,y, c='r',marker='*', s=200,alpha=0.7,linewidths=10,edgecolors='b')
# /////if we want to graph more than one data than we use also these functions like this
plt.scatter(x,y1, c='g',marker='o', s=200,alpha=0.3,linewidths=10,edgecolors='y')

# ////creating title and x and y names
plt.title("PLAY STORE DATA")
plt.xlabel("Rating")
# plt.ylabel("Reviews")
plt.ylabel("Reviews And Installs")
plt.show()

