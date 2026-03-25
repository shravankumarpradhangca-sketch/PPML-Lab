import matplotlib.pyplot as plt
# plot a simple line graph

x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("simple line plot")
plt.plot(x,y,linestyle="--",color="r",marker="o",label="Dataline")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()