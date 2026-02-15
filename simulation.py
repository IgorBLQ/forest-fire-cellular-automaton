import matplotlib.pyplot as plt
import matplotlib.animation as animation
from model import ForestFireModel
import numpy as np

model = ForestFireModel(size=100)

fig, ax = plt.subplots()

cmap = plt.matplotlib.colors.ListedColormap(
    ["white", "green", "red", "black"]
)

def update(frame):
    model.step()
    ax.clear()
    ax.imshow(model.grid, cmap=cmap, vmin=0, vmax=3)
    ax.set_title(f"Step {frame}")
    ax.set_xticks([])
    ax.set_yticks([])

ani = animation.FuncAnimation(fig, update, frames=150, interval=100)
plt.show()
