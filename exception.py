# <예외처리 : try except 구문>
# 1. 예외처리를 하는 이유는 프로그램 실행 중간에 예외가 발생하더라도 프로그램이 강제 종료되지 않도록 하기 위해.
#       -> 현실에서 빈번하게 발생할 수 있는 경우(사용자input, DB조회) 예외처리를 한다..! => cpu의 메모리 효율을 위해서 
while True:
    try:
        first = int(input("분자를 입력해주세요: "))
        second = int(input("분모를 입력해주세요: "))
    # 사용자가 0으로 숫자를 나누게 되면 division by zero 에러발생
    # 문제 발생 가능성이 있는 곳에 try
        print(first / second) 
    # 문제 발생했을 때 이후의 action except
    # except 순차적으로 실행된다. 
    except ZeroDivisionError as zd:
        print(f"{zd} 오류입니다.") 
    except ValueError as ve:
        print(f"{ve} 오류입니다.")
    except Exception:
        print(f"{Exception} 오류입니다.")  #모든 예외를 except 해준다. 쓰는 게 좋다!
    # finally는 문제가 있든 없든 무조건 실행
    finally:
        print("결과를 확인해주세요.")

# 2. 에러 강제의 예시
# while True:
#     raise Exception
class Bird:
    def fly(self):
        raise Exception
    
class Eagle(Bird):
    pass

eagle1 = Eagle() #객체만들기
eagle1.fly() #함수적용 => 출력 : Exception => 오버라이딩 강제

# -->  자식클래스로 하여금 overriding 재정의 유도 해준다. 
class Bird:
    def fly(self):
        raise Exception
    
class Eagle(Bird):
    def fly(self):
        print("fly fly")
    pass

eagle1 = Eagle() 
eagle1.fly()

