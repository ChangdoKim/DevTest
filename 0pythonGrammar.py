
#list : 변경가능한 list
a = [10, 20, 30, 40, 50]
print("a[0] = ", a[0], ", a[1] = ", a[1], ", a[2] = ", a[2], ", a[3] = ", a[3])
#a[0] =  10 , a[1] =  20 , a[2] =  30 , a[3] =  40
print("a[-1] = ", a[-1], ", a[-2] = ", a[-2], ", a[-3] = ", a[-3], ", a[-4] = ", a[-4])
#a[-1] =  50 , a[-2] =  40 , a[-3] =  30 , a[-4] =  20

b = [10, 20, "Hello", [True, 3.14]]
print("b[0] = ", b[0], ", b[1] = ", b[1], ", b[2] = ", b[2], ", b[3] = ", b[3])
#b[0] =  10 , b[1] =  20 , b[2] =  Hello , b[3] =  [True, 3.14]
print("b[-1] = ", b[-1], ", b[-2] = ", b[-2], ", b[-3] = ", b[-3], ", b[-4] = ", b[-4])
#b[-1] =  [True, 3.14] , b[-2] =  Hello , b[-3] =  20 , b[-4] =  10

c = []
c.append(100), c.append(200), c.append(300)
print(c)
#[100, 200, 300]


#[begin:end] -> index로 한번에 출력 하는 기능 
#[0 1 2 3 4 ] [-5 -4 -3 -2 -1]
#[index: index-1 까지]
print("a[0:2] = ", a[0:2], ", a[1:] = ", a[1:])
#a[0:2] =  [10, 20] , a[1:] [20, 30, 40, 50]
print("a[:3] = ", a[:3], ", a[:-2] = ", a[:-2])
#a[:3] =  [10, 20, 30] , a[:-2] = [10, 20, 30]
print("a[:] = ", a[:])
#a[:] =  [10, 20, 30, 40, 50]

#tuple : 변경할수 없는 list
#list 와 사용 방법 동일
d = (10, 20, 30, 40, 50)

#dictionary
score = {"KIM":90, "LEE":85, "JUN":95}
print("score[KIM] = ", score['KIM'])
#score[KIM] =  90
score['HAN'] = 100
print(score)
#{'KIM': 90, 'LEE': 85, 'JUN': 95, 'HAN': 100}
print("score key = ", score.keys())
#dict_keys(['KIM', 'LEE', 'JUN', 'HAN'])
print("score value = ", score.values())
#dict_values([90, 85, 95, 100])
print("score items = ", score.items())
#dict_items([('KIM', 90), ('LEE', 85), ('JUN', 95), ('HAN', 100)])

a = 'A73/,CD'
print(a[1])
#7
a = a + ', EFG'
print(a)
#A73/,CD, EFG
b = a.split(',')
print(b)
#['A73/', 'CD', ' EFG']

a = [10, 20, 30, 40, 50]
b = (10, 20, 30, 40, 50)
c = {"KIM":90, "LEE":85, "JUN":95}
d = 'Seoul, Korea'
e = [[100, 200], [300, 400], [500, 600]]
print(type(a), type(b), type(c), type(d), type(e))
#<class 'list'> <class 'tuple'> <class 'dict'> <class 'str'> <class 'list'>
print(len(a), len(b), len(c), len(d), len(e))
#5 5 3 12 3
#print(size(e)) duplicate 된것 같음

a = 'Hello'
c = {"KIM":90, "LEE":85, "JUN":95}
print(list(a))
#['H', 'e', 'l', 'l', 'o']
print(list(c.keys()))
#['KIM', 'LEE', 'JUN']
print(list(c.values()))
#[90, 85, 95]
print(list(c.items()))
#[('KIM', 90), ('LEE', 85), ('JUN', 95)]

