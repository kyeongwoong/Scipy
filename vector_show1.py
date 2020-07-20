# 스칼라와 벡터의 곱
# 양수와 벡터를 곱하면 벡터의 방향은 변하지 않고 그 양수의 크기만큼 벡커의 크기가 커진다.
# 음수를 곱하면 벡터의 방향은 반대방향이 된다.

import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2])
b = 2 * a
c = -1 * a

plt.annotate(' ', xy=b, xytext=(0,0), arrowprops=dict(facecolor='red'))
plt.text(0.9, 3.2, "$2a$", fontdict={"size":15})
plt.text(2.2, 4.0, "$(2,4)$", fontdict={"size":15})

plt.annotate('', xy=a, xytext=(0,0), arrowprops=dict(facecolor='black'))
plt.text(0.2, 1.2, "$a$", fontdict={"size":15})
plt.text(1.2, 1.5, "$(1,2)$", fontdict={"size":15})

plt.annotate('', xy=c, xytext=(0,0), arrowprops=dict(facecolor='yellow'))
plt.plot(c[0], c[1], 'go', ms = 15)
plt.text(-1.2, -0.7, "$-a$", fontdict={"size":15})
plt.text(-3, -2.2, "$(-1,-2)$", fontdict={"size":15})

plt.plot(0, 0, 'ko', ms = 20)
plt.xticks(np.arange(-4, 6))
plt.yticks(np.arange(-4, 6))
plt.xlim(-4.5, 5.5)
plt.ylim(-3.5, 5.5)
plt.grid(True)
plt.show()

# 단위 벡터(unit vector) : 길이가 1인 벡터를 단위 벡터라고 한다.

a = np.array([1,0])
b = np.array([0,1])
c = np.array([1/np.sqrt(2), 1/np.sqrt(2)])

avalue = np.linalg.norm(a)
bvalue = np.linalg.norm(b)
cvalue = np.linalg.norm(c)

print(avalue)
print(bvalue)
print(cvalue)




