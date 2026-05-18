import numpy as np
import matplotlib.pyplot as plt

a = np.sort(np.random.randint(1, 100, 20))
b = np.arange(1,21)

plt.plot(a,b,"--go")