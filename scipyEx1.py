import numpy as np
import matplotlib.pylab as plt

def f(x):
	return (x - 2)**2 + 2

x1 = np.linspace(-1, 6, 100)

plt.plot(x1, f(x1))
plt.plot(2,2, 'ro', ms=10)
plt.ylim(0, 10)
plt.grid(True)
plt.show()