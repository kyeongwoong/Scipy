# 베르누이 분포
# 베루누이 시도(Bernoulli trial) : 결과가 성공 또는 실패 두가지 중 하나로만 나오는 것
# 동전을 던져서 앞이나 뒤가 나오는 경우 베루누이 시도라 한다.

# 베루누이 시도 결과를 확률 변수(random variable) X로 나타날 때는 일반적으로 성공은 1로,
# 실패는 0으로 정한다. X=1, X = 0 (가끔 실패를 -1로 정하는 경우도 있다. X = -1)

# 베르누이 확률 변수는 0, 1 두 가지 값 중의 하나만 가질 수 있으므로 이산 확률 변수이다.
# 1이 나올 확률을 의미하는 theta(모수)로 표현하며, 0 이 나올 확률은 1-0로 표현한다.


#Scipy를 이용한 베르누이 분포
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# scipy에서 베르누이 분포의 모수 설정을 p 인수로 사용한다.
theta = 0.6
rv = sp.stats.bernoulli(theta)

# pmf 메서드를 이용하면 확률 질량 메소드(pmf: probability mass function)를 계산할 수 있다.

xx = [0, 1]
plt.bar(xx, rv.pmf(xx))
plt.xlim(-1, 2)
plt.ylim(0,1)

plt.xticks([0,1], ["X=0", "X=1"])
plt.grid(True)
plt.show() 

# 베르누이 분포 시뮬레이션
# 시뮬레이션을 하기 위해서는 rvs메서드를 사용한다.

x = rv.rvs(100, random_state = 0)
print(x)

sns.countplot(x)
plt.grid(True)
plt.show()

y = np.bincount(x, minlength=2) /float(len(x))

df = pd.DataFrame({"theory": rv.pmf(xx), "simulation" : y})
df.index = [0, 1]
print(df)

df2 = df.stack().reset_index() # stack() : 열인덱스 -> 행 인덱스로 교환, unstack(): 행인덱스->열인덱스로
# reset_index() : 기존의 행 인덱스를 제거하고 선두 데이터 열로 추가
# set_index() : 기존의 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정

df2.columns = ["sample value", "type", "%"]
print(df2)

sns.barplot(x = "sample value", y="%", hue="type", data = df2)
plt.show()

# seaborn barplot메소드는 : 범주 내에 있는 통계를 추정
# 	 pointplot 








