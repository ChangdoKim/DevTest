def sleep():
    print("sleep func")

class Person:
#__init__ 생성자
# 맴버변수를 반드시 생성하지 않고 맴버함수 내에서 생성 및 사용가능하다.
# 파이썬은 기본적으로 모든 멤버가 public 이다.
# 강자 private 만드는 방법은 __변수 이다.
    count = 0    #class variable : 전역 변수 의미
    def __init__(self, name) -> None: 
        self.name = name
        Person.count += 1
        print(self.name + " is initialized")
        
    def work(self, company):
        sleep() # 외부 func 를 호출
        self.sleep()    # class func 를 호출
        print(self.name + "is working in" + company)
        
    def sleep(self):
        print(self.name + "is sleeping ")
        
    def __printNames(self, name2):
        self.__name1 = name2
        print(self.__name1)

    @classmethod        #전역 함수 지정
    def getCount(cls):  # 전역함수는 cls를 첫번째 인수로 받아야함.
        return cls.count

obj = Person("PARK")        
obj.work("ANCD")
obj.sleep()
print("current person objec is ", obj.name) 

obj1 = Person("PARK1")         
obj2 = Person("PARK2")        

print("Person coutn = ", Person.getCount())
#Person coutn =  3
print(Person.count)
#3

#obj1.__printNames("adf") private 접근 안됨
#obj1.__name1 private 접근 안됨


#exception
def calc(list_data):
    sum = 0
    
    try:
        sum = list_data[0] + list_data[1] + list_data[2]
        
        if sum < 0:
            raise Exception("Sum is minus") # raise 인위적인 exception
        
    except IndexError as err:
        print(str(err))
    except Exception as err:
        print(str(err))
    finally:
        print(sum)
        
calc([1, 2])
calc([1, 2, -100])
        
# with : 자동 해제 기능
# ex> 파일 또는 session 순서는 보통 open()- > read() or write() -> close()
#일반적 방법
f = open("./file_test", "w")
f.write("hello")
f.close()

#with 구문 자동 close
with open("./file_test1", "w") as f1:
    f1.write("hello")

print("aa")