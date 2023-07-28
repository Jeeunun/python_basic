# # class의 사용 이유
# # 1) 같은 기능의 함수의 집합
# # 2) 객체를 만들기 위해 사용


# # 사칙연산 함수가 있을 때, 같은 기능을 하므로, Calculator 라는 클래스에 모아둘 수 있다. 
# # 명명 규칙 : 일반적으로 클래스는 대문자 알파벳으로 시작
# # 변수명, 함수명은 소문자로 시작 -> camelcase
# # ex) myImportantList / my_important_list 
# # 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태
# class Calculator:
#     def plus(a,b):
#         return a+b
#     def minus(a,b):
#         return a-b
#     def multiply(a,b):
#         return a*b
#     def divide(a,b):
#         return a/b
# print(Calculator.plus(10,20))
# # 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고 있지 않다. 
# class Calculator:
#     result = 0 
#     # 클래스 변수 접근가능 방법1: 클래스명.변수
#     # 클래스 변수 접근가능 방법2: classmethod 데코레이터 사용
#     # class내에 선언된 함수는 메서드라 부른다. 
#     @classmethod
#     def plus(cls,a): #@classmethod선언
#         cls.result+=a #Calculator함수에 누적변수result => result값에 계속해서 누적 가능.
#     def minus(a):
#         Calculator.result-=a
#     def multiply(a):
#         Calculator.result*=a 
#     def divide(a):
#         Calculator.result/=a       
# print(Calculator.result)
# Calculator.plus(10)
# print(Calculator.result)
# Calculator.minus(5)
# print(Calculator.result)

# # 객체란 클래스의 복제본, 인스턴스라 부르기도 한다.  (객체 = 인스턴스)
# # 객체의 사용이유
# # 클래스의 중복제거 : 변수와 함수의 재활용의 어려움 해결
# # 객체 형식의 클래스의 기본구조
# class Calculator:
#     # 객체가 생성될때 init은 가장 먼저 실행된다.
#     # 생성자는 객체생성될 때 객체변수를 초기화. 
#     # result와 self.result는 다른 값이다. => result(지역변수) / self.result(객체의 변수)
#     def __init__(self): # 생성자(__init__) 선언
#         self.result=0   # 최초값(객체변수의 초기화)
#     # 객체를 만들 때 매서드 내의 첫번째 매개변수는 객체(self)를 의미한다. 
#     def plus(self,a):
#         self.result+=a 
#     def minus(self,a):
#         self.result-=a
#     def multiply(self,a):
#         self.result*=a 
#     def divide(self,a):
#         self.result/=a    

# aCompany = Calculator() #객체가 만들어짐 => Calculator의 복제본. => aCompany의 Calculator => self = aCompany
# aCompany.plus(100)
# bCompany = Calculator() #객체가 만들어짐 => Calculator의 복제본. => bCompany의 Calculator => self = bCompany
# bCompany.plus(100) 
# print(aCompany.result)
# print(bCompany.result) 

# # ------------------------------------------------
# # 옵션주기
# # 클래스생성시 매개변수(a)를 통해 초기값 세팅가능 
# class Calculator:
#     def __init__(self,a): 
#         self.result=a   
#     def plus(self,a):
#         self.result+=a 
#     def minus(self,a):
#         self.result-=a
#     def multiply(self,a):
#         self.result*=a 
#     def divide(self,a):
#         self.result/=a    
# aCompany = Calculator(1000)
# print(aCompany.result)
# aCompany = Calculator(2000)
# print(bCompany.result) 

# # person이라는 클래스를 만든다. 생성자로 이름(name), 나이(age), 성별(gender), email이라는 매개변수를 받아 각각의 객체변수를 만든다. 
# # register 메서드를 만들어서 해당메서드에서는 myInfo라는 객체변수에 이름, 나이, 성별, email정보를 문자열로 담는다. 
# # 2명의 person을 만든다.
# # p1.register()
# # print(p1.myInfo)
# # print(p2.myInfo)
# class Person:
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#     def register(self):
#         self.myInfo = "이름: {}, 나이: {}, 성별: {}, email: {} " .format(self.name, self.age, self.gender, self.email)

# p1 = Person('홍길동', '25','남자','1234@naver.com')
# p2 = Person('손흥민', '30', '남자','5678@gmail.com')

# p1.register()
# p2.register()

# print(p1.myInfo)
# print(p2.myInfo)

# # --------------
# # 
# import datetime
# register_date = datetime.datetime.now()
# print(register_date)

# class Person:
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.register_date = str(datetime.datetime.now())
#     def register(self):
#         self.myInfo = "이름: {}, 나이: {}, 성별: {}, email: {}, 회원가입일: {} " .format(self.name, self.age, self.gender, self.email, self.register_date)

# p1 = Person('홍길동', '25','남자','1234@naver.com')
# p2 = Person('손흥민', '30', '남자','5678@gmail.com')

# p1.register()
# p2.register()

# print(p1.myInfo)
# print(p2.myInfo)

# -------------------
#  <클래스의 상속>
# 부모 클래스에서의 기능을 자식클래스에서 물려받는 것
# class 자식클래스명(부모클래스명) 이런 형식으로 선언
class Calculator:
    def __init__(self): 
        self.result= 0 
    def plus(self,a):
        self.result+=a 
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a

# Calculator 상속 후 divide 메서드 추가
class CalculatorChild(Calculator):
    # def __init__(self):
    #     self.result = 100
    #     # 자식클래스의 init설정할 수 있다. (=부모클래스의 init을 덮어쓰는 것.)
    def divide(self,a):
        self.result /= a
    # 부모한테 있는 기능을 재선언하게 되면, 부모의 기능보다 자식의 기능이 우선하게 되고, 이를 overriding이라 한다. 
    def multiply(self,a):
        self.result*=(a+1)  

        # Q. 오버로딩과 오버라이딩 구분할 것!!!! (파이썬은 오버로딩 지원X)

if __name__=="__main__": 
    cc1 = CalculatorChild() 
    cc1.plus(100)
    print(cc1.result)
# cc1.divide(10)
# cc1.multiply(10)

# print(cc1) 
#<__main__.CalculatorChild object at 0x000001C957F1C310> => 메모리 주소로 출력된다. 
# print함수가 속해있는 클래스는 object 클래스를 상속받고 있다.
# 그런데 object 클래스 안에는 list, dict 같은 파이썬에서 자주 사용되는 객체값을 value형식으로 출력해주는 함수가 내장돼있다.



