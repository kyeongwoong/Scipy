# Scipy를 이용한 이항 분포 시뮬레이션

# Scipy의 서브 모듈 binom 클래스가 이항분포 클래스이다. n과 theta 인수를 사용하여 모수를 설정한다.

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

N = 10
theta = 0.6
rv = sp.stats.binom(N, theta)

xx = np.arange(N+1)
plt.bar(xx, rv.pmf(xx))
plt.ylabel("pmf(x)")
plt.grid(True)
plt.show()

# 시뮬레이션 (rvs메서드 사용)
np.random.seed(0)
x = rv.rvs(100)
print(x)

sns.set()
sns.set_style("darkgrid")
sns.countplot(x)

plt.show()

y = np.bincount(x, minlength=N+1)/float(len(x))
df = pd.DataFrame({"theory": rv.pmf(xx), "simulation": y}).stack()
df = df.reset_index()
df.columns = ["sample", "type", "%"]
df.pivot("sample", "type", "%")
print(df)

sns.barplot(x = "sample", y="%", hue="type", data = df)
plt.show()











