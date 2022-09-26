import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
np.random.seed(3)
x = [1,2,3,5,6,8,2,0,0,4,4,7,5,10]
y = [0,0,0,1,2,2,3,4,4,5,5,6,8,7]

# plot
fig, ax = plt.subplots()

ax.step(x, y, linewidth=2.5)

ax.set(xlim=(-10, 15), xticks=np.arange(-10, 15),
       ylim=(-10, 15), yticks=np.arange(-10, 15))

plt.show()