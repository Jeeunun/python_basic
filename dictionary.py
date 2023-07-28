# tuple은 변경불가능한 자료형으로서, ()를 통해 표현한다. cf.list ->[] & 삭제, 수정, 추가 가능
# tuple의 값은 문자, 숫자, 리스트 모두 가능함. 
t1 = (1,2,'a','b')
print(t1)
# tuple은 인덱싱, 슬라이싱 둘다 리스트와 동일하게 허용 (변경하는 것이 아니라 조회만 하는 것이니까)
print(t1[0])

# tuple은 삭제 변경 불가 (조회만 가능)
# del t1[0]
# print(t1)
# -> TypeError: 'tuple' object doesn't support item deletion

# tuple은 더하기 곱하기 가능 -> 수정이 아니라 재정의 한 것이기 때문에 

# tuple을 사용하는 이유는? 개발자가 해당 자료를 수정하지 못하도록 강제적으로 지정한 것. (불변하는 값 강제사용!)
# 또한 리스트에 비해 메모리 효율적 -> list는 데이터 추가(append)할 수 있으므로 메모리 할당해 놓기 때문에(메모리에 여유를 두는 것) 
paymethod = ('card','cash','tmoney')
paymethod = ('cash','tmoney') #이건 재정의 한 것이지 수정한 것이 아니다.

# list와 tuple
# list -> mutable(가변적) , tuple -> immutable(불변적)
# 리스트는 요소가 몇 개 들어갈지 명확하지 않을 때, 튜플은 알고 있을 경우 사용

# -----------------------------------------------------------------------
# dictionary 자료형은 key와 value로 이루어져 있다. dic = { Key : 'value' }
dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남'}

# dictionary 특징1
# 1) 파이썬에서의 dictionary는 다른 language의 map 또는 hashmap과 유사한 자료형, jason이라는 자료형태와 유사하다. 
# 2) 영어사전에서 단어와 뜻으로 이루어져 있는 것에서 유래 
# 3) key는 중복이 불가하고 , value는 다른 키에도 존재할 수 있다. 
dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남','성별' : '여'} #-> key'성별'이 중복.
print(dic1) #오류가 나진 않지만, 성별 하나만 출력된다. {'이름': '홍길동', '나이': 25, '성별': '여'} 
# -> 왜? key값을 해시함수를 통해 인덱스 생성 -> '나이'를 덮어써서 (= 중복이 없는 이유)

# 딕셔너리의 기본호출 방식 : 변수명[key], 변수명.get(key)   cf.list에서는 인덱스를 통해 출력
print(dic1['이름'])             #홍길동
print(dic1.get('이름'))         #홍길동

# list vs dictionary vs tuple 비교하기
# 1) 리스트는 a = [value1, value2,....] 딕셔너리는 a = {key1 : value1, key2 : value2,....}, 튜플은 t = (value1, value2,...)
# 2) 리스트와 튜플은 a[index], 딕셔너리는 a[key]

# dictionary 특징2
# key 와 value로 이루어져 있다보니, 순서가 의미 없다. = index로 접근 불가. 
# key를 가지고 value검색할 때 해시함수를 통해 index를 찾다보니 매우 빠른 속도를 보장. 
# 순서가 없다는 의미 : dictionary는 해시함수(암호생성=난수)를 통해 -> 특정한 규칙 (10진수, 16진수...)
# -> 인덱스 생성 -> 메모리 주소 할당 -> list 보다 dictionary가 더 빠른 이유


dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남','성별' : '여'}
# dictionary에서 키를 이용한 key:value 추가
dic1['신분'] = '학생'
print(dic1) #{'이름': '홍길동', '나이': 25, '성별': '여', '신분': '학생'}

# dictionary에서 키를 이용한 key:value 삭제
del dic1['성별']
print(dic1) #{'이름': '홍길동', '나이': 25, '신분': '학생'}

# dictionary에서 key목록만을 뽑아낼 때
# iterable한 형태로 data가 뽑아져 나오므로 for문 사용가능
dic1 = {'이름': '홍길동', '나이': 25, '신분': '학생'}
keylist = dic1.keys()
print(keylist)  #dict_keys(['이름', '나이', '신분'])
# 위의 keylist에서 각각의 값을 출력해보자.
for a in keylist:
    print(a)
    #range를 활용하여 출력 X
    # for a in range(0,len(keylist)) : 
    #     print(keylist[a]) -> X (왜냐하면 딕셔너리의 인덱스의 순서는 정해져있지 않기 때문에)
for a in dic1:
    print(a)
    # key를 출력해주는 for문 안에서 value도 같이 출력하도록 해보자.
    print(dic1[a])

# 위의 for문을 활용해서, key가 담긴 list를 만들고, value가 담긴 list를 만들어 각각 출력해보자.
tempList1 = []
tempList2 = []
for a in keylist:
    tempList1.append(a)
    tempList2.append(dic1[a])
print(tempList1)
print(tempList2)

# value목록을 뽑아낼 때는 .values()
valuelist = dic1.values()
for a in valuelist:
    print(a)
for a in dic1.values():
    print(a)


# dictionary의 확장 : 변수.update()   cf.list는 변수.extend()
dic1 = {"a": 1, "b":2, "c":3}
dic2 = {"a": 2, "d":4 , "f":5}
dic1.update(dic2)
print(dic1)     #{'a': 2, 'b': 2, 'c': 3, 'd': 4, 'f': 5} 

# 연습문제
# 딕셔너리로 변환해서 출력해보자. 예를들어 'A':2, 'B':1, 'O':2 이렇게 출력되도록 코딩해보자. dic = {key : value}
# 방법1
lista = ['A','A','B','O','O','AB','AB']
dicta = {}

for a in lista :
    if a not in dicta.keys():
        dicta[a] = 1    
    else :
        dicta[a] = dicta[a] + 1
print(dicta)

# 방법2
for a in lista :
    if a not in dicta.keys():
        dicta[a] = lista.count(a)    
print(dicta)