# 정렬
# sort 명령이나 메소드를 사용하여 배열안의 원소를 크기에 따라 정렬하여
# 새로운 배열을 만들 수 있다.
# 2차원 이상인 경우에는 행이나 열을 각각 따로따로 정렬할 수 있는데
# 이때, axis 인수를 사용하여 행과 열을 결정할 수 있다.
# axis = 0 일 때 행 정렬, axis = 1 일 때는 열 정렬

import numpy as np

a = np.array([[4,3,5,7],
	      [1,12,11,9],
	      [2,15,1,14]])

print(np.sort(a))

print(np.sort(a, axis=-1))

print(np.sort(a, axis=0))

#argsort명령은 자료를 정렬하는 것이 아니라 순서만 알고 싶을 때
# 사용한다.

a = np.array([44,33,11,22])
j = np.argsort(a)

print(j)

print(a[j])
	