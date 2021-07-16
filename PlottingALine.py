# Author; MoneiBk

# Define the x-axis and corresponding y-axis values as lists.
# Plot them on canvas using .plot() function.
# Give a name to x-axis and y-axis using .xlabel() and .ylabel() functions.
# Give a title to your plot using .title() function.
# Finally, to view your plot, we use .show() function.

# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
