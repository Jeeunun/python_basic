# 대소문자 변경 : upper / lower()
a = "hello"
print(a.upper())
b = "HELLO"
print(b.lower())

# 문자열 양쪽 공백을 없애는 함수 : strip()
a = "  hello world  "
print(a.strip())

# 문자열 대체 : replace()
a = 'I studied python'
b = a.replace('python', 'java')
print(b)
# print(a.replace('python','java'))

# 문자열 나누기 : split()
# 공백을 기준으로 문자를 나눈다. 
a = "I studied python"
b = a.split()
print(b)

# 공백의 차이 
a = "I     studied     python"
b = a.split()
print(b)

a = "I     studied     python"
b = a.split(" ")
print(b)
# 왜 이런 결과가 나왔을까? 공백을 문자로 인식했기 때문에

a = "I:studied:python"
b = a.split(":")
print(b)

