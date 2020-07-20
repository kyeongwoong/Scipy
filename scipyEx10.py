# Scipy를 이용한 t 분포 알아보기

# scipy에서는 t명령을 이용하여 t분포 객체를 생성한다.
# 사용되는 인수는 표준편차, 기댓값, 자유도

# 자유도(degree of freedom)가 클수록 정규분포에 수렴한다.

import numpy as np
import matplotlib.pylab as plt
import scipy as sp
from scipy import stats

xx = np.linspace(-4, 4, 100)

for df in [ 1, 3, 5, 10, 20 ]:
	rv = sp.stats.t(df = df)
	plt.plot(xx, rv.pdf(xx), label = ("student-t (dof = %d)" % df))

plt.plot(xx, sp.stats.norm().pdf(xx), label = "Normal", lw=4, alpha = 0.5)
plt.legend()
plt.grid()
plt.show()







