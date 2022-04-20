import numpy as np

#gradient decent algorithm : 경사 하강법
x_data = np.array([1, 2, 3, 4, 5]).reshape(5, 1)
t_data = np.array([2, 3, 4, 5, 6]).reshape(5, 1)

W = np.random.rand(1, 1)
b = np.random.rand(1)
print("W = ", W, ", W.shape = ", W.shape, "b = ", b, "b.shape = ", b.shape)

def numerical_derivative(f, x):
    delta_x = 1e-4
    grad = np.zeros_like(x)
    # print("debug 1 initval input variable = ", x)
    # print("debug 2 initval grad = ", grad)
    # print("==================================")
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index

        #print("debug 3. idx = ", idx, ", x[idx] = ", x[idx])

        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)
        x[idx] = tmp_val - delta_x
        fx2 = f(x)
        
        grad[idx] = (fx1 - fx2) / (2 * delta_x)
        
        # print("debug 4 grad[idx] = ", grad[idx])
        # print("debug 5 grad = ", grad)
        # print("==================================")
        x[idx] = tmp_val

        it.iternext()

    return grad

def loss_func(x, t):
    y = np.dot(x, W) + b
    return (np.sum((t - y)** 2)) / (len(x))

def error_val(x, t):
    y = np.dot(x, W) + b
    return (np.sum((t - y) ** 2)) / (len(x))

def predict(x):
    y = np.dot(x, W) + b
    return y

learning_rate = 1e-2

f = lambda x : loss_func(x_data, t_data)

print("initial error value = ", error_val(x_data, t_data), "initial W = ", W, "\n, b = ", b)

for step in range(8001):
    W -= learning_rate* numerical_derivative(f, W)
    b -= learning_rate* numerical_derivative(f, b)

    if(step % 400):
        print("step = ", step, ", error Value = ", error_val(x_data, t_data), ", W = ", W, ", b = ", b)