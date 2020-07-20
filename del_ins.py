# 요소에 대한 추가 삭제

# delete

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,11,12,13]])

print(arr)

print("------------------------------")
arr1 = np.delete(arr, 1)
print(arr1)
print("------------------------------")

arr1 = np.delete(arr, 1, 0)

print(arr1)
print("------------------------------")

arr1 = np.delete(arr, 0, 0)
print(arr1)
print("------------------------------")
arr2 = np.delete(arr,2,1)
print(arr2)

#insert
print("------------------------------")
a = np.array([[1,1],[2,2],[3,3]])
print(a)
print("------------------------------")
a1 = np.insert(a, 1, 100)
print(a1)

print("------------------------------")
a1 = np.insert(a, 1, 100, axis=1)
print(a1)

a1 = np.insert(a, 1, 100, axis=0)
print(a1)
print("------------------------------")
a2 = np.insert(a, 1, [100,200,300], axis=1)
print(a2)

# append
print("------------------------------")
aa = np.array([[1,2,3],[4,5,6]])
print(aa)
print("------------------------------")
# aa2 = np.append(aa, [7,8,9], axis=0) #구문 오류

aa2 = np.append(aa, [[7,8,9]], axis=0)
print(aa2)

print("-----------------------------------------")
#resize
x = np.array([[0,1],[2,3]])#2행 2열
print(x)
print(" --------")
x1 = np.resize(x,(2,3))#x를 2행 3열로 resize하라
print(x1)
print(" --------")
x2 = np.resize(x,(2,4))
print(x2)

#trim_zeros : 좌우에 0을 제거
aa = np.array((0,0,0,1,2,3,0,1,2,0,0))
print(aa)
print(" --------")
aa1 = np.trim_zeros(aa)
print(aa1)
print(" --------")
aa2 = np.trim_zeros(aa, 'f') #'b'는 뒷부분의 0을 제거
print(aa2)

# unique 

print("------")
a = np.array([1,1,2,1,2,2,3,3,3])
print(a)

print("------")
a1 = np.unique(a)
print(a1)

print("------")
aa = np.array([[1,1],[2,3]])
print(aa)
aa1=np.unique(aa)
print(aa1)
print("------")

a = np.array([[1,0,0],[1,0,0], [2,3,4]])
print(a)

a1 = np.unique(a, axis=0)
print(a1)

# 요소의 재정렬
print("------")
#flip
A = np.arange(8).reshape((2,2,2))
print(A)
print("------")
A1 = np.flip(A, 0)
print(A1)

print("------")
A2 = np.flip(A,1)
print(A2)
print("------")

# fliplr : 왼쪽 / 오른쪽 방향으로 뒤집기

# diag : 대각선 배열을 만들거나, 추출할 때 사용하는 명령
A = np.diag([1,2,3])
print(A)
print("------")
A1 = np.fliplr(A)
print(A1)

# flipud : 배열을 위/아래 방향으로 뒤집는다.
print("------")
B = np.diag([1,2,3])
print(B)

B1 = np.flipud(B)
print(B1)

#rot90 : 90도 만큼 배열을 회전한다. (k옵션, axes옵션)
print("------")
m = np.array([[1,2],[3,4]])
print(m)

print("------")
m1 = np.rot90(m, 1)
print(m1)
print("------")
m1 = np.rot90(m) # k=1, axes(0,1) 옵션이 생략된 것
print(m1)
print("------")
m1 = np.rot90(m, 1, (1,0))
print(m1)
print("------")
m1 = np.rot90(m, 2, (1,0)) #시계방향으로 180도 회전
print(m1)
m1 = np.rot90(m, 1, (1,0))
print("------")
m1 = np.rot90(m, -1, (0,1))
print(m1)












