# 벡터의 차

import numpy as np
import matplotlib.pylab as plt

a = np.array([1,2])
b = np.array([2,1])
c = a - b

plt.annotate('', xy = a, xytext=(0,0), arrowprops=dict(facecolor='blue'))
plt.annotate('', xy =b, xytext=(0,0), arrowprops=dict(facecolor='blue'))
plt.annotate('',xy=a, xytext=b, arrowprops=dict(facecolor='red'))

plt.plot(0,0, 'go', ms=10)
plt.plot(a[0], a[1], 'go', ms=10)
plt.plot(b[0], b[1], 'go', ms=10)

plt.text(0.4, 1.2, "$a$", fontdict={"size":15})
plt.text(1.2, 0.3, "$b$", fontdict={"size":15})
plt.text(1.6, 1.7, "$a-b$", fontdict={"size":15})

plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1,4))

plt.xlim(-0.5, 2.6)
plt.ylim(-0.5, 2.6)
plt.grid(True)
plt.show()

# Word2Vec : 

a = np.array([3,4])
b = np.array([4, 3])
c = a + b

plt.annotate('', xy=a, xytext=(2,2), arrowprops=dict(facecolor='blue', ls="dashed"))
plt.annotate('', xy=(5,5), xytext=b, arrowprops=dict(facecolor='blue', ls="dashed"))

plt.plot(0,0, 'go', ms=15)
plt.plot(2,2, 'ro', ms=10)
plt.plot(a[0], a[1],  'ro', ms=10)
plt.plot(b[0], b[1], 'ro', ms=10)
plt.plot(c[0], c[1], 'ro', ms=10)

plt.text(1.5, 1.5, "$B$", fontdict={"size":15})
plt.text(2.6, 4.2, "$A$", fontdict={"size":15})
plt.text(4, 2.5, "$C$", fontdict={"size":15})
plt.text(4.8, 5.2, "$D$", fontdict={"size":15})

plt.xticks(np.arange(-2, 7))
plt.yticks(np.arange(-1, 6))
plt.xlim(-1.5, 6.5)
plt.ylim(-0.5, 5.7)
plt.grid(True)
plt.show()









