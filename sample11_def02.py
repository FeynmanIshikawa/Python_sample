import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.arange(0,10,0.01)
y = f(x)

print(y)

plt.plot(x,y)
plt.show()

