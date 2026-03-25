from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# Initialize the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data points
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]

# Creating the scatter plot
ax.scatter(x, y, z, color='r', label='3D Points')

# Setting labels and title
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Display legend and plot
plt.legend()
plt.show()
# Initialize the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data points
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]

# Creating the scatter plot
ax.scatter(x, y, z, color='r', label='3D Points')

# Setting labels and title
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Display legend and plot
plt.legend()
plt.show()