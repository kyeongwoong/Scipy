# Matplotlib의 triangular grid 사용

# 삼각 그리트 지원을 해주는 패키지 임포트
# import matplotlib.tri as mtri
# 삼각 그리드 생성

# 삼각 그리드는 Triangulation 클래스를 이용하여 생성한다.
# Triangulation(x, y, triangles) # triangles는 생략했을 경우 자동으로 생성된다.

import numpy as np
import matplotlib.tri as mtri
import matplotlib.pylab as plt

x = np.array([0, 1, 2])
y = np.array([0, np.sqrt(3), 0])
triangles = [[0,1,2]]
triang = mtri.Triangulation(x, y, triangles)
plt.triplot(triang, 'ro-')
plt.xlim(-0.1, 2.1)
plt.ylim(-0.1, 1.8)
plt.grid(True)
plt.show()

x = np.array([0,1,2,3,4,2])
y = np.array([0,np.sqrt(3),0,np.sqrt(3),0,2*np.sqrt(3)])
triangles =[[0,1,2], [2,3,4], [1,2,3],[1,3,5]]
triang = mtri.Triangulation(x, y, triangles)
plt.triplot(triang, 'bo-')
plt.xlim(-0.1, 4.1)
plt.ylim(-0.1, 3.7)
plt.grid(True)
plt.show()







