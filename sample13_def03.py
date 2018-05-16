import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.cos(x)

x = np.arange(0,10,0.01)
y = f(x)

plt.plot(x,y)
plt.show()
