import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60]])
print(a.shape)


row_add = np.array([70, 80, 90]).reshape(1, 3)  #vector -> matrix 변환

column_add = np.array([1000,2000]).reshape(2, 1)

b = np.concatenate((a, row_add), axis = 0)
print(b)
c = np.concatenate((a, column_add), axis = 1)
print(c)
