import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 - np.exp(-x)

x = np.arange(-10,10,0.01)
y = f(x)

print(y)

plt.plot(x,y)
plt.show()

