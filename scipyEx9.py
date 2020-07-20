# scipy를 이용한 정규 분포 시뮬레이션
# norm클래스를 이용해서 정규분포 객체를 생성할 수 있다. 평균과 표준편차를 모수로 사용한다.
# pdf를 이용해서 밀도 함수를 계산할 수 있음.

import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 0
std = 1
rv = sp.stats.norm(mu, std)

xx = np.linspace(-5, 5, 100)
plt.plot(xx, rv.pdf(xx))
plt.ylabel("P(x)")
plt.grid(True)
plt.show()

np.random.seed(0)
x = rv.rvs(100)
print(x)

sns.distplot(x, kde=True, fit=sp.stats.norm)
plt.grid(True)
plt.show()

# 통계 분석 중의 하나인 정규분포검정(normality test)을 시각적으로 확인하는 플롯 : Q-Q플롯 

# Q-Q 플롯 사용 순서

# 1. 샘플 데이터를 크기순으로 정렬
# 2. 각 샘플 데이터의 분위함수(quantile function)값을 구한다.
# 3. 각 샘플 데이터의 분위수(quantile)를 구한다. 
# 4. 샘플 데이터와 그에 대응한 정규 분포 값을 하나의 쌍으로 생각하고 2차원 공간에 
#     점으로 그린다.
# 5. 모든 샘플에 대해 2~4까지의 과정을 반복하여 스캐터 플롯을 완성한다.

# scipy에서는 Q-Q플롯을 그리기위한 명령 probplot을 제공한다.

# probplot : 기본적으로 인수로 보낸 데이터 샘플에 대한 Q-Q플롯 정보만을 반환하고 실제로
# 차트를 그리지 않는다. 

# plot 인수를 사용해서 플롯을 그린다. plot인수에는 matplotlib.pyplot 모듈 객체를 값으로 한다.

# 정규 분포를 따르는 데이터 샘플을 Q-Q플롯으로 보여주기
np.random.seed(0)
x = np.random.randn(100)
plt.figure(figsize=(5, 5))
sp.stats.probplot(x, plot=plt)
plt.axis("equal")
plt.grid()
plt.show()

# 정규 분포를 따르지 않는 데이터 샘플을 Q-Q플롯으로 보여주기
np.random.seed(0)

#random.rand는 균일 분포
x = np.random.rand(100)
plt.figure(figsize=(5,5))
sp.stats.probplot(x, plot=plt)
plt.ylim(-0.5, 1.5)
plt.grid()
plt.show()














