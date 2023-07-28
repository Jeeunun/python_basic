# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
a = "python"
print(a.count('o'))

# find, index : 대상 문자열에서 지정한 문자가 몇번째 인덱스에 있는지 확인하는 함수 / index : find와 같은 기능
print(a.find('o'))
print(a.index('o'))

# 없는 문자를 찾을 때는 -1 return
print(a.find('x'))

whatyouwant = input("아무런 문자나 입력해주세요")
search = input ("찾고자 하는 문자 1개만 입력해주세요")
result = whatyouwant.find(search)
if result == -1:
    print("찾고자 하는 값이 없습니다")
else:
    print("요청하신 문자는 %d 번째에 있습니다" % result)
    

# 연습문제
# 3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력하라
# <조건1> 각 단어 변수(word1,word2,word3)
# <조건2> 입력과 출력 구분선 : 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr)저장
word1 = input("첫번째 단어를 입력하시오.")
word2 = input("두번째 단어를 입력하시오.")
word3 = input("세번째 단어를 입력하시오.")
abbr = word1[0]+word2[0]+word3[0]
print("="*10)
print(abbr)