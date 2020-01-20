import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
y = np.sin(np.pi * x)

plt.plot(x,y)

plt.plot(x, 1.4280275 * x)
