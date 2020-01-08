import matplotlib.pyplot as plt
import numpy as np

x = list(range(0,256))
y = [v*v for v in x]

plt.plot(x,y)

plt.show()
