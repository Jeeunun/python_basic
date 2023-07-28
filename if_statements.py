a = 10
if (a>5) | (a>100) :
    print('참입니다1.')
    # if a > 5 | a > 100 : -> 에러 : 소괄호()로 범위를 명확하게 해야함.
    # print('참입니다2.')
if a > 5 or a > 100 :
    print('참입니다2.')
# 비트연산이란 2진법의 숫자를 |(or),&(and,^(xor)등으로 cpu내부적으로 계산하는 방식.
# ex)
# 1111 and(&) 1000 => 1000 
# 1111 or(|) 1000 => 1111

# and는 &와 같고, or은 |와 같고, not은 부정의 의미
# not True는 False가 되고, not False는 True가 된다. 
a = 10
# not True
if not(a > 5 or a > 100) :
    print('참입니다.')
# not False
if not(a > 5 and a > 100) :
    print('참입니다.')

# 대입연산자
a = 10
# a = a+1 이렇게 표현해도 되고, a+=1 이렇게 표현해도 된다.
a +=1
print(a)
# -=,/=,*=
# a/=5 => a=a/5
print(a/5)

# 비교연산자 중에 chaining(범위로 표현할 수 있다.) 
a = 10
if a > 5 and 100 < a : # 5<a<10 표현 가능 (and의 의미) 
    print("참입니다.")

# if문의 기본 문법
# else는 optional 요소.
# else 상단에 있는 if 또는 elif에 종속된다. 
# elif도 마찬가지로 elif상단에 if에 종속된다. 
# 문제 : 숫자를 입력받아서, 90이하면 예각입니다 출력, 90이면 직각, 91~179면 둔각, 180이면 평행
# ~중 하나만을 실행시키고자 할 때는 elif를 if에 종속시켜 실행하면 실수가 없다. 
num1 = int(input("숫자를 입력해주세요: "))
if num1 < 90 :
    print("예각입니다.")
elif num1 == 90 :
    print("직각입니다.")
elif 90 < num1 < 180 :
    print( "둔각입니다.") 
elif num1 == 180 :
    print("평행입니다.")
#  num1<90 과 num1 <180에서 문제가 된다. => elif를 쓰는 이유.
if num1 < 90 :
    print("예각입니다.")
if num1 == 90 :
    print("직각입니다.")
if  num1 < 180 :
    print( "둔각입니다.") 
if num1 == 180 :
    print("평행입니다.")


# if 조건: 조건식이 참일 경우에만 실행문 실행
#         실행문
# else: 조건식이 거짓일 경우 실행문 실행
#         실행문

# else
a = int(input("숫자를 입력해주세요."))
if a >10:
    print("a는 10보다 큽니다.")
else:
    print("a는 10보다 작습니다.")

a = 10
if a > 5 :
    print("참 입니다.")
if a > 100 :
    print("참 입니다.")
else :
    print("거짓 입니다.") #앞선 if a >100에 종속되는 것 (if a> 5에 종속 X)
# 비교
if a > 5 :
    print("참 입니다.")
elif a > 100 :
    print("참 입니다.")
else :
    print("거짓 입니다.") #else는 if와 elif에 종속


trueOrFalse = True #값을 할당할 수 있다.
if trueOrFalse:
    print("참입니다.")
else : 
    print("거짓입니다.") 

# 자료형 불(불리언 : T/F)

# 연습문제1
# 얼마를 가지고 있습니까?를 변수에 담고, 만약 30,000원 이상이 있으면, 택시를 타고 가시오를 출력. 그렇지 않으면, 걸어가시오를 출력.
money = int(input("얼마를 가지고 있습니까? : "))
if money >= 30000 :
    print("택시를 타고 가시오.") 
else :
    print("걸어가시오.")

# if문 한줄로 쓰기 가능 => 코드가 짧고 단순한 경우에 아래와 같이 한 줄로 쓰는 것을 권장. 
a = 10
if a>1 : print('a는 1보다 큽니다.')
# 두 줄이상의 코드를 한줄로 적고 싶으면 => ; 세미콜론으로 구분. 
if a>1 : print('a는 1보다 큽니다.') ; print('a는 1보다 작습니다.')

# 조건부표현식(삼항연산자) : 간단한 식으로 표현
# 먼저, ;을 빼고 if문의 실행문을 if문 앞으로
a = 10
print('A는 10보다 큽니다.')if a > 10 else print('A는 10보다 작습니다.')
# 실행문을 실행하기 위해 사용한다기 보다는, 참인 경우에 어떤 값, 거짓인 경우에 어떤 값을 쉽게 result에 담기 위해 사용. 
result = 'A는 10보다 큼' if a>10 else 'A는 10보다 작음'
print(result)

# 문제 : 1~10까지 담고 있는 하나의 리스트가 있다. 키보드로 정수 하나를 입력 받아 위 리스트에 그 값이 있는지 알아내라.
lista = [1,2,3,4,5,6,7,8,9,10]
num = int(input("숫자를 입력하시오: "))
if num in lista :
   print("입력하신 값이 존재합니다.")
else :
    print("리스트에 포함되지 않았습니다.")

# for 문의 기본 구조
# for 변수 in 반복가능한 자료형 (iterable)
#     실행문
list = [1,2,3,4,5,6,7,8,9,10] # list는 대괄호써야함 / multiple 한 자료형
for a in list : 
    print('원소 : ' , a)

# range 문법 : range(x,y) x이상 y미만
for a in range(1,101) : 
    print(a)

# 참고 다른 언어에서는...
# 예시 : listb값을 모두 출력해주세요
listb = ['a','b','c','d']
for b in range(0,len(listb)) : #0,1,2,3 값이 들어있다.
    print(listb[b])            #인덱스로 접근함. 

# 연습문제
# 내가 푼 것 -> 틀림
weight = int(input("짐의 무게는 얼마입니까? : "))
if weight >= 10 :
    print("수수료는 {}입니다." ,format(10000*(weight//10))) #print("수수료는 %d 입니다. " % 10000*(weight//10))
else :
    print("수수료는 없습니다.")

# 선생님이 푼 것
numinput = int(input("짐의 무게는 얼마입니까? : "))
weight = (numinput//10) * 10000
print( "짐의 무게는 %d 이고 수수료는 %d 입니다." %(numinput,weight))

# f formating
print(f"짐의 무게는 {numinput} 이고 수수료는 {weight} 입니다.")
print("짐의 무게는" + numinput + "수수료는"+ weight + "입니다.") #-> 로그를 찍을 때 사용. 

# 연습문제
# input값으로 가진 돈과 배가 고픈지 여부를 받아서 처리
# 돈이 만원이상 있고 배가 고프면 저녁을 사먹으시오를 출력. 그렇지 않으면 집에 가시오를 출력. 
money = int(input("가진 돈은 얼마 입니까? : "))
A = input("배가 고프신가요? yes or no로 대답해주세요 : ")
if money >= 10000 and A == "yes" :
    print("저녁을 사먹으시오.")
else :
    print("집에 가시오.")

# a와 b가 같은지 비교하는 연산자 is
# 객체 타입의 경우에는 메모리 주소를 비교하고 /  숫자, 문자, bool 기본타입의 경우 값을 비교한다. 
# 숫자, 문자, bool같은 경우에는 데이터 pool을 만들어서, 재활용한다. 
# 그래서, 값을 비교할 때 메모리 주소가 아니라, 데이터 pool에서 값을 비교.
a = 10
b = 10
if a is b:
    print("참입니다.") #=> 데이터 pool에서 값을 비교. => 같은 주소에 할당하여 맵핑. => #True
# a = [10,20]
# b = [10,20]
# if a is b:
#     print("참입니다.") => 데이터 메모리 주소에 각각 할당해서 비교. => 주소가 다름 => #false

a = 10
b = 10
if a == b : 
    pass    #pass 시킴.(pass를 명시적으로 표현한 것.)
else :
    print('두 값이 다릅니다.')

