from re import A
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = a.T
print("a.shape", a.shape, ", b.shape", b.shape)
# a.shape (3, 2) , b.shape (2, 3)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]
print(b)
# [[1 3 5]
#  [2 4 6]]

c = np.array([1, 2, 3, 4, 5])
d = c.T

print("c.shape", c.shape, ", d.shape", d.shape)
#c.shape (5,) , d.shape (5,)
# vector는 형 변형 불가능

e = c.reshape(1, 5)
f = e.T
print("f.shape", f.shape, ", e.shape", e.shape)
# f.shape (5, 1) , e.shape (1, 5)