# 차원 축소 연산
# 행렬의 하나의 행에 있는 원소들을 하나의 데이터 집합으로 보고 그 집합의
# 평균을 구하면 각 행에 대해 하나의 숫자가 나오게 되는 데 이경우 
# 차원 축소가 된다. 이러한 연산을 차원 축소(dimension reduction)연산이라 한다.

# Numpy에서 차원 축소 연산 명령 또는 메소드
# 최대/최소 : min, max, argmin(최소값의 위치), argmax(최대값의 위치)
# 통계 : sum, mean, median, std, var
# 불리언: all, any

import numpy as np

x = np.array([1,10, 100])
print(x.min())
print(x.max())

print(x.argmin())
print(x.argmax())

print(x.mean())

#여러개의 숫자들이 있을 때 크기순으로 정렬한 다음 가장 가운데 위치한 숫자
print(np.median(x)) 

a = np.array([1,2,3,1])

print(np.median(a))

# all : 배열의 모든 원소가 True인지 평가하는 메소드

print(np.all([True, True, False]))

#any : 배열의 1개 이상의 원소가 True인지 평가하는 메소드

print(np.any([False, False, True, False]))

#axis 인수를 이용하여 어느 차원으로 계산을 할지를 지정하면
# 이경우 대부분 차원 축소 명령에 적용될 수 있다.

xx = np.array([[1,1], [2,2]])

print(xx.sum())

print(xx.sum(axis=0)) # 열 합계
print(xx.sum(axis=1)) # 행 합계
