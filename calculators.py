# 파이썬 사칙 연산#
a = 3
b = 4
#  덧셈 : + 뺄셈 : - 곱하기 : * 나누기 : /, 몫 : //, 나머지 : %
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 제곱, 제곱근 
# 2의 10제곱을 출력하라
print(2**10)
print(pow(2,10))
import math
print(math.pow(2,10))
# 1024의 제곱근을 구하라
# 제곱근은 math라는 라이브러리를 import해줘야 한다.
import math
print(math.sqrt(1024))

# 연습문제
x = (int(input("x를 입력해주세요")))
y = 2.5 * pow(x,2) + 3.3 * x +6
print(y)