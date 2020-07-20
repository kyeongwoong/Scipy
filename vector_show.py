# Numpy를 이용한 벡터의 기하학적 의미

# 벡터를 N차원 공간상에서 표현을 할 때 점(point) 또는 화살표(arrow)로 표현할 수 있다.

# 차트상에서 주석 처리하는 함수: annotate(s, xy, xytext, xycoords, arrowprops)

# s: 주석, xy: 화살표시작, xytext: 주석 텍스트 시작

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line = plt.plot(t, s, lw = 2)

plt.annotate('max value', xy=(3,1), xytext=(4, 1.5), arrowprops=dict(facecolor='red')) 
plt.ylim(-2,2)
plt.show()

a = np.array([1,3])

plt.plot(0,0, 'yo', ms=20) # ms는 markersize
plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1,5))
plt.plot(a[0], a[1], 'ro', ms=20)

plt.annotate('',xy=a, xytext=(0,0), arrowprops=dict(facecolor='black'))
plt.text(0.1, 1.5, "$a$", fontdict={"size": 20})
plt.text(1.4, 3.1, "$(1,3)$", fontdict={"size":20})
plt.xlim(-2.5, 4.4)
plt.ylim(-0.6, 4.4)

plt.annotate('', xy=a + [-1, 1], xytext=(-1,1), arrowprops=dict(facecolor='black'))
plt.text(-0.9, 2.5, "$a$", fontdict={"size":20})

plt.grid(True)
plt.show()

#벡터의 길이
# 2차원 벡터 a의 길이는 피타고라스 정리를 이용하여 얻을 수 있는데, 그값을 벡터의 놈(norm)이라고 
# 한다. 수학 표기법은 ||a|| 이다. 

# numpy에서는 linalg 서브 패키지에 norm 함수를 이용해서 벡터의 길이를 알 수 있다.

a = np.array([1,3])
alength = np.linalg.norm(a)

print(alength)





