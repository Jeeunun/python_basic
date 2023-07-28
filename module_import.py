# import하고 싶은 모듈이 있으면 import구문을 사용
# from 패키지명 import 파일명 또는 import 패키지명.파일명
from module_test import module_statements #모듈테스트 폴더에 있는 모듈 스테이트먼트 파일 가져오기
print(module_statements.plus(10,20))
# as를 사용하여 약어로도 사용가능
import module_test.module_statements as ms 
print(ms.plus(10,20))

import class_stataements
c1 = class_stataements.CalculatorChild()

c1.plus(100)
print(f"module_import의 result : {c1.result}")

# # ex)
# from datetime import datetime as dt
# register_date = dt.now()
# print(register_date)

# class Person:
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.register_date = str(dt.now())
#     def register(self):
#         self.myInfo = "이름: {}, 나이: {}, 성별: {}, email: {}, 회원가입일: {} " .format(self.name, self.age, self.gender, self.email,)

# p1 = Person('홍길동', '25','남자','1234@naver.com')
# p2 = Person('손흥민', '30', '남자','5678@gmail.com')

# p1.register()
# p2.register()

# print(p1.myInfo)
# print(p2.myInfo)
