import numpy as np

def numerical_derivative( f, x):
    delta_x = 1e-4
    return (f(x + delta_x) - f(x - delta_x)) / (delta_x * 2)

def myfunc1(x):
     return x**2

result = numerical_derivative(myfunc1, 3)
print(result)

# f(x) = 3xe^x
# 공식으로 풀기
#f'(x) = 3e^x + 3xe^x
#f'(2) = 3e^2 + 6e^2
print(3*np.exp(2) + 6 * np.exp(2))

#미분함수로 풀기 
def myfunc2(x):
    return 3*x*(np.exp(x))

result2 = numerical_derivative(myfunc2, 2)
print(result2)
