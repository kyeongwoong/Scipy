﻿# 카테고리 분포

# 카테고리 분포는 1부터 K까지의 K개의 정수 값 중 하나가 나오는 확률 변수의 분포이다.
# 예를 들면, 주사위를 던져 나오는 수를 확률 변수라고 가정하면, 확률변수는 {1,2,3,4,5,6}값이 
# 나온다. 클래스의 수 K = 6인 카테고리 분포라고 한다.

# 카테고리 분포에서는 벡터 확률 변수로 사용한다.(다차원 벡터 형태)

#	x = 1 ---> x = (1, 0, 0, 0, 0, 0)
#	x = 2 ---> x = (0, 1, 0, 0, 0, 0)
#	x = 3 ---> x = (0, 0, 1, 0, 0, 0)
#	x = 4 ---> x = (0, 0, 0, 1, 0, 0)
#	x = 5 ---> x = (0, 0, 0, 0, 1, 0)
#	x = 6 ---> x = (0, 0, 0, 0, 0, 1)

# 이러한 인코딩 방식을 One-Hot-Encoding 방식이라고 한다.

# Scipy를 이용한 카테고리 분포 시뮬레이션

# scipy에서는 별도의 카테고리 분포 클래스를 제공 하지 않는다. 다항 분포를 위한 클래스 multinomial를
# 이용하여 카테고리 분포 객체를 생성 할 수 있다. multinomial 클래스에서 시행 횟수를 1로 설정하면
# 카테고리 분포가 되므로 이 클래스를 이용함

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

theta = np.array([1/6]*6)
rv = sp.stats.multinomial(1, theta)

xx = np.arange(1,7)
print (xx)
# get_dummies() 는 One-Hot-Encoding 을 만들 때 사용하는 함수이다.
# xx_ohe = np.eye(6)
# xx_ohe = sp.sparse.eye(6).toarray()
xx_ohe = pd.get_dummies(xx)
print(xx_ohe)
xx_ohe = xx_ohe.to_numpy()
print(xx_ohe)

plt.bar(xx, rv.pmf(xx_ohe))
plt.ylabel("P(x)")
plt.title("pmf of Categorical Distribution")
plt.show()


np.random.seed(1)
X =rv.rvs(1000)
print(X[:10])

y = X.sum(axis=0)/ float(len(X))
plt.bar(np.arange(1,7), y)
plt.title("Simulation of Categorical distribution")
plt.show()

df = pd.DataFrame({"theory": rv.pmf(xx_ohe), "simulation":y}, index = np.arange(1,7)).stack()
df = df.reset_index()
df.columns = ["sample", "type", "%"]
df.pivot("sample", "type", "%")
print(df)

sns.set()
sns.set_style("darkgrid")
sns.barplot(x ="sample", y="%", hue="type", data=df)
plt.show() 


eps = np.finfo(np.float).eps
theta = np.array([eps, eps, 0.2, 0.1, 0.4, 0.3])
rv = sp.stats.multinomial(1, theta)

X = rv.rvs(100, random_state=1)
y = X.sum(axis = 0) / float(len(X))

df = pd.DataFrame({"theory":rv.pmf(xx_ohe), "simulation":y}, index=np.arange(1,7)).stack()
df = df.reset_index()
df.columns = ["sample", "type", "%"]
df.pivot("sample", "type", "%")
sns.barplot(x="sample", y="%", hue="type", data=df)
plt.show()







