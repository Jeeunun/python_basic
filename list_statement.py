# list 는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로 한 변수에 값을 집합시켜놓은 것.
# 하나의 변수로 여러개의 데이터를 관리
# list의 경우에 [] 대괄호를 사용하여 데이터를 집합 cf.tuple -> {}()
lista = ['a', 'b' ,'c', 'd', 'e', 'f', 'g']

# list안의 각각의 값에 접근할 때에는 index를 사용.
print(lista[0])
print(lista[1])
print(lista[2])

 # 여러개의 데이터를 범위를 지정해서 가져오고 싶을 때는 slicing사용.
print(lista[:5])
print(type(lista[:5])) #데이터의 타입

# 문자열은 메모리 내부적으로 list와 유사한 자료구조
# 문자열은 값을 추가하거나 수정할 수가 없다.
# list는 값의 추가, 삭제, 수정이 가능한 구조를 가지고 있다.  순서가 있다. 

# 연습문제 (인덱싱)
# list안에 list의 값을 조회하는 방법 -> 인덱스 이용 cf.딕셔너리
# list_ex1 = ['a','b','c',[1,2,3]]이라는 리스트가 있다. 변수 number에 [1,2,3]을 담아 출력하라. number에 담은 값 중 1과 3을 더해 4를 출력하라. 
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number)
print(number[0]+number[2])
print(list_ex1[3][0]+list_ex1[3][2])

# 리스트 더하기 
# list를 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보고 출력.
lista = ['a','b','c','d','e']
listb = [1,2,3,4,5]
print(lista+listb)

# 리스트 곱하기 : 리스트*리스트 (X) 리스트*문자(O)
lista = ['a','b','c']
listb = [1,2,3]
listc = lista + listb
print(listc*2)
# 리스트 *문자 곱하기도 해보기

# 리스트 길이 구하기 : len
print(len(lista))

# 리스트 값 수정하기(인덱스로 활용)
# -> 1개의 값만 바꿀 땐 1개의 값으로 대체 
# -> 여러값을 바꿀 땐 다른 리스트로 대체
lista = [1,3,5,6,7,9]
lista[1] = 4
print(lista)
lista[2] = [5,5,5]
print(lista)

# 리스트 요소 개수 세기
lista = ["1","2","3","4","1","1","3"]
counta = lista.count("1")
print(counta)

# 리스트 요소 삭제하기 : del, remove
# del 변수 [index]
lista = ["1","2","3","4","1","1","3"]
del lista[0:3]
print(lista)
lista = ["1","2","3","4","1","1","3"]
del lista[2]
print(lista)
# remove : 리스트.remove(값)
lista = ["1","2","3","4","1","1","3"]
lista.remove("1")
print(lista)

# 모든 특정한 숫자 9값을 삭제하려면?
# lista = [1,3,9,3,5,6,9,9]
# for a in range(0,len(lista)) : 
#     if lista[a] == 9:
#         del lista[a]
# print(a) 
#왜 에러가 날까? 
# lista[0] != 9 -> lista[0] = 1
# lista[1] != 9 -> lista[1] = 3
# lista[2] == 9 -> del lista[2] => lista = [1,3,3,5,6,9,9]
# lista[3] != 9 -> lista[3] = 5 => index Error :  del 하면 인덱스가 삭제한 자리에 앞으로 땡겨진다. lista[2]를 해야하는데

# 해결 [방법1]
lista = [1,3,9,3,5,6,9,9]
count = 0 
for a in range(0,len(lista)) :
    if lista[a-count] == 9: 
        del lista[a-count]
        count = count + 1 
        # if lista[a]==9, del lista[a]라면 lista=[1,3,3,5,6,9,9] 
        # -> 다음 인덱스 검사는 lista[2]를 체크해야하는데 lista[3]부터 시작함 -> a-count해야함
print(lista)
# lista[0-0] != 9 -> lista =[1]
# lista[1-0] != 9 -> lista = [3]
# lista[2-0] == 9 -> lista[2-0] 삭제 & count = 0+1
# lista[3-1] !=3 ( )

# 해결 [방법2]
lista = [1,3,9,3,5,6,9,9]
listb = []
for a in range(0,len(lista)) :
    if lista[a] != 9: 
        listb = listb + [lista[a]]   #listb = 1 
        listb.append(lista[a])
print(listb) 
#lista[0] != 9 -> listb = listb + lista[0] = 1 -> listb.append(lista[0]) =listb.append(1) = print(listb) =[1]
#lista[1] != 9 -> listb = listb + lista[1] = [1] + [3] -> listb.append = print(listb) = [1,3]
#lista[2] == 9 -> X
#lista[3] != 9 -> listb = listb + lista[3] = [1,3] + [3] -> listb.append = print(listb) = [1,3,3]
#lista[4] != 9 -> listb = listb + lista[4] = [1,3,3] + [5] -> listb.append = print(listb) = [1,3,3,5]
#lista[5] != 9 -> listb = listb + lista[5] = [1,3,3,5] + [6] -> listb.append = print(listb) = [1,3,3,5,6]
#lista[6] == 9 -> X
#lista[7] == 9 -> X 
# 해결 [방법3]
lista = [1,3,9,3,5,6,9,9]
for a in range(0,len(lista)) : 
    if 9 in lista: 
        lista.remove(9)
    else:
        break
print(lista)
# lista[0]=1, lista[1]=3, lista[2]=9, lista[3]=3, lista[4]=5, lista[5]=6, lista[6]=9, lista[7]=9
# if 9 in lista -> lista.remove(9) -> remove lista[2],[6],[7]
# print(lista) = [1,3,3,5,6]

# Q. 
# #     for a in lista : 
#         if a == 9 :
#            lista.remove(a)
#         else : 
#         	break


# 리스트 값 추가하기 : append, insert, extend
# list append
# 9,10을 append를 이용하여 추가 출력
lista = [1,3,5,7]
lista.append(9)
lista.append(10)
print(lista) #1,3,5,7,9,10

# list insert : index를 지정하여 추가 가능
# lista.index(2,"abc") 추가 후 출력
lista.insert(2, "abc")
print(lista)    #[1, 3, 'abc', 5, 7, 9, 10]

# list extend : iterable 객체를 list에 추가할 때 사용
# extend는 각 요소를 꺼내어 맨 뒤에 추가 
listb = [10,20,30]
lista.append(listb)
print(lista)         #[1, 3, 'abc', 5, 7, 9, 10, [10, 20, 30]]
listb = [10,20,30]
lista.extend(listb)
print(lista)        #[1, 3, 'abc', 5, 7, 9, 10, [10, 20, 30], 10, 20, 30]


# list의 정렬은 sort() 함수 사용
# sort()는 오름차순 정렬
# #기본옵션은 오름차순 / 내림차순 옵션: reverse =True
numa = [5,3,7,2]
numa.sort(reverse=True) 
print(numa)
#활용 가장 높은 점수 구하기 
score = [30, 60, 20, 90]
score.sort(reverse = True)
print(score[0])


# 문자정렬도 가능
chlist = ['Brad','John','Tom']
chlist.sort()
print(chlist)

# list뒤집기 : reverse() #내림차순정렬 sort(reverse =True)와 헷갈리지 말 것. 
chlist.reverse()
print(chlist)

# list 위치반환(index) : 리스트.index(값)
lista = ['김돌쇠','김갑돌','김갑순','김철수']
print(lista.index('김철수'))


# list 마지막 요소 끄집어내기 : pop()
# remove and return last value
lastvalue = lista.pop()
print(lastvalue) #김철수

lista.pop()
lastvalue = lista.pop()
print(lastvalue) #김갑순

#비교
print(lista.pop()) #김철수

# 프로그래머스 배열 자르기 문제 
numbers = [1,2,3,4,5]
num1 = numbers[0]
num2 = numbers[2]
result = numbers[num1:num2+1]
print(result)

# 문자 리스트를 문자열로 만들기 (join)
lista = ["hello","world","python"]
st1 = ""
st2 = st1.join(lista)
print(st2)    #helloworldpython
        # # for문으로도 할 수 있다.
        # for a in lista:
        #         st1 = st1 + a
        # print(st1)

# 문자열을 문자 리스트로 만들기 (list, split)
sta = "hello world python"
mySta1 = list(sta)
print(mySta1)   #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n']
mySta2 = sta.split()
print(mySta2)   #['hello', 'world', 'python']


# 최대값 구하기
lista = [100,20,30,5,90]
# 위 리스트의 최대값을 정렬함수sort() X, 최대값함수max()X 
# 방법1
max_A = lista[0]
min_A = lista[0]
for a in lista:
    if max_A < a :
        max_A = a
    if min_A > a :
        min_A = a
        print(max_A,min_A)

min_A = lista[0]
for a in lista:
    if min_A > a :
        min_A = a
        print(min_A)

# 방법2
lista = [100,20,30,5,90]
max_A = max(lista)
min_A = min(lista)

# 방법3 lista.sort()
lista = [100,20,30,5,90]
lista.sort()
minA = lista[0]
maxA = lista[len(lista)-1]
maxA = lista[-1]
print(maxA)
print(minA)

# 내가 푼 것
# lista = [100,20,30,5,90]
# lista.sort()
# maxA = lista.sort(reverse=True)[0]
# minA = lista.sort(lista[0])
# print(maxA)
# print(minA)

# ?
# lista.sort()
# listb = []
# for a in range(len(lista)) :
#     listb.append(lista[len(lista)-a-1])






