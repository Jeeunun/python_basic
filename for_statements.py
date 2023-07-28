# while문의 기본 구조
# while 조건식: #조건식이 참인 경우 반복 => 무한반복이 기본전제
#      ~ 실행문
# a = 10
# while a>5:
#     print("참입니다.")

# 조건을 체크 후 True이면 실행문을 1회 실행시키고, 다시 조건을 체크하러 돌아온다. 그리고 True이면 또 다시 실행
# 그러다, 조건이 False가 되면 while문 종료.
a = 0
while a<5:
    print(str(a)+'번 반복')
    a+=1

# 1~1000까지만 프린트 되도록 출력
a = 1
while a <1001:
    print(str(a) + '번 반복')
    a+=1

a = 0
while a <1000:
    a+=1
    print(str(a) + '번 반복')
    
# 1~1000까지 모두 더한 값(b), 평균값 출력
a=1
b=0
while a <1001:
    b+=a
    a+=1
print(b)
print(b/1000)

# while문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
# 1) if문을 써서 XXX한 조건에 break
a=1
b=0
while True:
    b+=a
    if a == 1000:
        break
    a+=1
print(b)
print(b/1000)

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동.
# 하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다. 
# 아래와 같이 코딩하면 hello가 무한 출력
# a = 0
# while a<1000:
#     print("hello")
#     continue
#     a+=1
# 문제
a=0
b=0
while a<1000:
    a+=1
    if a % 2 == 0:
        #continue문을 활용해서 coding
        continue   
    b+=a       
print(b)

# 2) 1~1000중에 홀수만 더해서 출력 #251001
a=0
b=0
while a<1001:
    a+=1
    if a % 2!=0:
        b+=a
print(b)
#문제 : 나만의 리스트 만들기
# 리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고, 리스트의 크기와 값 전체를 출력하라.
# while True:
#     num = int(input("리스트의 크기를 입력하세요: "))
#     if num > 10:
#         print("다시 입력해주세요: ")
#         continue
#     lista=[]
#     a=0
#     while a < num:
#         listvalue = input("리스트의 값을 입력해주세요: ")
#         lista.append(listvalue)
#         a+=1
#     print(lista)

# # 내가 푼 것
# listsize = int(input("리스트의 크기를 입력하세요: "))
# a=0
# lista=[]
# while a<listsize:
#     listavalue=input("리스트의 값을 입력하세요: ")
#     lista.append(listavalue)
#     a+=1
# print(lista)

# 문제 : 로또 번호 생성기
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자. 
# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random 

import random
print(random.randint(1,45))
lista=[]
listasize=1
while listasize < 7:
    randNum = random.randint(1,45)
    lista.append(randNum)
    listasize+=1
print(lista)

# for 문의 기본 구조
# for 변수 in 반복가능한 자료형 (iterable)
#     실행문
list = [1,2,3,4,5,6,7,8,9,10] # list는 대괄호써야함 / multiple 한 자료형
for a in list : 
    print('원소 : ' , a)

# range문법 : range(x,y) x이상y미만
for a in range(1,101):

# range의 의미: iterable 객체
# a = list(range(1,10))
# print(v1)

# range(x,y) : x이상 y미만의 숫자를 담은 객체
# range(y) : 0이상 y미만의 숫자를 담은 객체
    v1 = list(range(10,20))
# for a in 리스트를 써서 v1의 값을 모두 출력
for a in v1:
    print(a)
# for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력
for a in range(0,10):
    print(v1[a])

# for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다. ->  인덱스로 !
lista = [10,20,30,40,50,60,70,80,90,100]
lista[5] = 100
# for a in lista:
#     a = 100 #이런 방식으로는 원본의 lista의 값을 변경할 수 없다.

# 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다. 
for a in range(len(lista)):
    lista[a] = 100

print(lista)

# 리스트를 만드는 방법 중에 리스트 컴프리헨션이라는 방법이 있다. 
# 리스트에 0~9까지를 담는 방법
#방법1
lista = [0,1,2,3,4,5,6,7,8,9]
#방법2
lista = list(range(10))
#방법3
lista =[]
for a in range(10):
    lista.append(a)
    
#방법4 : 리스트컴프리헨션
# 장점: 간결하다.
lista=[a*2 for a in range(10)]
print(lista)

# 홀수인 값에 2를 곱한 값만을 list로 만들어라.
lista =[]
for a in range(10):
    if a % 2!=0:
        lista.append(a*2)

lista=[a*2 for a in range(10) if a%2 !=0]
print(lista)


# 문제 : 1반에 수학점수가 60점이 넘으면 합격. 60점 미만이면 불합격.
lista = [90,25,67,45,80]
# 위 리스트가 학생의 번호순서대로 있을 때, 아래와 같이 출력하도록 코딩하여라. 
# 출력 예시 : "1번학생은 합격입니다."
# # 내가 푼 것 => 같은 점수가 있는 경우 문제가 된다. 
# for score in lista:
#     if score >= 60:
#         print(lista.index(score)+1,"번 학생은 합격입니다.")
#     else :
#         print(lista.index(score)+1,"번 학생은 불합격입니다.")
# 방법1
lista = [90,25,67,45,80]
num = 1
for score in lista:
    if score >= 60:
        print("%d 번 학생은 합격입니다."%num)
    else :
         print("%d 번 학생은 불합격입니다."%num)
    num+=1
# 방법2
lista = [90,25,67,45,80]
for a in range((len(lista))):
    if lista[a]>= 60:
        print("%d 번 학생은 합격입니다." %(a+1))
    else :
         print("%d 번 학생은 불합격입니다." %(a+1))

    
# for문과 break : for문에서 break를 반드시 써야 하는 상황
# 혈액형이 A형인 고객 선착순 1명만 찾는 상황.
lista = ['b','b','ab','a','b','a']
# 출력 결과 : n번째 고객이 이벤트에 당첨되었습니다. 
num = 1
for a in lista:
    if a == 'a':
        print("%d 번째 고객이 이벤트에 당첨되었습니다." %num)
        num+=1
        break

for a in range(len(lista)):
    if list[a] == 'a':
        print("%d 번째 고객이 이벤트에 당첨되었습니다." % (a+1))
        break

answer = 0
for a in range(len(lista)):
    if lista[a] == 'a':
        answer = a + 1
        # break를 넣고 안넣고 결과값 차이 확인
        break
print(str(answer),"번째 고객이 당첨되었습니다.")

# for문을 이용한 구구단
# 구구단 5단을 출력해보자 예를 들어)
# 5단 결과 출력 : 5X1 = 5.....5X10 = 50

for a in range(1,10):
    print(f' 5 * {a} = {5*a}')

numinput = int(input("구구단 몇단을 계산해드릴까요?: "))
for a in range(1,11):
    print(f"{numinput} X {a} = {numinput * a}") 


#2중 for문
# 구구단을 5단~9단까지 한꺼번에 출력
# 방법1
for a in range(5,10):
    for b in range(1,11):
        print(f"{a} X {b} = {a * b}")
# 방법2
num = 5        
while num < 10:
    for a in range(1,11):
        print(f"{num} X {a} = {num * a}") 
    num +=1

# 문제
lista = [10,20,30,40]
# lista[0]와 lista[1]의 자리를 바꾸려면? #lista = [20,20,30,40]
# 문제
lista[0] = lista[1]
lista[1] = lista[0] #문제 => 변경된 lista[0]이 lista[1]에 담겨짐.

# 방법
temp = lista[0]
lista[0] = lista[1]
lista[1] = temp
print(lista)

# 파이썬에서 지원하고 있는 문법
lista[0],lista[1] = lista[1],lista[0]

# for문을 이용한 정렬 알고리즘
lista = [93,45,21,30,20,94,66,71,45]
# 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# sort() 내장함수 이용
lista.sort()
print(lista)

# 선택정렬 : 0번째 index부터 가장 작은 값을 채워나가는 방식.
# 첫번째 for문은 채워나가야할 index를 의미.
# 두번째 for문은 비교의 대상이 되는 index를 의미.
# # 내가 푼 것
# for a in range(len(lista)):
#     for b in range(len(lista)-1):
#         if lista[a] > lista[b]:
#             lista[a] = lista[b]
#             lista[b] = lista[a]
# print(lista)  

# 방법
for a in range(len(lista)):
    k = len(lista) - 1
    for b in range(1,k):
        if lista[a] >= lista[b]:
            temp = lista[a]
            lista[a] = lista[b]
            lista[b] = temp
print(lista)

# 방법
for a in range(len(lista)-1): #lista의 마지막 자리는 비교대상이 없기 때문에 
    for b in range(a+1,len(lista)):
        if lista[a] >= lista[b]:
            temp = lista[a]
            lista[a] = lista[b]
            lista[b] = temp
print(lista)

# 버블정렬 : 큰 수를 마지막으로 밀어내는 것. 
lista = [93,45,21,30,20,94,66,71,45]
# 내가 푼 것.
for a in range(len(lista)): #a=0~8
    for b in range(1,len(lista)): #b=1~8
        if lista[a] > lista[b]:          
            lista[b] = lista[a]
            lista[a] = lista[b] 
print(lista)
# 방법
arr = [93,45,21,30,20,94,66,71,45]
for i in range(len(arr) - 1, 0, -1): #range(8,0,-1) => 8번째부터 0까지 간격0 => i =8~0
    for j in range(i):              #j = 7~0
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 프로그래머스 - 행렬의 덧셈
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 
# 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 
# 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 내가 푼 것
# arr1 = [[1],[2]]
# arr2 = [[3],[4]]

# for a in range(len(arr1)-1):
#     for b in range(len(arr2)-1):
#         print(arr1[a][a] + arr2[b][b])

# 방법
# 두행렬의 행과 열은 항상 같게 주어진다. 
# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# answer = []
# # answer = [[arr1[0][0]+arr2[0][0], arr1[0][1]+arr2[0][1]], [arr1[1][0]+arr2[1][0], arr1[1][1]+arr2[1][1]]]
# for a in range(len(arr1)):
#     temp = []
#     for b in range(len(arr1[a])):
#         temp.append(arr1[a][b]+arr2[a][b])
#     answer.apppend(temp)

def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):     
        temp = []
        for b in range(len(arr1[a])):
            temp.append(arr1[a][b]+arr2[a][b])
        answer.append(temp)
    return answer