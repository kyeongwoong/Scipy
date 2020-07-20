# seaborn 을 이용한 1차원 데이터 분포 표시

# 카운트 플롯
# countplot() : 각 카테고리 값 별로 데이터가 얼마나 있는지를 알 수 있는 플롯
# countplot명령은 데이터프레임에서만 사용할 수 있다.

# 사용예:
# countplot(x = "column_name", data=dataframe)

import seaborn as sns
import matplotlib.pylab as plt
titanic = sns.load_dataset("titanic") # 타이타닉 데이터 로드

sns.countplot(x = "class", data=titanic)

plt.show()


# 2차원 실수 데이터
# 산점도(scatter plot)
# Seaborn 패티지의 jointplot명령을 이용하여 표현한다. 
# 차트의 가장자리에 히스토그램도 표시된다.
# 이명령은 dataframe만을 사용할 수 있다.

# 사용법
# jointplot(x ="x_name", y="y_name", data=dataframe, kind='scatter')
# data 인수의 대상은 dataframe, x인수는 데이터프레임의 열이름 문자열, y인수는 데이터프레임의
# 열 이름을 넣는다. kind인수는 차트의 종류를 지정한다.


iris = sns.load_dataset("iris")
sns.set()
sns.set_style("whitegrid")
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)

plt.show()









