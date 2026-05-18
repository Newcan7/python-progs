import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1, 100, 20)
b = np.random.randint(1, 100, 20)
# Create a third variable to map colors to the 'autumn' scale
colors = np.linspace(0, 100, 20) 

plt.scatter(a, b, c=colors, marker="^", alpha=0.6, cmap="autumn")
plt.colorbar(label='Scale') # Now the colorbar shows the intensity
plt.grid(ls="--")
plt.show()
 