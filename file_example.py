# # <파이썬으로 file만들기>
# file 시스템 입출력 라이브러리 : open
# open함수는 mode(w,r,a)을 갖고 있다. 
# w:write(덮어쓰기), r:read, a:c추가
# open을 했을 때 해당 파일명이 없으면 자동 생성
f = open( "test.txt",'w')   #->파일생성
f.close()

# # -------------------------------------------
# # <'w'옵션>
f = open("test.txt","w", encoding="UTF-8") #encoding="UTF-8" => 한글이 안깨지게 해준다.
for i in range(0,10):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)   #file에 data 덮어쓰기
f.close()           

# # -----------------------------------------
# <'r'옵션>
#   1. readline = 첫번째 줄만 가져오는 함수
f = open("test.txt","r",encoding="UTF-8")
line = f.readline()
print(line)
f.close() #0번째 줄입니다. 

#   2. readlines : 데이터를 리스트형태로 라인별로 담아준다.
f = open("test.txt","w",encoding="UFT-8")
lines = f.readlines
print(lines)

#   3. read : 데이터를 한꺼번에 문자열로 담아준다.
f = open("test.txt","w",encoding="UFT-8")
lines = f.readlines
print(lines)

# read보다 readlines을 쓴다 => 데이터 parsing이 편하기 때문에


#   4.  while, if문으로 readline으로 전체 출력
# 방법1
line = f.readline
while line: #line이 없으면 False로 인식 -> 멈춤
    print(line)
    line = f.readline
f.close()

# 방법2
while True:
    line = f.readline()
    print(line)
    if not line:
        break
f.close()

# -----
# <'a'옵션> 으로 추가모드
f = open("test.txt","a",encoding="UTF-8")
# 0~9번째 줄입니다. -> 10번째~19번째 줄입니다. 
for i in range(10,20):
    data = "%d번째 줄입니다. \n" %i     
    f.write(data)
f.close()

# 파이썬에서 객체를 생성하고 나면, 힙메모리에 객체가 할당된다.
# 객체의 사용이 끝나면 객체를 close 해줘야 하나?
# 그럴 필요가 없는게 파이썬에는 GC(Garbage Collector)가 내장되어, 자동으로 사용빈도가 낮은 데이터는 메모리에서 삭제를 해준다. 
# 그러나 파일 시스템은 그렇지 못하므로 직접 닫아줘야 한다. 그래야 메모리 낭비가 없다. 

#--------------------
# <os 라이브러리를 활용한 디렉터리 내에 파일 검색>
#   1. 예시
import os
searchDir = r'C:\Users\한지은\OneDrive\바탕 화면\한지은'
# -> .py로 끝나는 파이썬 확장파일을 search할 것..!
# 현재 폴더에서만 검색
# dirList = os.listdir(searchDir) #파일, 디렉토리 목록을 뽑아내는 listdir함수 사용
# for dir in dirList:
#     dirTuple = os.path.splitext(dir)
#     # print(dirTuple)
#     # ('.git', '') ('python-basic-syntax', '')('test', '.txt')
#     if dirTuple[1] == '.py':
#         fullpath = os.path.join(searchDir, dir)

# 그 다음 폴더까지 검색
searchDir = r'C:\Users\한지은\OneDrive\바탕 화면\한지은'
dirList = os.listdir(searchDir)
for dir in dirList: 
    filename = os.path.join(searchDir, dir)                                            
    if os.path.isdir(filename):           
        dirList2 = os.listdir(filename)     
        for dir2 in dirList2:              
            dirTuple2 = os.path.splitext(dir2)
            if(dirTuple2[1]=='.py'):
                fullPath = os.path.join(filename, dir2)
                print(fullPath)
    dirTuple = os.path.splitext(dir)
    if(dirTuple[1]=='.py'):
        fullPath = os.path.join(searchDir, dir)
        print(fullPath)

# searchDir(목록 =dirList) > dirList(목록=dir) => searchDir+dir=filename 
# filename(목록 = dirList2) > dirList2(목록=dir2) => dir2을 '.'으로 split
# dir2.py 일때, filename+dir2 = fullpath
# <86~87>
#os.path.join으로 경로를 1개로 만든다.
# 출력결과)) print(filename)
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\.git
    # # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\test.txt
# <88~91>
# 만약 filename의 목록들을 dirList2라고 할때,for 문 실행 => dirList2의 목록을 하나하나 꺼내보기 (=dir2)
# dir2를 '.'으로 스플릿 = dirTuple2 dirList2(filename의 목록)=>dir2(dirList2의 목록)
# 출력결과)) print(dirTuple2)
        # ('COMMIT_EDITMSG', '')
        # ('config', '')
        # ('description', '')
        # ('FETCH_HEAD', '')
        # ('HEAD', '')
        # ('hooks', '')
        # ('index', '')
        # ('info', '')
        # ('logs', '')
        # ('objects', '')
        # ('refs', '')
        # ('.git', '')
        # ('calculators', '.py')
        # ('class_stataements', '.py')
        # ('dictionary', '.py')
        # ('examples', '.py')
        # ('examples2', '.py')
        # ('exception', '.py')
        # ('file_example', '.py')
        # ('for_statements', '.py')
        # ('function_etc', '.py')
        # ('function_statements', '.py')
        # ('if_statements', '.py')
        # ('list_statement', '.py')
        # ('method', '.py')
        # ('module_import', '.py')
        # ('module_test', '')
        # ('README', '.md')
        # ('set_statements', '.py')
        # ('str-df', '.py')
        # ('variables', '.py')
        # ('__pycache__', '')
# <92~94>
# 만약 dirTuple2의 인덱스1값이 .py 라면 filename에 dir2를 조인 = fullpath
# print(fullpath) = > searchDir => dirTuple2
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\calculators.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\class_stataements.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\dictionary.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\examples.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\examples2.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\exception.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\file_example.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\for_statements.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\function_etc.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\function_statements.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\if_statements.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\list_statement.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\method.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\module_import.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\set_statements.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\str-df.py
    # C:\Users\한지은\OneDrive\바탕 화면\한지은\python-basic-syntax\variables.py

# 모든 폴더까지 검색 => 재귀함수화.

def searchRecur(searchDir):
    try:
        dirList = os.listdir(searchDir)
        if not dirList:
            return                      #파일이 없을 때 return(함수 종료)
        for dir in dirList: 
            filename = os.path.join(searchDir, dir)                                            
            if os.path.isdir(filename):
                searchRecur(filename)
            dirTuple = os.path.splitext(dir)
            if(dirTuple[1]=='.py'):
                fullPath = os.path.join(searchDir, dir)
            print(fullPath)
    except Exception:
        print("예외입니다.")

searchDir = r'C:\Users\한지은\OneDrive\바탕 화면\한지은'
searchRecur(searchDir)

