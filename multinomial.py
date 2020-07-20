import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

theta = np.array([1/6]*6)
rv = sp.stats.multinomial(1, theta)

xx = np.arange(1,7)
print(xx)
# get_dummies() 는 One-Hot-Encoding 을 만들 때 사용하는 함수이다.
xx_ohe = pd.get_dummies(xx)
print(xx_ohe)

xx_ohe = np.eye(6)
print(xx_ohe)

plt.bar(xx, rv.pmf(xx_ohe))
plt.ylabel("P(x)")
plt.title("pmf of Categorical Distribution")
plt.show()
