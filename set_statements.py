# set은 (수학)집합이라 부른다.
# set의 특성은 딕셔너리와 마찬가지로, index가 없고, 중복이 없다. 
s1 = {'이름','나이','성별'}
# list의 중복을 제거하기 위해서
# list를 가지고 set으로 형변환 시키는 방식도 많이 사용. 
s1 = set(['이름','나이','성별'])  
s1 = {'이름','이름','나이','성별'}
# 집합의 개수를 구하는 함수는 : len
print(len(s1))
s1 = set(s1)
print(s1)   #{'이름', '성별', '나이'}
s2 = set('test')
print(s2)   #{'s', 't', 'e'}

# index로 접근이 불가하다. (순서가 없어서)
# print(s1[0])

# 예제문제 : 이 반 학생들의 혈액형 종류는 총 몇개인가?
lista = ['A','A','B','O','AB','B']
print(len(set(lista)))
# setA의 값을 하나씩 출력하려면? setA[0],setA[1] X
lista = ['A','A','B','O','AB','B']
setA = set(lista)
for a in setA :
    print(a)   # Q. 정렬은? set이 순서가 없는데 순서를 정하고 싶으면? set으로 변환 후 중복을 제거하고 + 리스트로 다시 변환?

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
# s3 = s1 | s2   #|는 or를 의미
s3 = s1.union(s2)       #s3= s1 | s2
print(s3)

# 교집합
# & 는 and를 의미 (앰퍼샌드)
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# 차집합
# s2에서 s1을 뺀 차집합을 구해보자. 
s3 = s2.difference(s1)
s3 = s2 - s1
print(s3)

# 집합에서 값 추가 : add
s1 = {1,2,3,4,5,6}
# 7을 추가한 다음에 s1출력
s1.add(7)
print(s1)

# 값 여러개 추가시 update함수(딕셔너리와 동일)
s1 = {1,2,3,4,5,6}
s2 = {1,2,10,11,12}
s1.update(s2)
print(s1)

# 값 삭제 : remove(), discard() 
# remove(), discard()
s1 = {1,2,3,4,5,6}
s1.remove(1)
s1.discard(6)
print(s1)
# remove와 discard의 차이 : 
# discard()경우 지우려는 Element가 없어도 정상종료하는 반면, remove() 메소드는 지우려는 Element가 없으면 KeyError가 발생

# boolean(불형) 타입
# : in, not in : in(또는 not in) 뒤에 iterable한 자료형이 나온다.
# a in list, a not in list, a in dict.keys(), a in set
# 비어있는 값들은 거짓, 값이 들어있으면 참
# [],{},(),0,"",None -> 거짓,

# while 조건 : 
#     실행문 #조건이 참인 한, 무한 반복
# for 변수 in 리스트 :
#     실행문 #리스트의 len만큼 반복

listA = [1,2,3]
while listA:
    print('참입니다.')
    listA.pop()      #비어있는 값은 거짓이므로 while무한반복 이어도 3번 반복.

# 숫자1은 참 숫자0은 거짓
if int(2/5) :           #0이되므로 else
    print('참입니다.')
else :
    print('거짓입니다.')
