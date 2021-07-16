# Author; MoneiBK

# Here, we use plt.scatter() function to plot a scatter plot.
# Like a line, we define x and corresponding y – axis values here as well.
# marker argument is used to set the character to use as marker. Its size can be defined using s parameter.

import matplotlib.pyplot as plt

# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]

# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green",
			marker= "*", s=30)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()
