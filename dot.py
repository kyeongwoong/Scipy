## numpy 제공하는 내적 함수 dot()

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11,12])

#벡터의 내적
print(v.dot(w))  # v[0]*w[0] + v[1]*w[1] = 219
print(np.dot(v,w))

#매트릭스 벡터 곱
print(x.dot(v)) #rank는 1
# 결과 과정은 [x[0,0]*v[0]+x[0,1]*v[1]=29, x[1,0]*v[0]+x[1,1]*v[1]=67]
print(np.dot(x,v))

#행렬(매트릭스)의 곱
print(x.dot(y))
#x[0,0]*y[0,0]+x[0,1]*y[1,0]=19, x[0,0]*y[0,1]+x[0,1]*y[1,1]=22,
#x[1,0]*y[0,0]+x[1,1]*y[1,0]=43, x[1,0]*y[0,1]+x[1,1]*y[1,1]=50
print(x.dot(y).ndim)

print(np.dot(x,y))


#유용한 함수 sum()
xx = np.array([[1,2],[3,4]])

print(np.sum(x)) #x의 모든 요소에 대한 합을 계산
print(np.sum(x, axis=0))#axis = 0은 각 칼럼에 대한 합계를 계산
print(np.sum(x, axis=1))#axis = 1은 각 행에 대한 합계를 계산

print("----------------------")
#전치 행렬의 표현은 T속성을 이용한다.
tt = np.array([[1,2], [3,4]])
print(tt)

print(tt.T)
#rank 가 1인 경우에는 전치가 되지 않는다. 아무것도 하지 않는다.
vv = np.array([1,2,3])
print(vv.T)








