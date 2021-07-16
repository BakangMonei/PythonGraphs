# Author; MoneiBk

# Here, we plot a pie chart by using plt.pie() method.
# First of all, we define the labels using a list called activities.
# Then, portion of each label can be defined using another list called slices.
# Color for each label is defined using a list called colors.
# shadow = True will show a shadow beneath each label in pie-chart.
# startangle rotates the start of the pie chart by given degrees counterclockwise from the x-axis.
# explode is used to set the fraction of radius with which we offset each wedge.
# autopct is used to format the value of each label. Here, we have set it to show the

import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
		radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()
