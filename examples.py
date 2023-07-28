# fat = int(input("지방의 그램을 입력하세요."))
# carbo = int(input("탄수화물의 그램을 입력하세요."))
# protein = int(input("단백질의 그램을 입력하세요."))
# total = fat * 9 + protein * 4 + carbo * 4
# print(str(total)+'cal')

# #문자열(String)
# #표현방식 : "",''
# #문자열은 순서가 있다 -> index
# string = 'python'
# print(string[0])
# print(string[-1])
# # 반복연산자
# print('='*10)


# 슬라이싱
# str[1:5:2] 문자열의 1번째부터 5번째미만번까지 간격은 2
a = "this is one line string"
print(len(a))
print(a[0:4]) #this
print(a[0:])  #this is one line string
print(a[:])   #this is one line string
print(a[-1])  #g

# 문자열 처리 함수
a = "HELLO"
print(a.lower())
b = "hello"
print(b.upper())
c = "   hello   "
print(c.strip())
d = "python is very fun"
print(d.count("o"))
a = "Java is fun"
print(a.replace("Java","Python"))
a = "Python is very fun"
print(a.split(" "))
a = "Python ! is very very fun"
print(a.split("!"))

# 이스케이프 문자
# \n : 줄바꿈 , \t : 탭, \\ : 있는 그대로(이스케이프문자 기능 차단)
print('이스케이프 문자 차단')
print('\n출력 이스케이프 문자')
print('\\n출력 이스케이프 문자')

# 제어문 = 조건문 & 반복문
# 조건문 : 단일조건문, 중첩조건문, 삼항조건문
# 단일조건문
var = 10
if var >= 5 : 
    print ('var=',var)
    print ('var은 5보다 크다')
    print ('조건이 참인 경우 실행')
else :
    print('var은 5보다 작습니다.')

#단순조건문->중첩조건문
var = 10
if var >= 5 : 
    print ('var=',var)
    print ('var은 5보다 크다')
    print ('조건이 참인 경우 실행')
elif var < 5 :
    print('var은 5보다 작습니다.')

# 중첩조건문
# 100~85 : '우수', 84~70 : '보통', 69이하 : '저조'
score = int(input('점수입력 : '))
if score >= 85 and score <=100 :
    print('우수')
elif score >=70 :
        print('보통')
else : 
    print('저조')

# 삼항조건문

# 연습문제 [문제1] p77
weight = int(input('짐의 무게는 얼마입니끼?'))
if weight >= 10 : 
     print ("수수료는 10,000원입니다.")
else :
     print ("수수료는 없습니다.")


weight = int(input("짐의 무게는 얼마입니까?"))
price = 10000*int(weight/10)
if weight >= 10 :
     print("수수료는" + format(price) + "입니다.") #format 함수는 중괄호 {, } 안에 포매팅을 지정하고 format 함수의 인자로 값들을 넣습니다.
elif weight <10 :
     print("수수료는 없습니다.")

#반복문 : cnt - 카운터변수 , tot - 누적변수
cnt = tot = 0
while cnt<5 : 
    cnt +=1    #cnt = cnt + 1 란 의미
    tot +=cnt  #tot = tot + cnt 
    print(cnt,tot)

cnt = tot = 0
dataset =[] #빈list
while cnt < 100 : #카운트 100번 반복
     cnt += 1 #cnt = cnt + 1 #1,2,3,4,5,6,,,,,,
     if cnt % 3 == 0 : #3의 배수 #cnt = 3,6,9,12,,,,,
          tot += cnt # tot = tot + cnt 3,9,18,,,,,
          dataset.append(cnt) 
print('1~100 사이 3의 배수 합 = %d % tot') # 정수는 %d 


#무한루프
numData = []
while True :
     num = int(input("숫자입력 : "))
     if num % 10 == 0 : 
          print("프로그램 종료")
          break
     else : 
          print(num)
          numData.append(num)

#break, continue 예
i = 0
while i < 10:
     i+=i #i=i+i
     if i == 3:
          continue
     if i ==6 : 
          break
     print(i, end ='')

#random모듈

#연습문제2 p78
import random
print('숫자 맞추기 게임')
com = random.randint(1,10) #1~10사이 난수 발생
while True : 
     my = int(input('예상 숫자를 입력하시오.'))
     if com == my :
          print ('~~성공~~')
          break
     elif com < my :
               print ('더 작은 수 입력')
               continue
     elif com > my :
               print ('더 큰 수 입력')
               continue

# break, continue
i = 0
while i < 10 :
     i+=1
     if i == 3 :
          continue
     if i == 6 :
          break
     print(i, end='')

# for 반복문
string = '홍길동'
print(len(string))

for s in string:
     print(s)

list = [1,2,3,4,5]
for e in list:
     print ('원소 :', e)

# 중첩반복문
# 구구단
for i in range(2,10):
     print('~~~{}단~~~'.format(i))
     for j in range(1,10):
          print('%d * %d = %d' % (i,j,i*j))

#연습문제 3 79p
# 1~100사이에서 3의 배수이면서 2의 배수가 아닌 수를 한 줄에 출력하고, 누적합을 출력하시오.
tot = 0
print('수열 = ', end =' ') 
for i in range(1,101):
     if i % 3 == 0 and i % 2 != 0 :
        print(i, end=' ')
        tot+=i

print('\n누적합 = %d' %tot)

# 문장과 단어 추출
string = """나는 홍길동입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""
sents = []
words = []
for sen in string.split(sep= "\n"): #sep=""와 end = ""의 차이 # Q.왜 온점(.)을 기준으로 안자름?
     sents.append(sen)
     for word in sen.split():
        words.append(word)
print('문장 : ', sents)
print('문장수: ', len(sents)) # Q.왜 count로 안하는지? count로 쓸경우, '주소는 서울시입니다'가 몇개 있는지 알려주는 것이고, len()는 길이를 구하는 것
print('단어 : ', words)
print('단어수 : ', len(words))

# 연습문제4 79p
multiline = """안녕하세요. 파이썬 세계로 오신걸 환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
cnt = 0
lines = []
words = []
for line in multiline.split("\n") :
     lines.append(line)
     for word in line.split(" ") :
          words.append(word)
          print(words)
          cnt += 1

print('단어 개수 : ', cnt)
print(lines)
print(words)

