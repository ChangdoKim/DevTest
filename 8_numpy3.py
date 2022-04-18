import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60]])
print(a.shape)


row_add = np.array([70, 80, 90]).reshape(1, 3)  #vector -> matrix 변환

column_add = np.array([1000,2000]).reshape(2, 1)

b = np.concatenate((a, row_add), axis = 0) # axis (축) 0 : row, 1: column
print(b)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
c = np.concatenate((a, column_add), axis = 1)
print(c)
# [[  10   20   30 1000]
#  [  40   50   60 2000]]

loaded_data = np.loadtxt('./data/data-01.csv', delimiter=',', dtype=np.float32)

x_data = loaded_data[:, 0: -1]
y_data = loaded_data[:, [-1]]

print("x_data.ndim = ", x_data.ndim, ", x_data.shape = ", x_data.shape)
print("y_data.ndim = ", y_data.ndim, ", y_data.shape = ", y_data.shape)

random_number1 = np.random.rand(3)
random_number2 = np.random.rand(1, 3)
random_number3 = np.random.rand(3, 1)

print(random_number1, ", ", random_number1.shape)
#[0.19888819 0.74045046 0.51470254] ,  (3,)
print(random_number2, ", ", random_number2.shape)
#[[0.33792927 0.03622947 0.12444007]] ,  (1, 3)
print(random_number3, ", ", random_number3.shape)
# [[0.83749403]
#  [0.10262031]
#  [0.83580936]] ,  (3, 1)

X = np.array([2, 4, 6, 7, 8])

print("sum ", np.sum(X))
# sum  27
print("exp ", np.exp(X)) # exponential 지수 e
# exp  [   7.3890561    54.59815003  403.42879349 1096.63315843 2980.95798704]
print("log ", np.log(X))
# log  [0.69314718 1.38629436 1.79175947 1.94591015 2.07944154]

print("max ", np.max(X))
# max  8
print("min ", np.min(X))
# min  2
print("argmax ", np.argmax(X))
# argmax 최고 값이 있는 index
# argmax  4 
print("argmin ", np.argmin(X))
# argmin 최소 값이 있는 index
# argmin  0

X = np.array([[2, 3, 4], [4, 6, 8], [10, 20, 30]])

print("max ", np.max(X, axis=0))
#max  [10 20 30]
print("min ", np.min(X, axis=0))
#min  [2 3 4]
print("max ", np.max(X, axis=1))
#max  [ 4  8 30]
print("min ", np.min(X, axis=1))
#min  [ 2  4 10]
print("argmax ", np.argmax(X, axis=0))
#argmax  [2 2 2]
print("argmin ", np.argmin(X, axis=0))
#argmin  [0 0 0]
print("argmax ", np.argmax(X, axis=1))
#argmax  [2 2 2]
print("argmin ", np.argmin(X, axis=1))
#argmin  [0 0 0]

a = np.ones([3, 4])
print("a.shape : ", a.shape, ", a = ", a)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

b = np.zeros([3, 2])
print("b.shape : ", b.shape, ", b = ", b)
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)
print(a[0, 0], ", ", a[0][0])   # 두가지 방법 사용가능

print(a[:, :])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a[:-1, 1:-1])
# [[2 3]
#  [6 7]]

#iterator
a = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(a)
print(a.shape)
#(2, 4)

it = np.nditer(a, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    idx = it.multi_index
    print("current value - ", a[idx])
    it.iternext()

