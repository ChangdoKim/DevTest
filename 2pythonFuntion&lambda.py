def multi_ret_func_(x):
    return x+1, x+2, x+3

x = 100
y1, y2, y3 = multi_ret_func_(x)
print(y1, y2, y3)

def print_name(name, count=2):
    for i in range(count):
        print("name = ", name)

print_name("DAVE")

def mutable_immutable_func(int_x, input_list):
    int_x += 1
    input_list.append(100)

# mutable  - 주소 복사 : list, dict, numpy  
# immutable - 값 복사 : 숫자, 문제,  tuple
x = 1
test_list = [1, 2, 3]
mutable_immutable_func(x, test_list)
print("x = ", x, ", test_list = ", test_list)

#lambda : 함수를 한줄로 표현하는 방법
func = lambda x, y : x + 100 + y

for i in range(3):
    print(func(i, 3))

def print_hello():
    print("hello python")

def test_lambda(s, t):
    print("input1 = ", s, ", input2 = ", t)

a = 100
b = 200

fx = lambda x, y : test_lambda(x, y)
fy = lambda x, y : print_hello()

fx(500, 1000)
fy(1000, 20000)