import matplotlib.pyplot as plt
import matplotlib.axes._axes as axes
import numpy as np
import matplotlib.animation as animation

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
assert isinstance(ax, axes.Axes)
t = np.linspace(0, 3, 50_000)
point_numbers = range(rw.num_points)
scatter = ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                     edgecolors='none', s=15)
# Emphasize the first and last points
ax.scatter(0, 0, c='yellow', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
           s=100)

line = ax.plot(rw.x_values, rw.y_values)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
#plt.show()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = t[:frame]
    # update the scatter plot
    data = np.stack([x, y]).T
    scatter.set_offsets(data)
    # update the line plot

    return scatter, line


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
