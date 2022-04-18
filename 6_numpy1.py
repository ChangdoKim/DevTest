
#import numpy
#from numpy import exp
import numpy as np

a = [[1, 0], [0, 1]]
b = [[1, 0], [0, 1]]
print(a + b)
#[[1, 0], [0, 1], [1, 0], [0, 1]]

a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 0], [0, 1]])
print(a + b)
#[[2 0]
# [0 2]]

#1차원 numpy array 는 vector
a = np.array([1, 0, 3])
b = np.array([4, 5, 6])
print(a + b)
#print(a + b)
print(a - b)
#[[-3 -5 -3]]
print(a * b)
#[[-3 -5 -3]]
print(a / b)
#[[0.25 0.   0.5 ]]

a = np.array([[1, 0], [0, 1], [0, 1]])
#형상 : shape, 차원 : dimension
print(a.shape)
#(3, 2)
print(a.ndim)
#2
#reshape vector -> matrix or matrix -> 다른 형상의 matrix 
c = np.array([1,2,3])
print(c)
#[1 2 3]
c = c.reshape(1, 3)
print(c)
#[[1 2 3]]
d = np.array([[1,2,3], [4,5,6]])
print(d)
#[[1 2 3]
# [4 5 6]]
D = d.reshape(3, 2)
print(D)
#[[1 2]
# [3 4]
# [5 6]]

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [4, 5], [4, 5]])

c = np.dot(a, b)
print(c)
# 2,3 dot 3,2 => 2, 2

# broadcast 사칙연산 계산에서 데이터를 확장시켜주는 방법
# dotproduct 는 불가 사칙연산만 가능
a = np.array([[1, 2], [4, 5]])
c = 5
print(a+c) # 5를확대해서 

# 전치행열 행과 열을 바꿔주는 기능
b = np.array([[1, 2], [4, 5], [4, 5]])
c = b.T
print(c)