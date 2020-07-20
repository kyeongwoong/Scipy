# Matplotlib : 시각화 패키지

# 데이터를 차트(chart)나 플롯(plot)으로 시각화하는 패키지
# 여러 다양한 시각화 기능을 제공한다.

# 라인플롯(line plot), 스캐터 플롯(scatter plot), 바 차트(bar chart), 히스토그램(histogram)..


# 서브 패키지
	# pylab 

# import matplotlib as mpl # matplotlib를 먼저 불러오고
# import matplotlib.pylab as plt

# 라인 플롯 : 선을 그리는 플롯, 데이터가 시간, 순서 등에 따라 어떻게 변하는지를
#	보여주기 위해서 사용된다.

import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

#plt.plot([1,5,8, 15]) #plot 명령은 ndarray 객체를 반환한다.
#plt.grid(True)
#plt.show()

#plt.plot([100,200,300,400],[1,4,10,17], 'm+-.')
#plt.grid(True)
#plt.show()

# 차트의 스타일 지정 순서 : 색상(color), 마커(marker), 선종류(line style)

# Matplotlib가 그리는 그림은 Figure객체, Axes객체, Axis 객체로 구성된다.
# Figure객체는 한개 이상의 Axes객체를 포함 할 수 있다.
# 그리고, Axes 객체는 다시 두개 이상의 Axis 객체를 포함한다.
# 즉, Axes객체는 하나의 플롯을 의미한다.
# Axis는 세로축(y축)이나 가로축(x축)등의 축을 의미한다.

# Figure 객체는 Matplotlib.figure.Figure클래스 객체이다.

# Figure는 플롯이 그려지는 캔버스(도화지)를 뜻한다.

# subplot : 하나의 Figure안에 여러개의 플롯을 배열 형태로 보이도록 할 때 사용한다.
# Figure안에 Axes를 생성하려면 원래는 subplot 명령을 사용해서 Axes객체를 얻어야 한다.
# 그러나, plot 명령을 사용해도 자동으로 Axes를 생성해준다.

# subplot(2,1,1), subplot(2,1,2)
# tight_layout  명령을 실행하면 플롯(Axes)간의 간격을 자동으로 조절해준다.

# np.linspace : (start, stop, num, endpoint=True, retstep=False, dtype)
#	start: 시작값, stop: endpoint가 False로 설정되지 않은 경우 끝 값이 된다.
#	num : 생성할 샘플 수, 기본값 50, 음수는 될 수 없다.
#	retstep : 샘플간의 간격을 설정할 수 있는 step을 반환한다.		

np.linspace(2.0, 3.0, num=5) #[2., 2.25, 2.5, 2.75, 3.]

np.linspace(2.0, 3.0, num=5, endpoint=False) # [2., 2.2, 2.4, 2.6, 2.8]

np.linspace(2.0, 3.0, num=5, retstep=True) # [2., 2.25, 2.5, 2.75, 3.], 0.25

N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)

plt.plot(x1, y, 'o')

plt.plot(x2, y+0.4, 'o')

#ylim : y축의 범위를 지정한다.
#xlim : x축의 범위를 지정한다.

plt.ylim([-0.5, 1])

plt.show()

xx1 = np.linspace(0.0, 5.0)
xx2 = np.linspace(0.0, 2.0)

yy1 = np.cos(2*np.pi * xx1) * np.exp(-xx1)
yy2 = np.cos(2*np.pi * xx2)

ax1 = plt.subplot(2,1,1)
plt.plot(xx1, yy1, 'ro-')
ax2 = plt.subplot(2,1,2)
plt.plot(xx2,yy2,'b.-')

plt.show()


# tick : 플롯이나 차트에서 축상의 위치 표시 지점을 의미한다.
# 틱에 씌어지는 숫자나 글자를 틱 라벨(tick label)이라고 한다.
# 일반적으로 틱 라벨은 Matplotlib가 자동으로 정해준다.
# 하지만, 사용자가 수동으로 설정을 하고 싶다면 xticks, yticks명령을 사용하여
# x축과 y축 설정해 줄 수 있다.

# 틱 라벨 문자열을 수학 기호로 표시하고 싶은 경우 $$사이에 LaTeX 수학 문자식을
# 넣어서 사용한다.

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],['$-\pi$', '$-\pi/2$','$0$','$+\pi/2$','$+\pi$'] )
plt.yticks([-1, 0,1], ["Low", "0", "High"])
plt.show()







