﻿# 3차원 배열 만들기
import numpy as np
d=np.array([[[1,2,3,4],
	     [5,6,7,8],
	     [9,10,11,12]],
	    [[11,12,13,14],
	     [15,16,17,18],
	     [19,20,21,22]]])

print(d) 

#3차원 배열의 행, 열, 깊이를 구하는 명령은 len
print(len(d))#깊이값을 구함
print(len(d[0])) #행을 구함
print(len(d[0][0])) #열을 구함