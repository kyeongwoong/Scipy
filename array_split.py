# 배열 나누기(쪼개기)

#split = array_split

import numpy as np

x = np.arange(9.0) 
print(x)

print(np.split(x, 3))

x1 = np.split(x,3)
print(x1[0])
print(x1[1])
print(x1[2])

x2 = np.split(x, [3,4])

print(x2)

x3 = np.split(x,[2,5,7])
print(x3)

x4 = np.split(x, [2,4,10])
print(x4)

x4 = np.array_split(x,[2,4,10])
print(x4)

#dsplit

print("------------------")
y = np.arange(16).reshape(2,2,4)
print(y)

y1 = np.dsplit(y, 2)
print(y1)
print("------------------")
#hsplit
h = np.arange(16).reshape(4,4)
print(h)

h1 = np.hsplit(h, 2)
print(h1)

h2 = np.hsplit(h, [3, 6])
print(h2)

hh = np.arange(8).reshape(2,2,2)
print(hh)

hh1 = np.hsplit(hh,2)
print(hh1)
print(" ")
print("#############################")
#vsplit

v = np.arange(16).reshape(4,4)
print(v)

v1 = np.vsplit(v, 2)
print(v1)

v2 = np.vsplit(v,[1,3])
print(v2)

vv = np.arange(8).reshape(2,2,2)
print(vv)

vv1 = np.vsplit(vv, 2)
print(vv1)






