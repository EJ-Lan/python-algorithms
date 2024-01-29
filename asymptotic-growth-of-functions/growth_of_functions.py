import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
n = np.linspace(1, 20.0, 100) # 100 points, evenly spaced

# y = points on the quadratic function
a = 1.
b = 1.
c = 1.
y = a*n*n +b*n + c

# y2 = points on the n*logn function
c2 = 20.
y2 = c2*n*np.log(n)

fig, ax = plt.subplots()
ax.plot(n, y, label='quadratic')
ax.plot(n, y2, label='n*logn')

ax.set(xlabel='n', ylabel='f(n)',
       title='Growth of Functions')
ax.grid()
ax.legend();  # Add a legend.
plt.show()