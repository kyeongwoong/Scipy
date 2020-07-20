# Matplotlib의 다양한 차트

# 바차트는 bar(세로방향), barh(가로방향) 명령으로 만들 수 있다. 
# bar(x, y) : x는 x축의 위치, y축의 값
import numpy as np
import matplotlib.pylab as plt

y = [2, 3, 1]
x = np.arange(3)
xlabel = ['A', 'B', 'C']
plt.bar(x, y)
plt.xticks(x, xlabel)
plt.grid(True)
plt.show()


np.random.seed(0)

yLabel = ['A', 'B', 'C', 'D']
yPos = np.arange(4)
yValue = 2+10*np.random.rand(4)

plt.barh(yPos, yValue, alpha=0.5)
plt.yticks(yPos, yLabel)
plt.show()

# 히스토 그램

# hist 명령으로 히스토그램을 만들 수 있다. bins인수를 사용한다.
# bins : 데이터를 집계할 구간 정보를 설정한다.

np.random.seed(0)
x = np.random.randn(1000)
plt.hist(x, bins=10)
plt.show()

# 파이 차트

# pie 명령으로 파이차트를 그릴 수 있다.
# pie(ratio, explode, labels, colors, autopct, shadow, startangle)
# 원의 형태를 유지하기 위해서 plt.axis('equal') 명령을 실행 한 후 그린다.

labels = 'A', 'B', 'C', 'D'
ratio = [10, 30, 40, 20]
colors = ['red', 'skyblue', 'yellowgreen', 'pink']
explode =(0,0.1,0,0)

plt.pie(ratio, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
shadow=True, startangle=90)
plt.axis('equal')
plt.show()

# 스캐터 플롯 : 두개의 실수 데이터 집합의 상관관계를 살펴볼 때 많이 사용하는 차트
# scatter 명령으로 그릴 수 있다.
np.random.seed(0)

#np.random.normal(평균, 표준편차, 샘플수)
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
plt.scatter(X,Y)
plt.grid(True)
plt.show()

# 데이터가 2차원이 아닌 3차원 이상의 경우에는 점 하나의 크기 또는
# 칼러를 이용하여 표현한다. 이런 차트를 버블(bubble chart)
# 크기를 표현 할 때 s, 칼러는 c 인수를 사용한다.

n = 30
np.random.seed(0)
x = np.random.rand(n)
y1 = np.random.rand(n)
y2 = np.random.rand(n)
y3 = np.pi *(15 * np.random.rand(n))**2
plt.scatter(x, y1, c=y2, s=y3)
plt.grid(True)
plt.show()











