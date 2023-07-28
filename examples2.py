# 문제 복습
# 각도기 문제
def solution(angle) : 
     if 0<angle<90 :
          return 1
     elif angle == 90 :
          return 2
     elif angle <180 : 
          return 3
     else :
          return 4 
    #다른방법이 있을까?

# 피자 나눠먹기 문제
def solution(n) :
     answer = 0
     if n % 7 == 0 :
          answer = (n/7,'판')
     else : 
          answer = n//7 + 1
    #다른방법이 있을끼?

# 배열 자르기
def solution(numbers, num1, num2) : 
     answer = []
     answer = numbers[num1:num2+1]
     return answer

# 배열 나누기
def solution(num_list):
     return(num_list.reverse())

# 문자열 뒤집기
def solution(my_string) : 
     answer = reversed(my_string)
     return answer
    
def solution (my_string) : #문자열을 리스트형으로 바꾸기! ->리스트형은 문자열과 달리 순서가 존재하기 때문에
     my_list = list(my_string)
     my_list.reverse()   #리스트의 문자배열 뒤집기
     answer = ''.join(my_list) #구분자를 공백으로 설정해서 출력
     return answer 

# 짝수 홀수 개수 구하기
def solution(num_list) :
     num1 = 0
     num2 = 0
     for a in num_list:
          if a % 2 == 0 :
               num1 = num1 +1 
          else :
               num2 = num2 +1
     answer = [num1,num2]
     return answer

# 원소들의 곱과 합
from functools import reduce 
def multiply(arr) :
    return reduce(lambda x,y :x*y,arr)
def solution(num_list):
    answer = 0
    if sum(num_list) ** 2 > multiply(num_list) :
        return 1
    else :
        return 0
    
# 문자리스트를 문자열로 변환하기
def solution(arr):
    return (''.join(arr))

# 배열의 평균값
    answer = 0
    for num in numbers:
     return sum(num)/len(numbers)
    
# 완주하지 못한 선수
# 내가 푼 것
# def solution(participant, completion):
    
#     for p in participant :
#         if p not in completion :
#             return p
def solution(participant, completion):
    for p in participant :              #효율성의 문제 -> 리스트가 아닌 딕셔너리로 바꾸기
        if p in completion :
             completion.remove(p)
        else:
            return p
# 효율성문제 해결
# completion를 dict로 변환
# participant를 for문으로 1개씩 꺼내서 completion[p] = completion[p] -1
def solution(participant, completion):
    answer = ""
    dictc = {}
    for c in completion:
        if c not in dictc.keys():
            dictc[c] = 1
        else:
            dictc[c] = dictc[c] + 1    
    for p in participant:
        if p in dictc and dictc[p] > 0:
            dictc[p] = dictc[p] -1
        else:
            answer = p
    return answer

#369게임 (다시 풀어보기)
def solution(order):
    answer = 0
    for a in ['3','6','9']:
        answer += str(order).count(a)
    return answer

def solution(order):
    answer = 0
    for a in list(str(order)):
        if a in ['3','6','9'] :
            answer += 1
    return answer