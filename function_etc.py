# 람다함수 : 1)함수를 간편하게 표현하기 위한 방식 2)함수를 변수에 담기 위한 방식(함수를 변수처럼 쓴다.)
# 기본 형태 : lambda 매개변수 :실행문

# 1) 함수를 간편하게 표현하기 위함
# 예시
def add(a,b):
    return a+b
print(add(1,2))
# 람다함수로 표현하기
add_lambda = lambda a, b : a+b
print(add_lambda(1,2))

# 매개변수 a를 입력했을때 a의 제곱이 출력되는 람다함수
lambdaA = lambda a : a**2

# list에 lambda함수를 담아서 사용가능.
cal_list = [lambda a,b: a+b , lambda a,b : a-b, lambda a,b : a*b]
print(cal_list[0](1,2))
print(cal_list[1](1,2))
print(cal_list[2](1,2))
# dictionary에 lambda함수 담아서 사용가능.
cal_dict = {"plus": lambda a,b: a+b , "minus": lambda a,b : a-b, "multiply": lambda a,b : a*b}
print(cal_dict["plus"](1,2))
print(cal_dict["minus"](1,2))
print(cal_dict["multiply"](1,2))

# 2) 함수를 변수로 쓰기 위함.
# lambda로 입력한 매개변수가 짝수이면 True, 홀수이면 False
# 예시 if else 쓸 수 있다.
def oddOrNot(x):
    if x %2 == 0:
        return True
    else:
        return False
# lambda로 표현하기
oddOrNot = lambda x : True if x % 2 == 0 else False
# truOrNot = True if input%2 == 0 else False (삼항연산자)

# break할 필요없이 함수내에서 return => 함수 자체가 종료되서
lista = [1,4,6,9,9]
def myIndex(i1,i2):
    result = -1
    for a in range(len(i1)):
        if lista[a] == i2:
            result = a
            #break할 필요 없이, 바로 return을 해도 된다.
            # return하게 되면 함수 전체가 강제 종료된다. 
            return result 
        
# --------------------
# map함수 : 특정함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을 return하는 함수
# 사용예시 : map(함수, 리스트(또는 튜플 등등))

# 예시
def two_times(x):
    return x*2
print(map(two_times, [1,2,3,4]))
# <map object at 0x0000020E6232EB90>
lst = list(map(two_times, [1,2,3,4]))
print(lst)
# [2, 4, 6, 8]

# map함수와 lambda함수를 사용해서 입력한 list의 제곱값을 담은 리스트를 출력하도록 하자.
lst = list(map(lambda x : x**2,[2,4,6,8]))
print(lst)
# [4, 16, 36, 64]

# ------------------------
# filter함수
# 비교 : map의 역할은 대상이 되는 리스트를 가지고, 함수를 적용하여 새로운 리스트를 만들어내는 것.
# filter의 역할은 대상이 되는 리스트에서 함수를 적용하여 참/거짓 조건으로 값을 걸러내는 것. -> 참인 것만 뽑는 것!
# filter(함수, 반복가능한 자료형)
# 예시:
def trueOrNot(x):
    if x > 0 :
        return True
    else:
        return False
lst = list(filter(trueOrNot, [-1,0,3,-2,5]))
print(lst)

# 위 로직을 lambda함수로 바꿔보자(삼항연산자)
lst = list(filter(lambda x : True if x > 0 else False, [-1,0,3,-2,5]))
print(lst)
    # map과 비교
    # lst = list(map(lambda x : True if x > 0 else False, [-1,0,3,-2,5]))
    # print(lst)
    # [False, False, True, False, True]
    # =true false가 새로운 리스트에 담기게 된다. 

# 함수형 프로그래밍(lambda,map,filter)을 사용하여, 주어진 list에서 홀수만 추출하도록 하여라.
lista = [4,7,1,2,5,6,8]
lst = list(filter(lambda x : True if x %2 != 0 else False, lista ))
lst.sort()
print(lst)
# [1, 5, 7]

# lst = list(map(lambda x : x**2, lst = list(filter(lambda x : True if x %2 != 0 else False, lista))))
# print(lst)
# --------------------------------------------
# sum : 주어진 자료들의 총합
print(sum([1,2,3])) #6
# 위 코드의 총합을 구하여라
sum_value = sum(filter(lambda x : True if x %2 != 0 else False, [4,7,1,2,5,6,8] )) 
print(sum_value)
# --------------------------------------------
# 문자를 아스키코드 변환 : ord()
print(ord('a')) #97
# 숫자 107이 의미하는 아스키코드상의 문자는 뭘까? chr()
print(chr(107)) #k
# 아스키코드 반환 활용
# - 문) 예를 들어 문자열이 주어질때 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라.
str = '123asdf512kjlk'
print(ord('z')) #122 => 소문자 a~z : 97~122
print(ord('Z')) #90 => 대문자 A~Z : 65~90

new_str = ""
for a in str:
    if (122>=ord(a) >=97) or (65>=ord(a)>=90):
        new_str +=a
print(new_str) #asdfkjlk

#   -> 현실에선 정규표현식으로 간단하게 표현함
# ------------------------------------------------
# 절대값 구하기 :abs()
print(abs(-3)) #3
#   문) map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트를 출력해보자. 
lista = [1,-5,12,-5]
lst = list(map(abs,lista))
print(lst)

    # 함수를 안쓰고 for 반복문으로도 풀어보기!!!!!!!!!!

# ----------------------------------------------
# 재귀함수
# 전형적인 예제 : factorial 예제 (10! = 10X9X8X...X1)
# 변수 n을 넣었을때 n!가 나오도록 함수를 만들어보자.

def solution(n):
    tot=1
    for a in range(1,n+1):
        tot*=a
    return tot

n = int(input("숫자를 입력하세요: "))
answer = solution(n)
print(answer)
# -------------
# <반복문for>
def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

print(factorial(5))
# <재귀함수로 구현>
#   -수학의 수열의 점화식 - 이웃한 항의 관계를 통해 수열을 나타내는 것
#   -팩토리얼 점화식 
#   n이 2이상의 수일 때 n!= n X (n-1)!
def factorial(n):
    if n==1:
        return 1
    elif n>=2:
        return n*factorial(n-1)
    

# 재귀함수를 통한 factorial 예제
# 재귀함수란 함수내에서 함수자기자신을 호출하는 방식.
# 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야 한다. 
    # def test(n):
    #     return  n+test(n)

    # result = test(10)
    # print(result)
    # # 10+test(10) => 10+10+test(10) =>..... (무한루프에 빠질 가능성)

    # def test(n):
    #     return  n+test(n-1)

    # result = test(10)
    # print(result)
    # #  10 + test(9) => 10+9+test(8)=> ..... 

def test(n):
    if n==1:
        return 1
    return  n+test(n-1)

result = test(10)
print(result)

# 재귀함수로 factorial구하기
def factorial(n):
    if n==1:
        return 1
    return  n*factorial(n-1)

# 출력해보기 
result = factorial(10)
print(result)

# 재귀함수를 반드시 써야만 하는 상황 = 반복의 횟수를 알 수 없을 때
#  문제) lista = [10,20,30,40,50]. 5개의 숫자 중에 2개씩 숫자를 추출하는 경우의 수를 구하고자 한다. 
#       2개씩 숫자를 추출하여 list에 담아 마지막에 모든 리스트를 출력하도록 하여라. = lista의 조합을 구하여라.
# 출력예시] [[10,20],[10,30],[10,40],[10,50],[20,30],[20,40],[20,50],[30,40],[30,50],[40,50]]
lista = [10,20,30,40,50]
listb =[]
for a in range(len(lista)-1): #a=0~4
    for b in range(a+1,len(lista)): #b=1~4
        listb.append([lista[a],lista[b]])
print(listb)
print(len(listb))

count = 0
for a in range(len(lista)-1): #a=0~4
    for b in range(a+1,len(lista)): #b=1~4
        count+=1
        listb.append([lista[a],lista[b]])
        print(count)
print(listb)

# # 재귀함수로 표현해보기 : 매개변수로 list와 조합해야할 k개의 숫자가 주어진다. lista의 m개씩의 조합을 구하여 리스트에 담아 출력하여라.
count = 0
for a in range(len(lista)-1): #a=0~4
    for b in range(a+1,len(lista)): #b=1~4
         for c in range(b+1,len(lista)): #b=1~4
            count+=1
            listb.append([lista[a],lista[b],lista[c]])
            print(count)
print(listb) # for문이 무한대가 된다... => 재귀함수

# 재귀함수
# 조합
def recur(lista, total_list, temp_list, n, m):
    if m == 0:
        total_list.append(temp_list[:]) #값을append하기 위해 [:] 사용.
        return                          #-----> recur 함수 종료
    for a in range(n, len(lista)):
        temp_list.append(lista[a])
        recur(lista, total_list, temp_list, a+1, m-1)
        temp_list.pop()                 


# 호출
input1 = [10,20,30,40,50]
total_list =[]
input2 = 3
recur(input1,total_list, [], 0, input2)
print(len(total_list)) #경우의 수 

# 순열?

# -----------------------------------------------------------------

# 재귀함수
# 팩토리얼

# def fac(n):
#     #기본으로 while True
#     return n * fac(n-1) *...fac(1)


# import math
# help(math.factorial(6))


# ---------------------------------------------

