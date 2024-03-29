import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Linear y=mx
# x = [1,2,3,4]

# ============
# Bar Plot
# ==============


# y = [98, 67, 88, 95, 88]
# x = ["Part1", "Part2", "Part3", "Part4", "Part5"]
#
# plt.bar(x, y, color="Red", edgecolor="Black")
#
# plt.xlabel("Parts of Harry Potter")
# plt.ylabel("Popularity")
# plt.title("Popularity comparison of Harry Potter series", fontsize=15)
#
# plt.show()

# data_emp = pd.read_excel("D:/Python excel/Emp.xlsx")
# df = pd.DataFrame(data_emp)
# # print(df)
#
# grp = df.groupby("AGE")["SALARY"].sum()
# # print(grp)
# plt.bar(grp.index,grp.values)
# plt.title("Age vs Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()


# ==============
# Line Plot
# ==============

# x = ["day1", "day2", "day3", "day4", "day5"]
# y = [300, 420, 280, 310, 360]
# y2 = [280, 370, 310, 400, 350]
#
# plt.plot(x, y, marker="^", ls="--", color="red", label="Week1")
# plt.plot(x, y2, marker="^", ls="--", color="green", label="Week2")
#
# plt.legend()
#
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Changing font style and size
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.title("Sports Watch Data", fontdict = font1, loc = "left")
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)
#
# plt.plot(x, y)
# plt.show()


# ===Grid Lines====

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burn")
#
# plt.plot(x, y)
#
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
#
# plt.show()


# =====Subplot========
# plt.subplot(1, 2, 1)
# #the figure has 1 row, 2 columns, and this plot is the first plot.
#
# plt.subplot(1, 2, 2)
# the figure has 1 row, 2 columns, and this plot is the second plot.

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 1)
# plt.plot(x, y)
# plt.title("Sales")
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 2)
# plt.plot(x, y)
# plt.title("Expenditure")
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 3)
# plt.plot(x, y)
# plt.title("Profit")
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 4)
# plt.plot(x, y)
# plt.title("Gross Margin")
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 5)
# plt.plot(x, y)
# plt.title("Fiscal Deficit")
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 6)
# plt.plot(x, y)
# plt.title("Growth rate")
#
# plt.suptitle("Annual Report")
# plt.show()

# =====Scatter Plot======

# # day one, the age and speed of 13 cars:
# x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
# y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# plt.scatter(x, y, label = "Day1")
# plt.xlabel("Age")
# plt.ylabel("Speed")
#
# # day two, the age and speed of 15 cars:
# x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
# y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
# plt.scatter(x, y, label = "Day2")
# plt.legend()
#
# plt.show()

# Manual assignment of colors

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
#
# plt.scatter(x, y, c=colors)
#
# plt.show()

# Include Color Map

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
#
# plt.scatter(x, y, c=colors, cmap='viridis')
#
# plt.colorbar()
#
# plt.show()

# Scatter sizes

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#
# plt.scatter(x, y, s=sizes)
#
# plt.show()

# Transparency(Alpha argument)

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#
# plt.scatter(x, y, s=sizes, alpha=0.5)
#
# plt.show()

# Color+Size+Transparency

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
#
# plt.colorbar()
#
# plt.show()

# ====Pie Charts=======

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
# plt.pie(y, labels = mylabels)
# plt.show()

# Staret angle

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show()

# Explode(Stand out edge)

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
#
# # mycolors = ["black", "hotpink", "b", "#4CAF50"]
#
# plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
# # plt.pie(y, labels = mylabels, colors = mycolors)  #manual color
#
# plt.legend( title = "Four Fruits")
# plt.show()


# =====Histogram=======

# Generate random data for the histogram
data = np.random.randn(1000)

# Plotting a basic histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Display the plot
plt.show()
