﻿# 그리드 서치와 수치적 최적화

# 최적화 문제 : 목적 함수의 값을 가장 최소로 하는 x의 위치를 찾는 것
# 최적화 문제를 푸는 가장 간단한 방법 : x의 값을 여러번 넣어 보고 그 중에서 가장 
#				작은 값을 선택하는 방법(그리드 서치(grid search)방법)


# 그리드 서치를 이용하면 목적함수의 값(예측 오차)을 찾기 위한 계산량이 많게된다.
# 목적함수의 계산량을 줄이기 위한 방법으로 수치적 최적화(numerical optimization)를 사용한다.

# 수치적 최적화 : 반복적 시행 착오(trial and error)에 의해 최적화 필요조건을 만족하는 x*를 찾는 방법
# 함수의 위치가 최저점이 될 때까지 가능한 한 적은 횟수로 x의 위치를 옮기는 방법

# 수치적 최적화 방법에 필요한 두가지 알고리즘
#	1. 어떤 위치 x를 시도한 뒤에 다음 번에 시도할 위치 x를 찾는 알고리즘
#	2. 현재 위치 x가 최저점인지를 판단할 수 있는 알고리즘 

# 기울기 필요 조건 : 모든 최소점은 기울기가 0이기 때문에 최소점이 되기 위해서는 기울기값이 
#		0 이어야 한다. 기울기가 0이어도 최소점이 아닐 수 있다.
# 기울기를 나타내는 벡터(함수)를 g 기호로 표현한다. g(그레디언트)

# SGD(Steepest Gradient Descent) 방법 : 현재 위치 x에서의 기울기 값 g(x)만을 
#				   이용해서 다음에 시도할 위치를 알아내는 방법

import numpy as np
import matplotlib.pylab as plt

def f1(x):
	return (x-2)**2 + 2

def f1d(x):
	return 2*(x - 2.0)

xx = np.linspace(-1, 6, 100)
plt.plot(xx, f1(xx), 'b-')

# step size 값 설정
mu = 0.4

# k는 위치값, 0부터 시작한다. k = 0 첫번 째 위치 시도값
x = 0

plt.plot(x, f1(x), 'ro', ms=10)
plt.plot(xx, f1d(x) * (xx - x) + f1(x), 'g--')
print("x = {}, g = {}".format(x, f1d(x)))


# k = 1 두번째 시도
x = x -mu*f1d(x)
plt.plot(x, f1(x), 'ro', ms=10)
plt.plot(xx, f1d(x)* (xx - x) +f1(x), 'g--')
print("x = {}, g = {}".format(x, f1d(x)))

# k = 2 세번째 시도
x = x - mu*f1d(x)
plt.plot(x, f1(x), 'ro', ms = 10)
plt.plot(xx, f1d(x) * (xx - x) + f1(x), 'g--')
print("x = {}, g = {}".format(x, f1d(x)))

plt.ylim(0, 10)
plt.grid(True)
plt.show()







