# SciPy를 이용한 최적화

# import scipy as sp

# scipy의 서브 패키지 optimize에 minimize메소드를 이용하여 최적화를 할 수 있다.
# 이 때 사용하는 알고리즘은 BFGS 이다.
# minimize 메소드는 최적화를 시작하기 위한 초기값과 목적함수를 인수로 사용한다. 

# minimize 명령은 최적화 결과를 OptimizeResult 클래스 객체로 반환한다.
# OptimizeResult 클래스는 다음과 같은 속성을 갖고 있다.

# x : 최적화 해
# success : 최적화를 성공 했을 때 True를 반환
# status : 종료 상태. 최적화에 성공 했을 때 0을 반환
# message : 메세지 문자열
# fun : x위치에서의 함수 값
# jac : x위치에서의 자코비안(그레디언트) 벡터 값
# hess : x위치에서 헤시안 행렬 값
# nfev : 목적 함수를 몇번 호출한 횟수
# njev : 자코비안 계산 횟수
# nhev: 헤시안 계산 횟수
# nit : x 이동 횟수

import scipy as sp
from scipy import optimize

def f1(x):
	return (x- 2) ** 2 + 2

x0 = 0 # 초기값 설정
res = sp.optimize.minimize(f1, x0)
print(res)





