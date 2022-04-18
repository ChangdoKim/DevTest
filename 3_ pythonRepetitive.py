#if문
a = 1
if a > 0:
    print("a == ", a)
    print("positive")
elif a == 1:
    print("a == ", a)
    print("zero")
else:
    print("a == ", a)
    print("negative")

list_data = [10, 20 , 30, 40]
score = {"key1":90, "LEE":85, "JUN":95}

if 45 in list_data:
    print("45 is in list_data")
else:
    print("45 is not in list_data")

if 'key1' in score:
    print("key1 is in score")
else:
    print("key1 is not in score")

#반복문
for data in range(10):
    print(data, " ", end='')
print("")
#0  1  2  3  4  5  6  7  8  9
for data in range(0, 10):
    print(data, " ", end='')
print("")
#0  1  2  3  4  5  6  7  8  9
for data in range(0, 10, 2):
    print(data, " ", end='')
print("")
#0  2  4  6  8

list_data = [10, 20 , 30, 40]
for data in list_data:
    print(data, " ", end='')
print("")
#10  20  30  40

score = {"key1":90, "LEE":85, "JUN":95}
for data in score:
    print(data, " " , end='')
print("")
#key1  LEE  JUN

for key, value in score.items():
    print(key, " ", value)
#key1   90
#LEE   85
#JUN   95

#list comprehension : 리스트 요소를 정의하는 기법
list_data = [x**2 for x in range(5)] # * :곱하기, ** : 제곱
print(list_data)
#[0, 1, 4, 9, 16]
raw_data = [[1, 10], [2, 20], [3, 30], [4, 40]]
all_data = [x for x in raw_data]
x_data = [x[0] for x in raw_data]
y_data = [x[1] for x in raw_data]

print(all_data)
#[[1, 10], [2, 20], [3, 30], [4, 40]]
print(x_data)
#[1, 2, 3, 4]
print( y_data)
#[10, 20, 30, 40]

#짝수를 출력하는 코드
even_numeber = []
for data in range(10):
    if data % 2 == 0:
        even_numeber.append(data)

print(even_numeber)

#while
data = 5
while data >= 0:
    print("data = ", data)
    data -= 1

    if data == 2:
        print("break hear")
        break
    else:
        print("continue")
        continue

