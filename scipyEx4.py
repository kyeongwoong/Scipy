# scipy의 서브 패키지(서브 모듈)

# scipy.optimize	: 최적화
# scipy.stats	: 통계
# scipy.interplate	: 보간법
# scipy.io		: 데이터 입출력
# scipy.linalg	: 선형 대수
# scipy.sparse	: 희소 행렬
# scipy.special	: 특수 수학 함수
# scipy.signal	: 신호 처리
# scipy.cluster	: 벡터 양자화
# scipy.constants	: 물리/수학 상수
# scipy.integrate	: 통합
# scipy.ndimage	: n차원 이미지 패키지
# scipy.spatial	: 공간 데이터 구조 및  알고리즘
# scipy.odr	: 직교 거리 회귀
# scipy.fftpack	: 푸리에 변환

#  확률 분포 객체를 다루기 위한 명령
#  이산 확률 분포(베르누이분포, 이항분포, 다항 분포), 연속 확률 분포(정규분포, 균등분포..)

#---------- stats 서브 패키지 안에 포함된 명령 ------------
# 이산 : bernoulli(베루누이 분포), binom(이항분포), multinomial(다항분포)
# 연속 : uniform(균일 분포), norm(가우시안 정규 분포), beta(베타분포), gamma(감마분포)
#	t(스튜던트 t분포), chi2(카이제곱분포), f(F분포), dirichlet(디리클리 분포),
#	multivariate_normal(다변수 가우시안 정규분포)


import scipy as sp
from scipy import stats
rv = sp.stats.norm() # 정규분포 객체 rv를 생성
print(type(rv))

# 모수 지정
# 확률 분포 객체를 생성할 때는 분포의 형태를 구체적으로 지정하는 모수(parameter)를
# 인수로 지정해야 한다.
# loc(분포의 기댓값), scale(표준편차) 두개의 모수는 대부분 공통적으로 사용한다.
# size(샘플 생성시 생성될 샘플의 크기), random_state(샘플 생성 시 사용되는 seed값)

rv = sp.stats.norm(loc=1, scale=2) # 기댓값이 1이고 표준 편차가 2인 정규분포 객체 생성

# 확률 분포 메소드
# pdf() : 확률 밀도 함수(probability density function)
# pmf() : 확률 질량 함수(probability mass function)
# cdf() : 누적 분포 함수(cumulative distribution function)
# rvs() : 랜덤 샘플 생성(random variable sampling)

# 확률 밀도 함수
import matplotlib.pylab as plt
import numpy as np
x = np.linspace(-6, 6, 100)
pdf = rv.pdf(x)
plt.plot(x, pdf)
plt.grid(True)
#plt.show()

# 누적 분포 함수
x = np.linspace(-6, 6, 100)
cdf = rv.cdf(x)
plt.plot(x,cdf)
plt.grid(True)
#plt.show()

# 랜덤 샘플 생성 (rvs메소드를 이용한다. size, random_state 모수를 사용한다.)
print(rv.rvs(size=(2,4), random_state=0))

import seaborn as sns
sns.distplot(rv.rvs(size=10000, random_state=0))
plt.xlim(-6, 6)
#plt.show()


# Seaborn: 데이터 분포 시각화 패키지
# 실수 분포 플롯 (seaborn : distplot, kdeplot, rugplot)
# Seaborn 사용하기 위해서는 import seaborn as sns
# seaborn의 스타일 지정
# set명령으로 색상, 틱, 전체적인 플롯 스타일을 Seaborn스타일로 바꿀수 있다.
# set_style은 틱 스타일만 바꿀 수 있다. darkgrid, whitegrid, dark, white, ticks 스타일 제공

# set_color_codes 기본 색상을 바꿀 수 있다.

# 사용순서
# sns.set()
# set_style('whitegrid')

# 색상 팔렛트 밝기 단계 : (deep, muted, pastel, dark, bright, colorblind)

# 붓꽃 데이터 로드
iris = sns.load_dataset("iris")

# rugplot : rug(작은 선분)를 이용하여 x축위에 실제 데이터들의 위치를 보여주는 플롯

data = iris.petal_length.values

sns.set()
sns.set_style("whitegrid")
sns.rugplot(data)
plt.show()

# kdeplot(kernel density plot) : 커널 함수를 겹치는 방법으로 히스토그램보다 부드러운 형태의
#			    분포곡선을 보여주는 플롯
sns.kdeplot(data)
plt.show()

#distplot : 러그 표시와 커널 밀도 표시 기능이 있어서 matplotlib에서 제공하는 hist 명령보다
#	  더 많이 사용되고 있다.

sns.distplot(data)
plt.show()

sns.distplot(data, rug=True) # kde= False설정하면 히스토그램으로 표시
plt.show()

sns.distplot(data, bins=20, kde = False, rug=True)
plt.show()

sns.distplot(data, hist=False, rug=True)
plt.show()



