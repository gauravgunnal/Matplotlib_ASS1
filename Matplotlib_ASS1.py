'''Q1'''
'''Matplotlib is a widely-used data visualization library in Python that allows you to create various types of 
static, animated, and interactive visualizations. It provides a flexible and comprehensive toolkit for creating 
high-quality plots, charts, and graphs, making it an essential tool for data analysis, scientific research, and 
other visual representation tasks.

Matplotlib's `pyplot` module is a collection of functions that provides a MATLAB-like interface for creating 
plots and visualizations. It simplifies the process of creating common types of plots by providing easy-to-use 
functions to customize plot appearance, labels, axes, and more.

Here are five types of plots that you can create using the `pyplot` module of Matplotlib:

1. **Line Plot**: A basic line plot is used to represent data points as connected line segments. It's commonly used to 
visualize trends over time or show the relationship between two variables.

2. **Bar Plot**: A bar plot displays categorical data using rectangular bars. It's useful for comparing values among 
different categories.

3. **Histogram**: A histogram represents the distribution of a continuous dataset by dividing it into intervals (bins) 
and showing the frequency or count of data points in each bin.

4. **Scatter Plot**: A scatter plot displays individual data points as dots, with one variable on the x-axis and another 
variable on the y-axis. It's often used to visualize the relationship between two continuous variables.

5. **Pie Chart**: A pie chart displays data as slices of a circular "pie," with each slice representing a portion of 
the whole. It's suitable for showing the composition of a categorical variable as a percentage of the whole.

These are just a few examples of the many types of plots you can create using Matplotlib's `pyplot` module. Matplotlib 
offers a wide range of customization options to tailor the appearance of your plots to your specific needs.'''

'''Q2'''
'''
A scatter plot is a type of data visualization that displays individual data points as dots on a two-dimensional coordinate system. It's particularly useful for showing the relationship between two continuous variables. In a scatter plot, each dot represents a single data point with its respective values on the x and y axes.'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

# Create a scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()

'''Q3'''
'''The subplot() function in Matplotlib is used to create multiple plots within the same figure. It's particularly useful when you want to display multiple plots side by side or in a grid layout. The function takes three integer arguments: the number of rows, the number of columns, and the index of the subplot you're currently creating.'''
import numpy as np
import matplotlib.pyplot as plt

# Data for line plots
x = np.array([0, 1, 2, 3, 4, 5])

# Data for different lines
y1 = np.array([0, 100, 200, 300, 400, 500])
y2 = np.array([50, 20, 40, 20, 60, 70])
y3 = np.array([10, 20, 30, 40, 50, 60])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Create a 2x2 grid of subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('Line Plot 1')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('Line Plot 2')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('Line Plot 3')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('Line Plot 4')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

'''Q4'''
'''A bar plot, also known as a bar chart or bar graph, is a type of data visualization that represents categorical data with rectangular bars. Each bar's length or height is proportional to the value it represents. Bar plots are commonly used to compare and visualize the relative values of different categories.

Bar plots are particularly useful for:

Comparing Data: They make it easy to compare values across different categories or groups.

Displaying Frequencies: Bar plots can show the frequency distribution of categorical data.

Visualizing Trends: They can highlight trends or changes in data over time or between groups.

Summarizing Data: Bar plots provide a concise visual summary of the data distribution.'''
import numpy as np
import matplotlib.pyplot as plt

company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Creating a vertical bar plot
plt.figure(figsize=(8, 5))  # Set figure size
plt.bar(company, profit, color='blue')
plt.title('Company Profits')
plt.xlabel('Company')
plt.ylabel('Profit ($)')
plt.show()

# Creating a horizontal bar plot
plt.figure(figsize=(8, 5))  # Set figure size
plt.barh(company, profit, color='green')
plt.title('Company Profits')
plt.xlabel('Profit ($)')
plt.ylabel('Company')
plt.show()

'''Q5'''
'''A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. It displays a summary of key statistical measures such as the median, quartiles, and potential outliers. The plot consists of a box that represents the interquartile range (IQR) of the data, along with "whiskers" that extend to indicate the range of the data outside the IQR.

Box plots are useful for:

Visualizing Data Distribution: Box plots provide a concise summary of the data's central tendency, spread, and potential outliers.

Comparing Distributions: They are effective for comparing distributions of different datasets or groups.

Identifying Outliers: Box plots can help identify potential outliers, which are data points that fall significantly outside the main distribution.

Showing Skewness: The skewness of the data (whether it's positively or negatively skewed) can be inferred from the box plot's asymmetry.'''

import numpy as np
import matplotlib.pyplot as plt

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

data = [box1, box2]

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['Box 1', 'Box 2'])
plt.title('Box Plot Example')
plt.ylabel('Values')
plt.show()
