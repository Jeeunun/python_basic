a = 100
# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자. 
# 그런데 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
result = (((a+10)*20)/10)**2
print(result)

b = 200
result2 = (((b+10)*20)/10)**2
print(result2)
# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자. 
# input값이 있어도 되고, 없어도 된다. 
# return값이 있어도 되고, 없어도 된다. 

def myFunc(myInput):
    calc = (((myInput+10)*20)/10)**2
    return calc
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출하게 된다. 
result2 = myFunc(200) #200을 함수식에 input해서 return값이 도출된다. 


# myInput = int(input("숫자를 입력하세요: "))
# def myFunc(myInput):
#     calc = (((myInput+10)*20)/10)**2
#     return calc
# result = myFunc(myInput)
# print(result)

# 함수 직접 구현해보기
# 함수명은 myPlustFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 함수
# 예를 들면 100을 입력하면 1+2+3+4....+100
myInput = int(input("숫자를 입력하세요: "))
def myPlusFunc(myInput):
    for a in range(1,myInput+1):
        tot +=a 
    return tot
# 출력해보기
result = myPlusFunc(10)
print(result)

# 함수 직접 구현해보기
# input값을 2개를 받아 2값을 더한 뒤, *2만큼 하여 return하는 함수를 만들어보자.
# 그리고, 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자.
def myPlusFunc(myInput1,myInput2):
    calc = (myInput1+myInput2)*2
    return calc
# 출력해보기
result = myPlusFunc(10,20)
print(result)

# 문제)
# 리스트의 index함수를 쓰지 않고, for문 또는 while문을 통해 숫자 9가 몇 번째 인덱스에 있는 값인지 
# print해보자.  
# index함수
lista = [1,4,6,9,9]
print(lista.index(9)) 
# for문/while문
lista = [1,4,6,9,9]
for a in range(len(lista)):
    if lista[a] == 9:
        print(a)
        break
# 함수로 구현
# 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# input값이 2개 (list, 찾고자하는 값)
# print는 함수내에서 하지 않고, return에 값을 담는다. 
def myIndex(n1,n2):
    result = 0
    for n2 in range(len(n1)):
        if lista[a] == n2:
            result = a
            return n2
            break
    return result
    
# 출력해보기
lista = [1,4,6,9,9]
result = myIndex(lista,9)
print(result)

def myIndex(n1,n2):
    for n2 in range(len(n1)):
        if lista[a] == n2:
            print(n2)
            break
        
lista = [1,4,6,9,9]
def myIndex(i1,i2):
    result = -1
    for a in range(len(i1)):
        if lista[a] == i2:
            result = a
            break
    return result

def myIndex(i1,i2):
    for a in range(len(i1)):
        if lista[a] == i2:
            print(a)
            break

lista = [1,4,6,9,9]
r1 = myIndex(lista, 9)
print(r1)

# 문제 : 키보드로 반지름의 길이를 입력받고, 원의 넓이를 구하는 함수를 만들어 결과를 출력하라.
def circleSize(num1):
    result = num1*num1*3.14 #num1**2*3.14
    return result
        # return num1*num1*3.14으로도 가능.
num1 = int(input("반지름의 길이를 입력하세요: "))        
result = circleSize(num1)
print("원의 넓이 : " + str(result))

# 문제 : 
def hello1():
    print("hello1 python")
hello1()

def hello2():
    result = "hello2 python"
    return result
    #return "hello2 python"
print(hello2())

# 입력값의 개수가 정해져 있지 않고 multiple한 함수 ( * = all )
def sum(*args):
    total = 0
    for a in args:
        total +=a
    return total

totalValue = sum(1,2,3,4,5)
print(totalValue)

# 2개 이상의 리턴값이 있는 경우 : 튜플형태로 데이터 return
def cal(a,b):
    result1 = a+b
    result2 = a-b
    result3 = a*b
    return result1,result2,result3
calValue = cal(1,2)

def cal(a,b):
    result1 = a+b
    result2 = a-b
    result3 = a*b
    return result1,result2,result3
calValue = cal(1,2)
#계산한 첫번째 결과값은 XX, 두번째 결과값은 yy, 세번째 결과값은 zz
# 1
print(f'계산한 첫번째 값 : {calValue[0]}')
print(f'계산한 두번째 값 : {calValue[1]}')
print(f'계산한 세번째 값 : {calValue[2]}')
# 2
for x in range(len(calValue)):
    print(f'계산한 {x+1} 값 : {calValue[x]}')


# 함수에서 defalut값 미리 세팅
# defalut 셋팅 안한 경우
def cal(a,b,c):
    if c == 'plus':
        result = a+b
    elif c == 'minus':
        result = a-b
    elif c == 'multiply':
        result = a*b
    return result
# 출력
print(cal(1,2,"plus"))
print(cal(1,2,"minus"))
print(cal(1,2,"multiply"))

# defalut 셋팅 한 경우
def cal(a,b,c="plus"):
    if c == 'plus':
        result = a+b
    elif c == 'minus':
        result = a-b
    elif c == 'multiply':
        result = a*b
    return result
# 출력
print(cal(1,2)) #default는 + #3

# 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어 함수를 호출하는 방법
def whoAreYou(name, age, gender):
    print(f"제 이름은 {name}이고, 나이는 {age},성별은 {gender}입니다.")

# whoAreYou(19,'홍길동','남자') #문제:name에 19 age에 홍길동이 들어감.
whoAreYou(age=19, name='홍길동', gender='남자')


# 파이썬에서 default값 세팅하는 대표적인 예시가 print함수
# print 2개를 사용해서 줄바꿈 없이 hello world라고 출력이 되도록 만들어보자. 
print("hello", end=" ") #end(매개변수)=''옵션 => default값 줄바꿈을 옵션으로 바꿔줌.
print("world")

# 지역변수와 전역변수
# 지역변수 : 함수 내에서의 변수, 함수내에서만 유효 =>스택메모리에 저장 
# 전역변수 : 함수 밖에서의 변수, 함수내에서도 인식가능. =>데이터 메모리에 저장
a = 100 #전역변수
c = 200
def sum(a,b,c): #지역변수
    # 여기서 a =100인가? a=10인가?
    # 전역변수인 a=100보다 , 함수내에서 선언한 a=10우선적으로 인식.
    # 함수내에서 지역변수가 전역변수에 우선한다. 
    result = a+b +c
    return result
result = sum(10,20,30) 
print(result) #60 
# 함수내의 result라는 변수는 함수밖에서 인식불가
# 우리가 result프린트 할 수 있었던 것은, 함수내에서 어떤 값을 return 해줬기 때문.
print(a)    #100
# --------------------------
a = 100 #전역변수
c = 200
def sum(a,b): #지역변수
    # 함수내에서 함수 밖의 전역변수를 사용하려면 global키워드 사용
    global c
    result = a+b +c
    return result
result = sum(10,20) 
print(result) #230
# -------------------------
# for문 마다 같은 변수를 사용하는 것은 전역변수이기는 하지만, 재할당해서 사용하는 것이므로
# 어차피 reset되서 문제되지 않는다. 
lista = [10,20,30,40]
for a in range(len(lista)):
    print(a) #0,1,2,3
print(a) #3

# 함수 내에서 전역변수에 영향을 끼치는 방법 : global
# 기본적으로 함수내에서 함수밖의 전역변수를 수정할 수 없다. 
# 그 이유는 저장되는 메노리 위치가 다르기때문에 
result = 0
def sum(a):
    global result
    result +=a
    return result

value = sum(10)
print(value)
# --------------------------------
# 이중 for문을 사용할 때는 문제가 될 여지가 있다. 
# 다중 for문을 쓸때는 상위의 for문의 변수를 잃어버리게 되므로, 다른 변수명 사용.
lista = [10,20,30,40]
for a in range(len(lista)): #여기의  a가
    for a in range(len(lista)): #이 a로 재할당되기 때문에 문제가 된다. 
        print(a) 
# 해결
lista = [10,20,30,40]
for a in range(len(lista)): 
    for b in range(len(lista)): #다른 변수b사용
        print(b) 
# ----------------------------
# 객체는 힙메모리 영역에 저장되는데, 함수내에서도 접근하여 추가/수정이 가능하다. 
# 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다. 
lista = [2,3,4]
def appendTest(input1,input2):
    input1.append(input2) #왜 global선언하지 않고도 append가능? 

appendTest(lista,5) 
# list는 객체형태로 저장 -> 힙메모리
# lista는 매개변수 =>값을 가져오는게 아니라 메모리 주소를 가져오는 것
print(lista)

# ---------------------------------------------------------------
# 지역변수는 함수호출이 끝난 뒤 사라짐.
# but 만약에 지역변수가 함수호출이 끝난 뒤에도 남아있다면 어떻게 될까?
# def test1(result):
#         result += 10
#         return result
# def test2():
#         result += 100
#         return result 

# a = test1(20) #30
# b = test2() 
# 만약 함수호출이 끝난 뒤 남아있다면 test2()의 result와 더해지면서 130값도출
 
# 따라서 함수에서 사용하는 지역변수가 계속 메모리에 남아있으면, 메모리 낭비 뿐만 아니라, 
# 다른 함수에서 해당 변수명을 사용할 수 없는 불편함이 있다. 
# -------------------------------------------------------------
# 아래 선택정렬을 함수화 시켜서 활용해보기
def mySort(lista):
    for a in range(len(lista)-1): 
        for b in range(a+1,len(lista)):
            if lista[a] >= lista[b]:
                temp = lista[a]
                lista[a] = lista[b]
                lista[b] = temp
lst = [2,9,6,8,3]
mySort(lst)  # list.sort(lst)로도 호출 가능.
#return안해도 된다. => 메모리주소로 저장하기 때문에 
print(lst)
#  = 객체가 아닌 것은 원본형태로 저장되지 않고 메모리 주소로 저장때문에 return을 해줘야하고, 
# 객체인 것은 원본형태로 저장되기 때문에 return안해도 된다. 
# ----------------------------------------------------------------------
# 예시
lista = [5,1,2]
lista[0],lista[1] = lista[1],lista[0]
print(lista) #원본이 바뀜

temp = lista[0]
lista[0] = lista[1]
lista[1] = temp

# lista에 listb를 담으면, 객체의 주소가 복사가 된다.
# 그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게 된다. 
listb = [5,1,2]
listb = lista #값 뿐만 아니라 메모리 주소까지 카피함. 
lista[0] = listb[1] #lista[0] = lista[1]이랑 같아짐.
lista[1] = listb[0] #lista[1] = 바뀐 lista[0]이랑 같아짐.
print(lista)

# 주소 출력하는 함수 : id
print(id(lista))
print(id(listb))
# 출력해보면 주소가 같음을 알 수 있다.

# lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용 copy.copy() 
import copy
lista = [5,1,2]
listb = copy.copy(lista)

print(id(lista))
print(id(listb))
# 출력해보면 주소가 다름을 알 수 있다. 

# copy함수를 사용하지 않고 값을 복사하는 방법
lista = [5,1,2]
listb = []
for a in lista:
    listb.append(a)
# 이렇게 하면 copy함수를 사용하지 않고도 메모리 주소가 다른 listb를 만들 수 있다. 
# -------------------------------------------------------------------------------------
# 얕은 복사 즉, 객체 안의 객체의 값은 메모리 주소로 복사가 된다. 
# 깊은 복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사.
