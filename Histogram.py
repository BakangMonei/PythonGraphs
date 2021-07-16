# Author; MoneiBk

# Here, we use plt.hist() function to plot a histogram.
# frequencies are passed as the ages list.
# Range could be set by defining a tuple containing min and max value.
# Next step is to “bin” the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. Here we have defined bins = 10. So, there are a total of 100/10 = 10 intervals

import matplotlib.pyplot as plt

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
		60,7,13,57,18,90,77,32,21,20,40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
		histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')

# function to show the plot
plt.show()
