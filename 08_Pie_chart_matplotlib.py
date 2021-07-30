# (08)***************************Pie_chart_Matplotlib***********************************
# //////information is converted to circle and also converted to percentages


import matplotlib.pyplot as plt

# /////starting to creat the data which we use to convert pie chart
classes=['python','Robotics','Machine Learning', 'Data Science', 'Deep Learning']
class1_students=[40,27,34,30,37]
explode=[0,0,0.2,0,0.1]
colors=['c','b','r','y','g']
textprops={"fontsize":15}
# ////single value of pie
# plt.pie([1])
# /////for creating the name use labels
# /////for slicing the graph we use explode
# /////colors function is use to ploting the colors we we wish
# /////to showing the percentage we use autopct function
# /////if we want to show the shadows of the graph than we use shadow=True function
# //////if we want to maximiz or minimize the figure og the graph than we use radius function 
# /////if we want to rotate the graph than we use startgraph function
# /////if we want to change the text style than we use testprops function
plt.pie(class1_students,labels=classes, explode=explode,colors=colors,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=360,textprops=textprops)
plt.show()