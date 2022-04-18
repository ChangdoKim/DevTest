import matplotlib.pyplot  as plt
import numpy as np

x_data = np.random.rand(100)
y_data = np.random.rand(100)

# plt.title('scatter plot')
# plt.grid()
# plt.scatter(x_data, y_data, color='b', marker='o')
# plt.show()

x_data = [x for x in range(-5, 5)]
y_data = [y*y for y in range(-5, 5)]

plt.title('line plot')
plt.grid()
plt.plot(x_data, y_data, color='b')
plt.show()