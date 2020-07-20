# 난수(random number) 발생

# seed(씨앗값) 설정
#np.random.seed()

#rand(x) : x만큼 0~1사이의 난수를 발생시키겠다.

# 데이터의 순서 바꾸기

# shuffle() : 섞는 함수

import numpy as np
x = np.arange(10)
print(x)
print("--------------")
np.random.shuffle(x)

print(x)

# 데이터 샘플링 : 이미 있는 데이터 집합에서 무작위로 선택하는 것을 
#	          샘플링(sampling)이라고 한다.

# choice : np.random.choice(a, size, replace=True/False, p)

# 인자 a :	원본 데이터, 정수이면 range(a)
# size : 샘플 숫자
# replace : True이면 한번 선택한 데이터를 다시 선택할 수 있다.
# p : 배열, 각데이터가 선택될 수 있는 활률

x  = np.random.choice(5,5, replace=False) #shuffle과 같은 결과
print("-------------")
print(x)
x1 = np.random.choice(5, 3, replace=False)
print(x1)
print("-------------")
x2 = np.random.choice(5, 10, replace=True)
print(x2)

print("-------------")
x3 = np.random.choice(5, 10, p=[0.1, 0, 0, 0.3, 0.6])
print(x3)

# 난수 생성하는 명령
# rand : 0~1사이의 균일 분포
# randn : 가우시안 표준 정규 분포
# randint : 균일 분포의 정수 난수

# randint(low, high, size)
# high 값이 없으면 low와 0사이의 숫자, high 값이 있으면  low~high사이의
# 숫자를 출력한다. size는 난수의 갯수를 의미한다.

np.random.randint(10, size=10) # 이때 10은 low 이다. high는 0이다.

# 정수 데이터 카운팅

# unique : 데이터에서 중복된 값을 제거하고 중복되지 않는 값의 리스트를 출력
# unique의 인수 중에 return_counts=True설정이면 데이터의 갯수도 출력한다.

# bincount : minlength 인수를 설정하여 사용하면 편리하다.

a = np.unique([1,1,2,2,3,3]) # array([1,2,3])

print(a)
print("-------------")
b = np.array(['a', 'b', 'b', 'c', 'a', 'd'])
print(b)
b1 = np.unique(b, return_counts = True)
print(b1)

print("----------------")
data, count = np.unique(b, return_counts = True)
print(data)
print(count)

# 주사위를 던졌을 때 나올 수 있는 숫자는 1~6 이다.
# unique는 실제로 던져서 나온 숫자만 카운트하므로
# 나올 수 있는 숫자에 대한 카운트는 하지 않는다.
# 하지만 bincount는 나올 수 있는 숫자의 카운트를 0으로 한다.
print("------------ bincount -------------")
cnt = np.bincount([1,1,2,2,3,4], minlength = 6)
print(cnt)






