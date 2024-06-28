import matplotlib.pyplot as plt
import numpy as np

xpoints = []
ypoints = []
for x in range(8):
    xpoints.append(x)
    ypoints.append(x**2)
plt.plot(xpoints,ypoints)
plt.show()