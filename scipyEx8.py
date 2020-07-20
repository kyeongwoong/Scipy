# Scipy를 이용한 다항 분포의 시뮬레이션

# seaborn의 2차원 복합데이터를 표현하는 플롯 소개
#	barplot
#	pointplot

# 	boxplot : 중앙값, 표준 편차 등 간략한 특성을 보여주며, 박스는 실수 값 분포에서 
#		1사분위수와 3사분위수를 의미한다. 박스내부에 있는 가로선은 중앙값을 의미
#		박스 외부의 세로선은 1.5 * IQR(Q3-Q1) 만큼 1사분위수보다 낮은 값과 
#		1.5 * IQR 만큼 3사분위수보다 높은 값의 구간을 기준으로 그구간의 내부에 있는
#		가장 큰값과 가장 작은 값을 이어준 선분
#		그 바깥에 있는 점은 아웃라이어(outlier)라고 한다.

#	violinplot : 세로 방향으로 커널 밀도 히스토그램을 표현하며, 좌우가 대칭이 되어 바이올린 
#		  모양으로 보여 진다.
#	stripplot : scatter plot처럼 모든 데이터를 점으로 표시한다. jitter = True 설정하면
#		 데이터가 겹치지 않도록 한다.
#	swarmplot : stripplot과 비슷한데, 데이터를 표시하는 점들이 겹치지 않도록 옆으로 이동됨.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
import pandas as pd

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data = tips)
plt.grid(True)
plt.show()

sns.violinplot(x = "day", y="total_bill", data = tips)
plt.grid(True)
plt.show()

np.random.seed(0)
sns.stripplot(x = "day", y="total_bill", data = tips, jitter=True)
plt.grid(True)
plt.show()

sns.swarmplot(x = "day", y="total_bill", data=tips)
plt.grid(True)
plt.show()

# 다차원 복합 데이터

sns.boxplot(x = "day", y="total_bill", hue="sex", data=tips)
plt.grid(True)
plt.show()

sns.violinplot(x="day", y="total_bill", hue="sex", data=tips)
plt.grid(True)
plt.show()

np.random.seed(0)
sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, jitter=True)
plt.grid(True)
plt.show()

sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
plt.grid(True)
plt.show()

sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
plt.grid(True)
plt.show()

sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, jitter=True, dodge=True)
plt.grid(True)
plt.show()


sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips, dodge=True)
plt.grid(True)
plt.show()

# scipy는 다항 분포를 위한 multinomial 클래스를 제공한다. 인수로는 시행 회수:N, theta

N = 30
theta = [0, 0, 0.1, 0.2, 0.3, 0.4]
rv = sp.stats.multinomial(N, theta)

np.random.seed(0)
X = rv.rvs(100)
X[:6]

print(X[:6])

plt.boxplot(X)
plt.grid(True)
plt.show()

df = pd.DataFrame(X).stack().reset_index()
df.columns = ["trial", "class", "binomial"]

sns.boxplot(x="class", y="binomial", data=df)
sns.stripplot(x="class", y="binomial", data=df, jitter=True, color=".2")
plt.grid(True)
plt.show()

#violinplot의 인수 inner={"box","point","stick",None, "quartile"}
sns.violinplot(x="class", y="binomial", data=df, inner=None)
sns.swarmplot(x="class", y="binomial", data=df, color=".2") 
plt.grid(True)
plt.show()





