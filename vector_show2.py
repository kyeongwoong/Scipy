# 벡터의 합 : 두벡터를 이웃하는 변으로 가지는 평행사변형의 다른 쪽 모서리가
# 두벡터를 합한 벡터의 위치이다.

import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2])
b = np.array([2,1])
c = a + b # a벡터와 b벡터를 합한 c도 역시 벡터가 된다.

plt.annotate('', xy=a, xytext=(0,0), arrowprops=dict(facecolor='black'))
plt.annotate('', xy=b, xytext=(0,0), arrowprops=dict(facecolor='black'))
plt.annotate('', xy=c, xytext=(0,0), arrowprops=dict(facecolor='red'))

plt.plot(0,0, 'bo', ms=15)
plt.plot(a[0], a[1], 'bo', ms = 15)
plt.plot(b[0], b[1], 'bo', ms = 15)
plt.plot(c[0], c[1], 'bo', ms = 15)

plt.plot([a[0], c[0]], [a[1], c[1]], 'r--') 
plt.plot([b[0], c[0]], [b[1], c[1]], 'r--')

plt.text(0.4, 1.2, "$a$", fontdict={"size":15})
plt.text(1.2, 0.2, "$b$", fontdict={"size":15})
plt.text(1.4, 1.6, "$c$", fontdict={"size":15})

plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.5, 4.5)
plt.ylim(-0.5, 3.7)
plt.grid(True)
plt.show()

# 기하학적인 또다른 벡터의 합 표현

plt.annotate('', xy=a, xytext=(0,0), arrowprops=dict(facecolor='blue'))
plt.annotate('', xy=c, xytext=a, arrowprops=dict(facecolor='blue'))
plt.annotate('', xy=c, xytext=(0,0), arrowprops = dict(facecolor='red'))

plt.plot(0,0, 'go', ms=10)
plt.plot(a[0], a[1], 'go', ms =10)
plt.plot(c[0], c[1], 'go', ms=10)

plt.text(0.4, 1.2, "$a$", fontdict={"size" : 15})
plt.text(1.4, 2.5, "$b$", fontdict={"size" : 15})
plt.text(1.3, 1.5, "$c$", fontdict={"size" : 15})

plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1,4))
plt.xlim(-1.4, 4.5)
plt.ylim(-0.5, 3.7)
plt.grid(True)
plt.show()

plt.annotate('', xy=b, xytext=(0,0), arrowprops=dict(facecolor='blue'))
plt.annotate('', xy=c, xytext=b, arrowprops=dict(facecolor='blue'))
plt.annotate('', xy=c, xytext=(0,0), arrowprops=dict(facecolor='red'))

plt.plot(0,0, 'go', ms=10)
plt.plot(b[0], b[1], 'go', ms=10)
plt.plot(c[0], c[1], 'go', ms=10)

plt.text(1.2, 0.3, "$b$", fontdict={"size": 15})
plt.text(2.5, 1.5, "$a$", fontdict = {"size" : 15})
plt.text(1.3, 1.4, "$c$", fontdict={"size" : 15})

plt.xticks(np.arange(-2,5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.4, 4.5)
plt.ylim(-0.5, 3.7)
plt.grid(True)
plt.show()






